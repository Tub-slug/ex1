x = randint(2, 9)
basic.show_string("" + str((x)))
y = x
for index in range(x):
    basic.show_string("" + str((y)))
    y += 1
basic.show_string("" + str((y)))