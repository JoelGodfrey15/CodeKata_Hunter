def main():
    n=int(input())
    a=input()
    l=a.split()
    k=[]
    for i in range(n):
        l[i]=int(l[i])
    for i in range(len(l)):
        if(l[i]%2==0 and i%2==1) or (l[i]%2==1 and i%2==0):
            k.append(str(l[i]))
    b=' '.join(k)
    print(b)

if __name__ == '__main__':
    main()
