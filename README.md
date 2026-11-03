# Wrapped catalog client lab

Small synthetic client of the catalog SDK in
[qodo-governance-lab](https://github.com/1984ys129/qodo-governance-lab).
`client.py` imports `catalog.service.Catalog` from that repository and calls its
`get_product` facade. SDK transport details remain inside the catalog service.

This integration follows the SDK source from its main branch; it is not a
separately published package or a pinned production deployment. Candidate SDK
revisions are checked by placing the selected SDK checkout on `PYTHONPATH`.

With both repositories checked out as siblings, run from this directory in PowerShell:

```powershell
$env:PYTHONPATH = (Resolve-Path ../qodo-governance-lab).Path
python -m unittest discover -s tests -v
```

Python 3.10+, standard library only. The transport is supplied by callers and the
test transport is in memory. Names and data are fictional; no customer code,
credentials, external API calls, or third-party package installation is involved.
This sample is MIT licensed.
