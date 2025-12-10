import string
def compute_frequencies(filename):
    file_in = open(filename, 'r')
    allFile = file_in.read()
    file_in.close()
    words = allFile.split()
    clean_words = []
    for word in words:
        newWord = word.strip(string.punctuation)
        clean_words.append(newWord)
    freq = {}
    for word in clean_words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1