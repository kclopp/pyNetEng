import json
from os import device_encoding
from napalm import get_network_driver

devicelist = ['192.168.122.11', '192.168.122.12']

for ip_address in devicelist:
    print("Connecting to " +str(ip_address))
    driver = get_network_driver('ios')
    iosvl2 = driver(ip_address, 'kevin', 'cisco')
    iosvl2.open()
    iosvl2.load_merge_candidate(filename = 'ACL1.cfg')
    diffs = iosvl2.compare_config()
    if len(diffs) > 0:
        print(diffs)
        iosvl2.commit_config()
    else:
        print('No changes required.')
        iosvl2.discard_config()

    iosvl2.load_merge_candidate(filename = 'ospf1.cfg')

    diffs = iosvl2.compare_config()
    if len(diffs) > 0:
        print(diffs)
        iosvl2.commit_config()
    else:
        print('No OSPF changes required.')
        iosvl2.discard_config()

    iosvl2.close()




