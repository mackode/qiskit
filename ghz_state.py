from qiskit import QuantumCircuit, execute, Aer, QuantumRegister

qc = QuantumCircuit(3, 3)
qc.h(0)
qc.cx(0, 1)
qc.cx(0, 2)
qc.measure_all()

simulator = Aer.get_backend('qasm_simulator')
job = execute(qc, simulator, shots=4000)
result = job.result()
counts = result.get_counts()

print(counts)
