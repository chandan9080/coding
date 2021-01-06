for _ in range(int(input())):
    nkd = list(map(int, input().strip().split()))
    n = nkd[0]
    k = nkd[1]
    d = nkd[2]
    ai = list(map(int, input().strip().split()))
    a = sum(ai)
    result = int(a / k)
    if result >= d:
        print(d)
    else:
        print(result)
