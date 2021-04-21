from datetime import datetime, time, timedelta
import time as t
import sys
import os

os.system('mode 50, 15')
os.system('color')
clear = lambda: os.system('cls')
now = datetime.now()
clockSpeed = 3.75

try:
    userTimeInput = datetime.strptime(input('Сколько показывают часы сейчас?\n(Формат: ЧЧММ | Например: 1345)\n'), "%H%M")
except:
    print("Пожалуйста, введите время в формате ЧЧММ (Например: 1345)")

if userTimeInput.strftime("%H:%M") > now.strftime("%H:%M"):
    print("Часы показывают большее время, чем на самом деле\nСтоит остановить их")
    t.sleep(5)
    sys.exit()
clear()
while userTimeInput.strftime("%H:%M:%S") < now.strftime("%H:%M:%S"):
    clockTimeInSeconds = 60*60*int(userTimeInput.strftime("%H")) + 60*int(userTimeInput.strftime("%M")) + int(userTimeInput.strftime("%S")) # Переводим часы и минуты башни в секунды, складываем с уже имеющимися секундами)
    theDifference = now - timedelta(seconds=clockTimeInSeconds) # Высчитываем разницу между башней и реальным временем
    print(f"Время на башне: {userTimeInput.strftime('%H:%M:%S')} (Отставание: {theDifference.strftime('%H:%M:%S')})")
    print('')
    os.system('curl "http://192.168.1.119/cmd.cgi?cmd=REL,1,1"')
    t.sleep(3)
    os.system('curl "http://192.168.1.119/cmd.cgi?cmd=REL,1,0"')
    t.sleep(0.1)
    userTimeInput = userTimeInput + timedelta(seconds=clockSpeed)*3.1 # Добавляем к введенному пользователем времени скорость прокрутки и умножаем на t.sleep
    now = datetime.now() # Обновляем текущее время
    clear()
if userTimeInput.strftime("%H:%M") == now.strftime("%H:%M"):
    print("Часы идут ровно. Закрытие через 5 сек.")
    t.sleep(5)
    sys.exit()