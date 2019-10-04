import os
import subprocess
import pytest

from addition_package import add_two_numbers


@pytest.mark.parametrize("n1, n2, res", [
    (1, 2, 3),
    (0, -1, -1)
    ])
def test_addition_backend(n1, n2, res):
    assert add_two_numbers(n1, n2) == res


@pytest.mark.parametrize("n1, n2, res", [
    (1, 2, 3),
    (0, -1, -1)
    ])
def test_cli(n1, n2, res):
    o = subprocess.Popen([str(x) for x in ('add-two', n1, n2)], stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
    assert n1 + n2 == int(o[0])
