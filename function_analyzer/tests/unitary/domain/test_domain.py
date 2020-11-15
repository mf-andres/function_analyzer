import pytest

from function_analyzer.domain.domain import get_domain_len


@pytest.mark.parametrize(
    "from_domain, to_domain, domain_step, expected_domain_len",
    [
        (0, 100, 1, 100),
        (0, 100, 2, 50),
        (0, 100, 3, 33),
    ],
)
def test_returns_proper_domain_len(
    from_domain, to_domain, domain_step, expected_domain_len
):
    domain_len = get_domain_len(from_domain, to_domain, domain_step)
    assert domain_len == expected_domain_len
