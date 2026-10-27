# Static Code Analysis — Issues and Fixes

| Issue | Type | Line(s) | Description | Fix Approach |
|---|---|---|---|---|
| 1 | Security | 5 | Hardcoded officer password in source code. | Use an environment variable or secure configuration to store credentials. |
| 2 | Code Quality | 1 | Unused `os` import. | Removed the unused import. |
| 3 | Style | 7 | Line exceeds the recommended maximum length. | Split the long line into multiple lines. |
| 4 | Style | 38 | Insufficient blank lines between functions. | Added the required blank lines. |
| 5 | Style | 64 | Function name `lowStock` does not follow snake_case naming. | Renamed it to `low_stock`. |
| 6 | Code Quality | 69–71 | Excessive blank lines and resource handling concerns. | Removed extra blank lines and used a context manager where appropriate. |
| 7 | Style | 95–96 | Incorrect spacing around an inline comment and operator. | Corrected whitespace according to Python style conventions. |
| 8 | Code Quality | 20, 83 | Missing function docstrings. | Added docstrings describing function behaviour. |
| 9 | Correctness | 84–87 | Calls used `registerDonor`, which was undefined. | Used the existing `register_donor` function name consistently. |

## Summary

Static analysis was performed using Pylint, Flake8 and Bandit. The identified issues were reviewed and fixes were applied while preserving the blood donation management system's functionality. The tools were rerun to verify the changes.