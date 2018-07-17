def main():
    n=int(input())
    a=input()
    s=0
    k=None
    l=a.split()
    l=l[0:n]
    for i in range(n):
        if s==0:
            j=l.count(l[i])
            if j>1:
                k=l[i]
                print(k)
                s=1
    if k==None:
        print('unique')


if __name__ == '__main__':
    main()
