#!/usr/bin/env python3
"""Exact sanity anchors for the revised OB-44B prompt.

The script checks the canonical normalization, graded factorization, moment
closed form, clean-carrier valuations, and one CRT-poisoned configuration.
It is finite sanity evidence only, not a proof.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations
from math import gcd

RationalComplex = tuple[Fraction, Fraction]


def zadd(x: RationalComplex, y: RationalComplex) -> RationalComplex:
    return x[0] + y[0], x[1] + y[1]


def zsub(x: RationalComplex, y: RationalComplex) -> RationalComplex:
    return x[0] - y[0], x[1] - y[1]


def zmul(x: RationalComplex, y: RationalComplex) -> RationalComplex:
    return x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0]


def zpow(x: RationalComplex, exponent: int) -> RationalComplex:
    result: RationalComplex = (Fraction(1), Fraction(0))
    for _ in range(exponent):
        result = zmul(result, x)
    return result


def zconjugate(x: RationalComplex) -> RationalComplex:
    return x[0], -x[1]


def chebyshev_coefficients(degree: int) -> list[Fraction]:
    """Low-to-high coefficients of T_degree."""
    if degree < 0:
        raise ValueError("degree must be nonnegative")
    previous: list[Fraction] = [Fraction(1)]
    if degree == 0:
        return previous
    current = [Fraction(0), Fraction(1)]
    for _ in range(2, degree + 1):
        shifted = [Fraction(0), *[Fraction(2) * value for value in current]]
        padded_previous = [
            *previous,
            *([Fraction(0)] * (len(shifted) - len(previous))),
        ]
        new = [
            left - right
            for left, right in zip(shifted, padded_previous)
        ]
        previous = current
        current = new
    return current


def quotient_by_x_minus_one(coefficients: list[Fraction]) -> list[Fraction]:
    """Divide a polynomial vanishing at 1 by x-1; low-to-high output."""
    size = len(coefficients)
    result = [Fraction(0)] * (size - 1)
    running = coefficients[-1]
    result[-1] = running
    for index in range(size - 2, -1, -1):
        running = coefficients[index] + running
        if index > 0:
            result[index - 1] = running
    return result


def graded_matrix(order: int) -> list[list[Fraction]]:
    """The matrix B in OB-44B, padded to width order."""
    matrix: list[list[Fraction]] = []
    for degree in range(1, order + 1):
        cheb = chebyshev_coefficients(degree)
        numerator = [Fraction(1) - cheb[0]] + [-value for value in cheb[1:]]
        quotient = quotient_by_x_minus_one(numerator)
        scaled = [Fraction(4) * value for value in quotient]
        matrix.append([*scaled, *([Fraction(0)] * (order - len(scaled)))])
    return matrix


def determinant(matrix: list[list[Fraction]]) -> Fraction:
    """Exact determinant by rational Gaussian elimination."""
    size = len(matrix)
    work = [row[:] for row in matrix]
    sign = 1
    for column in range(size):
        pivot_row = next(
            (row for row in range(column, size) if work[row][column] != 0),
            None,
        )
        if pivot_row is None:
            return Fraction(0)
        if pivot_row != column:
            work[column], work[pivot_row] = work[pivot_row], work[column]
            sign *= -1
        pivot = work[column][column]
        for row in range(column + 1, size):
            scale = Fraction(work[row][column]) / Fraction(pivot)
            for next_column in range(column, size):
                work[row][next_column] -= scale * work[column][next_column]
    result = Fraction(sign)
    for index in range(size):
        result *= work[index][index]
    return result


def p_valuation(value: Fraction, prime: int) -> int:
    if value == 0:
        raise ValueError("zero has no finite valuation here")

    def integer_valuation(integer: int) -> int:
        result = 0
        while integer % prime == 0:
            integer //= prime
            result += 1
        return result

    return integer_valuation(value.numerator) - integer_valuation(value.denominator)


def orbit_vector(a: int, n: int, order: int) -> list[Fraction]:
    sigma = Fraction(a, n)
    atoms: tuple[RationalComplex, ...] = (
        (sigma, Fraction(1)),
        (sigma, Fraction(-1)),
        (Fraction(1) - sigma, Fraction(1)),
        (Fraction(1) - sigma, Fraction(-1)),
    )
    vector: list[Fraction] = []
    one: RationalComplex = (Fraction(1), Fraction(0))
    for degree in range(1, order + 1):
        total: RationalComplex = (Fraction(0), Fraction(0))
        for rho in atoms:
            norm = zmul(rho, zconjugate(rho))[0]
            inverse: RationalComplex = (rho[0] / norm, -rho[1] / norm)
            base = zsub(one, inverse)
            power = zpow(base, degree)
            term = zsub(one, power)
            total = zadd(total, term)
        vector.append(Fraction(2) * total[0])
    return vector


def moment_closed_form(a: int, n: int, order: int) -> list[Fraction]:
    gaussian: RationalComplex = (
        Fraction(a * a - n * n - n * a),
        Fraction(n * (2 * a - n)),
    )
    norm = zmul(gaussian, zconjugate(gaussian))[0]
    beta: RationalComplex = zmul(
        (Fraction(n * n) / (2 * norm), Fraction(0)),
        zconjugate(gaussian),
    )
    values: list[Fraction] = []
    for degree in range(order):
        left = zmul(
            beta,
            zpow(zadd((Fraction(1), Fraction(0)), beta), degree),
        )
        beta_bar = zconjugate(beta)
        right = zmul(
            beta_bar,
            zpow(zadd((Fraction(1), Fraction(0)), beta_bar), degree),
        )
        values.append((left[0] + right[0]))
    return values


def multiply_matrix_vector(
    matrix: list[list[Fraction]], vector: list[Fraction]
) -> list[Fraction]:
    return [
        sum((entry * vector[column] for column, entry in enumerate(row)), Fraction(0))
        for row in matrix
    ]


def node_x(node: Fraction) -> Fraction:
    square = node * node
    return (Fraction(4) * square - 1) / (Fraction(4) * square + 1)


def elementary_symmetric(values: list[Fraction], degree: int) -> Fraction:
    """Return e_degree(values), exactly."""
    if degree == 0:
        return Fraction(1)
    if not values or degree < 0:
        return Fraction(0)
    return sum(
        (
            values[index] * elementary_symmetric(values[index + 1 :], degree - 1)
            for index in range(len(values) - degree + 1)
        ),
        Fraction(0),
    )


def multiply_matrices(
    left: list[list[Fraction]], right: list[list[Fraction]]
) -> list[list[Fraction]]:
    size = len(right)
    return [
        [
            sum(
                (
                    left[row][index] * right[index][column]
                    for index in range(size)
                ),
                Fraction(0),
            )
            for column in range(size)
        ]
        for row in range(len(left))
    ]


def observation_matrix(
    nodes: list[Fraction], a: int, n: int, order: int | None = None
) -> tuple[list[list[int]], list[int], int]:
    if order is None:
        order = len(nodes)
    if not 2 <= order <= len(nodes):
        raise ValueError("order must satisfy 2 <= order <= number of nodes")
    # Use a direct exact Chebyshev recurrence; no floating point is involved.
    rational_columns = []
    for node in nodes:
        x = node_x(node)
        chebs: list[Fraction] = [Fraction(1), x]
        for degree in range(2, order + 1):
            chebs.append(Fraction(2) * x * chebs[-1] - chebs[-2])
        rational_columns.append(
            [
                Fraction(4) * (Fraction(1) - chebs[degree])
                for degree in range(1, order + 1)
            ]
        )
    d_vector = orbit_vector(a, n, order)
    entries = [value for column in rational_columns for value in column]
    entries.extend(d_vector)
    common = 1
    for value in entries:
        denominator = value.denominator
        common = common * denominator // gcd(common, denominator)
    integer_columns = [
        [int(value * common) for value in column] for column in rational_columns
    ]
    integer_d = [int(value * common) for value in d_vector]
    return integer_columns, integer_d, common


def determinantal_divisor(
    columns: list[list[int]], order: int
) -> int:
    """GCD of all order-by-order minors of the column sequence."""
    result = 0
    for column_indices in combinations(range(len(columns)), order):
        rows = [
            [columns[column][row] for column in column_indices]
            for row in range(order)
        ]
        result = gcd(result, abs(int(determinant(rows))))
    return result


def q_min(
    nodes: list[Fraction], a: int, n: int, order: int | None = None
) -> int:
    columns, d_vector, _ = observation_matrix(nodes, a, n, order)
    if order is None:
        order = len(nodes)
    numerator = determinantal_divisor(columns, order)
    denominator = determinantal_divisor(columns + [d_vector], order)
    if denominator == 0 or numerator % denominator != 0:
        raise AssertionError("invalid q_min ratio")
    return numerator // denominator


def check() -> None:
    a, n = 1, 10
    order = 3
    matrix_b = graded_matrix(order)
    d_vector = orbit_vector(a, n, order)
    moments = moment_closed_form(a, n, order)
    assert multiply_matrix_vector(matrix_b, moments) == d_vector

    clean_nodes = [Fraction(1), Fraction(2), Fraction(3)]
    xs = [node_x(node) for node in clean_nodes]
    vandermonde = [
        [x ** degree for x in xs] for degree in range(order)
    ]
    diagonal = [
        [Fraction(0) if row != column else xs[column] - 1 for column in range(order)]
        for row in range(order)
    ]
    factored = multiply_matrices(multiply_matrices(matrix_b, vandermonde), diagonal)
    rational_columns: list[list[Fraction]] = []
    for node in clean_nodes:
        x = node_x(node)
        chebs: list[Fraction] = [Fraction(1), x]
        for degree in range(2, order + 1):
            chebs.append(Fraction(2) * x * chebs[-1] - chebs[-2])
        rational_columns.append(
            [Fraction(4) * (Fraction(1) - chebs[degree]) for degree in range(1, order + 1)]
        )
    assert [list(column) for column in zip(*factored)] == rational_columns

    arbitrary_w = [Fraction(7, 5), Fraction(-3, 2), Fraction(11, 7)]
    arbitrary_d = multiply_matrix_vector(matrix_b, arbitrary_w)
    for replaced in range(order):
        direct_rows = [row[:] for row in factored]
        for row in range(order):
            direct_rows[row][replaced] = arbitrary_d[row]
        direct_minor = determinant(direct_rows)

        remaining = [value for index, value in enumerate(xs) if index != replaced]
        reduced_vandermonde = determinant(
            [[value**degree for value in remaining] for degree in range(order - 1)]
        )
        alternating_sum = sum(
            (
                Fraction((-1) ** (row + replaced))
                * elementary_symmetric(remaining, order - 1 - row)
                * arbitrary_w[row]
                for row in range(order)
            ),
            Fraction(0),
        )
        product = Fraction(1)
        for index in range(order):
            if index != replaced:
                product *= xs[index] - 1
        formula_minor = (
            determinant(matrix_b)
            * product
            * reduced_vandermonde
            * alternating_sum
        )
        assert direct_minor == formula_minor

    clean_q = q_min(clean_nodes, a, n)
    assert p_valuation(Fraction(clean_q), 101) >= order
    assert p_valuation(Fraction(clean_q), 181) >= order

    poisoned_nodes = [Fraction(17276), Fraction(1)]
    poisoned_q = q_min(poisoned_nodes, a, n)
    assert p_valuation(Fraction(poisoned_q), 101) == 1
    assert p_valuation(Fraction(poisoned_q), 181) == 1

    sharp_nodes = [Fraction(19286), Fraction(26164)]
    sharp_q = q_min(sharp_nodes, a, n)
    assert sharp_q == 18
    assert p_valuation(Fraction(sharp_q), 101) == 0
    assert p_valuation(Fraction(sharp_q), 181) == 0
    columns, d_vector, _ = observation_matrix(sharp_nodes, a, n)
    coefficients = (-1788723758742137225, 3292056116081922725)
    for row in range(2):
        relation_value = (
            columns[0][row] * coefficients[0]
            + columns[1][row] * coefficients[1]
            + sharp_q * d_vector[row]
        )
        assert relation_value == 0

    rectangular_nodes = [Fraction(1005), Fraction(7883), Fraction(-10398)]
    rectangular_q = q_min(rectangular_nodes, a, n, order=2)
    rectangular_coefficients = (
        -339609544170,
        16156893919328,
        8242578942472,
    )
    columns, d_vector, _ = observation_matrix(
        rectangular_nodes, a, n, order=2
    )
    assert rectangular_q == 1
    for row in range(2):
        assert (
            sum(
                columns[column][row] * rectangular_coefficients[column]
                for column in range(3)
            )
            + d_vector[row]
            == 0
        )

    print(f"PASS: B*w=d and A=BVdiag(x-1) for m={order}")
    print("PASS: replacement-minor identity for an arbitrary rational w")
    print(f"PASS: clean q_min={clean_q}; v_101=v_181={order}")
    print(
        "PASS: CRT-poisoned q_min="
        f"{poisoned_q}; v_101=v_181=1"
    )
    print(
        "PASS: sharp poisoned q_min=18 with v_101=v_181=0; "
        "exact relation coefficients replayed"
    )
    print(
        "PASS: K=m+1 poisoned configuration has q_min=1; "
        "full relation sup-norm 16156893919328"
    )


if __name__ == "__main__":
    check()
