input_str = "192.168.1.1"  # 替换成你的输入

input_type = check_input_format(input_str)

if input_type == "ip":
    # 处理IP地址
    pass
elif input_type == "bin":
    # 处理二进制子网掩码
    pass
elif input_type == "oct":
    # 处理十进制子网掩码
    pass
else:
    print("无效的输入格式")