import pytest

import src.osm_configurator.view.utility_methods as utility_methods_i


@pytest.mark.parametrize("string,line_length,rows,dots,rows_unlimited,word_break",
                         [("Test", 0, 0, False, False, False),
                          ("Test", -1, -1, False, False, False),
                          ("Test", 0, 1, False, False, False),
                          ("Test", 1, 0, False, False, False),
                          ("Test", -1, 1, False, False, False),
                          ("Test", 1, -1, False, False, False)])
def test_valid_input(string, line_length, rows, dots, rows_unlimited, word_break):
    with pytest.raises(ValueError):
        new_string = utility_methods_i.reformat_string(string=string, line_length=line_length, rows=rows, dots=dots,
                                                       rows_unlimited=rows_unlimited, word_break=word_break)


def test_empty_string():
    string = ""
    assert "" == utility_methods_i.reformat_string(string=string, line_length=1, rows=1, dots=False,
                                                   rows_unlimited=False, word_break=False)

@pytest.mark.parametrize("string,line_length,rows,dots,rows_unlimited,word_break,result",
                         [("Testing", 4, 1, True, False, False, "T..."),
                          ("Test", 4, 1, True, False, False, "Test"),
                          ("Test Something", 10, 1, True, False, False, "Test So..."),
                          ("Test", 10, 1, True, False, False, "Test")])
def test_dots(string, line_length, rows, dots, rows_unlimited, word_break, result):
    new_string = utility_methods_i.reformat_string(string=string, line_length=line_length, rows=rows, dots=dots,
                                                   rows_unlimited=rows_unlimited, word_break=word_break)
    assert new_string == result

@pytest.mark.parametrize("string,line_length,rows,dots,rows_unlimited,word_break,result",
                         [("Testing", 4, 1, False, True, False, "Test\ning"),
                          ("Testing Something", 4, 1, False, True, False, "Test\ning \nSome\nthin\ng")])
def test_rows_unlimited(string, line_length, rows, dots, rows_unlimited, word_break, result):
    new_string = utility_methods_i.reformat_string(string=string, line_length=line_length, rows=rows, dots=dots,
                                                   rows_unlimited=rows_unlimited, word_break=word_break)
    assert new_string == result

@pytest.mark.parametrize("string,line_length,rows,dots,rows_unlimited,word_break,result",
                         [("Testing", 4, 2, False, False, True, "Tes-\nting"),
                          ("Testing Something", 4, 5, False, True, True, "Tes-\nting\nSom-\neth-\ning")])
def test_word_break(string, line_length, rows, dots, rows_unlimited, word_break, result):
    new_string = utility_methods_i.reformat_string(string=string, line_length=line_length, rows=rows, dots=dots,
                                                   rows_unlimited=rows_unlimited, word_break=word_break)
    assert new_string == result
