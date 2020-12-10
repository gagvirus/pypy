try:
    5 / 0
except ZeroDivisionError:  # catch
    print('shit happens')
    raise  # raise without argument will "throw" the same exception
finally:
    print('eventually')

raise ValueError('woala')  # throw
