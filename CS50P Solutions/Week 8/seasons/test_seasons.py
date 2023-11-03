import datetime
import inflect
import re
import sys
import pytest
from seasons import validate_date, process_date, convert




def test_convert_with_custom_input():
    assert convert(100) == 'One hundred minutes'
    assert convert(200) == 'Two hundred minutes'


def test_validate_date():
    with pytest.raises(SystemExit):
        assert validate_date('z')





