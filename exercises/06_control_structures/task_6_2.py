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
from email.headerregistry import UniqueSingleAddressHeader
from socket import IPV6_RTHDR_TYPE_0


ip = input ("Введите IP устройства: ")
Читаем пооктетно адрес делаем из него список
берем первый элемент для сравнения
сравниваем с 223, если меньше то выводим unicast и стоп
если больше то выводим multicast и идем дальше

берем весь список 
если равен 255.255.255.255 то вывод local broadcast и стоп
если 0.0.0.0 то вывод unassigned и идем дальше

выводим Unused

add_type = {
   'unicast' : ip_type[1], 
   'multicast' : ip_type[2],
   'local boroadcast' : ip_type[3],
   'unassigned' : ip_type[4],
   'unused' : ip_type[5]
}
print(output)