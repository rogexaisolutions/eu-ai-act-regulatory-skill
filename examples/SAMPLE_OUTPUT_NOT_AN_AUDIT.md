# Exemple de sortida — agent de proveïdors (fictici)

**Type:** INITIAL DESIGN REVIEW (sample). **NOT ASSESSED.**

**Objectiu:** convertir correus de sol·licitud de material en esborranys de petició i comparativa d'ofertes. S'exigeix aprovació humana abans de l'enviament.

**Decisió d'arquitectura:** extracció estructurada -> identificació d'articles/proveïdors -> generació d'esborrany -> validació humana -> enviament per eina amb permisos limitats -> registre de l'acció. Considerar parser determinista per a parts repetitives.

**Preguntes que poden canviar la classificació:** Qui és responsable del tractament de dades? Quins correus s'importen? Les dades s'envien fora de la UE? El sistema pot crear ordres de compra o únicament esborranys? Quin és l'ús previst exactament?

**Controls proposats (encara no verificats):**

| Risc | Control | Prova d'acceptació | Estat |
|---|---|---|---|
| Instruccions malicioses dins correu | Tractar correus com dades no fiables; restringir eines | Correu de prova que demana exfiltració no pot activar enviament | PLANNED |
| Enviament accidental | Porta d'aprovació humana amb vista prèvia | Cap correu surt sense aprovació explícita | PLANNED |
| Accés excessiu a bústia | Scopes mínims, secrets al vault | Tests de denegació d'accés i revisió d'API scopes | PLANNED |
| Informació personal | Minimització i política de retenció | Data map, base jurídica/contractes verificats i test de purga | NOT VERIFIED |
| Referències equivocades | Validació de dades i traçabilitat | Conjunt de casos sintètics amb falsos positius mesurats | PLANNED |

**Regulatory screening:** pendent de verificació de la normativa actual i dels fets específics del client. En aquest exemple **no** es conclou que compleixi l'AI Act ni el RGPD.

**Final audit must verify:** còpia del flux d'aprovació, permisos API, tests d'atacs, contractes de dades, proves de recuperació i revisions humanes.
