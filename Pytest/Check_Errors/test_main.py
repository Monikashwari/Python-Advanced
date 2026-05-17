from main import checker
import pytest

def test_divide():
    c = checker()
    assert c.divide(10, 2) == 5
    assert c.divide(-10, 2) == -5
    assert c.divide(6,2) == 3

    
    # We use pytest.raises() instead of assert because assert can only check returned values.
    # Here the function raises an exception, so pytest.raises() lets us verify both the exception type (ValueError) and the exact error message.
    with pytest.raises(ValueError, match="Cannot divide by zero!"):
        c.divide(10, 0)
    