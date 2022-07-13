from os import system
from items import Upgrade, items


def rgb(r, g, b):
    return f"\033[38;2;{r};{g};{b}m"


class CookieClicker:

    _bold = "\033[1m"
    _brown = rgb(170, 120, 80)
    _l_brown = rgb(190, 140, 100)
    _fecha = "\033[0m"

    def __init__(self, cookies: float, upgrades: list):
        self._cookies = cookies
        self._cps = self._cpc = 0
        self.upgrades = upgrades
    
    @property
    def cookie(self): return (10 - len(f'{self._cookies}')) * ' ' + f'{self._cookies}'

    @staticmethod
    def clear(): system('cls')

    def load_upgrades(self):
        up = Upgrade(items, self.upgrades)

        for cps, cpc in up.load_upgrades():
            self._cps += cps
            self._cpc += cpc

    def save_game(self):
        pass

    def adc_cookies(self):
        self._cookies += self._cpc

    def interface(self):
        print(f"""\n
                    {self._bold}{self._l_brown}Cookie {self._brown}Clicker{self._fecha} 🍪            Estatísticas 📈                        
        ───────────────────────────────────────────────────────────────────────────────     
           {self.cookie} 🍪                         
                                                 CPS: {self._cps} (cookies por segundo)                 
                                                 CPC: {self._cpc} (cookies por click)              
                                                 Items: {sum(self.upgrades)}
    
    
                        Loja 🛒                            Notícias 📰                          
        ───────────────────────────────────────────────────────────────────────────────
              [1] Cursor: 15 🍪
              [2] Grandma: 100 🍪
              [3] Fingers: 400 🍪
              [4] Farm: 1100 🍪
              [5] Mine: 12000 🍪
    

                                        Rankings 🏆
        ───────────────────────────────────────────────────────────────────────────────
              🥇 Player 01: 0 🍪
              🥈 Player 02: 0 🍪
              🥉 Player 03: 0 🍪
    
    
                  Certifique-se de pressionar [S] para salvar seu progresso!
""")
