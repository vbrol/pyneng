#!/home/python/venv/pyneng-py3-7/bin/python

from sys import argv
filename = argv[1]
dst = argv[2]

ignore = ["duplex", "alias", "configuration"]

with open(filename,'r') as f, open(dst,'w') as fdst:
  for line in f:
    if line and line[0]!='!':
      if not set(ignore) & set(line.split()):
        fdst.write(line)
