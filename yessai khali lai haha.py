def loop():
    r=range(100,200)
    sum=0
    for x in r:
        if x%2==0:
            sum+=x
    print(sum)
