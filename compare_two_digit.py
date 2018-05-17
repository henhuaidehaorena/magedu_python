while 1:
    a=int(input('first digit:'))
    b=int(input('second digit:'))
    if(a>b):
        print(b,a)
        print('a is bigger than b')
    else:
        print(a,b)
        print('b is bigger than a')
    #比較兩個數的大小,輸出時小的在前，大的在后