#!/usr/bin/python3
def raise_exception_msg(message=""):
    try:
        # Attempt to access a non-existent variable
        nonexistent_variable
    except NameError as e:
        raise NameError(message) from e
