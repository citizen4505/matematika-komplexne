# Operace s množinami – řešení

Zpět na [příklady](priklady.md) · [výklad](vyklad.md)

## Úloha 1

- $A \cup B = \{1, 2, 3, 4, 5, 6, 7\}$
- $A \cap B = \{4, 5\}$
- $A \setminus B = \{1, 2, 3\}$
- $B \setminus A = \{6, 7\}$

## Úloha 2

- a) $\{a, b, c, d, e\}$
- b) $\{c\}$
- c) $\emptyset$
- d) Disjunktní jsou $A$ a $C$ a také $B$ a $C$. Množiny $A$ a $B$ disjunktní nejsou, mají společný prvek $c$.

## Úloha 3

- $A = \{2, 4, 6, 8, 10\}$, $\ B = \{1, 2, 3, 4\}$
- $A' = \{1, 3, 5, 7, 9\}$: lichá čísla ze $Z$.
- $B' = \{5, 6, 7, 8, 9, 10\}$
- $A \cap B = \{2, 4\}$
- Nejdřív sjednocení: $A \cup B = \{1, 2, 3, 4, 6, 8, 10\}$. Doplněk jsou zbylé prvky $Z$: $(A \cup B)' = \{5, 7, 9\}$.

## Úloha 4

- a) Čísla dělitelná 2 i 3, tedy násobky 6: $\{6, 12, 18, \dots\}$.
- b) Každé přirozené číslo je sudé, nebo liché: výsledek je $\mathbb{N}$.
- c) $\{4, 5, 6, \dots\}$

## Úloha 5

- a) $A \cup A = A$
- b) $A \cap Z = A$, protože všechny prvky $A$ jsou v $Z$.
- c) $A \setminus A = \emptyset$
- d) $A \cup A' = Z$

## Úloha 6

- Levá strana: $A \cap B = \{2, 4\}$, takže $(A \cap B)' = \{1, 3, 5, 6, 7, 8, 9, 10\}$.
- Pravá strana: $A' = \{1, 3, 5, 7, 9\}$, $\ B' = \{5, 6, 7, 8, 9, 10\}$, takže $A' \cup B' = \{1, 3, 5, 6, 7, 8, 9, 10\}$.

Obě strany se rovnají, zákon platí.

## Úloha 7

Kruh $B$ leží celý uvnitř kruhu $A$. Proto:

- $A \cup B = A$: sjednocení nepřidá nic nového.
- $A \cap B = B$: společné prvky jsou právě prvky $B$.

## Úloha 8

Označme $F$ žáky hrající fotbal a $L$ žáky hrající florbal. Vyplňujeme od průniku:

- oba sporty: $4$,
- jen fotbal: $12 - 4 = 8$,
- jen florbal: $9 - 4 = 5$.

$|F \cup L| = 12 + 9 - 4 = 17$. Ani jeden sport nehraje $25 - 17 = 8$ žáků.

> ⚠️ Pozor: Sečíst jen $12 + 9 = 21$ je chyba. Čtyři žáci by se tak započítali dvakrát.

## Úloha 9

Ze vzorce $|A \cup B| = |A| + |B| - |A \cap B|$:

$$12 = 10 + 7 - |A \cap B| \quad \Rightarrow \quad |A \cap B| = 17 - 12 = 5$$

$A \setminus B$ jsou prvky $A$ bez společných: $|A \setminus B| = 10 - 5 = 5$.

## Úloha 10

- a) Vybarví se oba kruhy **kromě** jejich společné části. Jsou to prvky, které patří **právě do jedné** z množin. Tato množina se nazývá **symetrický rozdíl**.
- b) Vybarví se vše v základní množině mimo oba kruhy. Jsou to prvky, které nepatří **ani do $A$, ani do $B$**. Podle De Morgana je to totéž co $A' \cap B'$.

## Úloha 11

Označme $T$ (čaj), $K$ (káva) a $C$ (kakao). Diagram tří množin vyplňujeme od středu:

1. všechny tři: $3$,
2. jen čaj a káva: $10 - 3 = 7$; jen čaj a kakao: $5 - 3 = 2$; jen káva a kakao: $6 - 3 = 3$,
3. jen čaj: $24 - 7 - 2 - 3 = 12$; jen káva: $28 - 7 - 3 - 3 = 15$; jen kakao: $12 - 2 - 3 - 3 = 4$.

Aspoň jeden nápoj pije $12 + 15 + 4 + 7 + 2 + 3 + 3 = 46$ lidí.

- Žádný z nápojů nepijí $50 - 46 = $ **4 lidé**.
- Jen kávu pije **15 lidí**.

Kontrola vzorcem pro tři množiny: $24 + 28 + 12 - 10 - 5 - 6 + 3 = 46$. Odečítáme dvojice, které jsme započítali dvakrát, a pak přičteme střed, který jsme tím odečetli o jednou víc.
