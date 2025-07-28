# Python Exceptions

## Exceptions

Exceptions are raised when something goes wrong.

```python
try:
    # do something
except:
    # do something else
```
### Example

```python
try:
    print("Hello")
except:
    print("Something went wrong")
``` 
### Raising an Exception

You can also raise an exception if something goes wrong:

```python
raise Exception("Something went wrong")
```
### Exception Types

There are different types of exceptions:

- SyntaxError
- TypeError
- NameError
- ValueError
- AttributeError
- KeyError
- IndexError
- ImportError
- OSError
- EOFError
- StopIteration
- SystemExit
- KeyboardInterrupt
- BaseException
- Exception
- ArithmeticError
- AssertionError
- LookupError
- EnvironmentError
- FloatingPointError
- MemoryError
- OverflowError
- ReferenceError
- SystemError
- ZeroDivisionError
- GeneratorExit
- BlockingIOError

