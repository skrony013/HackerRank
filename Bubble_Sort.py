def countSwaps(n):
    listA = list(map(int, input().strip().split(' ')))[:n]
    cnt = 0
    for i in range(len(listA)):
        for j in range(len(listA) - i - 1):
            if listA[j] > listA[j + 1]:
                cnt = cnt + 1
                temp = listA[j]
                listA[j] = listA[j + 1]
                listA[j + 1] = temp

    print("Array is sorted in", cnt, "swaps.")
    print("First Element:", listA[0])
    print("Last Element:", listA[-1])


A = int(input())
countSwaps(A)
