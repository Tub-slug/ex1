let x = randint(2, 9)
basic.showString("" + x)
let y = x
for (let index = 0; index < x; index++) {
    basic.showString("" + y)
    y += 1
}
basic.showString("" + y)
