#!/usr/bin/env python3
"""Monta o HTML do quiz interativo embutindo os dados JSON no template."""
import json
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
DADOS = RAIZ / "dados"
TEMPLATE = Path(__file__).parent / "quiz_template.html"
SAIDA = RAIZ / "dist" / "quiz.html"


def carregar(categoria: str) -> list:
    pasta = DADOS / categoria
    testes = []
    for arquivo in sorted(pasta.glob("teste-*.json")):
        testes.append(json.loads(arquivo.read_text(encoding="utf-8")))
    return testes


def main():
    dados = {
        "ingles": carregar("ingles"),
        "mestrado": carregar("mestrado"),
    }
    dados_json = json.dumps(dados, ensure_ascii=False)
    # Evita que "</script" dentro dos dados feche a tag <script> no HTML.
    dados_json = dados_json.replace("</script", "<\\/script").replace("</SCRIPT", "<\\/SCRIPT")

    template = TEMPLATE.read_text(encoding="utf-8")
    html = template.replace("__DADOS_JSON__", dados_json)

    SAIDA.parent.mkdir(parents=True, exist_ok=True)
    SAIDA.write_text(html, encoding="utf-8")
    print(f"Gerado: {SAIDA} ({SAIDA.stat().st_size / 1024:.1f} KB)")


if __name__ == "__main__":
    main()
