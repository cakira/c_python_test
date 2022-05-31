from environment.environment import get_color_a, get_color_b


def get_result():
    color_a = get_color_a()
    color_b = get_color_b()
    color = []
    color.append(list(get_rgb_from_hex(color_a)))
    color.append(list(get_rgb_from_hex(color_b)))
    color_add = [color[0][i] + color[1][i] for i in range(3)]
    return get_hex_from_rgb(color_add)


def get_rgb_from_hex(hex_string):
    red_hex = hex_string[1:3]
    green_hex = hex_string[3:5]
    blue_hex = hex_string[5:7]
    return (hex2int(red_hex), hex2int(green_hex), hex2int(blue_hex))


def hex2int(hex_value):
    return int(hex_value, 16)


def get_hex_from_rgb(rgb_list):
    return f'#{rgb_list[0]:02x}{rgb_list[1]:02x}{rgb_list[2]:02x}'
