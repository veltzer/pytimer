# TOFIX

Findings from a code scan on 2026-10-04.

## High

- `src/pytimer/pytimer.py:16` - `__enter__` returns `None`, so `with Timer() as t:` binds `t` to `None` and the caller cannot read the timings. Return `self`, and add a test for the `as` form.
- `src/pytimer/pytimer.py:17` - timing uses `time.time()` (also line 20), which is wall-clock and jumps with NTP/DST adjustments, so measured durations can be wrong or negative. Use `time.perf_counter()`.

## Medium

- `src/pytimer/pytimer.py:21` - the computed duration is a local `diff` that is only printed; with `do_print=False` the caller has to subtract the two timestamps manually. Store it (e.g. `self.elapsed`) and test it.
- `rsconstruct.toml:27` - `[processor.ruff]` and `[processor.mypy]` (line 31) list `config` in `src_dirs`, but `config/` holds only `.lua` files. List only `src` and `tests`.
- `.yamllint.yaml:1` - the repo carries the fleet yamllint config but `rsconstruct.toml` has no `[processor.yamllint]`, so `.github/` YAML is never yamllinted. Add `[processor.yamllint]` with `src_dirs = [".github"]` (or drop the config if YAML linting is not wanted here).
- `README.md:6` - the generated README has no usage example. Add a `tera.snippets/main.md.tera` (included by `tera.templates/README.md.tera`) showing `with Timer(do_title="phase"):`.

## Low

- `src/pytimer/pytimer.py:9` - `Timer` and its constructor have no docstring or type hints; the parameter name `do_title` is odd for a string title (consider `title`, keeping `do_title` as a deprecated alias if anyone depends on it).
- `tests/unit_tests/test_timer.py:8` - nothing tests the printed output (with and without a title); add a test using `contextlib.redirect_stdout`.
- `doc/TODO.txt:1` - empty file; delete it.
- `pyproject.toml:83` - `mypy_path = "src:python:scripts"` names `python` and `scripts`, which do not exist here (same line in many py* repos; fix fleet-wide).
