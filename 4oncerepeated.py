def main():
    n=int(input())
    a=input()
    l=a.split()
    for i in l:
        if l.count(i)==1:
            print(i)

if __name__ == '__main__':
    main()
