def main():
    n=input()
    l=list(n)
    q=l.count('0')
    s=1
    for i in range(len(l)-1):
        if int(l[i]+l[i+1])<=26 and int(l[i]+l[i+1])>=1:
            s=s+1
            for j in range(i+2,len(l)-1):
                if int(l[j]+l[j+1])<=26 and int(l[j]+l[j+1])>=1:
                    s=s+1
                    for k in range(j+2,len(l)-1):
                        if int(l[k]+l[k+1])<=26 and int(l[k]+l[k+1])>=1:
                            s=s+1
    print(s)

if __name__ == '__main__':
    main()
