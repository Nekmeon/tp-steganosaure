import numpy


def encode_string(string: str) -> numpy.ndarray:
    object_byte = string.encode()
    array = numpy.fromiter(object_byte, dtype="uint8")
    binary_array = numpy.unpackbits(array)
    return binary_array


def decode_bits(bits: numpy.ndarray) -> str:
    array = numpy.packbits(bits)
    string = bytes(array).decode()
    return string
