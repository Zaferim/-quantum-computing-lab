"""
Quantum Computing Lab
Klasik optimizasyon temeli.

Bu bölümde önce klasik bilgisayarla
optimizasyon yapacağız.
Daha sonra aynı problemi kuantum
yöntemleriyle karşılaştıracağız.
"""


def calculate_score(values):
    """
    Bir değer listesinin toplam skorunu hesaplar.
    """

    if not values:
        return 0

    return sum(values)


def find_best(values):
    """
    Listedeki en yüksek değeri bulur.
    """

    if not values:
        return None

    return max(values)


def optimize(values):
    """
    Basit klasik optimizasyon.

    Şimdilik en yüksek skoru seçiyoruz.
    """

    best = find_best(values)

    return {
        "best_value": best,
        "score": calculate_score(values)
    }


if __name__ == "__main__":

    values = [10, 25, 18, 42, 31]

    result = optimize(values)

    print("Classical Optimization")
    print("----------------------")

    print(
        "Values:",
        values
    )

    print(
        "Best value:",
        result["best_value"]
    )

    print(
        "Total score:",
        result["score"]
    )