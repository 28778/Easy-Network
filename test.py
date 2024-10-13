# 通过用户输入的IP地址和子网掩码，实现：
# 1.IP地址/子网掩码自动转换二进制（互相转换）

# \033[1;34m+------------------------\033[0m
# \033[1;34m+========================\033[0m
# \033[1;34m|\033[0m

import re
print(
    "\033[1;34m+=========START==========\033[0m\n\033[1;34m|\033[0m 请输入需要转换的\n\033[1;34m|\033[0m "
    "例如：192.168.1.1\n\033[1;34m|\033[0m 例如：19\n\033[1;34m|\033[0m 例如：11101110.00010001.00000001.00000001\n\033["
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


while True:
    users_input_ = input("\033[1;34m|\033[0m Users:")
    if users_input_ == "":
        continue
    elif users_input_ == "exit":
        break
    else:
        print(trans(users_input_))
