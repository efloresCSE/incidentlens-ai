# Import the function we want to test.
# "incidentlens" is our Python package.
# "preprocessing" is the module (preprocessing.py).
# "normalize_message" is the function inside that module.
from incidentlens.preprocessing import (
    classify_severity,
    normalize_message,
)


# TEST CASE 1: Normal input/Happy Path
# pytest discovers functions whose names start with "test_".
# This is a unit test because we test one small function.
def test_normalize_message():

    # ARRANGE: Prepare the test input.
    message = "  DATABASE   TIMEOUT  "

    # ACT: Execute the function being tested.
    result = normalize_message(message)

    # ASSERT: Compare actual output with expected output.
    # If the condition is False, the test fails.
    assert result == "database timeout"


# TEST CASE 2: Empty input (edge case)
# Also acts as a regression test in future changes.
def test_empty_message():

    # ARRANGE: Prepare an empty string.
    message = ""

    # ACT: Call our function with the empty input.
    result = normalize_message(message)

    # ASSERT: Verify the expected behavior.
    assert result == ""


def test_classify_error():
    result = classify_severity("ERROR: Database connection failed")
    assert result == "error"


def test_classify_other():
    result = classify_severity("Database connection established")
    assert result == "other"
