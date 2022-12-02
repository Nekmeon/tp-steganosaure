"""Bits manipulation utilities."""

import numpy

from steganosaure.bits_manipulation import (
    modify_least_significant_bits,
    pad_message,
    retrieve_least_significant_bits,
)


def test_retrieve_least_significant_bits() -> None:
    numpy.testing.assert_array_equal(
        retrieve_least_significant_bits(numpy.array([1, 3, 2])), numpy.array([1, 1, 0])
    )


def test_modify_least_significant_bits() -> None:
    numpy.testing.assert_array_equal(
        modify_least_significant_bits(numpy.array([1, 1, 0]), numpy.array([1, 2, 3])),
        numpy.array([1, 3, 2]),
    )


def test_pad_message() -> None:
    numpy.testing.assert_array_equal(
        pad_message(numpy.arange(10), numpy.array([1, 1, 0])),
        numpy.array([1, 1, 0, 0, 0, 0, 0, 0, 0, 0]),
    )
