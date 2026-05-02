# SPHY Engine - Entangled Bloch Sphere Auditor

This repository contains the real-time interactive visualizer and dataset for the **SPHY (Symbiotic Phase Harmonic Yielding) Engine** simulation. The project demonstrates the validation of quantum-gravitational phase anchoring through high-fidelity visual analysis and cryptographic integrity checks.

## Project Overview

The simulation models **12 entangled qubits** across **6,000 frames** of processing. It utilizes a unique entanglement summing methodology where each local sum corresponds to the qubit's identity, contributing to a total system yield.

### Key Features
*   **Cryptographic Sovereignty**: Every single frame is signed with a **SHA-256 hash**. The visualizer reconstructs the entangled payload in real-time to verify the data's integrity against the stored hash.
*   **Interactive Geodesic Visualization**: Built with a 3D engine, the auditor allows users to navigate the Bloch Sphere environment using an interactive camera.
*   **Real-Time Validation**: The system provides constant feedback on "Quantum Sovereignty," alerting the user to any core breaches or data corruption.
*   **Fibonacci Geodesic Alignment**: Qubit trajectories follow precise mathematical formalisms simulated within the SPHY framework.

## Technical Specifications

*   **Qubits Simulated**: 12
*   **Temporal Resolution**: 6,000 frames
*   **Data Format**: High-performance Parquet storage (`sphy_bloch_data.parquet`)
*   **Integrity Protocol**: Frame-by-frame SHA-256 validation
*   **Simulation Core**: SPHY (Symbiotic Phase Harmonic Yielding)

## How to Run

### Prerequisites
Ensure you have Python installed along with the following dependencies:
```bash
pip install ursina pandas pyarrow
```

### Execution
1. Clone this repository.
2. Ensure the `sphy_bloch_data.parquet` file is in the same directory as the script.
3. Run the auditor:
```bash
python sphy_parquet_viewer.py
```

### Controls
*   **Mouse**: Rotate and orbit the Bloch Sphere.
*   **Spacebar**: Reset the simulation to Frame 0.
*   **Escape**: Exit the application.

---
**Author**: Deywe Okabe  
**Framework**: SPHY Engine
