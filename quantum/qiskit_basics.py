"""
Quantum Computing Lab
Qiskit ile ilk kuantum devresi.
"""

from qiskit import QuantumCircuit


def create_bell_circuit():
    """
    İki qubit arasında Bell durumu oluşturur.

    |00> → H → CX → Bell state
    """

    circuit = QuantumCircuit(2)

    # İlk qubit'i süperpozisyona sok
    circuit.h(0)

    # Qubit'leri dolaştır (entangle)
    circuit.cx(0, 1)

    return circuit


if __name__ == "__main__":

    circuit = create_bell_circuit()

    print("Qiskit Quantum Circuit")
    print("----------------------")

    print(circuit)