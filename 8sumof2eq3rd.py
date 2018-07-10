def main():
    n=int(input())
    l=[]
    for i in range(n):
        l.append(int(input()))
    l.sort()
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            for k in range(i+2,len(l)):
                if (l[i]+l[j])==l[k]:
                    print(l[i],' ',l[j],' ',l[k])



if __name__ == '__main__':
    main()
