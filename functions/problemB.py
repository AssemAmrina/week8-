def pow(a,b):
    res = 1
    for i in range(b):
        res *=a
    return res
print(pow(2,4))