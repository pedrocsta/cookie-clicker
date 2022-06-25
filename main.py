import keyboard
from interface import Menu

if __name__ == '__main__':
    id = input("Qual o seu ID? ")

    menu = Menu(0, 0, 1, 0)

    while True:
        menu.interface()
        keyboard.read_key()
        menu.clear()

        if keyboard.is_pressed('enter'):
            menu.adc_cookies()

        if keyboard.is_pressed('esc'):
            break
            