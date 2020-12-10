nums = [4, 5, 6]
msg = "Numbers: {0}, {1}, {2}".format(nums[0], nums[1], nums[2])
print(msg)

nums = (55, 44, 33, 22)
print(max(min(nums[:2]), abs(-42)))


def fib(x):
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x - 1) + fib(x - 2)


print(fib(4))
