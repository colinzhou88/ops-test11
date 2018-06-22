#！/usr/bin/python
for i in range(1,10):
    for k in range(1,10):
        for m in range(1,10):
            if(i != k) and (i != m) and (k != m):
                print (i,k,m)
                