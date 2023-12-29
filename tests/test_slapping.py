import pytest
from slapping.slap_that_like_button import LikeState, slap_many


def test_slap_many_empty():
    assert slap_many(LikeState.empty, "") is LikeState.empty


def test_slap_many_invalid_slap_raises_valueerror():
    with pytest.raises(ValueError):
        slap_many(LikeState.empty, "x")


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("l", LikeState.liked),
        ("d", LikeState.disliked),
        ("ll", LikeState.empty),
        ("dd", LikeState.empty),
        ("ld", LikeState.disliked),
        ("dl", LikeState.liked),
        ("ldd", LikeState.empty),
        ("lldd", LikeState.empty),
        ("ddl", LikeState.liked),
    ],
)
def test_slap_many_valid_returns_expected(test_input, expected):
    assert slap_many(LikeState.empty, test_input) is expected


@pytest.mark.skip(reason="regexes not supported yet")
def test_regex_slaps():
    assert slap_many(LikeState.empty, "[ld]*ddl") is LikeState.liked


@pytest.mark.xfail #used to demo xfail
def test_divide_by_zero():
    assert 1 / 0 == 1


@pytest.mark.xfail #no DB support yet
def test_db_slap(db_conn):
    db_conn.read_slaps()
    assert ...
