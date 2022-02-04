# -*- coding: utf-8 -*-
"""
Задание 4.6

Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:
Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

Предупреждение: в разделе 4 тесты можно легко "обмануть" сделав нужный вывод,
без получения результатов из исходных данных с помощью Python.
Это не значит, что задание сделано правильно, просто на данном этапе сложно иначе
проверять результат.
"""

ospf_route = "      10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"
ospf_route = ospf_route.split(" ")
ospf_route1 = ospf_route[6::]
ospf_route2 = ospf_route1[1][1:6]
ospf_route1[1] = ospf_route2
ospf_route1.remove('via')
output = 'Prefix{:>27}\nAD/Metric{:>17}\nNext-Hop{:>23}\nLast update{:>16}\nOutbound Interface{:>18}\n'
print(output.format(ospf_route1[0],ospf_route1[1],ospf_route1[2],ospf_route1[3],ospf_route1[4]))
