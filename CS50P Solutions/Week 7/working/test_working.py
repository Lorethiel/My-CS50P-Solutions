import working
import pytest

def test_valid_input():

    result = working.convert('9:30 AM to 5:45 PM')
    assert result == '09:30 to 17:45'

def test_invalid_input():

    with pytest.raises(ValueError):
        working.convert('9 AM - 5 PM')

    with pytest.raises(ValueError):
        working.convert('10:7 AM - 5:1 PM')

def test_invalid_time_format():

    with pytest.raises(ValueError):
        working.convert('9:60 AM to 5:45 PM')

    with pytest.raises(ValueError):
        working.convert('9:30 AM to 5:70 PM')

def test_invalid_hour_range():

    with pytest.raises(ValueError):
        working.convert('13:30 AM to 5:45 PM')

    with pytest.raises(ValueError):
        working.convert('0:30 AM to 5:45 PM')

if __name__ == '__main__':
    pytest.main()
