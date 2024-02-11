## Language
[English](./README.md) | [中文](./README_CN.md)

## Project Overview
This project is a Python implementation of a practical Secure Multi-party Computation (SMPC) scenario, simulating how two millionaires (A and B) can compare their wealth without revealing their exact financial status. We utilize SMPC techniques to ensure data privacy.

## File Structure
- utils.py: Contains fundamental utility functions related to RSA encryption, including key generation, encryption, and decryption.
- utils_test.py: Tests the functionality of the tools in the utils file, ensuring that the encryption and decryption processes are working as expected.
- index.py: The core code for simulating the millionaire's problem, demonstrating how a designed secure communication protocol allows both parties to effectively compare their wealth while remaining encrypted.

## Running Instructions
First, run utils_test.py to verify the correctness of the encryption utilities.
Then, proceed with running index.py to see the simulated process and the final outcome.