def print_word_frequencies(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()
    clean_text = ""
    for ch in text:
        if ch.isalpha() or ch == " ":
            clean_text += ch.lower()
        else:
            clean_text += " "

    words = clean_text.split()
    freq_dict = {}
    for w in words:
        freq_dict[w] = freq_dict.get(w, 0) + 1

    freq_list = [(freq, word) for word, freq in freq_dict.items()]
    freq_list.sort(reverse=True)
    print("WORD".ljust(20), "FREQUENCY")
    print("-" * 30)
    for freq, word in freq_list:
        print(word.ljust(20), freq)