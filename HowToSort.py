

list_1 = [4,7,1,2,8,2,5]
list_2 = [5,1,4,14,56,13,17,42,51]

def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0,n-i-1):
            if lst[j] > lst[j+1]:
                lst[j] = lst[j] + lst[j+1]
                lst[j+1] = lst[j] - lst[j+1]
                lst[j] = lst[j] - lst[j+1]
    print(lst)


bubble_sort(list_2)