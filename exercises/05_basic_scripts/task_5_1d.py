# -*- coding: utf-8 -*-
"""
Задание 5.1d

Переделать скрипт из задания 5.1c таким образом, чтобы, при запросе параметра,
пользователь мог вводить название параметра в любом регистре.

Пример выполнения скрипта:
$ python task_5_1d.py
Введите имя устройства: r1
Введите имя параметра (ios, model, vendor, location, ip): IOS
15.4


Ограничение: нельзя изменять словарь london_co.

Все задания надо выполнять используя только пройденные темы. То есть эту задачу можно
решить без использования условия if.
"""

london_co = {
    "r1": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.1",
    },
    "r2": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.2",
    },
    "sw1": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "3850",
        "ios": "3.6.XE",
        "ip": "10.255.0.101",
        "vlans": "10,20,30",
        "routing": True,
    },
}
device_id = input ("Введите имя устройства: ")
device_list = (str(list(london_co[device_id].keys())[::])).replace("[","(").replace("]",")").replace("'", "")
parameter_id = input ("Введите имя параметра{}".format(device_list))
dev_id = london_co[device_id].setdefault(parameter_id.lower(), "Такого параметра нет")
print(dev_id)