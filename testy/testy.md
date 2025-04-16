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

