def select_words(s, fn):
    file_in = open(fn, 'r')
    allFile = file_in.readlines()
    file_in.close()
    acc = []
    for line in allFile:
        line = line.strip()
        if s in line:
            acc.append(line)
    return acc
print(select_words("ii", "../TextFiles/shortcross.txt"))
print(select_words("quo", "../TextFiles/shortcross.txt"))