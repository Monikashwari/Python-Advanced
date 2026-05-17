# Pytest - A Practical Guide    

A practical guide to understanding Python testing with pytest.

---

## What is pytest?

pytest is a Python testing framework. You write functions that check if your code behaves correctly. If something breaks, pytest tells you exactly where and why.

---

## Setup

```bash
pip install pytest
pip install pytest-mock  # only needed for mocking
```

---

## Core Rules

- Test files must be named `test_*.py` or `*_test.py`
- Test functions must start with `test_`
- Use `assert` to check results

pytest finds and runs all tests automatically — no manual registration needed.

---

## Concepts

### 1. Basic Tests
Write a function starting with `test_` and use `assert` to verify the output of your function. One `assert` = one check.

---

### 2. Testing Classes
Create an instance of your class inside the test function, then call its methods normally. Use one test function per method for clarity.

---

### 3. Testing Exceptions — `pytest.raises()`
When a function is supposed to raise an error, you can't use a plain `assert` — the error would crash the test. Wrap the call in `with pytest.raises(ErrorType):` to catch and verify it. Use `match=` to also check the error message.

---

### 4. Parametrize — Multiple Inputs
Use `@pytest.mark.parametrize` when you need to test the same function with many different inputs. Each row runs as its own independent test, so a failure in one case doesn't hide the others.

---

### 5. Mocks — Testing Without Real Dependencies

#### Why mocking exists
Your function might call a real API, database, or file. In tests you don't want that — the internet could be slow, the API could be down, or you might hit rate limits. Mocking replaces the real dependency with a fake that instantly returns whatever you tell it to.

The key idea: **you are not testing the API — you are testing your own function.** The mock lets you focus only on whether your function handles the response correctly.

#### What the fake data means
When you write `mock_get.return_value.json.return_value = {"main": {"key": "value"}}`, you are saying: *"When my function calls `requests.get(url).json()`, return this dictionary instead of hitting the real API."*

Your function then wraps it into `{"Data": {"main": {"key": "value"}}}`. The outer `"Data"` key is added by your own function — not the API. So the `assert` is checking whether your function correctly wrapped the fake response. That is **your function's logic** being tested, not the API.

#### The 3-step mock pattern
1. **Patch** — replace the real function with a fake using `mocker.patch()`
2. **Control** — tell the fake what to return using `.return_value`
3. **Assert** — check that your function processed the response correctly

#### Important rule
Always patch where the function is *used*, not where it is *defined*.
- `mocker.patch('main.requests.get')` ✅ patches it inside your file
- `mocker.patch('requests.get')` ❌ your code won't see this patch

---

## Running Tests

| Command | What it does |
|---|---|
| `python -m pytest` | Run all tests |
| `python -m pytest test_main.py` | Run a specific file |
| `python -m pytest test_main.py::test_divide` | Run one specific test |
| `python -m pytest -v` | Verbose — shows each test name |
| `python -m pytest -x` | Stop after first failure |
| `python -m pytest -s` | Show `print()` output |

---

## Quick Reference

| Scenario | Tool |
|---|---|
| Check a return value | `assert result == expected` |
| Check an exception | `with pytest.raises(ErrorType):` |
| Check the error message | `pytest.raises(ErrorType, match="...")` |
| Test many inputs cleanly | `@pytest.mark.parametrize` |
| Fake an external dependency | `mocker.patch('module.function')` |
