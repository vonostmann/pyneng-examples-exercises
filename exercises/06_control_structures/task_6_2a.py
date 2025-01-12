# -*- coding: utf-8 -*-
"""
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса.
Адрес считается корректно заданным, если он:
   - состоит из 4 чисел (а не букв или других символов)
   - числа разделенны точкой
   - каждое число в диапазоне от 0 до 255

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'

Сообщение "Неправильный IP-адрес" должно выводиться только один раз,00
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
ip = input ("Введите IP устройства: ")
try:
   ip_spl = ip.split(".")
   #делаем строку из ip:
   ip_int = ip_spl[0] + ip_spl[1] + ip_spl[2] +ip_spl[3] 
   #проверка на присутствие букв в адресе:
   int((ip_spl[0]),10)/int((ip_spl[1]),10)/int((ip_spl[2]),10)/int((ip_spl[3]),10) 
   #проверка на наличие разделителя "."
   if '.' in ip:
      # проверка на количество октетов
      if len(ip_spl) == 4:
      #проверка на значение октетов меньше 255
         if int((ip_spl[0]),10) <= 255 and int((ip_spl[1]),10) <= 255 and int((ip_spl[2]),10) <= 255 and int((ip_spl[3]),10) <= 255: 
            #ip_int = ip_spl[0] + ip_spl[1] + ip_spl[2] +ip_spl[3]
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
      else:
         print('Неправильный IP-адрес')
   else:
      print('Неправильный IP-адрес')
except ZeroDivisionError:
   if ip_int == "0000":
            print('unassigned')
except ValueError:
    print('Неправильный IP-адрес')
except IndexError:
   print('Неправильный IP-адрес')