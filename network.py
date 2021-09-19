'''
    python-network-scanner
    Copyright (C) 2021  devmarcstorm

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
    
'''

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
