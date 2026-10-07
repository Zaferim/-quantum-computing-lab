"""
Quantum Computing Lab
İlk kuantum algoritması örneği
"""

from .circuits import create_superposition


def measure_superposition():
    """
    Süperpozisyon durumunun ölçüm
    olasılıklarını hesaplar.
    """

    state = create_superposition()

    probabilities = []

    for amplitude in state:
        probabilities.append(
            amplitude ** 2
        )

    return probabilities


def run_first_algorithm():
    """
    İlk kuantum algoritması.

    |0> → Hadamard → |+>

    Ölçüm sonucunda:

    P(0) = 50%
    P(1) = 50%
    """

    probabilities = measure_superposition()

    return {
        "state": "|+>",
        "probability_0": probabilities[0],
        "probability_1": probabilities[1]
    }


if __name__ == "__main__":

    result = run_first_algorithm()

    print("First Quantum Algorithm")
    print("-----------------------")

    print("State:", result["state"])

    print(
        "P(0):",
        result["probability_0"] * 100,
        "%"
    )

    print(
        "P(1):",
        result["probability_1"] * 100,
        "%"
    )