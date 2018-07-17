def main():
    n=int(input())
    a=input()
    l=a.split()
    for i in range(n):
        l[i]=int(l[i])
    for i in range(len(l)):
        if(l[i]%2==0 and i%2==1) or (l[i]%2==1 and i%2==0):
            print(l[i],end=' ')

if __name__ == '__main__':
    main()
