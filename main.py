from getmac import get_mac_address
from prettytable import PrettyTable

from datetime import date

from device import Device
from network import Network

import json
import os
import sys

def create_device_list(devices, data):
    ''' Return a dictonary like {'known': [], 'unknown': []}

    Creates 2 lists from devices (class Device) and makes them available in a dictionary
       - 'known': list of known devices (mac address included in the data/device.json)
       - 'unknown': list of unknown devices (not included)
    '''
    known_devices = []
    unknown_devices = []

    for host, info in devices:
        device = Device(info['mac'], host, info['hostnames'][0]['name'], data)
        if device.name:
            known_devices.append(device)
        else:
            unknown_devices.append(device)

    return {'known': known_devices, 'unknown': unknown_devices}

if __name__ == '__main__':
    dataPath = 'data'
    try:
        with open("{}/devices.json".format(dataPath), "r") as readFile:
                json_devices = json.load(readFile)
    except FileNotFoundError:
                json_devices = {}
                print('''No valid "data/devices.json" found. Please create one with the following format:
{
    "00:00:00:00:00:00":
    {
      "type": "Device",
      "owner": "John Appleseed",
      "location": null,
      "allowed": true
    }
}
            ''')

    network = Network()

    try:
        devices = network.get_devices()
    except KeyboardInterrupt:
        print('You stopped scanning. Scanning may take a while. If it takes too long, there may be a problem with the connection. Did you specify the correct network?')
        sys.exit()

    for host, info in devices:
        info['mac'] = get_mac_address(ip=host)

    data = create_device_list(devices, json_devices)
    log_text = ''

    table = PrettyTable()
    table.field_names = ["MAC ADDRESS", "IP", "NAME IN NETWORK", "NAME", 'LOCATION', 'ALLOWED']
    for device in data['known']:
        table.add_row(device.to_list())
        log_text += '{}\n'.format(device.to_string())
    
    print('Known Devices\n{}'.format(table))

    table = PrettyTable()
    table.field_names = ["MAC ADDRESS", "IP", "NAME IN NETWORK"]
    for device in data['unknown']:
        table.add_row(device.to_list()[:3])
        log_text += '{}\n'.format(device.to_string())
    
    print('Unknown Devices\n{}'.format(table))

if not os.path.isdir(dataPath):
    os.mkdir(dataPath)

with open("{}/{}.log".format(dataPath, date.today()), "a") as appendFile:
    appendFile.write(log_text)
    print('You can find a log file with all devices in "data/{}.log"'.format(date.today()))
