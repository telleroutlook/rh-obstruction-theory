#!/usr/bin/env python3
"""Exact finite sanity check for Theorem J.

This checks the determinantal-divisor formula on one integer matrix.  It is
not a proof of the abstract theorem.
"""

from __future__ import annotations

from itertools import combinations
from math import gcd
from typing import Sequence

Matrix = list[list[int]]


def determinant(matrix: Sequence[Sequence[int]]) -> int:
    """Return an exact integer determinant using fraction-free Bareiss."""
    size = len(matrix)
    work = [[int(value) for value in row] for row in matrix]
    sign = 1
    previous = 1
    for step in range(size - 1):
        if work[step][step] == 0:
            swap_row = next(
                (row for row in range(step + 1, size) if work[row][step] != 0),
                None,
            )
            if swap_row is None:
                return 0
            work[step], work[swap_row] = work[swap_row], work[step]
            sign *= -1
        pivot = work[step][step]
        for row in range(step + 1, size):
            for column in range(step + 1, size):
                work[row][column] = (
                    pivot * work[row][column]
                    - work[row][step] * work[step][column]
                ) // previous
            work[row][step] = 0
        previous = pivot
    return sign * work[size - 1][size - 1]


def determinantal_divisor(matrix: Matrix, order: int) -> int:
    """Return the GCD of all order-by-order integer minors."""
    if order == 0:
        return 1
    rows, columns = len(matrix), len(matrix[0])
    if order > min(rows, columns):
        return 0
    result = 0
    for chosen_columns in combinations(range(columns), order):
        minor = [
            [matrix[row][column] for column in chosen_columns]
            for row in range(rows)
        ]
        result = gcd(result, abs(determinant(minor)))
    return result


def lattice_index(matrix: Matrix, extra: list[int]) -> int:
    augmented = [row + [value] for row, value in zip(matrix, extra)]
    numerator = determinantal_divisor(matrix, len(matrix))
    denominator = determinantal_divisor(augmented, len(matrix))
    if denominator == 0 or numerator % denominator != 0:
        raise AssertionError("rank assumption failed")
    return numerator // denominator


def in_column_lattice(matrix: Matrix, target: list[int]) -> bool:
    """Small exact solver used only by this finite sanity instance."""
    for a in range(-10, 11):
        for b in range(-10, 11):
            for c in range(-10, 11):
                product = [
                    matrix[row][0] * a + matrix[row][1] * b + matrix[row][2] * c
                    for row in range(len(matrix))
                ]
                if product == target:
                    return True
    return False


def check() -> None:
    matrix: Matrix = [
        [6, 0, 10],
        [0, 6, 15],
    ]
    off_line = [1, 1]
    original_index = lattice_index(matrix, off_line)
    assert original_index == 6

    assert in_column_lattice(matrix, [6, 6])
    for q in range(1, original_index):
        assert not in_column_lattice(matrix, [q, q])

    mutated_index = lattice_index(matrix, [2, 2])
    assert mutated_index == 3
    assert mutated_index != original_index

    print("PASS: exact determinantal-divisor index is 6")
    print("PASS: q=1..5 are rejected and q=6 is accepted")
    print("PASS: adversarial off-line mutation changes the index to 3")


if __name__ == "__main__":
    check()
