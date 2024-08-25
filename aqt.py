from qiskit_aqt_provider import AQTProvider

aqt = AQTProvider('TOKEN')
print(aqt.backends())

sim_backend = aqt.backends.aqt_qasm_simulator

