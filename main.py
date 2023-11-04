# 通过用户输入的IP地址和子网掩码，实现：
# 1.IP地址/子网掩码自动转换二进制（互相转换）
import re


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


True_False = "1"
while True_False == "1":
    users_input = input("\033[1;34m+=========START==========\033[0m\n\033[1;34m|\033[0m 请输入需要转换的\n\033[1;34m|\033[0m 例如：192.168.1.1\n\033[1;34m|\033[0m 例如：19\n\033[1;34m|\033[0m 例如：11101110.00010001.00000001.00000001\n\033[1;34m+------------------------\033[0m\n\033[1;34m|\033[0m 输入：")
    # \033[1;34m+------------------------\033[0m
    # \033[1;34m+========================\033[0m
    # \033[1;34m|\033[0m
    # 转换开始
    if check_input_format(users_input) == "ip":  # 如果是IP
        transition = users_input.split(".")
        bin_parts = [bin(int(part))[2:].zfill(8) for part in transition]
        formatted_ip = ".".join(bin_parts)
        True_False = input(f"\033[1;34m+------------------------\033[0m\n\033[1;34m|\033[0m [二进制IP地址]\n\033[1;34m|\033[0m {formatted_ip} \n\033[1;34m+------------------------\033[0m\n\033[1;34m|\033[0m 键入'1'重新开始\n\033[1;34m|\033[0m 输入：")

    elif check_input_format(users_input) == "bin":  # 如果是二进制
        transition = users_input.split(".")
        oct_parts = [oct(int(part))[2:].zfill(8) for part in transition]
        formatted_ip = ".".join(oct_parts)
        True_False = input(f"\033[1;34m+------------------------\033[0m\n\033[1;34m|\033[0m [十进制IP地址]\n\033[1;34m|\033[0m {formatted_ip} \n\033[1;34m+------------------------\033[0m\n\033[1;34m|\033[0m 键入'1'重新开始\n\033[1;34m|\033[0m 输入：")

    elif check_input_format(users_input) == "oct":  # 如果是子网掩码
        bin_subnet = "1" * int(users_input) + "0" * (32 - int(users_input))
        binary_subnet_with_dot = ".".join([bin_subnet[i:i + 8] for i in range(0, 32, 8)])
        True_False = input(f"\033[1;34m+------------------------\033[0m\n\033[1;34m|\033[0m [二进制子网掩码]\n\033[1;34m|\033[0m {binary_subnet_with_dot} \n\033[1;34m+------------------------\033[0m\n\033[1;34m|\033[0m 键入'1'重新开始，或键入其他结束\n\033[1;34m|\033[0m 输入：")
    elif check_input_format(users_input) == "None":  # 如果不存在
        input("\033[1;34m+------------------------\033[0m\n\033[1;34m|\033[0m 无效的，请键入回车重新开始\n\033[1;34m|\033[0m 输入：")
        continue
