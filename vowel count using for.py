def vwl():
    txt=input("enter the text :")
    count=0
    for i in txt:
        if i == 'a' or i=='e' or i=='i' or i=='o' or i=='u':
            count += 1
    print('The total vowel is :',count)
