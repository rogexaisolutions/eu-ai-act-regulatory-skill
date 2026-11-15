# Comencem — ROGEX Regulatory Assistant v0.1

**Missió:** una skill pública, original i reutilitzable perquè els equips dissenyin i desenvolupin solucions amb IA d'una manera responsable i amb orientació normativa europea. **No audita, no certifica i no actualitza les lleis per si sola.**

## Pas 1 — Posar-la en un entorn de proves

- Obre un repositori **de proves**, sense secrets ni dades personals de clients.
- Descomprimeix el paquet i copia el directori `.agents/skills/rogex-regulatory-assistant/` a `.claude/skills/rogex-regulatory-assistant/`.
- També es pot instal·lar per a l'usuari a `~/.claude/skills/rogex-regulatory-assistant/`.
- Per a Codex, fes servir el directori de skills propi de l'entorn (p. ex. `.agents/skills/`).
- Verifica que Claude Code detecta la skill; invoca-la explícitament i no assumeixis autoactivació.

## Pas 2 — Primer test: proposta realista però sense dades reals

Prompt de prova:

> Usa `rogex-regulatory-assistant`. Estem dissenyant un agent que rep correus de petició de peces, identifica proveïdors, redacta sol·licituds i compara pressupostos. No envia correus sense revisió humana. Les dades inclouen noms i correus de contacte professionals. Estem a Espanya i el client pot tenir proveïdors fora de la UE. Dona'm: (1) alternativa sense IA, (2) triatge normatiu provisional amb fonts oficials verificades, (3) arquitectura, (4) controls i proves d'acceptació, (5) documents/evidències que haurem de preparar, (6) punts pendents per a un expert.

Resultat correcte: recomanacions concretes i traçables; permisos limitats; supervisió humana; tractament de dades personals; prompt-injection; transferències i proveïdors; condicions de classificació. **Cap afirmació de certificació.**

## Pas 3 — Avaluació sistemàtica

- Prova els 8 casos de `evals/cases.json`.
- Consulta `evals/HOW_TO_EVALUATE.md` i puntua els resultats, no només que la skill s'activi.
- Si falla en una situació d'alt risc, **no publiquis** fins corregir-ho.

## Pas 4 — Primera iteració

- Simplifica sortides massa llargues.
- Millora controls concrets, evidències i preguntes d'abast.
- Comprova les citacions i els terminis amb fonts oficials vigents.
- No copiïs text d'altres skills encara que estiguin disponibles en GitHub.

## Pas 5 — Publicar quan passi els tests

- Escull llicència i avisos de copyright de **la nostra** distribució.
- Publica el paquet amb versió, changelog, limitacions i enllaços a la normativa.
- A la web: `Design AI systems with documented regulatory considerations. Not a legal compliance certification.`
- **No** incloguis una Assurance Card que sembli una certificació sense haver-la revisat separadament.

## Després d'aquesta skill

1. Biblioteca normativa versionada (compartida).
2. Agent intern d'auditoria amb dos workflows (Proposal Review i Solution Audit), diferenciant propi/tercers com a metadada.
3. Regulatory Watcher amb actualització proposada i aprovada, mai autoaprovació legal.
