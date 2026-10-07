"""
Quantum Computing Lab
Temel kuantum kavramları
"""

from math import sqrt


def zero_state():
    """
    |0> kuantum durumunu temsil eder.

    |0> = [1, 0]
    """
    return [1, 0]


def one_state():
    """
    |1> kuantum durumunu temsil eder.

    |1> = [0, 1]
    """
    return [0, 1]


def hadamard_state():
    """
    Hadamard kapısından sonra oluşan
    temel süperpozisyon durumunu döndürür.

    |+> = 1/sqrt(2) [1, 1]
    """
    value = 1 / sqrt(2)

    return [value, value]


def probability(amplitude):
    """
    Bir genlikten ölçüm olasılığı hesaplar.
    """
    return amplitude ** 2


if __name__ == "__main__":

    print("Quantum Computing Lab")
    print("--------------------")

    print("|0> =", zero_state())
    print("|1> =", one_state())

    state = hadamard_state()

    print("|+> =", state)

    print(
        "0 ölçüm olasılığı:",
        probability(state[0])
    )

    print(
        "1 ölçüm olasılığı:",
        probability(state[1])
    )