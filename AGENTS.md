# Agent Guidelines

These instructions describe how to work effectively in this repository. They consolidate widely recommended practices from the Python community (e.g. PEP 8, Real Python, PyPA) and commonly endorsed workflows from maintainers' forums.

## Repository-wide workflow
- Keep `work` as a release-ready branch. Do all changes on a feature branch and keep commits focused.
- Write meaningful commit messages in the imperative mood ("Add tests"), wrapping the subject at 50 characters where possible and following up with context in the body when needed.
- Every change should include or update automated tests. Run `pytest` from the repository root before pushing.
- Prefer incremental, review-friendly pull requests. Provide a summary of behaviour changes and test evidence in the PR description.

## Python style and quality
- Format Python code with `black` (line length 88) and sort imports with `isort` using the `black` profile. These tools reflect the recommendations from the PSF and the wider Python ecosystem for maintaining consistent diffs.
- Adhere to PEP 8 and type-hint new or updated functions (PEP 484). Retain or add docstrings that explain behaviour, inputs, and return values.
- Guard against timezone pitfalls: use timezone-aware `datetime` objects in UTC when interacting with tariffs or schedules, matching the existing modules.
- Avoid introducing side effects at import time. Place I/O and network calls behind functions so they can be stubbed during tests.

## Testing guidance
- Use `pytest` (which will happily execute the existing `unittest`-style tests) for all test execution.
- When updating logic around tariffs or schedules, add representative fixtures under `tests/` or extend the JSON snapshots so behaviour changes are captured.
- Write tests that cover boundary conditions (e.g. daylight savings transitions, empty rate lists) to reflect the advice from testing best-practice guides.

## Documentation and maintenance
- Update `README.md` or other user-facing docs whenever behaviour, configuration options, or workflows change.
- Keep dependencies minimal and document any new installation requirements.
- Never commit secrets or credentials (Tesla tokens, API keys, etc.); follow the security guidance shared across Home Assistant and PyPA communities.

