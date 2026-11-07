#!/usr/bin/env bash
# Sestaví celou učebnici do jednoho PDF.
# Použití (z kořene repozitáře):  ./nastroje/pdf/sestav-pdf.sh [výstup.pdf]
# Výchozí výstup: Matematika-komplexne.pdf v kořeni repozitáře.
set -euo pipefail

SLOZKA="$(cd "$(dirname "$0")" && pwd)"        # nastroje/pdf
REPO="$(cd "$SLOZKA/../.." && pwd)"           # kořen repozitáře
VYSTUP="${1:-$REPO/Matematika-komplexne.pdf}"

# při prvním spuštění doinstaluj závislosti (KaTeX a Playwright s prohlížečem)
if [ ! -d "$SLOZKA/node_modules" ]; then
  echo "Instaluji závislosti…"
  (cd "$SLOZKA" && npm install --silent && npx playwright install chromium)
fi

# 1) Markdown → jedno HTML (pořadí kapitol podle README.md)
python3 "$SLOZKA/sestav.py" "$REPO" "$SLOZKA/ucebnice.html"
# 2) HTML → PDF přes Chromium (vysází vzorce, očísluje stránky)
(cd "$SLOZKA" && node tisk.js ucebnice.html "$VYSTUP")

echo "Hotovo: $VYSTUP"
