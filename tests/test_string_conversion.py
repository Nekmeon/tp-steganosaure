import hypothesis
import numpy

from steganosaure.string_conversion import decode_bits, encode_string


def test_encode_empty_string() -> None:
    numpy.testing.assert_array_equal(encode_string(""), numpy.array([]))


def test_decode_empty_bits() -> None:
    numpy.testing.assert_array_equal("", decode_bits(numpy.array([])))


def test_encode_string() -> None:
    numpy.testing.assert_array_equal(
        encode_string("ABC"),
        numpy.array(
            [0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1]
        ),
    )


def test_decode_bits() -> None:
    assert (
        decode_bits(
            numpy.array(
                [0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1]
            )
        )
        == "ABC"
    )


@hypothesis.given(hypothesis.strategies.text())
def test_encode_decode(text: str) -> None:
    assert text == decode_bits(encode_string(text))
