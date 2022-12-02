from steganosaure.string_conversion import encode_string
from steganosaure.string_conversion import decode_bits
import numpy

numpy_array = numpy.array([0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0,
                          0, 0, 1, 1])


def test_encode_string() -> None:
    numpy.testing.assert_array_equal(encode_string("ABC"), numpy_array)


def test_decode_bits() -> None:
    numpy.testing.assert_array_equal(decode_bits(numpy_array), "ABC")


def test_encode_decode() -> None:
    assert decode_bits(encode_string("ABC")) == "ABC"
