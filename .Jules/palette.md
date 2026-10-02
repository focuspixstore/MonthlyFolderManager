## 2025-05-18 - Flexible CLI Confirmation Prompts
**Learning:** In CLI user interactions, requiring strict single-letter responses (`y`/`n`) increases user error rates. Capitalizing default options (e.g. `[Y/n]`) and allowing full-word inputs (`yes`/`no`) along with `Enter` key fallback significantly improves interaction smoothness and accessibility.
**Action:** Always provide uppercase default choice hints and word alias mapping when implementing CLI prompt helpers.
