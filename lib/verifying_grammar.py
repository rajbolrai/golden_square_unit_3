def verifying_grammar_of_text(string):
    if type(string) != str:
        raise Exception("Error: invalid sentence")
    elif len(string) == 0:
        raise Exception("Error: empty sentence")
    return string[0].isupper() and string[-1] == '!'