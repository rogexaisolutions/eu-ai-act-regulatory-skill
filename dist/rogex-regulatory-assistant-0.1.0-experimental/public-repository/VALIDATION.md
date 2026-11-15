# Distribution validation — 2026-11-16

## Passed

- Export allowlist: 11 regular Markdown files (SKILL.md, five references, five templates); no symlinks, runtime scripts, development artifacts, hidden metadata or evaluations in the standalone payload.
- All 11 exported files match source bytes and SHA-256 hashes.
- Bundled skill-creator `quick_validate.py`: exit 0; `Skill is valid!`. Validator SHA-256: `ee6dba90f44d37171c5a6edb8095979c54919ff6822c1a907afca2e78c48738c`. Checks YAML frontmatter, supported keys, naming, description limits and scaffold placeholders.
- 16 local Markdown links in the standalone skill resolve within the folder.
- Heuristic path, credential and personal-information scan: no findings. Reviewed export scope and source content; no machine-specific paths, user details or client records identified. This is not a guarantee of absence of secrets or third-party rights issues.
- ZIP CRC integrity, exact entry allowlist, safe relative paths and decompressed byte equality passed. Archive has fixed timestamps, regular-file permissions and no user-identifying metadata.
- Canonical skill and existing evaluation file hashes unchanged from the pre-build snapshot (597 protected files).

## External links

Attempted 15 unique public URLs with HTTP GET. 15 were unreachable, challenged or otherwise unverified; see [per-URL results](LINK-CHECKS.json). Reachability does not establish complete content, currency, authenticity, amendments, relevant dates or system-specific applicability. Unverified links must be checked before publication; source content was preserved without repair.

## Not run / not established

- `skills-ref`: not installed or available on PATH; no installation attempted. Only the bundled Agent Skills validator and supplemental structural checks ran.
- Existing repository validator was not run against canonical files: it hardcodes the source/evaluation layout and is not a standalone-export validator. Equivalent resource/link checks above target the export; no evaluation records were modified.
- New behavioral/scenario evaluations, live Codex discovery, Claude Code installation/execution and cross-host compatibility.
- Legal-source accuracy or freshness, regulatory compliance, legal certification, originality/ownership and exhaustive secret detection.
- No Git revision available (source working tree has no HEAD commit); provenance uses exact content hashes rather than an invented commit or validation endorsement.

## Publication blockers

- Distribution license and licensing authority require explicit owner decision; no license granted or inserted.
- Public release/brand and rights review and publication authorization remain pending.
- Resolve or explicitly accept any unverified external links in LINK-CHECKS.json before release; perform live source verification before any verified legal claims.
- Runtime compatibility and behavior remain unverified and must not be advertised as tested. None of these structural checks establishes legal assurance.

No GitHub publication, website deployment, push or remote write was performed. Packaging version 0.1.0 does not alter the skill's internal v1.0 label.
