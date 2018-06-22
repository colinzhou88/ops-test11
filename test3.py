#！/usr/bin/python
i = int(input('总利润：'))
if i <= 10:
    print(0.1*i)

elif 10 < i <=20:
    print(1+0.075*(i-10))

elif 20 < i <=40:
    print(1+0.75+0.05*(i-20))