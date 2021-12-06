input.onButtonPressed(Button.A, function () {
    if (x == 1) {
        basic.showIcon(IconNames.Yes)
    } else {
        basic.showIcon(IconNames.No)
    }
})
input.onButtonPressed(Button.AB, function () {
    basic.showString("" + (x))
})
input.onButtonPressed(Button.B, function () {
    if (x == 2) {
        basic.showIcon(IconNames.Yes)
    } else {
        basic.showIcon(IconNames.No)
    }
})
let x = 0
basic.showString("GUESS A NUM, EITHER 1A OR 2B")
x = randint(1, 2)
