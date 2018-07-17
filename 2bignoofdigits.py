def main():
    n=int(input())
    a=input()
    l=a.split()
    l.sort()
    l.reverse()
    a=''.join(l)
    print(a)


if __name__ == '__main__':
    main()
