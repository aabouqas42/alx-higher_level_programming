#!/usr/bin/python3
def raise_exception():
    try:
        result = 42 + "hello"
    except TypeError as e:
        raise e
    except:
        pass
