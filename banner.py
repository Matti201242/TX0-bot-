from colorama import Fore, Style
import platform, os

OsName = platform.system().lower()

def banner():
    if OsName == "windows":
        os.system("cls")
    else:
        os.system("clear")

    print(Fore.LIGHTMAGENTA_EX+"""
⠄⠄⠄⠄⠄⠄⣀⣤⣴⣶⣾⠟⠉⠻⣷⣶⣦⣤⣀⠄⠄⠄⠄⠄⠄
⠄⠄⠄⢀⣴⣾⣿⣿⣿⠟⠁⠄⠄⠄⣨⣿⣿⣿⣿⣷⣦⡀⠄⠄⠄
⠄⠄⣴⣿⣿⣿⣿⠟⠁⠄⠄⠄⣠⣾⣿⣿⣿⠿⣿⣿⣿⣿⣦⠄⠄
⠄⣼⣿⣿⣿⣏⠁⠄⠄⠄⠠⣾⣿⣿⡿⠏⠁⠄⠈⠹⢿⣿⣿⣧⠄
⢸⣿⡿⣿⣿⣿⣷⣄⠄⠄⠄⠈⠻⠋⠄⠄⠄⠄⠄⠄⠄⠙⢿⣿⡇
⡿⠋⠄⠈⠻⣿⣿⣿⣷⣄⠄⠄⠄⠄⠄⢀⣴⣿⣦⡀⠄⠄⠄⠙⢿
    """)
    print(Fore.LIGHTYELLOW_EX+"the sun will rise and we will try again"+Style.RESET_ALL)

banner()
