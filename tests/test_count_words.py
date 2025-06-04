from lib.count_words import count_words

# purpose:
# A function called count_words 
# that takes a string as an argument 
# and returns the number of words in 
# that string.

"""" 
if an empty string is passed 
return zero
"""
def test_with_empty_string():
    result = count_words("")
    assert result == 0
    
""" 
Given a singular word
return 1 
"""
def test_with_one_word_string():
    result = count_words("hello")
    assert result == 1
    
"""
Given a singular word with whitespace
return 1
"""
def test_with_one_word_and_whitespaces_at_start_and_end_string():
    result = count_words(" hello ")
    assert result == 1
    
"""
Given multiple words with white spaces
return the number of words
"""
def test_with_multiple_words_and_whitespaces_in_string():
    result = count_words(" hello world how are you doing")
    assert result == 6
    

