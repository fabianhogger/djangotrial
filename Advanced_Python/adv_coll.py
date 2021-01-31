import collections


def main():
    Point=collections.namedtuple('Point','x y')
    p1=Point(20,30)
    p2=Point(40,30)
    print(p1,p2)
    print('p1 values, ',p1.x,p1.y)
    p1=p1._replace(x=100)
    print('p1 after changing x val,',p1.x)
if __name__=='__main__':
    main()
