vlan=input("VLAN: ")
mactable = []
with open('CAM_table.txt') as f:
  for line in f:
    if '.' in line:
      line=line.split()
      if int(line[0])==int(vlan):
        mactable.append([int(line[0]),line[1],line[3]])

#      print("{:15} {:15} {}".format(line[0],line[1],line[3]))
#print(mactable)
print('-'*30)
for vlan,mac,iface in sorted(mactable):
  print(f"{vlan:<9} {mac:<20} {iface}")