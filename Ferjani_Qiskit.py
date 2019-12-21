# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 08:51:53 2019

@author: hp
"""

from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit import available_backends, execute
# Create three quantum and classical registers
q = QuantumRegister(3)
c = ClassicalRegister(3)
qc = QuantumCircuit(q, c)
# Create an initial superposition + state
qc.h(q[0])
# Take the qubit out of superposition
qc.h(q[0])
# Perform a CNOT between the qubits
qc.cx(q[0], q[1])
# Put the qubits into superposition and now the states are the same
qc.h(q[0])
qc.h(q[1])
# Prepare an initial state for qubit ① using a single unitary
qc.u1(0.5, q[0])
# Perform a CNOT between qubit ① and qubit ②
qc.cx(q[0], q[1])
# Measure qubit ① in the + - basis
qc.h(q[0])
qc.measure(q[0], c[0])
# If needed Perform a phase correction to qubit ②
if c[0] == 1:
   qc.z(q[1]
# Prepare an initial state for qubit ① using a single unitary
qc.u1(0.5, q[0])
# Prepare an entangled pair using qubit ② and qubit ③
qc.h(q[1])
qc.cx(q[1], q[2])
# Barrier to prevent gate reordering for optimization
qc.barrier(q)
# Perform a CNOT between qubit ① and qubit ②
qc.cx(q[0], q[1])
# Measure qubit ② in the computational basis
qc.measure(q[1], c[1])
# If needed Perform a bit flip correction to qubit ③
if c[1] == 1:
    qc.x(q[2])
# Measure qubit ① in the + - basis
qc.h(q[0])
qc.measure(q[0], c[0])
# If needed Perform a phase correction to qubit ③
if c[0] == 1:
    qc.z(q[2])