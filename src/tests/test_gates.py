import pytest

from typing import Any
from py_hardware.exceptions import ComponentException
from py_hardware import Wire, AND, OR, NOR, XOR, XNOR, NOT, INVCBUF
from .cases import A_B_Y_COMPONENT_ERROR_CASES, A_B_Y_TYPE_ERROR_CASES, A_B_Y_INPUT_CASES, A_Y_INPUT_CASES, A_Y_COMPONENT_ERROR_CASES, A_Y_TYPE_ERROR_CASES

class TestAND:
    @pytest.mark.parametrize("a, b", A_B_Y_INPUT_CASES)
    def test_andInputs(self, a: bool | None, b: bool | None) -> None:
        _a = Wire(a)
        _b = Wire(b)
        _y = Wire()
        AND(_a, _b, _y)

        if(a is None):
            a = False

        if(b is None):
            b = False

        expected = a and b
        assert _y.value == expected

    class TestAND_errors:
        @pytest.mark.parametrize("a, b, y, message", A_B_Y_COMPONENT_ERROR_CASES)
        def test_andComponentError(self, a: Wire | None, b: Wire | None, y, message: str) -> None:
            with pytest.raises(ComponentException, match=message):
                AND(a, b, y)

        @pytest.mark.parametrize("a, b, y, message", A_B_Y_TYPE_ERROR_CASES)
        def test_andTypeError(self, a: Wire | Any, b: Wire | Any, y: Wire | Any, message: str) -> None:
            with pytest.raises(TypeError, match=message):
                AND(a, b, y)

class TestOR:
    @pytest.mark.parametrize("a, b", A_B_Y_INPUT_CASES)
    def test_orInputs(self, a: bool | None, b: bool | None) -> None:
        _a = Wire(a)
        _b = Wire(b)
        _y = Wire()
        OR(_a, _b, _y)

        if(a is None):
            a = False

        if(b is None):
            b = False

        expected = a or b
        assert _y.value == expected

    class TestOR_errors:
        @pytest.mark.parametrize("a, b, y, message", A_B_Y_COMPONENT_ERROR_CASES)
        def test_orComponentError(self, a: Wire | None, b: Wire | None, y, message: str) -> None:
            with pytest.raises(ComponentException, match=message):
                OR(a, b, y)

        @pytest.mark.parametrize("a, b, y, message", A_B_Y_TYPE_ERROR_CASES)
        def test_orTypeError(self, a: Wire | Any, b: Wire | Any, y: Wire | Any, message: str) -> None:
            with pytest.raises(TypeError, match=message):
                OR(a, b, y)

class TestNOR:
    @pytest.mark.parametrize("a, b", A_B_Y_INPUT_CASES)
    def test_norInputs(self, a: bool | None, b: bool | None) -> None:
        _a = Wire(a)
        _b = Wire(b)
        _y = Wire()
        NOR(_a, _b, _y)

        if(a is None):
            a = False

        if(b is None):
            b = False

        expected = not (a or b)
        assert _y.value == expected

    class TestNOR_errors:
        @pytest.mark.parametrize("a, b, y, message", A_B_Y_COMPONENT_ERROR_CASES)
        def test_norComponentError(self, a: bool | None, b: bool | None, y: bool | None, message: str) -> None:
            with pytest.raises(ComponentException, match=message):
                NOR(a, b, y)

        @pytest.mark.parametrize("a, b, y, message", A_B_Y_TYPE_ERROR_CASES)
        def test_norComponentError(self, a: bool | None, b: bool | None, y: bool | None, message: str) -> None:
            with pytest.raises(TypeError, match=message):
                NOR(a, b, y)

class TestXOR:
    @pytest.mark.parametrize("a, b", A_B_Y_INPUT_CASES)
    def test_xorInputs(self, a: bool | None, b: bool | None) -> None:
        _a = Wire(a)
        _b = Wire(b)
        _y = Wire()
        XOR(_a, _b, _y)

        if(a is None):
            a = False

        if(b is None):
            b = False

        expected = a ^ b
        assert _y.value == expected

    class TestXOR_errors:
        @pytest.mark.parametrize("a, b, y, message", A_B_Y_COMPONENT_ERROR_CASES)
        def test_xorComponentError(self, a: bool | None, b: bool | None, y: bool | None, message: str) -> None:
            with pytest.raises(ComponentException, match=message):
                XOR(a, b, y)

        @pytest.mark.parametrize("a, b, y, message", A_B_Y_TYPE_ERROR_CASES)
        def test_xorComponentError(self, a: bool | None, b: bool | None, y: bool | None, message: str) -> None:
            with pytest.raises(TypeError, match=message):
                XOR(a, b, y)

class TestXNOR:
    @pytest.mark.parametrize("a, b", A_B_Y_INPUT_CASES)
    def test_xnorInputs(self, a: bool | None, b: bool | None) -> None:
        _a = Wire(a)
        _b = Wire(b)
        _y = Wire()
        XNOR(_a, _b, _y)

        if(a is None):
            a = False

        if(b is None):
            b = False

        expected = not (a ^ b)
        assert _y.value == expected

    class TestXNOR_errors:
        @pytest.mark.parametrize("a, b, y, message", A_B_Y_COMPONENT_ERROR_CASES)
        def test_xnorComponentError(self, a: bool | None, b: bool | None, y: bool | None, message: str) -> None:
            with pytest.raises(ComponentException, match=message):
                XNOR(a, b, y)

        @pytest.mark.parametrize("a, b, y, message", A_B_Y_TYPE_ERROR_CASES)
        def test_xnorComponentError(self, a: bool | None, b: bool | None, y: bool | None, message: str) -> None:
            with pytest.raises(TypeError, match=message):
                XNOR(a, b, y)

class TestNOT:
    @pytest.mark.parametrize("a", A_Y_INPUT_CASES)
    def test_notInputs(self, a: bool | None) -> None:
        _a = Wire(a)
        _y = Wire()
        NOT(_a, _y)

        if(a is None):
            a = False

        expected = not a
        assert _y.value == expected

    class TestNOT_errors:
        @pytest.mark.parametrize("a, y, message", A_Y_COMPONENT_ERROR_CASES)
        def test_notComponentError(self, a: bool | None, y: bool | None, message: str) -> None:
            with pytest.raises(ComponentException, match=message):
                NOT(a, y)

        @pytest.mark.parametrize("a, y, message", A_Y_TYPE_ERROR_CASES)
        def test_notComponentError(self, a: bool | None, y: bool | None, message: str) -> None:
            with pytest.raises(TypeError, match=message):
                NOT(a, y)


class TestINVCBUF:
    @pytest.mark.parametrize("a, oe, expected", [
        (False, False, None),
        (False, True,  True),
        (True,  False, None),
        (True,  True,  False),
        (None, False, None),
        (None, True, None),
        (None, None, None),
        (False, None, None),
        (True, None, None),
    ])
    def test_invcbufInputs(self, a: bool | None, oe: bool | None, expected: str) -> None:
        _a = Wire(a)
        _oe = Wire(oe)
        _y = Wire()
        INVCBUF(_a, _oe, _y)

        assert _y.value == expected

    def test_cbufBusState(self) -> None:
        _a = Wire()
        _oe = Wire()
        _y = Wire()
        test = INVCBUF(_a, _oe, _y)
        assert not test.is_driving

        _oe.value = True
        assert test.is_driving

        _oe.value = False
        assert not test.is_driving

    class TestINVCBUF_errors:
        @pytest.mark.parametrize("a, oe, y, message", [
            (None, None, None, "Input wire is missing."),
            (None,  None, Wire(), "Input wire is missing."),
            (None,  Wire(), None, "Input wire is missing."),
            (None,  Wire(), Wire(), "Input wire is missing."),
            (Wire(), None, None, "Output enable wire is missing."),
            (Wire(),  None, Wire(), "Output enable wire is missing."),
            (Wire(),  Wire(), None, "Output wire is missing."),
        ])
        def test_invcbufComponentError(self, a: Wire | None, oe: Wire | None, y: Wire | None, message: str) -> None:
            with pytest.raises(ComponentException, match=message):
                    INVCBUF(a, oe, y)

        @pytest.mark.parametrize("a, oe, y, message", [
            (1, Wire(), Wire(), "Input wire is not a wire object."),
            (1, 1, Wire(), "Input wire is not a wire object."),
            (1, 1, 1, "Input wire is not a wire object."),
            (1, Wire(), 1, "Input wire is not a wire object."),
            (Wire(), 1, Wire(), "Output enable wire is not a wire object."),
            (Wire(), 1, 1, "Output enable wire is not a wire object."),
            (Wire(), Wire(), 1, "Output wire is not a wire object.")
        ])
        def test_invcubfTypeError(self, a: Wire | Any, oe: Wire | Any, y: Wire | Any, message: str) -> None:
            with pytest.raises(TypeError, match=message):
                INVCBUF(a, oe, y)
