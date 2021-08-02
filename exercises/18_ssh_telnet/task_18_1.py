# -*- coding: utf-8 -*-
"""
Задание 18.1

Создать функцию send_show_command.

Функция подключается по SSH (с помощью netmiko) к ОДНОМУ устройству
и выполняет указанную команду.

Параметры функции:
* device - словарь с параметрами подключения к устройству
* command - команда, которую надо выполнить

Функция возвращает строку с выводом команды.

Скрипт должен отправлять команду command на все устройства из файла devices.yaml
с помощью функции send_show_command (эта часть кода написана).

"""
import yaml
from netmiko import (
    ConnectHandler,
    NetmikoTimeoutException,
    NetmikoAuthenticationException,
)

def send_show_command(device,command):
    print(device["host"])
    result = {}
    try:
        with ConnectHandler(**device) as ssh:
            ssh.enable()
#            for command in commands:
            output = ssh.send_command(command)
#                result[command] = output
        return output
    except (NetmikoTimeoutException, NetmikoAuthenticationException) as error:
        print(error)

if __name__ == "__main__":
    command = "show ver | i uptime"
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)
#    print(devices)
    for dev in devices:
        print(send_show_command(dev, command))
