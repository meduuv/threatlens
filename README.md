# ThreatLens

> Structured threat-intelligence analysis for defensive security workflows.

ThreatLens is a lightweight Python toolkit for turning user-supplied indicators into normalized, structured defensive analysis. It is designed for local investigation, triage and reporting rather than active exploitation.

## What it does

- Accepts indicator data for local analysis
- Normalizes security-relevant values into consistent records
- Produces structured findings suitable for downstream tooling
- Keeps analysis deterministic and easy to integrate
- Works without requiring a network connection

## Design goals

ThreatLens follows a simple principle: **make security data easier to reason about**.

The project separates indicator handling from reporting so the resulting data can be consumed by scripts, dashboards or other defensive tools.

## Example

```python
from threatlens import analyze

result = analyze(["example.com", "192.0.2.10"])

for finding in result:
    print(finding)
```

The exact API depends on the current package implementation. See the source and tests for the supported interface.

## Security boundary

ThreatLens is intended for systems and data you are authorized to analyze.

It does not provide exploitation, credential theft, payload delivery or unauthorized access functionality.

## Development

```bash
python -m pytest
```

## License

MIT. See `LICENSE`.

## Author

Built by **Medu** · https://guns.lol/meduu