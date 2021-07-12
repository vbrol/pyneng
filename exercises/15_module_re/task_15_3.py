# -*- coding: utf-8 -*-
"""
Задание 15.3

Создать функцию convert_ios_nat_to_asa, которая конвертирует правила NAT
из синтаксиса cisco IOS в cisco ASA.

Функция ожидает такие аргументы:
- имя файла, в котором находится правила NAT Cisco IOS
- имя файла, в который надо записать полученные правила NAT для ASA

Функция ничего не возвращает.

Проверить функцию на файле cisco_nat_config.txt.

Пример правил NAT cisco IOS
ip nat inside source static tcp 10.1.2.84 22 interface GigabitEthernet0/1 20022
ip nat inside source static tcp 10.1.9.5 22 interface GigabitEthernet0/1 20023

И соответствующие правила NAT для ASA:
object network LOCAL_10.1.2.84
 host 10.1.2.84
 nat (inside,outside) static interface service tcp 22 20022
object network LOCAL_10.1.9.5
 host 10.1.9.5
 nat (inside,outside) static interface service tcp 22 20023

В файле с правилами для ASA:
- не должно быть пустых строк между правилами
- перед строками "object network" не должны быть пробелы
- перед остальными строками должен быть один пробел

Во всех правилах для ASA интерфейсы будут одинаковыми (inside,outside).
    results = [ p.groups() for p in re.finditer(regex,srcf.read()) ]
      for line in srcf:
      match = re.search(regex,line)
      if match:
        proto, ip, inport, outport = match.groups()
        results.append(f"object network LOCAL_{ip}")
        results.append(f" host {ip}")
        results.append(f" nat (inside,outside) static interface service {proto} {inport} {outport}")
    print(results)
    dstf.write("\n".join(results))

"""
import re

def convert_ios_nat_to_asa(infile, outfile):
  regex=r"ip nat inside source static (?P<proto>\S+) (?P<ip>\S+) (?P<inport>\S+) interface \S+ (?P<outport>\S+)"
  asa_template = (
                    "object network LOCAL_{ip}\n"
                    " host {ip}\n"
                    " nat (inside,outside) static interface service {proto} {inport} {outport}\n"
                )

  with open(infile) as srcf, open(outfile,'w') as dstf:
    for match in re.finditer(regex,srcf.read()):
      dstf.write(asa_template.format(**match.groupdict()))


if __name__ == "__main__":
  convert_ios_nat_to_asa("cisco_nat_config.txt","1.txt")
