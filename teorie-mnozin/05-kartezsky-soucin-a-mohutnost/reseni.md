# Kartézský součin a mohutnost – řešení

Zpět na [příklady](priklady.md) · [výklad](vyklad.md)

## Úloha 1

- a) Neplatí: první složky se liší ($2 \ne 5$).
- b) Platí: u množin na pořadí nezáleží.
- c) Platí.
- d) Platí: $[1, 4] = [1, 4]$.

## Úloha 2

Složky se musí rovnat po sobě:

- první složky: $x + 1 = 4$, tedy $x = 3$,
- druhé složky: $6 = 2y$, tedy $y = 3$.

## Úloha 3

$$A \times B = \{[a, 1], [a, 2], [a, 3], [b, 1], [b, 2], [b, 3]\}$$

$$B \times A = \{[1, a], [1, b], [2, a], [2, b], [3, a], [3, b]\}$$

Obě množiny mají $2 \cdot 3 = 6$ prvků, ale nerovnají se.

## Úloha 4

$$M \times M = \{[0, 0], [0, 1], [1, 0], [1, 1]\}$$

Má $2 \cdot 2 = 4$ prvky.

## Úloha 5

- a) $4 \cdot 6 = 24$
- b) $5 \cdot 0 = 0$: s prázdnou množinou nelze vytvořit žádnou dvojici, $A \times \emptyset = \emptyset$.
- c) $10 \cdot 10 = 100$

## Úloha 6

Výsledky jsou prvky $K \times K$, kde $K = \{1, 2, 3, 4, 5, 6\}$. Všech výsledků je $6 \cdot 6 = 36$.

Stejné číslo na obou kostkách: $[1, 1], [2, 2], \dots, [6, 6]$, tedy **6 výsledků**.

## Úloha 7

$|A \times B| = |A| \cdot |B|$, tedy $15 = 3 \cdot |B|$ a $|B| = 5$.

## Úloha 8

Přiřadíme $n \mapsto 2n - 1$ (šipku $\mapsto$ čtěte „přiřadíme“):

| $n$ | 1 | 2 | 3 | 4 | … |
|---|---|---|---|---|---|
| liché číslo | 1 | 3 | 5 | 7 | … |

Číslu 100 odpovídá $2 \cdot 100 - 1 = 199$.

## Úloha 9

Přiřadíme $n \mapsto 10n$: $1 \mapsto 10$, $2 \mapsto 20$, $3 \mapsto 30$, … Každé přirozené číslo má právě jednoho partnera a každý násobek deseti je partnerem právě jednoho přirozeného čísla.

## Úloha 10

Seznam s pořadím:

| místo | 1. | 2. | 3. | 4. | 5. | 6. | 7. | … |
|---|---|---|---|---|---|---|---|---|
| číslo | 0 | 1 | −1 | 2 | −2 | 3 | −3 | … |

Kladné číslo $n$ stojí na místě $2n$, záporné číslo $-n$ na místě $2n + 1$.

- Číslo $5$ stojí na **10.** místě.
- Číslo $-5$ stojí na **11.** místě.
- Číslo $-n$ stojí na místě $2n + 1$.

Každé celé číslo má tedy v seznamu své pořadí, proto je $\mathbb{Z}$ spočetná.
