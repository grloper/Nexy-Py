def throw_StopIteration():
    raise StopIteration("StopIteration exception")

def throw_ZeroDivisionError():
    raise ZeroDivisionError("ZeroDivisionError exception")

def throw_AssertionError():
    raise AssertionError("AssertionError exception")

def throw_ImportError():
    raise ImportError("ImportError exception")

def throw_KeyError():
    raise KeyError("KeyError exception")

def throw_SyntaxError():
    raise SyntaxError("SyntaxError exception")

def throw_IndentationError():
    raise IndentationError("IndentationError exception")

def throw_TypeError():
    raise TypeError("TypeError exception")

# Testing the exceptions
try:
    throw_StopIteration()
except StopIteration as e:
    print("StopIteration exception was thrown")

try:
    throw_ZeroDivisionError()
except ZeroDivisionError as e:
    print("ZeroDivisionError exception was thrown")

try:
    throw_AssertionError()
except AssertionError as e:
    print("AssertionError exception was thrown")

try:
    throw_ImportError()
except ImportError as e:
    print("ImportError exception was thrown")

try:
    throw_KeyError()
except KeyError as e:
    print("KeyError exception was thrown")

try:
    throw_SyntaxError()
except SyntaxError as e:
    print("SyntaxError exception was thrown")

try:
    throw_IndentationError()
except IndentationError as e:
    print("IndentationError exception was thrown")

try:
    throw_TypeError()
except TypeError as e:
    print("TypeError exception was thrown")