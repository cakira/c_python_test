from dataclasses import dataclass
import webcolors


@dataclass
class StaticVariablesWrapper:
    color_a = ''
    color_b = ''


StaticVariables = StaticVariablesWrapper


def set_colors(color_name_a, color_name_b):
    StaticVariables.color_a = webcolors.name_to_hex(color_name_a)
    StaticVariables.color_b = webcolors.name_to_hex(color_name_b)


def get_color_a():
    return StaticVariables.color_a


def get_color_b():
    return StaticVariables.color_b
