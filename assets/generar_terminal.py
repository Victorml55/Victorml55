# Uso: python3 generar_terminal.py   ->  crea terminal.svg en esta carpeta
# Edita SOLO esta lista (maximo ~40 caracteres por frase):
FRASES = [
    "docker compose up y a rezar",
    "probablemente estoy comiendo",
    "o jugando",
    "ayer si funcionaba",
    "ya dejalo asi, ya jala",
    "ya luego documentamos",
    "bug?? es una funcion no documentada",
    "¿de verdad alguien lee esto?",
    "127.0.0.1",
    "no le abre mi proyecto en localhost?",
    "ya fin"
]
TITULO = "victorml@TecNM: ~"

CW = 12             # ancho por caracter
SLOT = 5.0          # segundos por frase
ESCRIBIR, PAUSA, BORRAR = 1.5, 2.0, 1.0
TOTAL = SLOT * len(FRASES)

def esc(c):
    return {"&": "&amp;", "<": "&lt;", ">": "&gt;", "'": "&apos;", '"': "&quot;"}.get(c, c)

filas = []
for k, frase in enumerate(FRASES):
    if len(frase) > 40:
        print(f"Aviso: '{frase}' tiene {len(frase)} caracteres, puede salirse de la ventana")
    n = len(frase)
    base = k * SLOT
    for i, c in enumerate(frase):
        if c == " ":
            continue
        t_on = (base + ESCRIBIR * (i + 1) / n) / TOTAL
        t_off = (base + ESCRIBIR + PAUSA + BORRAR * (n - i) / n) / TOTAL
        filas.append(
            f'  <text x="{52 + i * CW}" y="94" fill="#e6edf3" opacity="0">{esc(c)}'
            f'<animate attributeName="opacity" dur="{TOTAL:g}s" repeatCount="indefinite" '
            f'calcMode="discrete" keyTimes="0;{t_on:.5f};{t_off:.5f};1" values="0;1;0;0"/></text>'
        )

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="560" height="150" viewBox="0 0 560 150">
  <style>text {{ font-family: 'Courier New', Courier, monospace; font-size: 20px; }}</style>
  <rect x="1" y="1" width="558" height="148" rx="10" fill="#0d1117" stroke="#30363d" stroke-width="2"/>
  <rect x="1" y="1" width="558" height="34" rx="10" fill="#161b22"/>
  <rect x="1" y="20" width="558" height="15" fill="#161b22"/>
  <circle cx="24" cy="18" r="6" fill="#ff5f56"/>
  <circle cx="44" cy="18" r="6" fill="#ffbd2e"/>
  <circle cx="64" cy="18" r="6" fill="#27c93f"/>
  <text x="280" y="23" font-size="13" fill="#8b949e" text-anchor="middle">{TITULO}</text>
  <text x="28" y="94" fill="#3fb950">$</text>
{chr(10).join(filas)}
</svg>
'''
open("terminal.svg", "w", encoding="utf-8").write(svg)
print("terminal.svg generado con", len(FRASES), "frases")
