file_in = open("../TextFiles/alice.txt", 'r')
print(file_in)
# Result should look something like:
# <_io.TextIOWrapper name='alice.txt', mode='r' encoding='US-ASCII'>
file_in = open("../TextFiles/alice.txt", 'r')

count = 0
for text_line in file_in:
    text_line = text_line.strip()   # removes the newline character at the end
    print("Line", count, ":", text_line)
    count = count + 1

file_in.close()