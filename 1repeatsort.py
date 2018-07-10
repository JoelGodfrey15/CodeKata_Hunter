def main():
    n=int(input())
    l=[]
    c=[]
    for i in range(n):
        l.append(input())
    for i in l:
        j=l.count(i)
        if j>1:
            k=c.count(i)
            if k==0:
                c.append(i)
    c.sort()
    if c==[]:
        print('unique')
    else:
        q=' '.join(c)
        print(q)



if __name__ == '__main__':
    main()
