pi = 3.14
while 1:
    radius = int(input('please input radius value:'))
    area = pi*radius*radius
    zhouchang = 2*pi*radius
    #方法1
    print('area=',area)
    print('area='+str(area))
    # 方法2
    print('zhouchang=', zhouchang)
    #print('zhouchang='+str(zhouchang))
    # 方法3
    print('area=%d,zhouchang=%d'%(area,zhouchang))

#s.isdigit()
