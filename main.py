import keyboard
from interface import Menu

if __name__ == '__main__':
    menu = Menu(0, 0, 0, 0)

    while True:
        menu.interface()
        keyboard.read_key()
        menu.clear()

        if keyboard.is_pressed('enter'):
            menu.cookie += menu.cpc

        if keyboard.is_pressed('esc'):
            break
        