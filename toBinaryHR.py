
def bin(n):
    count = 0
    while n:
        n &= n << 1
        count += 1

    print(count)

if __name__ == '__main__':
    n = int(input())
    bin(n)


