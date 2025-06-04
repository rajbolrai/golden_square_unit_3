def make_snippet_from_string(string):
    string_words = string.split(" ")
    
    if len(string_words) <= 5:
        return string
    
    result = string_words[:5]
    snippet = " ".join(result)
    
    return snippet + "..."