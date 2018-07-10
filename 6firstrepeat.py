def main():
    n=int(input())
    l=[]
    s=0
    k=None
    for i in range(n):
        l.append(input())
    for i in l:
        if s==0:
            j=l.count(i)
            if j>1:
                k=i
                print(k)
                s=1
    if k==None:
        print('unique')


if __name__ == '__main__':
    main()
