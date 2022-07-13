import keyboard
from interface import CookieClicker

if __name__ == '__main__':
    id_ = input("Qual o seu ID? ")

    game = CookieClicker(0, [0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 0, 0])
    game.load_upgrades()

    while True:
        game.interface()

        {'esc': exit,
         's': game.save_game

         }.get(keyboard.read_key(), game.adc_cookies)()

        game.clear()
