def main():
    n=int(input())
    a=input()
    c=[]
    l=a.split()
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
