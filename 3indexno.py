def main():
    n=int(input())
    l=[]
    c=[]
    for i in range(n):
        l.append(input())
    for i in range(len(l)):
        if int(l[i])==i:
            c.append(l[i])
    if c==[]:
        print('-1')
    else:
        q=' '.join(c)
        print(q)

if __name__ == '__main__':
    main()
