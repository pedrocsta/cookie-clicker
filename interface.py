from os import system


def rgb(r, g, b):
    return f"\033[38;2;{r};{g};{b}m"


class Menu:

    _bold = "\033[1m"
    _brown = rgb(170, 120, 80)
    _l_brown = rgb(190, 140, 100)
    _fecha = "\033[0m"

    def interface(self, qtd_cookies, cookies_sec, cookies_click, itens):
        print(f"""\n
                    {self._bold}{self._l_brown}Cookie {self._brown}Clicker{self._fecha} 🍪            Estatísticas 📈                        
        ───────────────────────────────────────────────────────────────────────────────     
                0 🍪                                CPS: 0 (cookies por segundo)                 
                                                    CPC: 0 (cookies por enter)              
                                                    Items: 0
    
    
                            Loja 🛒                        Notícias 📰                          
        ───────────────────────────────────────────────────────────────────────────────
              [1] Cursor: 15 🍪
              [2] Grandma: 100 🍪
              [3] Fingers: 400 🍪
              [4] Farm: 1100 🍪
              [5] Mine: 12000 🍪
    
    
                                        Rankings 🏆
        ───────────────────────────────────────────────────────────────────────────────
              🥇 Player 01: 🍪
              🥈 Player 02: 🍪
              🥉 Player 03: 🍪
    
    
                  Certifique-se de pressionar [S] para salvar seu progresso!
    """)

    @staticmethod
    def clear():
        system('cls')
