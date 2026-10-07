from .core import Wire, Component
from .exceptions import ComponentException


class SR_latch(Component):
    """Set / Reset latch built from NOR (active-high) or NAND (active-low) logic"""

    __slots__ = "nand", "S", "R", "Q", "Qbar", "_q_state"

    def __init__(self, nand: bool, S: Wire, R: Wire, Q: Wire, Qbar: Wire | None = None):
        if S is None:
            raise ComponentException("Set wire is missing.")
        if R is None:
            raise ComponentException("Reset wire B is missing.")
        if Q is None:
            raise ComponentException("Output wire is missing.")

        if not isinstance(S, Wire):
            raise TypeError("Set wire is not a wire object.")
        if not isinstance(R, Wire):
            raise TypeError("Rest wire is not a wire object.")
        if not isinstance(Q, Wire):
            raise TypeError("Output wire is not a wire object.")
        if Qbar is not None and not isinstance(Qbar, Wire):
            raise TypeError("Qbar is optional, but must be a Wire object.")
        if not isinstance(nand, bool):
            raise TypeError("nand must be a bool.")

        self.nand = nand
        self.S = S
        self.R = R
        self.Q = Q
        self.Qbar = Qbar if Qbar is not None else Wire()
        
        if isinstance(Q.value, bool):
            self._q_state = Q.value
        elif Qbar is not None and isinstance(Qbar.value, bool):
            self._q_state = not Qbar.value
        else:
            self._q_state = False

        inactive_value = nand
        if self.S.value is None:
            self.S.value = inactive_value
        if self.R.value is None:
            self.R.value = inactive_value

        self.S.connect(self)
        self.R.connect(self)
        self.update()

    def update(self):
        active_value = not self.nand
        set_active = self.S.value == active_value
        reset_active = self.R.value == active_value

        if set_active and reset_active:
            self.Q.value = self.nand
            self.Qbar.value = self.nand
        elif set_active:
            self._q_state = True
            self.Q.value = True
            self.Qbar.value = False
        elif reset_active:
            self._q_state = False
            self.Q.value = False
            self.Qbar.value = True
        else:
            self.Q.value = self._q_state
            self.Qbar.value = not self._q_state
