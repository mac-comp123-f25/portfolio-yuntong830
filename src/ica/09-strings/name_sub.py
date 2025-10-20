def count_words(word,text):
    words=text.split()
    count=0
    for n in words:
        if n ==word:
            count+=1
    return count
print(count_words("tre","tre is a tree"))