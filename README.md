# py_hardware

A Python framework for modeling simple digital hardware behavior with wires, logic gates, and bus-like signal handling.

Status: pre-0.1.0 / alpha

This project is actively under development and is intentionally not yet treated as a stable 0.1.0 release. Current package metadata is still in the 0.0.x range while the API and feature set continue to mature.

This project is planned to be published to PyPI when a stable 0.1.0 release is achieved.

## What it does

`py_hardware` provides a minimal hardware simulation layer for experimenting with logic components in Python. The current core primitives include:

- `Wire`: a signal carrier that supports boolean states and a high-impedance (`None`) state
- `NAND`: a 2-input NAND gate with pull-down behavior on undefined inputs
- `CBUF`: a controlled buffer with output-enable semantics
- `Component`: a base class for hardware building blocks

These building blocks are useful for educational projects, digital logic prototyping, and small hardware-oriented simulations without a full HDL toolchain.

## Installation

From a local checkout:

```bash
git clone https://github.com/42-Slices-of-Cheese/py_hardware.git
cd py_hardware
python -m pip install -e .
```

## Quick example

```python
from py_hardware import Wire, NAND

A = Wire(False)
B = Wire(True)
Y = Wire()

NAND(A, B, Y)
print(Y.value)  # True
```

This example builds a NAND gate and evaluates the result of `A NAND B`.

## Current design goals

- Keep the API small and easy to understand
- Model signal behavior close to real digital hardware primitives
- Support simple composition of logic components into larger systems
- Maintain a clear migration path toward a more complete simulation toolkit

## Example behaviors

The `Wire` type intentionally supports `True`, `False`, and `None` values:

- `True` / `False` represent driven signal states
- `None` represents a high-impedance state
- Use `hardcode=True` when a permanently fixed wire value is wanted

## Project status

This repository is intended for active development and experimentation rather than a stable public release yet. The project may change shape significantly before reaching a 0.1.0 milestone.

## License

This project is licensed under the GNU General Public License v3.0 or later.

## Contributing

Contributions are welcome as this project evolves. If you want to help shape the library before the first public release, open an issue or submit a pull request with your proposed changes.
