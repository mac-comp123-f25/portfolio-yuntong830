def up_to_period(filename):
    with open(filename, 'r') as file_in:
        text = file_in.read()

    result = ""
    for ch in text:
        result += ch
        if ch == '.':
            break
    return result