import string

def clean(str):
    if len(str) == 0:
        return ""
    else:
        first_chr = str[0]
        rest_str = clean(str[1:])
        if first_chr in string.punctuation + string.whitespace:
            return rest_str
        else:
            return first_chr + rest_str
clean('The big elephant')
clean("--A man, a plan, a canal: Panama!")
clean("One")
clean("")
