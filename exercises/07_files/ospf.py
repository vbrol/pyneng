#!/home/python/venv/pyneng-py3-7/bin/python
"""
O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0
O        10.0.28.0/24 [110/31] via 10.0.13.3, 3d20h, FastEthernet0/0
O        10.0.37.0/24 [110/11] via 10.0.13.3, 3d20h, FastEthernet0/0
O        10.0.41.0/24 [110/51] via 10.0.13.3, 3d20h, FastEthernet0/0
O        10.0.78.0/24 [110/21] via 10.0.13.3, 3d20h, FastEthernet0/0
O        10.0.79.0/24 [110/20] via 10.0.19.9, 4d02h, FastEthernet0/2

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0
"""

template='''
Prefix                {}
AD/Metric             {}
Next-Hop              {}
Last update           {}
Outbound Interface    {}
'''

with open('ospf.txt','r') as f:
  for line in f:
    line = line.split()
    print(template.format(line[1],line[2],line[4],line[5],line[6]))
