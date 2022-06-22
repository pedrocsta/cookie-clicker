from os import system

def rgb(r, g, b):
    return f"\033[38;2;{r};{g};{b}m"


class Menu:
    def __init__(self, cookie, cps, cpc, itens):
        self._cookie = cookie
        self.cps = cps
        self.cpc = cpc
        self.itens = itens
    
    @property
    def cookie(self):
        mensagem = (10 - len(f'{self._cookie}')) * ' ' + f'{self._cookie}'
        return mensagem


    _bold = "\033[1m"
    _brown = rgb(170, 120, 80)
    _l_brown = rgb(190, 140, 100)
    _fecha = "\033[0m"

    def interface(self):
        print(f"""\n
                    {self._bold}{self._l_brown}Cookie {self._brown}Clicker{self._fecha} 🍪            Estatísticas 📈                        
        ───────────────────────────────────────────────────────────────────────────────     
           {self.cookie} 🍪                         CPS: {self.cps} (cookies por segundo)                 
                                                 CPC: {self.cpc} (cookies por enter)              
                                                 Items: {self.itens}
    
    
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

    @staticmethod
    def clear():
        system('cls')
