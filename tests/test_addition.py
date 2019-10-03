import pytest
import os

from cpp_python_hybrid import add_two_numbers


@pytest.mark.parametrize("n1, n2, res", [
    (1, 2, 3),
    (0, -1, -1)
    ])
def test_addition_backend(n1, n2, res):
    assert n1 + n2 == res

# def test_cli():
#     o = subprocess.Popen([os.path.join(where_am_i, '../../', ADDITION_LIB), a, b], stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
#     return int(o[0].decode('utf-8'))
#     os.e