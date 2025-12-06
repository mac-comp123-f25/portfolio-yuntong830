def print_abbrev(filename):
    file_in = open(filename, 'r')
    for line in file_in:
        line = line.strip()
        short = line[:20]
        print(short)

    file_in.close()
print_abbrev(“../TextFiles/alice.txt”)