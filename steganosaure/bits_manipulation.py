import numpy


def retrieve_least_significant_bits(array: numpy.ndarray) -> numpy.ndarray:
    return array & 1


def modify_least_significant_bits(message: numpy.ndarray,
                                  image: numpy.ndarray) -> numpy.ndarray:
    return image >> 1 << 1 | message


def pad_message(image: numpy.ndarray, message: numpy.ndarray) -> numpy.ndarray:
    pass
