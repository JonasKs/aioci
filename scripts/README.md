Generate stubs by:

```bash
poetry run monkeytype run scripts/generate_base.py
poetry run monkeytype stub aioci.core > aioci/core.pyi 
poetry run python scripts/inject_aci_stubs.py
```
