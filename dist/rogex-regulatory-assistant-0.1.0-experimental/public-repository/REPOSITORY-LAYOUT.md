# Proposed public GitHub repository layout

The `public-repository/` staging directory is the proposed repository root:

```text
README.md
CHANGELOG.md
LICENSE-DECISION.md
MANIFEST.json
VALIDATION.md
LINK-CHECKS.json
REPOSITORY-LAYOUT.md
rogex-regulatory-assistant/
  SKILL.md
  references/  (five unchanged Markdown files)
  templates/   (five unchanged Markdown files)
```

Add a LICENSE file only after explicit authorization of its terms. The standalone ZIP is a sibling of this proposed root, suitable as a future release asset after approval. It contains only the skill folder. Canonical development files, evaluations, local configuration, Git history and private provenance paths are excluded. No remote repository has been created.
