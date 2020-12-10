assert 5 == 2 + 3

try:
    assert 4 == 2 / 2, "four is not equal to two divided by two !!!"
except AssertionError as e:
    print('nope:', e)
