"""Module docstring goes here."""
from nose.tools import eq_
import cap


def test_one_word():
    """Module docstring goes here."""
    text = 'duck'
    result = cap.just_do_it(text)
    eq_(result, 'Duck')


def test_multiple_words():
    """Module docstring goes here."""
    text = 'a veritable flock of ducks'
    result = cap.just_do_it(text)
    eq_(result, 'A Veritable Flock Of Ducks')


def test_words_with_apostrophes():
    """Module docstring goes here."""
    text = "I'm fresh out of ideas"
    result = cap.just_do_it(text)
    eq_(result, "I'm Fresh Out Of Ideas")


def test_words_with_quotes():
    """Module docstring goes here."""
    text = "\"You're despicable,\" said Daffy Duck"
    result = cap.just_do_it(text)
    eq_(result, "\"You're Despicable,\" Said Daffy Duck")
