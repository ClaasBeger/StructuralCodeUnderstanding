def binary_search(l, value):
    low = 0
    high = len(l)-1
    while low <= high:
        mid = (low+high)//2
        if l[mid] > value: high = mid-1
        elif l[mid] < value: low = mid+1
        else: return mid
    return -1

if __name__ == "__main__":
    print(binary_search([7, 14, 21, 28, 35], 28))