import unicodedata
# Both look the same (in most places at least), mean the same, but are different
x1 = 'café'  # Hello 'cafe\u0301'
x2 = 'café'


def test_strings_are_equal_nfc():
    # NFC always takes the shorter form.
    left = unicodedata.normalize('NFC', x1)
    right = unicodedata.normalize('NFC', x2)
    assert len(left) == len(right) == 4
    assert left == right == x2 == 'café'
    assert left != x1
    assert right != x1


def test_strings_are_equal_nfd():
    # NFD always takes the longer form (character + accent combo).
    left = unicodedata.normalize('NFD', x1)
    right = unicodedata.normalize('NFD', x2)
    assert len(left) == len(right) == 5
    assert left == right == x1 == 'café' == 'cafe\u0301'
    # unicode-byte sequence!
    assert left != x2
    assert right != x2
