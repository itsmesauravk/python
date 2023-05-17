phrase="Ram is a boy he studies in Herald College kathmandu, he is very popular among student in college."
phrase=phrase.lower()
result= {}
word_list=phrase.split()
for word in word_list:
    if word not in result:
        result[word]=1
    else:
        result[word] += 1
print(result)
