
from contextlib import redirect_stdout
from io import StringIO
from typing import Callable, Protocol


class Wrapper(Protocol):
    stdout: str = ""

class OutputWrapper(Wrapper):
    def __init__(self, fn: Callable) -> None:
        with redirect_stdout(StringIO()) as f:
            fn()

        self.stdout: str = f.getvalue() or ""
        super().__init__()
    
    def __call__(self):
        return self

    
class EmptyWrapper(Wrapper):
    ...
