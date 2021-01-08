for _ in range(int(input())):
    n = int(input())
    str1 = input()
    lis = []
    for i in range(n):
        if(i%4==0):
            str2 = str1[i:i+4]
            lis.append(str2)
    str3 = ''
    for j in range(len(lis)):
        lis[j] = chr(int(lis[j],2)+97)
        str3 =str3+ str(lis[j])

    print(str3)