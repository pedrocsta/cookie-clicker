import keyboard

from interface import interface

if __name__ == '__main__':
        interface(0, 0, 0, 0)
        print(f'\nTecla pressionada: {keyboard.read_key()}')
        
        if keyboard.is_pressed('esc'):
            print("\n" * 30)