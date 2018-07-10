def main():
    n=int(input())
    l=[]
    for i in range(n):
        l.append(input())
    l.sort()
    l.reverse()
    a=''.join(l)
    print(a)


if __name__ == '__main__':
    main()
