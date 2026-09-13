from .exceptions import ComponentException, WireException

class Component:
    pass

class Wire:
    def __init__(self, value: bool | None = None, hardcode: bool = False) -> None:
        """A wire that can be hardcoded and/or set to high impedance.

        Args:
            value (bool | None, optional): The state of the wire. Defaults to None.
            hardcode (bool, optional): Hardcoded wire selector. Defaults to False.

        Raises:
            TypeError: If value is not a bool or None
            WireException: If an attempt to set a hardcoded wire or hardcode mode is not set.
        """
        if not isinstance(value, bool):
            if value is not None:
                raise TypeError("Value must be bool or None.")

        if hardcode is None:
            raise WireException("Choose between a hardcoded wire or a free wire.")
        
        self._value = value

        self.hardcode = hardcode

        self.connections = []

    @property
    def value(self) -> bool | None:
        return self._value

    @value.setter
    def value(self, value: bool | None) -> None:
        if self.hardcode:
            raise WireException("This wire is hardcoded.")

        if not isinstance(value, bool):
            if value is not None:
                raise TypeError("Value must be bool or None.")

        if self._value == value:
            return
        
        self._value = value

        self.update()

    def connect(self, components) -> None:
        if not isinstance(components, list):
            components = [components]

        for component in components:
            if not isinstance(component, Component):
                raise WireException("Cannot connect non-component objects.")
            self.connections.append(component)

    def update(self) -> None:
        for component in self.connections:
                    component.update()

class NAND(Component):
    def __init__(self, A: Wire, B: Wire, Y: Wire):
        """NAND Gate with pull downs on the inputs

        Args:
            A (Wire): Input wire A
            B (Wire): Input wire B
            Y (Wire): Output wire

        Raises:
            ComponentException: If A, B, C is missing
            TypeError: If A, B, C is not a wire
        """
        if A is None:
            raise ComponentException("Input wire A is missing.")
        if B is None:
            raise ComponentException("Input wire B is missing.")
        if Y is None:
            raise ComponentException("Output wire is missing.")

        if not isinstance(A, Wire):
            raise TypeError("Input wire A is not a wire object.")
        if not isinstance(B, Wire):
            raise TypeError("Input wire B is not a wire object.")
        if not isinstance(Y, Wire):
            raise TypeError("Output wire is not a wire object.")
        
        self.A = A
        self.B = B
        self.Y = Y

        A.connect(self)
        B.connect(self)

        self.update()

    def update(self):
        if self.A.value is None:
            self.A.value = False
        if self.B.value is None:
            self.B.value = False
        self.Y.value = not (self.A.value and self.B.value)

class CBUF(Component):
    def __init__(self, A: Wire, OE: Wire, Y: Wire):
        """A controlled buffer with pull downs on OE

        Args:
            A (Wire): Input wire
            OE (Wire): Output enable wire
            Y (Wire): Output wire

        Raises:
            ComponentException: When input, output, and output enble wires are missing.
        """
        if A is None:
            raise ComponentException("Input wire is missing.")
        elif OE is None:
            raise ComponentException("Output enable wire is missing.")
        elif Y is None:
            raise ComponentException("Output wire is missing.")

        if not isinstance(A, Wire):
            raise TypeError("Input wire is not a wire object.")
        if not isinstance(OE, Wire):
            raise TypeError("Output enable wire is not a wire object.")
        if not isinstance(Y, Wire):
            raise TypeError("Output wire is not a wire object.")

        self.A = A
        self.OE = OE
        self.Y = Y

        self.is_driving = False

        A.connect(self)
        OE.connect(self)

        self.update()

    def update(self):
        if self.OE.value is None:
            self.OE.value = False

        if self.OE.value:
            self.Y.value = self.A.value
            self.is_driving = True
        else:
            if self.is_driving:
                self.Y.value = None
                self.is_driving = False
