#變量說明：形如：i*j
# i：表示行；1<=i<=9
# i<=j<=9
# k：表示空格數目:k=i-1
for i in range(1,10):
    for k in range(1,i):#表示空格的數量
        print('      ',end=(' '))#6ge konge
    for j in range(i,10):
        print('%d*%d=%d'%(i,j,i*j),end=(' '))
    print('\n')
    #一行輸出完畢，換行輸出
