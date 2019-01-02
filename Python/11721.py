n = input()
def PrintStr():
    k = 0
    for i in range(len(n)):
        a = ""
        for j in range(0, 10):
            a = a + n[k]
            k = k + 1
            if k == len(n):
                print(a)
                return
        print(a)

PrintStr()