# Kalkulačka 

# Vstup uživatele do kalkulačky
vstup = input("Pro vstup do kalkulačky prosím stisknete Enter")

# Zadání čísel od uživatele
cislo1 = input("Zadejte první číslo (pokud chcete zadat desetinné číslo použijte .) a stisknete Enter: ")
cislo2 = input("Zadejte druhé číslo (pokud chcete zadat desetinné číslo použijte .) a stisknete Enter: ")

# Výpis zadaných čísel
print("první zadané číslo: ", cislo1)
print("druhé zadané číslo: ", cislo2)

# Převod vstupů na celá čísla
cislo1 = float(cislo1)
cislo2 = float(cislo2)

# Výpočty
print("Sčítání:", cislo1 + cislo2 )
print("Odčítání:", cislo1 - cislo2 )
print("Násobení:", cislo1 * cislo2 )      
print("Dělení:", cislo1 / cislo2 )
print("Modulo:", cislo1 % cislo2)
