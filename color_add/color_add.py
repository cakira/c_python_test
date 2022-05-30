from dataclasses import dataclass


@dataclass
class Color:
    r: int
    g: int
    b: int


def get_result():
    return Color(0, 0, 0)
