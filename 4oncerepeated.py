def main():
    n=int(input())
    l=[]
    for i in range(n):
        l.append(input())
    for i in l:
        if l.count(i)==1:
            print(i)

if __name__ == '__main__':
    main()
