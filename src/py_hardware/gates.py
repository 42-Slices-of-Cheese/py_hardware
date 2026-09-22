from .exceptions import ComponentException
from .core import Component, Wire

class AND(Component):
    """AND Gate with pull downs on the inputs
    """

    __slots__ = "A", "B", "Y"
    
    def __init__(self, A: Wire, B: Wire, Y: Wire):
        """Initializes the instance

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
        self.Y.value = self.A.value and self.B.value

class OR(Component):
    """OR Gate with pull downs on the inputs
    """

    __slots__ = "A", "B", "Y"

    def __init__(self, A: Wire, B: Wire, Y: Wire):
        """Initializes the instance
        
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
        self.Y.value = self.A.value or self.B.value

class NOR(Component):
    """NOR Gate with pull downs on the inputs
    """
    __slots__ = "A", "B", "Y"

    def __init__(self, A: Wire, B: Wire, Y: Wire):
        """Initializes the instance
        
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
        self.Y.value = not (self.A.value or self.B.value)

class XOR(Component):
    """XOR Gate with pull downs on the inputs
    """

    __slots__ = "A", "B", "Y"

    def __init__(self, A: Wire, B: Wire, Y: Wire):
        """Initializes the instance

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
        self.Y.value = self.A.value ^ self.B.value
    

class XNOR(Component):
    __slots__ = "A", "B", "Y"

    def __init__(self, A: Wire, B: Wire, Y: Wire):
        """Initializes the instance
        
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
        self.Y.value = not (self.A.value ^ self.B.value)

class NOT(Component):
    __slots__ = "A", "Y"
    
    def __init__(self, A: Wire, Y: Wire):
        """Initializes the instance
        
        Args:
            A (Wire): Input wire
            Y (Wire): Output wire

        Raises:
            ComponentException: If A, B, C is missing
            TypeError: If A, B, C is not a wire
        """
        if A is None:
            raise ComponentException("Input wire is missing.")
        if Y is None:
            raise ComponentException("Output wire is missing.")

        if not isinstance(A, Wire):
            raise TypeError("Input wire is not a wire object.")
        if not isinstance(Y, Wire):
            raise TypeError("Output wire is not a wire object.")

        self.A = A
        self.Y = Y

        A.connect(self)

        self.update()

    def update(self):
        if self.A.value is None:
            self.A.value = False
        self.Y.value = not self.A.value

class INVCBUF(Component):
    __slots__ = "A", "OE", "Y", "is_driving"

    def __init__(self, A: Wire, OE: Wire, Y: Wire):
        """Initializes the instance
        
        Args:
            A (Wire): Input wire A
            B (Wire): Input wire B
            Y (Wire): Output wire

        Raises:
            ComponentException: If A, B, C is missing
            TypeError: If A, B, C is not a wire
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
            if self.A.value is None:
                self.Y.value = None
            else:
                self.Y.value = not self.A.value
            self.is_driving = True
        else:
            if self.is_driving:
                self.Y.value = None
                self.is_driving = False
