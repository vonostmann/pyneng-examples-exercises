# -*- coding: utf-8 -*-
"""
Задание 6.2

Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
В зависимости от типа адреса (описаны ниже), вывести на стандартный поток вывода:
   'unicast' - если первый байт в диапазоне 1-223
   'multicast' - если первый байт в диапазоне 224-239
   'local broadcast' - если IP-адрес равен 255.255.255.255
   'unassigned' - если IP-адрес равен 0.0.0.0
   'unused' - во всех остальных случаях

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

ip = input ("Введите IP устройства: ")
ip_spl = ip.split(".")
ip_int = ip_spl[0] + ip_spl[1] + ip_spl[2] +ip_spl[3]
if ip_int == "0000":
      print('unassigned')
elif ip_int == "255255255255":
      print('local broadcast')
else:
   if int((ip_spl[0]),10) < 223:
      print('unicast')
   elif  int((ip_spl[0]),10) < 239:
      print('multicast')
   else:
      print ('unused')