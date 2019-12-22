# Network scanner

> A small project that I wrote on the fly in order to identify and label the devices in my networks.

## What are you getting
```
Please input network IP (press return for 192.168.1.1):

Scanning 192.168.1.1/24...
Known Devices
+-------------------+---------------+------------------------------+-------------------------------------------+-------------------+---------+
|    MAC ADDRESS    |       IP      |       NAME IN NETWORK        |                    NAME                   |     LOCATION      | ALLOWED |
+-------------------+---------------+------------------------------+-------------------------------------------+-------------------+---------+
| 00:00:00:00:00:00 | 192.168.1.102 |          iphonex             |        iPhone X of John Appleseed         |      My Home      |   True  |
| 00:00:00:00:00:01 | 192.168.1.103 |       PC192-168-1-103        |         Windows PC of my Neighbor         |  Neighbor's house |   False |
+-------------------+---------------+------------------------------+-------------------------------------------+-------------------+---------+
Unknown Devices
+-------------------+---------------+-----------------+
|    MAC ADDRESS    |       IP      | NAME IN NETWORK |
+-------------------+---------------+-----------------+
| 00:00:00:00:00:02 | 192.168.1.104 | PC192-168-1-104 |
+-------------------+---------------+-----------------+
You can find a log file with all devices in "data/2007-01-09.log"
```

and a log file:

```
Log: 2007-01-09 09:41:00.000000 
	 Mac Address: 00:00:00:00:00:00 
	 Name in network:  iphonex 
	 Given name: iPhone X of John Appleseed 
	 Allowed on network: True
Log: 2007-01-09 09:41:00.000001 
	 Mac Address: 00:00:00:00:00:01
	 Name in network: PC192-168-1-103
	 Given name: Windows PC of my Neighbor  
	 Allowed on network: False
Log: 2007-01-09 09:41:00.000002 
	 Mac Address: 00:00:00:00:00:02
	 Name in network: PC192-168-1-104
	 Given name: None 
	 Allowed on network: None
```

## How to use

### Getting started
 1. clone or download the project and `cd` into the project folder
 2. install virtualenv and create venv 
    1. `pip3 install virtualenv`
    2. `virtualenv -p python3 <venvname>`
 3. activate venv
    1. Unix like: `source <venvname>/bin/activate` 
    2. Windows `\<venvname>\Scripts\activate.bat`
 4. install dependencies
    1. `brew install nmap`
    2. `pip install -r requirements.txt`
       1. or `pip install python-nmap getmac prettytable`

### How to run
1. run: `python main.py`
2. input network to scan: e.g. `192.168.1.1`

***Scanning could take a little while (around 20sec is normal). In addition, it may have to be run several times to get all devices.***

***You will find a `<date>.log`in a `data` directory with all devices found this day***

### Save known devices
1. create json file: `data/devices.json`
2. Use the following format:
```json
   {
    "00:00:00:00:00:00":
    {
      "type": "iPhone X",
      "owner": "John Appleseed",
      "location": "My Home",
      "allowed": true
    },
```
- **KEY** is mac address
- "type" is how the device should be called
- "owner" is simply the user of the device
  
  ***The device will be shown as e.g. `iPhone X of John Appleseed`***

- "location" is the standard location e.g. `null`, `"living room"`, `"office"` etc.

## Contributing
This is a very small project that arose out of a quick need. So I keep it as simple as possible. If you are motivated to improve it, you can simply fork the project and make a pull request with your changes. 

**Code of Conduct: Be nice to everyone and have fun coding.**
