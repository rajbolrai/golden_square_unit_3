# {{PROBLEM}} Function Design Recipe


## 1. Describe the Problem

As a user
So that I can improve my grammar
I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark.

## 2. Design the Function Signature

```python

def verifying_grammar_of_text(text):
    """
    Parameters: 
        text : a string containing a sentence
    Returns: 
        A bool which returns true if the start of the sentence of is a capital letter and ends with a punctuation mark
    """
    pass # 
```

## 3. Create Examples as Tests

```python
# EXAMPLE

"""
Given a empty string
return error message
"""
reading_time_for_text("") => "Error: input is empty"

"""
Given a empty string
return error message
"""
reading_time_for_text(1212) => "Error: input is invalid"

"""
Given sentence with correct grammar
return True
"""
reading_time_for_text("Hello, how are you!") => True

"""
Given a sentence with incorrect grammar, missing end
return False
"""
reading_time_for_text("Hello, how are you") => False


```

## 4. Implement the Behaviour

```python
# EXAMPLE

from lib.reading_speed import *

"""
Given a empty string
return 0 seconds
"""
def test_given_empty_text_return_zero():
    result = extract_uppercase("")
    assert result == 0




```


