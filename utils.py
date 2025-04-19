from typing import Sequence, Iterable, Callable

def allFloats (values: Iterable[float]) -> bool:

    for v in values:
        if not type(v) == float: return False

    return True