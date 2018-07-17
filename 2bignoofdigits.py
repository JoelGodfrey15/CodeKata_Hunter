def main():
    n=int(input())
    a=input()
    l=a.split()
    l.sort()
    l.reverse()
    a=''.join(l)
    a=int(a)
    print(a)


if __name__ == '__main__':
    main()
