def reading_time_for_text(text):
    if type(text) != str:
        raise Exception("Error: invalid type")
    elif len(text) == 0:
        raise Exception("Error: empty text")
    else:
        list_words = text.split()
        read_rate_per_second = 200.0/60.0
        time_taken = round((len(list_words) / read_rate_per_second), 2)
    
    return f"time taken to read {time_taken} seconds"
    