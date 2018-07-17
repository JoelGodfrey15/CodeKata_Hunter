def main():
    n=int(input())
    a=input()
    l=a.split()
    for i in range(n):
    	l[i]=int(l[i])
    l.sort()
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            for k in range(i+2,len(l)):
                if (l[i]+l[j])==l[k]:
                    print(l[i],' ',l[j],' ',l[k])



if __name__ == '__main__':
    main()
