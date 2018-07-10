def main():
    n=int(input())
    m=int(input())
    a=[]
    b=[]
    for i in range(n):
        a.append(int(input()))
    for i in range(m):
        b.append(int(input()))
    a=set(a)
    b=set(b)
    if b<=a:
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':
    main()
