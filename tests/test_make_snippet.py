from lib.make_snippet import make_snippet_from_string


""""
if the input string has less then or equal to 5 letters
return the original string back
"""
def test_with_string_less_than_five_words():
    result = make_snippet_from_string("hey there stranger")
    assert result == "hey there stranger"
    

""""
if the input string has greater than characters 
return the first 5 characters then '...'
"""
def test_with_string_greater_than_five_characters():
    result = make_snippet_from_string("hello world how are all you doing tonight")
    assert result == "hello world how are all..."