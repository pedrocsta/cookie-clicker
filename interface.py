from os import system
from items import Upgrades, items
import time


def rgb(r, g, b):
    return f"\033[38;2;{r};{g};{b}m"


class Delay:

    @staticmethod
    def sleep(delay: float):
        def features(foo):
            def wrapper(self, *args, **kwargs):
                foo(self, *args, **kwargs)
                time.sleep(delay)
            return wrapper
        return features


class CookieClicker:

    _bold = "\033[1m"
    _brown = rgb(170, 120, 80)
    _l_brown = rgb(190, 140, 100)
    _fecha = "\033[0m"

    def __init__(self, cookies: float, upgrades: list[int]):
        self._cookies = cookies
        self._cps = self._cpc = 0
        self.upgrades = Upgrades(items, upgrades)
    
    @property
    def cookie(self): return (10 - len(f'{round(self._cookies, 2)}')) * ' ' + f'{round(self._cookies, 2)}'

    @staticmethod
    def clear(): system('cls')

    def load_upgrades(self):
        for cps, cpc in self.upgrades.load_upgrades():
            self._cps += cps
            self._cpc += cpc

    def save_game(self):
        pass

    def adc_cookies(self):
        self._cookies += self._cpc

    def upgrade(self, index: int):
        upgrade = self.upgrades.upgrade(self.sort_shop[index], self._cookies)
        self._cookies -= upgrade[0]
        self._cps += upgrade[1]
        self._cpc += upgrade[2]

    @property
    def sort_shop(self):
        for index, item in enumerate(self.upgrades.items):
            if self._cookies <= item.cost:
                break

        if index <= 4:
            return self.upgrades.items[:5]

        if self._cookies >= self.upgrades.items[-5].cost:
            return self.upgrades.items[-5:]

        return self.upgrades.items[index - 3:index + 2]

    @Delay.sleep(.04)
    def interface(self):
        shop = self.sort_shop
        print(f"""\n
                    {self._bold}{self._l_brown}Cookie {self._brown}Clicker{self._fecha} 🍪            Estatísticas 📈                        
        ───────────────────────────────────────────────────────────────────────────────     
           {self.cookie} 🍪                         
                                                 CPS: {round(self._cps, 2)} (cookies por segundo)                 
                                                 CPC: {round(self._cpc, 2)} (cookies por click)              
                                                 Items: {sum(self.upgrades.upgrades)}
    
    
                        Loja 🛒                            Notícias 📰                          
        ───────────────────────────────────────────────────────────────────────────────
              [1] {shop[0].name}: {shop[0].cost} 🍪
              [2] {shop[1].name}: {shop[1].cost} 🍪
              [3] {shop[2].name}: {shop[2].cost} 🍪
              [4] {shop[3].name}: {shop[3].cost} 🍪
              [5] {shop[4].name}: {shop[4].cost} 🍪
    

                                        Rankings 🏆
        ───────────────────────────────────────────────────────────────────────────────
              🥇 Player 01: 0 🍪
              🥈 Player 02: 0 🍪
              🥉 Player 03: 0 🍪
    
    
                  Certifique-se de pressionar [S] para salvar seu progresso!
""")
