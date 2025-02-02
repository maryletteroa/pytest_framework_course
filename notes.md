
# Notes
## Getting started

Set up python and virtual environment

Install pytest  
`pip install pytest`


Call pytest  
- `pytest`  
- `pytest -v` - verbose
- `pytest -h` - see documentation
- `pytest -s` - see STDOUT including `print()` results

Configuration file  
`pytest.ini`

Organize tests (can use functions, classes, directories)


## Test search
Group things together in a way that makes sense logically for you, other developers, and future developers. Don't build a test suite that just works for only you.

Run only some tests


### markers
- a way to mark tests to delineate only those that needed to be run
- makes for self-maintaining test suites
- import:
    `from pytest import mark`
- decorate test function
    `@marker.engine`

☝ Over mark rather than under mark.

Command  
`pytest -m engine`
    - only run tests that have been marked `engine`

Document the markers especially if they are meant to be used, including by other developers, in `pytest.ini`. This also remove warnings, 
```yaml
markers =
    engine: Runs test for engine
```

Can stack markers on top of each other which makes it easy to add and remove tests from suites.
```python
@marker.smoke
@marker.engine
def test_engine():
    assert True
```
Smoke test - for critical functions e.g. body and engine for, and not entertainment for car

Combine tests  
`pytest -m "body or engine"`

Exclude tests  
`pytest -m "not entertainment"`


Can also mark (and stack markers) on Class level. The marker will cascade down to methods  

```python
@mark.smoke
@mark.body
class BodyTests:
    ...
```

See all markers, includes documented markers in `pytest.ini`  
`pytest --markers`


## Test fixtures

`conftest.py`
- any fixture that's created in this file becomes accessible in the directory that the file resides in, and any directory below it
- no need to import said fixtures (saves code)

`@fixture(scope="function")`
- default scope is the function decorated (lowest-level that can be scoped in pytest)
- `scope="session"` - one fixture to use for the duration of the test session no matter how many times the fixture is being called
- e.g.
```python
from pytest import fixture
from selenium import webdriver

@fixture(scope="function")
def chrome_browser():
    browser = webdriver.Chrome()
    return browser
```
- usage e.g.
```python
@def test_something(chrome_browser):
    chrome_browser.get("www.example.com")
    assert True
```
- fixture can also  handle its own teardown; use `yield`

```python
@fixture(scope="function")
def chrome_browser():
    browser = webdriver.Chrome()
    yield browser

    # check teardown
    print("I am tearing down this browser")
```

## Test Report and History

Generate html report  

`pip install pytest-html`  

e.g. Usage:  
`pytest --html="results.html"`  

Built in in Pytest, generates xml. Can be integrated into CI/CD such as Jenkins  
`pytest --junitxml="results.xml"`





# Reference
- [Pytest Documentation](https://docs.pytest.org)
- [Elegant Automaton Frameworks with Python and Pytest](https://www.udemy.com/course/elegant-automation-frameworks-with-python-and-pytest)