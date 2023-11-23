# all test files have to start/end with "_/test_"
#pytest method names required, should start with test
#code wrapped in method(def) only
#method names should make sense
#cmd prompts: -k method name exec, -s logs in output, -v more info
#can run specific file with py.test (filename.py)
#marking/tagging tests with a @pytest.mark.smoke command, run it with -m "name of the tag(smoke)"
#skipping: @pytest.mark.skip
#if operation is necessary: @pytest.mark.xfail (will not display failed message)
#fixtures: setup/tear down methods for test cases
#conftest file: to generalize a fixture and make it available for all test cases
#datadriven/parameterization can be done with return statements in tuple format
#fixture scope to class only = run once before class is initiated + at the end
#for reporting: python -m pytest --html=report.html
#logging levels: debug, info, warning, error, critical

import pytest


@pytest.fixture()
def setup():
    print("First execution")
    yield
    print("Last execution")


def test_fixture_demo(setup):
    print("Executing steps in fixture_demo method")

@pytest.mark.smoke
def test_first_program():
    print("Hello")


@pytest.mark.xfail
def test_second_greeting_card():
    print("Wazzup")


def test_cross_browser(cross_browser):
    print(cross_browser[0])