# Estudo-Mestrado

Repositório de preparação para a prova de seleção do mestrado na USP (fim deste mês): inglês (compreensão de texto acadêmico) e conteúdo específico da área.

## Estrutura

- `materiais/` — materiais de referência enviados por você (PDFs, textos, resumos) que servem de base para gerar os testes. Organize por assunto se enviar vários (ex: `materiais/ingles/`, `materiais/topico-x/`).
- `testes/ingles/` — 10 testes de inglês (compreensão de texto acadêmico), um arquivo markdown por teste.
- `testes/mestrado/` — 10 testes da matéria específica do mestrado, um arquivo markdown por teste.

## Formato de cada teste

Cada arquivo markdown contém:
- Enunciado/texto-base (quando aplicável) e as questões.
- Gabarito ao final.
- Para cada questão **errada possível**, um comentário explicando por que a alternativa correta é certa e por que as demais estão erradas.

O formato exato da questão (múltipla escolha, discursiva curta, etc.) é escolhido conforme o que fizer mais sentido para o material/assunto de cada teste.

## Versão interativa

Quiz interativo (responde, corrige na hora e mostra a explicação de cada questão): https://claude.ai/artifact/3siyTpsKFFAhc4dq1nJVmN

Fonte dos dados: `dados/ingles/*.json` e `dados/mestrado/*.json`. Para gerar os arquivos derivados depois de editar os JSON:

```
python3 scripts/gerar_markdown.py   # atualiza testes/ingles/*.md e testes/mestrado/*.md
python3 scripts/build_quiz.py       # gera dist/quiz.html (publicar de novo manualmente)
```

## Status

- Inglês: 10 testes prontos (20 questões cada, texto em inglês + perguntas/alternativas em português), seguindo o formato da Parte 1 do edital 2610 Poli-Produção (compreensão de leitura, 20 questões, 2h15min).
- Mestrado: 10 testes prontos (10 questões cada) sobre a linha de pesquisa Qualidade e Sustentabilidade (QS) do PPGEP.
- Todas as questões têm explicação em português para cada alternativa (certa e erradas).
