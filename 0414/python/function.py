def my_func(x):
    if x >= 0:
        return x
    else:
        return -x

print my_func(10)
print my_func(-20)


def nothing():
    pass


def move(x, y, step_x, step_y):
    return x+step_x, y+step_y

print move(0, 0, 5, 3)
print move(0, 0, 5, 3)[0]
print move(0, 0, 5, 3)[1]