from lib.verifying_grammar import verifying_grammar_of_text
import pytest

def test_given_empty_sentence_output_error():
    with pytest.raises(Exception) as e:
        verifying_grammar_of_text("")
    error_message = str(e.value)
    assert error_message == "Error: empty sentence"
    
def test_given_invalid_sentence_type_output_error():
    with pytest.raises(Exception) as e:
        verifying_grammar_of_text(123123)
    error_message = str(e.value)
    assert error_message == "Error: invalid sentence"

def test_given_sentence_with_correct_grammar_output_true():
    is_grammar_correct = verifying_grammar_of_text("Hey, over here!")
    assert is_grammar_correct == True
    
def test_given_sentence_with_no_punctuation_mark_output_false():
    is_grammar_correct = verifying_grammar_of_text("Hey, over here")
    assert is_grammar_correct == False
    
def test_given_sentence_with_no_starting_capital_letter_output_false():
    is_grammar_correct = verifying_grammar_of_text("hey, over here!")
    assert is_grammar_correct == False
    
def test_givent_sentence_with_incorrect_grammar():
    is_grammar_correct = verifying_grammar_of_text("hey, over here")
    assert is_grammar_correct == False