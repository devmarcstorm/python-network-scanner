from datetime import datetime
from colors import r, g, n

class Device(object):
    def __init__(self, mac, ip, network_name, data={}):
        self.mac = mac
        self.ip = ip
        self.network_name = network_name

        self.name = None
        self.allowed = None
        self.location = None

        device_check = self.device_known(data)
        if device_check:
            self.name = device_check['name']
            self.allowed = device_check['allowed']
            self.location = device_check['location']

    def device_known(self, data):
        '''Return a str (given name of the device) or None

        Checks whether the device is contained in the Dictonary (based on the mac address)
        '''
        mac = ''
        if self.mac in data:
            mac = self.mac
        elif self.mac.upper() in data:
            mac = self.mac.upper()

        if mac:
            name = '{} of {}'.format(data[mac]['type'], data[mac]['owner'])
            return {'name': name, 'allowed': data[mac]['allowed'], 'location': data[mac]['location']}

        return None

    def to_list(self):
        '''Return a list [mac, ip, network_name, name, location, allowed]

        Creates a list of device attributes as colored strings
            green: allowed in the network
            red: not allowed
        '''
        if self.allowed:
            color = g
        else:
            color = r

        mac = '{}{}{}'.format(color, self.mac, n)
        ip = '{}{}{}'.format(color, self.ip, n)
        network_name = '{}{}{}'.format(color, self.network_name, n)
        name = '{}{}{}'.format(color, self.name, n)
        location = '{}{}{}'.format(color, self.location, n)
        allowed = '{}{}{}'.format(color, self.allowed, n)

        return [mac, ip, network_name, name, location, allowed]

    def to_string(self):
        '''Return a str

        Device information as a string with indentations for the log file
        '''
        return 'Log: {} \n\t Mac Address: {} \n\t Name in network: {} \n\t Given name: {} \n\t Allowed on network: {}'.format(datetime.now(), self.mac, self.network_name, self.name, self.allowed)
