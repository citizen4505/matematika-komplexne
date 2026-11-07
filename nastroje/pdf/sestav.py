#!/usr/bin/env python3
"""Sestaví z učebnice Matematika komplexně jeden HTML soubor připravený k tisku do PDF.

Použití: python3 sestav.py <cesta k repozitáři> <výstupní html>
Obvykle se nespouští přímo, ale přes sestav-pdf.sh.
Pořadí kapitol se bere z README.md, matematiku vysází KaTeX v prohlížeči.
"""
import os, re, sys, subprocess, datetime, html

REPO, VYSTUP = sys.argv[1], sys.argv[2]
SLOZKA = os.path.dirname(os.path.abspath(__file__))          # nastroje/pdf
KATEX = os.path.join(SLOZKA, 'node_modules/katex/dist')


def slug(cesta):
    """Z cesty souboru udělá jednoznačné id, např. zaklady/01-cisla/vyklad.md -> zaklady-01-cisla-vyklad."""
    return re.sub(r'[^a-z0-9]+', '-', os.path.splitext(cesta)[0].lower()).strip('-')


def kapitoly_z_readme():
    """Vrátí seznam oblastí [(název oblasti, [(název kapitoly, složka), ...]), ...] v pořadí README."""
    oblasti = []
    for radek in open(os.path.join(REPO, 'README.md'), encoding='utf-8'):
        m = re.match(r'^- \[(.+?)\]\((.+?)\)', radek)          # oblast
        k = re.match(r'^\s+- \[(.+?)\]\((.+?)/vyklad\.md\)', radek)  # kapitola
        if m:
            oblasti.append((m.group(1), []))
        elif k and oblasti:
            oblasti[-1][1].append((k.group(1), k.group(2)))
    # jen oblasti, které už mají kapitoly (prázdné složky do PDF nepatří)
    return [o for o in oblasti if o[1]]


def preved(cesta):
    """Převede jeden .md soubor na HTML a přepojí odkazy a obrázky dovnitř dokumentu."""
    rel = os.path.relpath(cesta, REPO)
    prefix = slug(rel)
    vystup = subprocess.run(
        ['pandoc', '-f', 'gfm+tex_math_dollars', '-t', 'html', '--katex', f'--id-prefix={prefix}--', cesta],
        capture_output=True, text=True, check=True).stdout

    def odkaz(m):
        href, text = m.group(1), m.group(2)
        if href.startswith('http'):  # externí odkazy necháme
            return m.group(0)
        cil, _, kotva = html.unescape(href).partition('#')
        if not cil:  # odkaz uvnitř téhož souboru
            return f'<a href="#{prefix}--{kotva}">{text}</a>'
        abs_cil = os.path.normpath(os.path.join(os.path.dirname(cesta), cil))
        if not abs_cil.endswith('.md') or not os.path.exists(abs_cil):
            return text  # odkaz na složku nebo neexistující soubor: ponecháme jen text
        p = slug(os.path.relpath(abs_cil, REPO))
        return f'<a href="#{p}--{kotva}">{text}</a>' if kotva else f'<a href="#{p}">{text}</a>'

    vystup = re.sub(r'<a href="([^"]+)">(.*?)</a>', odkaz, vystup, flags=re.S)
    # obrázky: absolutní cesta, ať je prohlížeč najde
    vystup = re.sub(r'src="([^"]+)"',
                    lambda m: f'src="file://{os.path.normpath(os.path.join(os.path.dirname(cesta), m.group(1)))}"',
                    vystup)
    return f'<section class="soubor" id="{prefix}">\n{vystup}\n</section>\n'


oblasti = kapitoly_z_readme()
casti, obsah, reseni = [], [], []

for c_obl, (nazev_obl, kapitoly) in enumerate(oblasti, 1):
    id_obl = f'oblast-{c_obl}'
    casti.append(f'<div class="cast" id="{id_obl}"><p class="cast-cislo">Část {c_obl}</p><h1 class="cast-nazev">{nazev_obl}</h1></div>')
    obsah.append(f'<li class="obsah-cast"><a href="#{id_obl}">Část {c_obl}: {nazev_obl}</a><ol>')
    for nazev_kap, slozka in kapitoly:
        v = os.path.join(REPO, slozka, 'vyklad.md')
        casti.append(preved(v))
        casti.append(preved(os.path.join(REPO, slozka, 'priklady.md')))
        reseni.append(preved(os.path.join(REPO, slozka, 'reseni.md')))
        obsah.append(f'<li><a href="#{slug(os.path.relpath(v, REPO))}">{nazev_kap}</a></li>')
    obsah.append('</ol></li>')

# řešení všech úloh na konci, pak přílohy
casti.append('<div class="cast" id="reseni"><p class="cast-cislo">Řešení</p><h1 class="cast-nazev">Řešení úloh</h1></div>')
casti += reseni
obsah.append('<li class="obsah-cast"><a href="#reseni">Řešení úloh</a></li>')
casti.append('<div class="cast" id="prilohy"><p class="cast-cislo">Přílohy</p><h1 class="cast-nazev">Vzorce a slovníček</h1></div>')
for soubor, nazev in (('prilohy/vzorce.md', 'Vzorce'), ('prilohy/slovnicek.md', 'Slovníček pojmů')):
    casti.append(preved(os.path.join(REPO, soubor)))
obsah.append('<li class="obsah-cast"><a href="#prilohy">Přílohy: vzorce a slovníček</a></li>')

datum = datetime.date.today().strftime('%-d. %-m. %Y')
stranka = f'''<!DOCTYPE html>
<html lang="cs"><head><meta charset="utf-8">
<title>Matematika komplexně</title>
<link rel="stylesheet" href="file://{KATEX}/katex.min.css">
<link rel="stylesheet" href="file://{os.path.join(SLOZKA, 'styl.css')}">
<script src="file://{KATEX}/katex.min.js"></script>
</head><body>
<div class="titul">
  <h1>Matematika komplexně</h1>
  <p class="podtitul">Ucelená učebnice matematiky od základů po střední školu</p>
  <p class="datum">Pracovní verze, {datum}</p>
</div>
<nav class="obsah"><h2>Obsah</h2><ol>{"".join(obsah)}</ol></nav>
{"".join(casti)}
<script>
// vysázení vzorců: pandoc nechal TeX v <span class="math inline|display">
document.querySelectorAll('span.math').forEach(el => {{
  const tex = el.textContent;
  try {{ katex.render(tex, el, {{displayMode: el.classList.contains('display'), throwOnError: true}}); }}
  catch (e) {{ el.classList.add('chyba-vzorce'); console.log('CHYBA VZORCE: ' + tex + ' :: ' + e.message); }}
}});
document.body.dataset.hotovo = '1';
</script>
</body></html>'''
open(VYSTUP, 'w', encoding='utf-8').write(stranka)
print('oblastí:', len(oblasti), 'kapitol:', sum(len(k) for _, k in oblasti))
