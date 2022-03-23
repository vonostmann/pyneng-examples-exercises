# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова.

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'
Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
ip = input ("Введите IP устройства: ")
flag = False
while not flag:
    try:
        ip_spl = ip.split(".")
       #делаем строку из ip:
        ip_int = ip_spl[0] + ip_spl[1] + ip_spl[2] +ip_spl[3] 
       #проверка на присутствие букв в адресе:
        int((ip_spl[0]),10)/int((ip_spl[1]),10)/int((ip_spl[2]),10)/int((ip_spl[3]),10) 
       #проверка на наличие разделителя "."
        if '.' in ip:
          #проверка на значение октетов меньше 255
            if int((ip_spl[0]),10) <= 255 and int((ip_spl[1]),10) <= 255 and int((ip_spl[2]),10) <= 255 and int((ip_spl[3]),10) <= 255: 
                flag = True
                if ip_int == "255255255255":
                    print('local broadcast')
                else:
                    if int((ip_spl[0]),10) < 223:
                       print('unicast')
                    elif  int((ip_spl[0]),10) < 239:
                       print('multicast')
                    else:
                       print ('unused')      
            else:
                print('Неправильный IP-адрес')
                ip = input ("Введите IP устройства еще раз: ")
        else:
            print('Неправильный IP-адрес')
            ip = input ("Введите IP устройства еще раз: ")
    except ZeroDivisionError:
        if ip_int == "0000":
            print('unassigned')
    except ValueError:
        print('Неправильный IP-адрес')
        ip = input ("Введите IP устройства еще раз: ")
    except IndexError:
        print('Неправильный IP-адрес')
        ip = input ("Введите IP устройства еще раз: ")
