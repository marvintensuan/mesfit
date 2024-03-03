from subprocess import run
from typing import Callable

from utils.lazy_importer import lazy_import
from utils.wrappers import OutputWrapper, EmptyWrapper


    
def execute(command, config: dict | None = None) -> OutputWrapper | None:
    if config is None:
        return EmptyWrapper

    scripts = config["scripts"]

    script, *flags = command.split(" ")

    if script not in scripts.keys():
        return EmptyWrapper
    
    program = scripts[script]
    if program.get("importlib_spec", None):
        container = python_container(program["importlib_spec"], args=flags)
        return OutputWrapper(container)


def python_container(importlib_spec: str, args=None) -> Callable:
    def func():
        main = lazy_import(importlib_spec).main
        main(*args)
    return func

def pythonize(*args) -> Callable:
    def wrap_this():
        run(*args)
    return wrap_this

