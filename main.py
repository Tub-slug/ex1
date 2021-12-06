def on_button_pressed_a():
    basic.show_leds("""
        . . . . .
                . . . . .
                . . # . .
                . . . . .
                . . . . .
    """)
    basic.pause(100)
    basic.show_leds("""
        . . . . .
                . # . # .
                . . # . .
                . # . # .
                . . . . .
    """)
    basic.pause(100)
    basic.show_leds("""
        # . . . #
                . # . # .
                . . # . .
                . # . # .
                # . . . #
    """)
    basic.pause(100)
    basic.show_leds("""
        # . # . #
                . # # # .
                # # # # #
                . # # # .
                # . # . #
    """)
    basic.pause(100)
    basic.show_leds("""
        . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
    """)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    for index in range(5):
        basic.show_icon(IconNames.SMALL_HEART)
        basic.pause(100)
        basic.show_icon(IconNames.HEART)
        basic.pause(100)
    basic.show_leds("""
        . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
    """)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    basic.show_string("UPS")
input.on_button_pressed(Button.B, on_button_pressed_b)
