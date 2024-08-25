from qiskit_ibm_runtime import QiskitRuntimeService, Sampler, options
from qiskit_ibm_runtime.ibm_backend import QuantumCircuit
from qiskit.circuit.library import XOR

N = 5
qc2 = QuantumCircuit(N)
qc2.h(0)

for x in range (1, N):
    qc2.cx(0, x)

qc2.compose(XOR(N, 1), inplace=True)
qc2.measure_all()

program_inputs = {
    "circuits": qc2,
    "circuit_indices": [0]
}

service = QiskitRuntimeService(channel="ibm_quantum", token=IBM-Quantum-API-Key)
options = { 'backend_name': 'ibmq_lima' }

job = service.run(
    program_id="sampler",
    options=options,
    inputs=program_inputs,
)

print(job.result())

