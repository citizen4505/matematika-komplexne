# CLAUDE.md – pravidla projektu Matematika komplexně

Ucelená učebnice matematiky od úplných základů po úroveň střední školy (maturita).
Píše se česky, v Markdownu, zobrazuje se přímo na GitHubu.

## Cílový čtenář
- Samouk nebo žák, který začíná od nuly; nepředpokládej nic, co nebylo vysvětleno dříve.
- Každý nový pojem se zavede až po pojmech, na kterých stojí (kapitoly jdou za sebou).
- Když se kapitola opírá o dřívější látku, odkaž na ni relativním odkazem, např. `[zlomky](../02-zlomky/vyklad.md)`.

## Struktura
```
<oblast>/                  # zaklady, algebra, geometrie, funkce, analyza, ...
  NN-nazev-kapitoly/       # NN = dvouciferné pořadí, název bez diakritiky, pomlčky
    vyklad.md              # výklad látky
    priklady.md            # zadání úloh
    reseni.md              # řešení úloh ze stejné kapitoly
    obrazky/               # obrázky jen pro tuto kapitolu
prilohy/
  vzorce.md                # přehled vzorců ze všech kapitol
  slovnicek.md             # pojmy abecedně, s odkazem na kapitolu
```
- Novou kapitolu zakládej vždy se všemi třemi soubory a složkou `obrazky/` (s `.gitkeep`).
- Po přidání kapitoly aktualizuj `README.md` (obsah) a případně `prilohy/`.

## vyklad.md – osnova
1. `# Název kapitoly`
2. **Co se naučíte** – 3–5 odrážek.
3. **Co potřebujete znát** – odkazy na předchozí kapitoly (u první kapitoly vynech).
4. Výklad rozdělený na sekce `##`; každá sekce: vysvětlení → definice/pravidlo → řešený příklad.
5. **Shrnutí** – nejdůležitější pravidla a vzorce v bodech.
6. Odkaz na `priklady.md`.

## priklady.md a reseni.md
- Úlohy číslované `1.`, `2.`, … a seřazené od nejlehčí; těžší označ ⭐ (náročné) nebo ⭐⭐ (výzva).
- Řešení ve stejném pořadí a se stejným číslem; ukaž postup, ne jen výsledek.
- Na konci každé úlohy v `priklady.md` odkaz na její řešení.

## Matematický zápis
- Vzorce pište v LaTeXu, GitHub je vykresluje:
  - v řádku: `$\frac{1}{2}$`
  - samostatně na řádku: blok `$$ ... $$`
- Desetinná čárka (`3{,}14`), ne tečka – v LaTeXu psát `{,}`, aby nevznikla mezera.
- Násobení `\cdot`, dělení `:` nebo zlomkem; české značení (např. `\mathrm{tg}\,x`, ne `\tan x`).
- Proměnné kurzivou (LaTeX to dělá sám), jednotky ne: `$5\ \mathrm{cm}$`.

## Styl textu
- Čtenáři vykat (`naučíte se`, `všimněte si`), nikdy netykat. Krátké věty, jeden nový pojem najednou.
- Definice tučně při prvním výskytu: **zlomek je …**
- Upozornění na časté chyby jako citace: `> ⚠️ Pozor: …`
- Žádné odkazy na externí stránky, které se mohou změnit; učebnice má být soběstačná.

## Obrázky
- Formát SVG (preferovaně) nebo PNG, uložené v `obrazky/` dané kapitoly.
- Název souboru bez diakritiky, popisný: `ciselna-osa.svg`.
- Každý obrázek má alternativní text: `![Číselná osa od −5 do 5](obrazky/ciselna-osa.svg)`.

## Git
- Commit po každé ucelené změně (jedna kapitola nebo jeden soubor), zpráva česky v rozkazovacím způsobu:
  `Přidej výklad kapitoly 02-zlomky`.
- Push na `main` prováděj sám, bez čekání na schválení autorem.
