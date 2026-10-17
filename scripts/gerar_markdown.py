#!/usr/bin/env python3
"""Gera os arquivos markdown em testes/ a partir dos JSON em dados/."""
import json
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
FONTES = {
    "ingles": RAIZ / "dados" / "ingles",
    "mestrado": RAIZ / "dados" / "mestrado",
}
DESTINOS = {
    "ingles": RAIZ / "testes" / "ingles",
    "mestrado": RAIZ / "testes" / "mestrado",
}


def render(teste: dict) -> str:
    linhas = [f"# {teste['titulo']}", ""]
    linhas.append(f"**Tópico:** {teste['topico']}  ")
    linhas.append(f"**Instruções:** {teste['instrucoes']}")

    dificuldades = [q["dificuldade"] for q in teste["questoes"] if q.get("dificuldade")]
    if dificuldades:
        contagem = {nivel: dificuldades.count(nivel) for nivel in ["básico", "intermediário", "avançado"]}
        linhas.append(
            f"**Dificuldade:** básico {contagem['básico']} · "
            f"intermediário {contagem['intermediário']} · "
            f"avançado {contagem['avançado']}"
        )
    linhas.append("")

    if teste.get("texto"):
        linhas.append("## Texto")
        linhas.append("")
        for paragrafo in teste["texto"].split("\n"):
            paragrafo = paragrafo.strip()
            if paragrafo:
                linhas.append(f"> {paragrafo}")
                linhas.append(">")
        if linhas[-1] == ">":
            linhas.pop()
        linhas.append("")

    linhas.append("## Questões")
    linhas.append("")
    for q in teste["questoes"]:
        tags = []
        if q.get("dificuldade"):
            tags.append(q["dificuldade"])
        if q.get("tipo"):
            tags.append(q["tipo"])
        if q.get("assunto"):
            tags.append(q["assunto"])
        sufixo_tags = f" _({' · '.join(tags)})_" if tags else ""
        linhas.append(f"**{q['numero']}.** {q['enunciado']}{sufixo_tags}")
        linhas.append("")
        for letra, texto in q["alternativas"].items():
            linhas.append(f"- **{letra})** {texto}")
        linhas.append("")

    linhas.append("## Gabarito e explicações")
    linhas.append("")
    for q in teste["questoes"]:
        linhas.append(f"**{q['numero']}. Resposta: {q['resposta']}**")
        linhas.append("")
        for letra, explicacao in q["explicacoes"].items():
            marcador = "✅" if letra == q["resposta"] else "❌"
            linhas.append(f"- {marcador} **{letra})** {explicacao}")
        linhas.append("")

    return "\n".join(linhas).rstrip() + "\n"


def main():
    for categoria, pasta_fonte in FONTES.items():
        pasta_destino = DESTINOS[categoria]
        pasta_destino.mkdir(parents=True, exist_ok=True)
        gitkeep = pasta_destino / ".gitkeep"
        if gitkeep.exists():
            gitkeep.unlink()
        for arquivo_json in sorted(pasta_fonte.glob("teste-*.json")):
            teste = json.loads(arquivo_json.read_text(encoding="utf-8"))
            markdown = render(teste)
            destino = pasta_destino / arquivo_json.with_suffix(".md").name
            destino.write_text(markdown, encoding="utf-8")
            print(f"Gerado: {destino.relative_to(RAIZ)}")


if __name__ == "__main__":
    main()
