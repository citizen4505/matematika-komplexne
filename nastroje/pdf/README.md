# Sestavení učebnice do PDF

Skript vezme všechny hotové kapitoly a vytvoří z nich jedno PDF (A4) s titulní stranou, obsahem, řešeními úloh na konci a přílohami. Odkazy uvnitř PDF jsou proklikávací.

## Co je potřeba

- **Python 3**
- **pandoc** (převod Markdownu na HTML)
- **Node.js** s `npm` (KaTeX na vzorce, Playwright s Chromiem na tisk)

Závislosti pro Node se doinstalují samy při prvním spuštění.

## Spuštění

Z kořene repozitáře:

```bash
./nastroje/pdf/sestav-pdf.sh
```

Výsledek je v `Matematika-komplexne.pdf` v kořeni repozitáře. Jiný výstup zadáte parametrem:

```bash
./nastroje/pdf/sestav-pdf.sh ~/Plocha/ucebnice.pdf
```

## Jak to funguje

1. `sestav.py` přečte obsah v `README.md` repozitáře a podle něj seřadí oblasti a kapitoly. Oblasti bez kapitol vynechá.
2. Každý soubor převede `pandoc` na HTML. Odkazy mezi soubory skript přepojí na místa uvnitř dokumentu a obrázkům doplní cestu.
3. Pořadí v PDF: u každé kapitoly výklad a příklady, potom všechna řešení, nakonec vzorce a slovníček.
4. `tisk.js` otevře HTML v Chromiu, KaTeX vysází vzorce a stránka se vytiskne do PDF s čísly stránek.

Když je ve vzorci chyba, `tisk.js` ji vypíše (`CHYBA VZORCE: …`) a v PDF je vzorec červeně.

## Soubory

| soubor | účel |
|---|---|
| `sestav-pdf.sh` | spouští celý postup |
| `sestav.py` | Markdown → jedno HTML |
| `styl.css` | vzhled stránek (písmo, okraje, zalomení) |
| `tisk.js` | HTML → PDF |
| `package.json` | závislosti pro Node |
