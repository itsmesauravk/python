def text():
    try:
        file = open("original_text.txt")
        line =[]
        count = 0
        for i in file:
            line.append(i.strip("\n"))
        for j in line:
            for k in j:
                if k == "e":
                    count +=1
        file.close()
        print("e repeated times is",count)
    except FileNotFoundError:
        print("file not found")



    
