# {{PROBLEM}} Function Design Recipe


## 1. Describe the Problem

As a user
So that I can manage my time 
I want to see an estiamte of rading time for a text
assuming that I can read 200 words a minute

## 2. Design the Function Signature

```python

def reading_time_for_text(text):
    """Find how long it takes to read text

    Parameters: 
        text : a string containing words (e.g. "hello WORLD")

    Returns: 
        A number that represents the time taken to read the text. The reader reads 200 words per minute
    """
    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests

```python
# EXAMPLE

"""
Given a empty string
return 0 seconds
"""
reading_time_for_text("") => 0.0 secs

"""
Given a string with words
return the time taken to read the text
"""
reading_time_for_text("HELLO WORLD") => 0.6 secs

"""
Given a None value
It throws an error
"""
reading_time_for_text(None) throws an error
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

