from .color_add_wrapper import lib, ffi  # pylint: disable-msg = E0611


def get_result():
    color_result = ffi.new('char[8]')
    lib.get_result(color_result)
    return ffi.string(color_result).decode()
