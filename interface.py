def rgb(r, g, b):
    return f"\033[38;2;{r};{g};{b}m"

bold = "\033[1m"

brown = rgb(170,120,80)
l_brown = rgb(190,140,100)

fecha = "\033[0m"

def interface(qtd_cookies, cookies_sec, cookies_click, itens):
    print(f"""\n
                {bold}{l_brown}Cookie {brown}Clicker{fecha} 🍪            Estatísticas 📈                        
    ───────────────────────────────────────────────────────────────────────────────     
            0 🍪                                CPS: 0 (cookies por segundo)                 
                                                CPC: 0 (cookies por enter)              
                                                Items: 0


                        Loja 🛒                        Notícias 📰                          
    ───────────────────────────────────────────────────────────────────────────────
          [1] Cursor: 15 🍪
          [2] Gradma: 100 🍪
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