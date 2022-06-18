import keyboard
from interface import Menu

if __name__ == '__main__':
    menu = Menu()

    while True:
        menu.interface(0, 0, 0, 0)
        keyboard.read_key()
        menu.clear()

        if keyboard.is_pressed('esc'):
            break
