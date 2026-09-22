from py_hardware import Wire

A_B_Y_COMPONENT_ERROR_CASES = [
    (None, None, None, "Input wire A is missing."),
    (None, None, Wire(), "Input wire A is missing."),
    (None, Wire(), None, "Input wire A is missing."),
    (None, Wire(), Wire(), "Input wire A is missing."),
    (Wire(), None, None, "Input wire B is missing."),
    (Wire(), None, Wire(), "Input wire B is missing."),
    (Wire(), Wire(), None, "Output wire is missing."),
]

A_B_Y_TYPE_ERROR_CASES = [
    (1, Wire(), Wire(), "Input wire A is not a wire object."),
    (1, 1, Wire(), "Input wire A is not a wire object."),
    (1, 1, 1, "Input wire A is not a wire object."),
    (1, Wire(), 1, "Input wire A is not a wire object."),
    (Wire(), 1, Wire(), "Input wire B is not a wire object."),
    (Wire(), 1, 1, "Input wire B is not a wire object."),
    (Wire(), Wire(), 1, "Output wire is not a wire object.")
]

A_B_Y_INPUT_CASES = [
    (False, False),
    (False, True),
    (True,  False),
    (True,  True),
    (None, False),
    (None, True),
    (False, None),
    (True, None),
]

A_Y_COMPONENT_ERROR_CASES = [
    (None, None, "Input wire is missing."),
    (None, Wire(), "Input wire is missing."),
    (Wire(), None, "Output wire is missing."),
]

A_Y_TYPE_ERROR_CASES = [
    (1, 1, "Input wire is not a wire object."),
    (1, Wire(), "Input wire is not a wire object."),
    (Wire(), 1, "Output wire is not a wire object."),
]

A_Y_INPUT_CASES = [
    (False),
    (True),
    (None),
]