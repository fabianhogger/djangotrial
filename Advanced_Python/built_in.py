def main():
    list1=[1,2,3,0,5,6]
    #print(any(list1))
    #print(all(list1))
    ##############
    days=['Mon','Tues','Wed','Thur','Fri','Sat','San']
    daysfr=['Dim','Lun','Mar','Mer','Jeu','Ven','Sam']
    i=iter(days)
    print(next(i))
    print(next(i))
    print(next(i))
    with open('testfile.txt','r') as fp:
        for line in iter(fp.readline,''):
            print(line)
    for i,m in enumerate(days,start=1):
        print(i,m)
    #   combine lists
    for m in zip(days,daysfr):
        print(m)
    for i,m in enumerate(zip(days,daysfr),start=1):
        print(i,m[0]," = ",m[1],"in French")
    
if __name__ == "__main__":
    main()
