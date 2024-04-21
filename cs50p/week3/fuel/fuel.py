while True :
    try:
        x,y = input('Fraction: ').split('/')
        x,y = int(x), int(y)

        if x>y:
            raise Exception
        elif y==0:
            raise ZeroDivisionError

    except:
        pass
    else:
        break

percent = (x/y)*100
if percent >= 99 :
    print('F')

elif percent <= 1 :
    print('E')

else:
    print(f'{percent:.0f}' + '%' ,sep='')





