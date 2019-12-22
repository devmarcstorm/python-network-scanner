from nmap import PortScanner

class Network(object):
    def __init__(self):
        self.ip_default = '192.168.1.1'
        self.ip = input('Please input network IP (press return for ' + self.ip_default + '):\n')
        
    def get_devices(self):
        '''Return a list

        Creates a list of items that contain device information
        '''
        if len(self.ip) >= 1:
            network_to_scan = self.ip + '/24'
        else:
            network_to_scan = self.ip_default + '/24'

        p_scanner = PortScanner()
        print('Scanning {}...'.format(network_to_scan))
        p_scanner.scan(hosts=network_to_scan, arguments='-sn') 
        device_list = [(device, p_scanner[device]) for device in p_scanner.all_hosts()]
        return device_list
