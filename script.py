import math
import os
import sys
import typing


print(sys.version)
print(sys.executable)


def greeting(who: str) -> str:
    test = "Test"
    greeting = f"Hello, {who}"
    return greeting


print(greeting("Word"))
print(greeting("Elcolie"))
