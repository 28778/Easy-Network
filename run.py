import datetime
import random
import re


def usrInput():
    usr_name = input("\033[1;34m>\033[0m 用户名：")
    if usr_name == '':
        return 'RET'
    usr_cell = input("\033[1;34m>\033[0m 用户电话：")
    linux_ver = input("\033[1;34m>\033[0m Linux版本：")
    web_framework = input("\033[1;34m>\033[0m 网站框架：")
    usr_use = input("\033[1;34m>\033[0m 用户用途：")
    print('\033[1;34m>\033[0m -------------------')
    usr_order = str((datetime.datetime.now().strftime('%Y%m')) + '-' + str("".join(list(usr_cell)[-4:])) + '-' + str(
        random.randint(1000, 9999)))
    return [usr_order, usr_name, usr_cell, linux_ver, web_framework, usr_use]


def usrPrint():  # 输入完整列表
    with open("access.txt", "r") as f_:
        usr_list_ = f_.read()

    for i in usr_list_.split(';'):
        if i == '\n':
            print('>')
            break
        else:
            print('>')
            for j in [i.split(',')]:
                print('\033[1;34m>\033[0m  单号 ' + j[0][-18:])
                print('\033[1;34m>\033[0m  用户' + j[1])
                print('\033[1;34m>\033[0m  电话' + j[2])
                print('\033[1;34m>\033[0m  Linux版本' + j[3])
                print('\033[1;34m>\033[0m  框架' + j[4])
                print('\033[1;34m>\033[0m  用途' + j[5][:-1])


def wlRun():
    print('\033[1;34m>\033[0m  /$$      /$$           /$$             /$$       /$$             /$$    \n'
          '\033[1;34m>\033[0m | $$  /$ | $$          | $$            | $$      |__/            | $$    \n'
          '\033[1;34m>\033[0m | $$ /$$$| $$  /$$$$$$ | $$$$$$$       | $$       /$$  /$$$$$$$ /$$$$$$  \n'
          '\033[1;34m>\033[0m | $$/$$ $$ $$ /$$__  $$| $$__  $$      | $$      | $$ /$$_____/|_  $$_/  \n'
          '\033[1;34m>\033[0m | $$$$_  $$$$| $$$$$$$$| $$  \\ $$      | $$      | $$|  $$$$$$   | $$    \n'
          '\033[1;34m>\033[0m | $$$/ \\  $$$| $$_____/| $$  | $$      | $$      | $$ \\____  $$  | $$ /$$\n'
          '\033[1;34m>\033[0m | $$/   \\  $$|  $$$$$$$| $$$$$$$/      | $$$$$$$$| $$ /$$$$$$$/  |  $$$$/\n'
          '\033[1;34m>\033[0m |__/     \\__/ \\_______/|_______/       |________/|__/|_______/    \\___/  \n\033[1;34m>\033[0m '
          )
    print('\033[1;34m>\033[0m WELCOME TO WEB LIST!')
    while True:
        acc = usrInput()
        if acc == 'RET':
            break
        else:
            with open("access.txt", "a") as fi:
                fi.writelines('test_number:' + str(acc) + ';' + '\n')


def netWorkKit():
    print("\033[1;34m>\033[0m  _   _      ___          __        _      _  ___ _   ")
    print("\033[1;34m>\033[0m | \\ | |    | \\ \\        / /       | |    | |/ (_) |  ")
    print("\033[1;34m>\033[0m |  \\| | ___| |\\ \\  /\\  / /__  _ __| | __ | ' / _| |_ ")
    print("\033[1;34m>\033[0m | . ` |/ _ \\ __\\ \\/  \\/ / _ \\| '__| |/ / |  < | | __|")
    print("\033[1;34m>\033[0m | |\\  |  __/ |_ \\  /\\  / (_) | |  |   <  | . \\| | |_ ")
    print("\033[1;34m>\033[0m |_| \\_|\\___|\\__| \\/  \\/ \\___/|_|  |_|\\_\\ |_|\\_\\_|\\__|")

    print(
        "\033[1;34m+------------------------\033[0m\n\033[1;34m|\033[0m 请输入需要转换的\n\033[1;34m|\033[0m "
        "例如：192.168.1.1\n\033[1;34m|\033[0m 例如：19\n\033[1;34m|\033[0m 例如：11101110.00010001.00000001.00000001\n\033[1;34m|\033[0m 输入exit退出\n\033["
        "1;34m+------------------------\033[0m")

    def check_input_format(input_str):  # 判断是否是IP地址或子网掩码
        # 正则表达式用于匹配IP地址
        ip_pattern = r"^\d{1,3}(\.\d{1,3}){3}$"
        # 正则表达式用于匹配二进制子网掩码
        binary_subnet_pattern = r"^[01]{8}(\.[01]{8}){3}$"
        # 正则表达式用于匹配十进制子网掩码
        decimal_subnet_pattern = r"^\d+$"
        if re.match(ip_pattern, input_str):
            return "ip"
        elif re.match(binary_subnet_pattern, input_str):
            return "bin"
        elif re.match(decimal_subnet_pattern, input_str):
            return "oct"
        else:
            return "None"

    def trans(users_input):  # 转换各个

        if check_input_format(users_input) == "ip":  # 如果是IP
            transition = users_input.split(".")
            bin_parts = [bin(int(part))[2:].zfill(8) for part in transition]
            formatted_ip = ".".join(bin_parts)
            return f"\033[1;34m+------------------------\033[0m\n\033[1;34m|\033[0m [二进制IP地址]\n\033[1;34m|\033[0m {formatted_ip} \n\033[1;34m+------------------------\033[0m"

        elif check_input_format(users_input) == "bin":  # 如果是二进制
            li = []
            for i in users_input.split("."):
                int_parts = int(i, 2)
                li.append(int_parts)
            return f"\033[1;34m+------------------------\033[0m\n\033[1;34m|\033[0m [十进制IP地址]\n\033[1;34m|\033[0m {'.'.join(map(str, li))} \n\033[1;34m+------------------------\033[0m"

        elif check_input_format(users_input) == "oct":  # 如果是子网掩码
            bin_subnet = "1" * int(users_input) + "0" * (32 - int(users_input))
            binary_subnet_with_dot = ".".join([bin_subnet[i:i + 8] for i in range(0, 32, 8)])
            return f"\033[1;34m+------------------------\033[0m\n\033[1;34m|\033[0m [二进制子网掩码]\n\033[1;34m|\033[0m {binary_subnet_with_dot} \n\033[1;34m+------------------------\033[0m"
        else:
            return '\033[1;34m|\033[0m [NetWork]请使用LittleKit进行算数操作.'

    while True:
        users_input_ = input("\033[1;34m|\033[0m [NetWork]")
        if users_input_ == "":
            continue
        elif users_input_ == "exit":
            print('\033[1;34m+------------------------\033[0m')
            break
        else:
            print(trans(users_input_))


def ui():
    while True:
        acc = input('\033[1;34m[User]\033[0m')
        if acc == 'weblist' or acc == 'wl':
            wlRun()
        elif acc == 'print' or acc == 'pr':
            usrPrint()
        elif acc == 'clear' or acc == 'cl':
            for i in range(50):
                print("\n")
        elif acc == 'network' or acc == 'nw':
            netWorkKit()
        elif acc == 'help':
            print(
                '\033[1;34m>\033[0m[计算公式] 直接输入算式 \n\033[1;34m>\033[0m[表单工具] weblist\n\033[1;34m>\033[0m[网络工具] network\n\033[1;34m>\033[0m[打印单子] print\n\033[1;34m>\033[0m[清除屏幕] clear')
        else:
            try:
                print('\033[1;34m[User]\033[0m' + str(acc) + '=' + str(eval(acc)))
            except SyntaxError:
                continue
            except NameError:
                print('\033[1;34m[User]\033[0m' + '错误：未知的指令')


print("\n"
      "██╗     ██╗████████╗████████╗██╗     ███████╗    ██╗  ██╗██╗████████╗\n"
      "██║     ██║╚══██╔══╝╚══██╔══╝██║     ██╔════╝    ██║ ██╔╝██║╚══██╔══╝\n"
      "██║     ██║   ██║      ██║   ██║     █████╗      █████╔╝ ██║   ██║   \n"
      "██║     ██║   ██║      ██║   ██║     ██╔══╝      ██╔═██╗ ██║   ██║   \n"
      "███████╗██║   ██║      ██║   ███████╗███████╗    ██║  ██╗██║   ██║   \n"
      "╚══════╝╚═╝   ╚═╝      ╚═╝   ╚══════╝╚══════╝    ╚═╝  ╚═╝╚═╝   ╚═╝   ")
print('v1.0 input "help" to read more command\n')
ui()
