import pytest
from typing import Any

from py_hardware import *

class DummyComponent(Component):
    """A dummy component to test wire connections
    """

    def __init__(self):
        self.update_count = 0

    def update(self):
        self.update_count += 1

class TestWire:
    @pytest.mark.parametrize("a, expected", [
        (False, False),
        (True,  True),
        (None, None),
    ])
    def test_wireValues(self, a : bool |  None, expected: bool | None) -> None:
        wire = Wire(a)
        assert wire.value == expected

    def test_wirePropagation(self):
        wire = Wire()
        component_1 = DummyComponent()
        component_2 = DummyComponent()

        wire.connect([component_1, component_2])

        for component in wire.connections:
            assert isinstance(component, DummyComponent)

        wire.value = True

        assert component_1.update_count == 1
        assert component_2.update_count == 1

        wire.value = False

        assert component_1.update_count == 2
        assert component_2.update_count == 2

    class TestWire_errors:
        @pytest.mark.parametrize("value, message", [
            (False, "Choose between a hardcoded wire or a free wire."),
            (True, "Choose between a hardcoded wire or a free wire."),
        ])
        def test_init_wireErrors(self, value: bool, message: str) -> None:
            with pytest.raises(WireException, match=message):
                Wire(value, None)

            with pytest.raises(TypeError, match="Value must be bool or None."):
                Wire("True", value)

        @pytest.mark.parametrize("value, message", [
            (False, "This wire is hardcoded."),
            (True, "This wire is hardcoded."),
            (None, "This wire is hardcoded."),
        ])
        def test_set_wireErrors(self, value: bool | None, message: str) -> None:
            wire = Wire(None, True)
        
            with pytest.raises(WireException, match=message):
                wire.value = value

            wire = Wire()
            with pytest.raises(TypeError, match="Value must be bool or None."):
                wire.value = 1

        def test_wireConnectionError(self) -> None:
            wire = Wire()

            with pytest.raises(WireException, match="Cannot connect non-component objects."):
                wire.connect(1)

class TestNAND:
    @pytest.mark.parametrize("a, b, expected", [
        (False, False, True),
        (False, True,  True),
        (True,  False, True),
        (True,  True,  False),
        (None, False, True),
        (None, True, True),
        (False, None, True),
        (True, None, True),
    ])
    def test_nandInputs(self, a: bool | None, b: bool | None, expected: str) -> None:
        _a = Wire(a)
        _b = Wire(b)
        _y = Wire()
        NAND(_a, _b, _y)

        assert _y.value == expected

    class TestNAND_errors:
        @pytest.mark.parametrize("a, b, y, message", [
            (None, None, None, "Input wire A is missing."),
            (None,  None, Wire(), "Input wire A is missing."),
            (None,  Wire(), None, "Input wire A is missing."),
            (None,  Wire(), Wire(), "Input wire A is missing."),
            (Wire(), None, None, "Input wire B is missing."),
            (Wire(),  None, Wire(), "Input wire B is missing."),
            (Wire(),  Wire(), None, "Output wire is missing."),
        ])
        def test_nandComponentError(self, a: Wire | None, b: Wire | None, y: Wire | None, message: str) -> None:
            with pytest.raises(ComponentException, match=message):
                NAND(a, b, y)

        @pytest.mark.parametrize("a, b, y, message", [
            (1, Wire(), Wire(), "Input wire A is not a wire object."),
            (1, 1, Wire(), "Input wire A is not a wire object."),
            (1, 1, 1, "Input wire A is not a wire object."),
            (1, Wire(), 1, "Input wire A is not a wire object."),
            (Wire(), 1, Wire(), "Input wire B is not a wire object."),
            (Wire(), 1, 1, "Input wire B is not a wire object."),
            (Wire(), Wire(), 1, "Output wire is not a wire object.")
        ])
        def test_nandTypeError(self, a: Wire | Any, b: Wire | Any, y: Wire | Any, message: str) -> None:
            with pytest.raises(TypeError, match=message):
                NAND(a, b, y)

class TestCBUF:
    @pytest.mark.parametrize("a, oe, expected", [
        (False, False, None),
        (False, True,  False),
        (True,  False, None),
        (True,  True,  True),
        (None, False, None),
        (None, True, None),
        (None, None, None),
        (False, None, None),
        (True, None, None),
    ])
    def test_cbufInputs(self, a: bool | None, oe: bool | None, expected: str) -> None:
        _a = Wire(a)
        _oe = Wire(oe)
        _y = Wire()
        CBUF(_a, _oe, _y)

        assert _y.value == expected

    def test_cbufBusState(self) -> None:
        _a = Wire()
        _oe = Wire()
        _y = Wire()
        test = CBUF(_a, _oe, _y)
        assert not test.is_driving

        _oe.value = True
        assert test.is_driving

        _oe.value = False
        assert not test.is_driving

    class TestCBUF_errors:
        @pytest.mark.parametrize("a, oe, y, message", [
                    (None, None, None, "Input wire is missing."),
                    (None,  None, Wire(), "Input wire is missing."),
                    (None,  Wire(), None, "Input wire is missing."),
                    (None,  Wire(), Wire(), "Input wire is missing."),
                    (Wire(), None, None, "Output enable wire is missing."),
                    (Wire(),  None, Wire(), "Output enable wire is missing."),
                    (Wire(),  Wire(), None, "Output wire is missing."),
                ])
        def test_cbufComponentError(self, a: Wire | None, oe: Wire | None, y: Wire | None, message: str) -> None:
            with pytest.raises(ComponentException, match=message):
                    CBUF(a, oe, y)

        @pytest.mark.parametrize("a, oe, y, message", [
            (1, Wire(), Wire(), "Input wire is not a wire object."),
            (1, 1, Wire(), "Input wire is not a wire object."),
            (1, 1, 1, "Input wire is not a wire object."),
            (1, Wire(), 1, "Input wire is not a wire object."),
            (Wire(), 1, Wire(), "Output enable wire is not a wire object."),
            (Wire(), 1, 1, "Output enable wire is not a wire object."),
            (Wire(), Wire(), 1, "Output wire is not a wire object.")
        ])
        def test_cubfTypeError(self, a: Wire | Any, oe: Wire | Any, y: Wire | Any, message: str) -> None:
            with pytest.raises(TypeError, match=message):
                CBUF(a, oe, y)


