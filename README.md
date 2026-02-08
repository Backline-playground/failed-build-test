# Failed Build Test

Test repository for testing the "skip build when main also fails" feature.

## What this repo has

1. **Vulnerable dependencies** - Trivy will detect CVEs in:
   - `requests==2.19.1` (CVE-2018-18074)
   - `urllib3==1.24.1` (multiple CVEs)
   - `pyyaml==5.3.1` (CVE-2020-14343)
   - `flask==0.12.2` (CVE-2018-1000656)

2. **Failing build** - `broken_module.py` has a syntax error that causes:
   - `python setup.py build` to fail
   - `pip install .` to fail
   - Any Python import of the module to fail

## Testing the feature

1. Scan with Trivy to get vulnerability report
2. Create a remediation for one of the CVEs (e.g., upgrade requests)
3. The build will fail on both main and fix branch
4. Expected: PR should be created with "Build skipped" status

## Verifying the build fails

```bash
# This should fail with syntax error
python -c "import broken_module"

# This should also fail
pip install .
```
