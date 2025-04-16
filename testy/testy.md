 # Manuální testy – Kalkulačka

**Verze:** 1.0
**Autor:** *Dominik Jílek*

---

## Test 1 – Sčítání dvou kladných čísel
**Vstup:** 8 a 6
**Očekávaný výstup:**
- Sčítání: 14
- Odčítání: 2
- Násobení: 48
- Dělení: 1.333...
- Modulo: 2
**Výsledek:** **OK**

---

## Test 2 – Dělení nulou
**Vstup:** 10 a 0
**Očekávaný výstup:**
- Program by měl zobrazit chybu nebo výjimku

**Skutečný výstup:**
- Program spadl s chybou: `ZeroDivisionError: float division by zero`
**Výsledek:** **FAIL**
**Poznámka:** Výjimka není ošetřena. Uživatel by měl vidět hlášku např. "Chyba: Dělení nulou není možné."

---

## Test 3 – Záporná čísla
**Vstup:** -12 a -3
**Očekávaný výstup:**
- Sčítání: -15
- Odčítání: -9
- Násobení: 36
- Dělení: 4
- Modulo: 0
**Výsledek:** **OK**

---

## Test 4 – Desetinná čísla
**Vstup:** 3.7 a 2.8
**Očekávaný výstup:**
- Sčítání: 6.5
- Odčítání: 0.9
- Násobení: 10.36
- Dělení: 1.321...
- Modulo: 0.9
**Výsledek:** **OK**

---

## Test 5 – Velká čísla
**Vstup:** 1000000 a 2000000
**Očekávaný výstup:**
- Sčítání: 3000000
- Odčítání: -1000000
- Násobení: 2000000000000
- Dělení: 0.5
- Modulo: 1000000
**Výsledek:** **OK**

---

## Test 6 – První číslo je nula
**Vstup:** 0 a 9
**Očekávaný výstup:**
- Sčítání: 9
- Odčítání: -9
- Násobení: 0
- Dělení: 0
- Modulo: 0
**Výsledek:** **OK**

---

## Test 7 – Záporné a kladné číslo
**Vstup:** -5 a 2
**Očekávaný výstup:**
- Sčítání: -3
- Odčítání: -7
- Násobení: -10
- Dělení: -2.5
- Modulo: 1
**Výsledek:** **OK**

---

## Test 8 – Dlouhá desetinná čísla
**Vstup:** 7.123456 a 2.345678
**Očekávaný výstup:**
- Sčítání: 9.469134
- Odčítání: 4.777778
- Násobení: 16.714837
- Dělení: cca 3.036...
- Modulo: cca 2.4321...
**Výsledek:** **OK**

---

## Test 9 – Modulo s desetinnými čísly
**Vstup:** 5.5 a 2.2
**Očekávaný výstup:**
- Sčítání: 7.7
- Odčítání: 3.3
- Násobení: 12.1
- Dělení: 2.5
- Modulo: 1.1
**Výsledek:** **OK**

---

## Test 10 – Neplatný vstup (např. písmena)
**Vstup:** „a“ a „b“
**Očekávaný výstup:**
- Program by měl vyhodit chybu při převodu vstupu na číslo (ValueError)

**Skutečný výstup:**
- `ValueError: could not convert string to float: 'a'`
**Výsledek:** **OK**

---

## Test 11 – Nevyplněné první pole
**Vstup:** [prázdné] a 5
**Očekávaný výstup:**
- Program by měl vyhodit chybu při převodu na číslo (např. ValueError).

**Skutečný výstup:**
- `ValueError: could not convert string to float: ''`
**Výsledek:** **OK**
**Poznámka:** Doporučujeme přidat informaci pro uživatele, že první pole musí být vyplněno číslem.

---

## Test 12 – Nevyplněné druhé pole
**Vstup:** 7 a [prázdné]
**Očekávaný výstup:**
- Program by měl vyhodit chybu při převodu na číslo (např. ValueError).

**Skutečný výstup:**
- `ValueError: could not convert string to float: ''`
**Výsledek:** **OK**
**Poznámka:** Doporučujeme přidat informaci pro uživatele, že druhé pole musí být vyplněno číslem.

---

## Test 13 – Obě pole nevyplněná
**Vstup:** [prázdné] a [prázdné]
**Očekávaný výstup:**
- Program by měl vyhodit chybu při převodu na číslo (např. ValueError).

**Skutečný výstup:**
- `ValueError: could not convert string to float: ''`
**Výsledek:** **OK**
**Poznámka:** Doporučujeme informovat uživatele, že obě pole musí být vyplněna číslem.

---

## Test 14 – Kombinace číslo a písmeno
**Vstup:** 4 a „x“
**Očekávaný výstup:**
- Program by měl vyhodit chybu při převodu na číslo (např. ValueError).

**Skutečný výstup:**
- `ValueError: could not convert string to float: 'x'`
**Výsledek:** **OK**
**Poznámka:** Pole musí obsahovat platné číslo. Písmena nejsou platný vstup.

---

## Test 15 – Kombinace písmeno a číslo
**Vstup:** „x“ a 9
**Očekávaný výstup:**
- Program by měl vyhodit chybu při převodu na číslo (např. ValueError).

**Skutečný výstup:**
- `ValueError: could not convert string to float: 'x'`
**Výsledek:** **OK**
**Poznámka:** Pole musí obsahovat platné číslo. Písmena nejsou platný vstup.

---

## Test 16 – Velmi malá desetinná čísla
**Vstup:** 0.000001 a 0.000002
**Očekávaný výstup:**
- Sčítání: 0.000003
- Odčítání: -0.000001
- Násobení: 0.000000000002 (2e-12)
- Dělení: 0.5
- Modulo: 0.000001 (1e-06)

**Skutečný výstup:**
- Sčítání: 3e-06
- Odčítání: -1e-06
- Násobení: 2e-12
- Dělení: 0.5
- Modulo: 1e-06
**Výsledek:** **OK**
**Poznámka:** Výstupy jsou zobrazeny ve vědeckém zápisu. Doporučujeme informovat uživatele.

---

## Test 17 – Velmi velká čísla
**Vstup:** 99999999999 a 888888888888
**Očekávaný výstup:**
- Sčítání: 988888888887
- Odčítání: -788888888889
- Násobení: velmi velké číslo (ve vědeckém formátu)
- Dělení: přibližně 0.1125
- Modulo: 99999999999

**Skutečný výstup:**
- Sčítání: 988888888887.0
- Odčítání: -788888888889.0
- Násobení: 8.888888888791111e+22
- Dělení: 0.1124999999989875
- Modulo: 99999999999.0
**Výsledek:** **OK**
**Poznámka:** Výstupy mohou být ve vědeckém formátu (např. `e+22`).

---

## Test 18 – Dvě velmi velká čísla
**Vstup:** 999999999999 a 888888888888
**Očekávaný výstup:**
- Sčítání: 1888888888887
- Odčítání: 111111111111
- Násobení: velmi velké číslo (ve vědeckém formátu)
- Dělení: přibližně 1.125
- Modulo: 111111111111

**Skutečný výstup:**
- Sčítání: 1888888888887.0
- Odčítání: 111111111111.0
- Násobení: 8.888888888871112e+23
- Dělení: 1.125
- Modulo: 111111111111.0
**Výsledek:** **OK**
**Poznámka:** Výstupy jsou správné, ale program je zobrazuje ve vědeckém zápisu.