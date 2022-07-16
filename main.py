import keyboard
from interface import CookieClicker

if __name__ == '__main__':
    id_ = input("Qual o seu ID? ")

    game = CookieClicker(0, [0, 0, 0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    game.load_upgrades()

    while True:
        game.interface()
        options = {'1': lambda: game.upgrade(0),
                   '2': lambda: game.upgrade(1),
                   '3': lambda: game.upgrade(2),
                   '4': lambda: game.upgrade(3),
                   '5': lambda: game.upgrade(4),
                   's': game.save_game,
                   'g': game.given_golden_cookie,
                   'esc': exit,
                   }

        options.get(keyboard.read_key(), game.adc_cookies)()

        game.clear()
