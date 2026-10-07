"""
Quantum Computing Lab
Temel kuantum kavramları.
"""

from math import sqrt


def zero_state():
    """|0> kuantum durumunu döndürür."""
    return [1, 0]


def one_state():
    """|1> kuantum durumunu döndürür."""
    return [0, 1]


def hadamard_state():
    """
    |0> durumunu Hadamard ile
    süperpozisyona sokar.
    """

    value = 1 / sqrt(2)

    return [value, value]


def probability(amplitude):
    """Kuantum genliğinden olasılık hesaplar."""
    return amplitude ** 2


if __name__ == "__main__":

    print("Quantum Computing Lab")
    print("---------------------")

    print("|0> =", zero_state())
    print("|1> =", one_state())

    state = hadamard_state()

    print("|+> =", state)

    print("P(0) =", probability(state[0]))
    print("P(1) =", probability(state[1]))