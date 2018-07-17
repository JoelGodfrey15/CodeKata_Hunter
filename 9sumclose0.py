def main():
    n=int(input())
    q=input()
    a=10000
    l=q.split()
    for i in range(n):
        l[i]=int(l[i])
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            if abs(l[i]+l[j])<a:
                a=l[i]+l[j]
                b,c=l[i],l[j]
    print(b,' ',c)

if __name__ == '__main__':
    main()
