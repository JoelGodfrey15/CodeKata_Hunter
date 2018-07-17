def main():
    p=input()
    l=p.split()
    n=int(l[0])
    m=int(l[1])
    c=input()
    a=c.split()
    v=input()
    b=v.split()
    for i in range(n):
        a[i]=int(a[i])
    for i in range(m):
        b[i]=int(b[i])
    a=set(a)
    b=set(b)
    if b<=a:
        print('YES')
    else:
        print('NO')
if __name__ == '__main__':
    main()
