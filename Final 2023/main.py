import psutil
import ctypes
from ctypes import wintypes
import time
import os
from weekly_stats import weekly
from func_data_time import data_time

def reporter():
    file = "report_" + user_name + ".txt"
    with open(file, "a", encoding="utf8") as file:
        file.write(
             '__________________________' + '\n' + "C " + start + ' По ' + start + '\n' +
                "Telegram: " + str(round(time_spend_tg / 60, 2)) + '\n' + "Atom: " + str(round(time_spend_atom / 60, 2)) + '\n' +
                "PyCharm: " + str(round(time_spend_pycharm / 60, 2)) + '\n' + "Opera GX: " + str(round(time_spend_opera_gx / 60, 2)) + '\n' +
                "Visual Studio Code: " + str(round(time_spend_vs_code / 60, 2)) + '\n' + "Steam: " + str(round(time_spend_steam / 60, 2)) + '\n' +
                "Discord: " + str(round(time_spend_discord / 60, 2)) + '\n' + "Yandex Browser: " + str(round(time_spend_yandex / 60, 2)) + '\n')
    print(start, "Цикл остановлен")
    print("Telegram: ", round(time_spend_tg / 60, 2), "минут.", "Atom: ", round(time_spend_atom / 60, 2), "минут.",
          "PyCharm: ", round(time_spend_pycharm / 60, 2), "минут.", "Opera GX: ", round(time_spend_opera_gx / 60, 2), "минут.",
          "Visual Studio Code: ", round(time_spend_vs_code / 60, 2), "минут.", "Steam: ", round(time_spend_steam / 60, 2), "минут.",
          "Discord: ", round(time_spend_discord / 60, 2), "минут.", "Yandex Browser: ", round(time_spend_yandex / 60, 2), "минут.")

def write_temp():
    tmp = "temp.txt"
    with open(tmp, "w", encoding="utf8") as file:
        file.write('\n' + "C " + start + ' По ' + start + '\n' +
                   "Telegram: " + str(round(time_spend_tg / 60, 2)) + '\n' + "Atom: " + str(round(time_spend_atom / 60, 2)) + '\n' +
                   "PyCharm: " + str(round(time_spend_pycharm / 60, 2)) + '\n' + "Opera GX: " + str(round(time_spend_opera_gx / 60, 2)) + '\n' +
                   "Visual Studio Code: " + str(round(time_spend_vs_code / 60, 2)) + '\n' + "Steam: " + str(round(time_spend_steam / 60, 2)) + '\n' +
                   "Discord: " + str(round(time_spend_discord / 60, 2)) + '\n' + "Yandex Browser: " + str(round(time_spend_yandex / 60, 2)) + '\n')


start = data_time()
user_name = os.getlogin()
print(start, "Старт, пользователь: ", user_name, ", что-бы завершить нажми CTRL-C")
time_spend_tg = 0
time_spend_atom = 0
time_spend_pycharm = 0
time_spend_opera_gx = 0
time_spend_vs_code = 0
time_spend_steam = 0
time_spend_discord = 0
time_spend_yandex = 0
try:
    while True:
        pid = wintypes.DWORD()
        active = ctypes.windll.user32.GetForegroundWindow()
        active_window = ctypes.windll.user32.GetWindowThreadProcessId(active, ctypes.byref(pid))
        pid = pid.value

        for item in psutil.process_iter():
            if pid == item.pid:
                process_name = item.name()
                if process_name == "Telegram.exe":
                    time_spend_tg = time_spend_tg + 1
                    write_temp()
                    print(start, "Active Telegram", end='\r')
                elif process_name == "aCentral (new).exe":
                    time_spend_atom = time_spend_atom + 1
                    write_temp()
                    print(start, "Active ATOM", end='\r')
                elif process_name == "pycharm64.exe":
                    time_spend_pycharm = time_spend_pycharm + 1
                    write_temp()
                    print(start, "Active PyCharm  ", end='\r')
                elif process_name == "opera.exe":
                    time_spend_opera_gx = time_spend_opera_gx + 1
                    write_temp()
                    print(start, "Active Opera GX", end='\r')
                elif process_name == "code.exe":
                    time_spend_vs_code = time_spend_vs_code + 1
                    write_temp()
                    print(start, "Active Visual studio code", end='\r')
                elif process_name == "Discord.exe":
                    time_spend_discord = time_spend_discord + 1
                    write_temp()
                    print(start, "Active discord", end='\r')
                elif process_name == "steam.exe":
                    time_spend_steam = time_spend_steam + 1
                    write_temp()
                    print(start, "Active steam", end='\r')
                elif process_name == "browser.exe":
                    time_spend_yandex = time_spend_yandex + 1
                    write_temp()
                    print(start, "Active Yandex", end='\r')
                else:

                    print(start, "Prog Not Active", end='\r')
        time.sleep(1)

except KeyboardInterrupt:
    reporter()
    weekly()