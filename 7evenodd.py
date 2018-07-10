def main():
    n=int(input())
    l=[]
    for i in range(n):
        l.append(int(input()))
    for i in range(len(l)):
        if(l[i]%2==0 and i%2==1) or (l[i]%2==1 and i%2==0):
            print(l[i],end=' ')

if __name__ == '__main__':
    main()
