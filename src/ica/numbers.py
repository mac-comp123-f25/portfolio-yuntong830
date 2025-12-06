def write_to_n(n, filename):
    file_out = open(filename, 'w')
    for i in range(1, n + 1):
        file_out.write(str(i) + '\n')
    file_out.close()
print(write_to_n(1, '../TextFiles/newname.txt'))