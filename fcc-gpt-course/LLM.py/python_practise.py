def first_repeating_char(input_str):
    seen_chars = set()
    for i, char in enumerate(input_str):
        if char in seen_chars:
            return i
        seen_chars.add(char)
    return -1