def main():
    n=int(input())
    l=[]
    a=10000
    for i in range(n):
        l.append(int(input()))
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            if (l[i]+l[j])<a:
                a=l[i]+l[j]
                b,c=l[i],l[j]
    print(b,' ',c)

if __name__ == '__main__':
    main()
