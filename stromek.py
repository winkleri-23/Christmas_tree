import time
import os

def vykresli_stromek_animace(vyska):
    """Funkce pro vykreslení vánočního stromku s animací."""
    if vyska < 3:
        print("Vánoční stromek musí mít alespoň výšku 3!")
        return

    print("\n🎄 Tvůj vánoční stromek roste! 🎄\n")
    
    # Animované kreslení koruny stromu
    for i in range(1, vyska + 1):
        os.system('cls' if os.name == 'nt' else 'clear')  # Vyčištění obrazovky
        mezery = ' ' * (vyska - i)
        vetve = '*' * (2 * i - 1)

        # Zobraz aktuální stav stromu
        for j in range(1, i + 1):
            print(' ' * (vyska - j) + '*' * (2 * j - 1))
        time.sleep(0.5)  # Pauza pro efekt růstu

    # Kreslení kmene s animací
    for _ in range(2):  # Dvě vrstvy kmene
        os.system('cls' if os.name == 'nt' else 'clear')  # Vyčištění obrazovky
        for j in range(1, vyska + 1):
            print(' ' * (vyska - j) + '*' * (2 * j - 1))
        print(' ' * (vyska - 1) + '|')
        time.sleep(0.5)

    os.system('cls' if os.name == 'nt' else 'clear')  # Finální vyčištění obrazovky

    # Finální zobrazení stromku
    for i in range(1, vyska + 1):
        print(' ' * (vyska - i) + '*' * (2 * i - 1))
    print(' ' * (vyska - 1) + '|')
    print(' ' * (vyska - 1) + '|')

    print("\n🎅 Veselé Vánoce! 🎅\n")

# Interaktivní část programu
try:
    vyska = int(input("Zadej výšku stromku (např. 5): "))
    vykresli_stromek_animace(vyska)
except ValueError:
    print("Zadej platné číslo pro výšku stromku!")
