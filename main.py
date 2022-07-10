import keyboard
from interface import CookieClicker

if __name__ == '__main__':
    id_ = input("Qual o seu ID? ")

    game = CookieClicker(0, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 100000])
    game.load_upgrades()

    while True:
        game.interface()
        keyboard.read_key()
        game.clear()

        if keyboard.is_pressed('enter'):
            game.adc_cookies()

        if keyboard.is_pressed('esc'):
            break
