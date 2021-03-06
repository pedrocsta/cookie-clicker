from os import system
from threading import Thread
from items import Upgrades, items
from random import randint, choice
from news import starter_news, intermediate_news, pro_news, legendary_news, mythical_news
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
    _golden = rgb(219, 180, 107)
    _reset = "\033[0m"

    def __init__(self, cookies: float, upgrades: list[int]):
        self._cookies = cookies
        self._cps, self._cpc = 0, 1
        self._golden_cookie = ''
        self.upgrades = Upgrades(items, upgrades)
        self.headline = 'Olá :)'

        Thread(target=self._auto_click).start()

    @staticmethod
    def clear():
        system('cls')

    def _auto_click(self):
        while True:
            self._cookies += self._cps
            time.sleep(1)

    def load_upgrades(self):
        for cps, cpc in self.upgrades.load_upgrades():
            self._cps, self._cpc = self._cps + cps, self._cpc + cpc

    def save_game(self):
        self.headline = 'Progresso salvo!'

    def adc_cookies(self):
        self._cookies += self._cpc

    def draw_golden_cookie(self):
        self._golden_cookie = f"{self._golden}[G] COOKIE DE OURO!!!{self._reset}" if randint(1, 100) == 1 else ''

    def given_golden_cookie(self):
        self._cookies += int(self._cookies / (4 / 3)) if self._golden_cookie else self._cpc // 10

    def upgrade(self, index: int):
        cookies, cps, cpc = self.upgrades.upgrade(self.sort_shop[index], self._cookies)
        self._cookies, self._cps, self._cpc = self._cookies - cookies, self._cps + cps, self._cpc + cpc

    def new_change(self):
        if randint(1, 10) == 1:
            news = {starter_news: 0, intermediate_news: 100, pro_news: 1000, legendary_news: 15000,
                    mythical_news: 200000}

            for key, value in news.items():
                if self._cookies < value:
                    break

                self.headline = choice(key)

    @property
    def sort_shop(self):
        index = None
        for c, item in enumerate(self.upgrades.items):
            if self._cookies <= item.cost:
                index = c
                break

        if index <= 4:
            return self.upgrades.items[:5]

        if self._cookies >= self.upgrades.items[-5].cost:
            return self.upgrades.items[-5:]

        return self.upgrades.items[index - 3:index + 2]

    @Delay.sleep(.08)
    def interface(self):
        shop = self.sort_shop
        self.draw_golden_cookie()

        def cookies(): return (10 - len(f'{round(self._cookies, 2)}')) * ' ' + f'{round(self._cookies, 2)}'
        def spaces(s): return (25 - len(shop[s].name) - len(str(shop[s].cost))) * ' '

        print(f"""\n
                    {self._bold}{self._l_brown}Cookie {self._brown}Clicker{self._reset} 🍪            Estatísticas 📈                        
        ───────────────────────────────────────────────────────────────────────────────     
           {cookies()} 🍪                         
                                                 CPS: {round(self._cps, 2)} (cookies por segundo)                 
                                                 CPC: {round(self._cpc, 2)} (cookies por click)              
                                                 Itens: {sum(self.upgrades.upgrades)}
    
    
                        Loja 🛒                            Notícias 📰                          
        ───────────────────────────────────────────────────────────────────────────────
              [1] {shop[0].name}: {shop[0].cost} 🍪{spaces(0)}{self._bold}{' '.join(self.headline.split()[:6])}{self._reset}
              [2] {shop[1].name}: {shop[1].cost} 🍪{spaces(1)}{self._bold}{' '.join(self.headline.split()[6:])}{self._reset}
              [3] {shop[2].name}: {shop[2].cost} 🍪
              [4] {shop[3].name}: {shop[3].cost} 🍪{spaces(3)}{self._golden_cookie}
              [5] {shop[4].name}: {shop[4].cost} 🍪
    

                                        Rankings 🏆
        ───────────────────────────────────────────────────────────────────────────────
              🥇 Player 01: 0 🍪
              🥈 Player 02: 0 🍪
              🥉 Player 03: 0 🍪
    
    
                  Certifique-se de pressionar [S] para salvar seu progresso!
""")

        self.new_change()
