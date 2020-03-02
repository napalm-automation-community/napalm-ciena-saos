# NAPALM COMMUNITY DRIVER FOR CIENA SAOS DEVICES

This Napalm driver connects to Ciena devices running SAOS operating system. It has been tested on multiple platforms.

It is only possible to connect using ```SSH``` so telnet will not work.


## INSTALLING THE DRIVER

```
git clone https://github.com/napalm-automation-community/napalm-ciena-saos.git
cd napalm-ciena-saos
python setup.py
```

> Installation with PIP will be available soon.


## HOW TO USE

Use driver name ```ciena_saos``` and 

```
    driver = napalm.get_network_driver("ciena_saos")
    device = driver(hostname=<host>, username=<user>, password=<pwd>, optional_args={  })
    device.open()
    device.get_config()
    device.get_facts()
    device.get_virtual_switch()
    device.close()
```


## AVAILABLE FUNCTIONS

The standard commands are implememented: get_facts, get_cli, get_config, save_config


### get_facts()

The default get_facts() function returns the following info:

```
        facts = {
            "vendor": "Ciena",
            "uptime": None,
            "os_version": None,
            "os_version_installed": None,
            "boot_version": None,
            "application_build": None,
            "serial_number": None,
            "device_id": None,
            "device_type": None,
            "model": None,
            "description": None,
            "hostname": None,
            "fqdn": None,
            "domain_name": None,
            "loopback_ipv4": None,
            "remote_ipv4": None,
            "chassis_mac": None
        }
```


### get_virtual_switch()

This returns all the virtual switches.

For each vswitch the following facts are found:

```
            vswitch = {
                "name": None,
                "id": None,
                "description": None,
                "active_vlan": None,
                "vc": None
            }
```


## AUTHOR

This driver is currently work in progress. Please feel free to contact me via GIT.

Maarten Wallraf  (https://github.com/mwallraf)


