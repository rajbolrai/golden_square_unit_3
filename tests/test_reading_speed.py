from lib.reading_speed import *
import pytest

"""
Given a string with words
return the time taken to read the text
"""
def test_given_string_with_two_words_return_time_taken_to_read():
    result = reading_time_for_text("HELLO WORLD")
    assert result == "time taken to read 0.6 seconds"
"""
Given a string with 200 words
return the time taken to read the text
"""
def test_given_string_with_200_words_return_time_taken_to_read():
    result = reading_time_for_text(
                " one two three four five six seven eight nine ten "
                " one two three four five six seven eight nine ten "
                " one two three four five six seven eight nine ten "
                " one two three four five six seven eight nine ten "
                " one two three four five six seven eight nine ten "
                " one two three four five six seven eight nine ten "
                " one two three four five six seven eight nine ten "
                " one two three four five six seven eight nine ten "
                " one two three four five six seven eight nine ten "
                " one two three four five six seven eight nine ten "
                " one two three four five six seven eight nine ten "
                " one two three four five six seven eight nine ten "
                " one two three four five six seven eight nine ten "
                " one two three four five six seven eight nine ten "
                " one two three four five six seven eight nine ten "
                " one two three four five six seven eight nine ten "
                " one two three four five six seven eight nine ten "
                " one two three four five six seven eight nine ten "
                " one two three four five six seven eight nine ten "
                " one two three four five six seven eight nine ten "
                )
    assert result == "time taken to read 60.0 seconds"
"""

Given a invalid type value
It throws an error
"""
def test_given_raise_exception_with_invalid_type():
    with pytest.raises(Exception) as e:
        result = reading_time_for_text(123)
    error_message = str(e.value)
    assert error_message == "Error: invalid type"
    

"""
Given a empty text value
It throws an error
"""
def test_given_raise_exception_with_empty_text():
    with pytest.raises(Exception) as e:
        result = reading_time_for_text("")
    error_message = str(e.value)
    assert error_message == "Error: empty text"
    