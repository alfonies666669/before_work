import pytest


@pytest.mark.skip()
@pytest.mark.parametrize("a, b, res", [(2, 3, 5),
                                       (6, 7, 13),
                                       (50, 75, 125)])
def test_assert(a, b, res):
    assert (a + b) == res


@pytest.mark.skip()
@pytest.mark.parametrize("division, devisioned, exception, res", [(10, 0, ZeroDivisionError, 2),
                                                                  (25, "2", TypeError, 3)])
def test_error(division, devisioned, exception, res):
    with pytest.raises(exception):
        assert (division / devisioned) == res
