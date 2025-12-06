def i_words(filename):
    with open(filename, 'r') as file_in:
        text = file_in.read()

    words = text.split()

    i_list = []
    for w in words:
        if 'i' in w:
            i_list.append(w)

    return i_list
