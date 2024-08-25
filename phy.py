from qiskit import IBMQ

provider = IBMQ.load_account()
provider = IBMQ.get_provider(hub='ibm-q')
print(provider.backends())

device = provider.get_backend('ibmq_lima')
job = execute(qc, backend=device, shots=4000)
result = job.result()
counts = result.get_counts()
print(counts)

