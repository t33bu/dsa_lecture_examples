def reverse(text):
    if len(text) == 0:
        return ""
    else:
        chr = text[-1]
        text = text[:-1]
        #print(chr,'<-', text)
        result_str = chr + str(reverse(text))
        #print(result_str)
        return result_str

my_text = "Mary had a little lamb"
print(my_text)
print(reverse(my_text))
