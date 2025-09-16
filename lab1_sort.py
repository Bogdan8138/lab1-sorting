def selection_sort(arr):
    n = len(arr)
    comparisons = 0
    assignments = 0

    for i in range(n - 1):
        min_index = i
        assignments += 1
        for j in range(i + 1, n):
            comparisons += 1 
            if arr[j] < arr[min_index]:
                min_index = j
                assignments += 1 
        comparisons += 1  
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            assignments += 3  
    return arr, comparisons, assignments

def insertion_sort(arr):
    n = len(arr)
    comparisons = 0
    assignments = 0
    for i in range(1, n):
        key = arr[i]
        assignments += 1
        j = i - 1
        assignments += 1
        while j >= 0 and arr[j] > key:
            comparisons += 1  
            arr[j + 1] = arr[j]
            assignments += 1
            j -= 1
            assignments += 1
        if j >= 0:
            comparisons += 1
        arr[j + 1] = key
        assignments += 1

    return arr, comparisons, assignments

if __name__ == "__main__":
    my_list = [54, 65, 7, 33, 86, 29, 11, 91, 12]

    print("=== Selection Sort ===")
    sorted_sel, comps_sel, assigs_sel = selection_sort(my_list.copy())  
    print("Оригінальний список:", my_list)
    print("Відсортований список:", sorted_sel)
    print(f"Кількість порівнянь: {comps_sel}")
    print(f"Кількість присвоєнь: {assigs_sel}\n")

    print("=== Insertion Sort ===")
    sorted_ins, comps_ins, assigs_ins = insertion_sort(my_list.copy())
    print("Оригінальний список:", my_list)
    print("Відсортований список:", sorted_ins)
    print(f"Кількість порівнянь: {comps_ins}")
    print(f"Кількість присвоєнь: {assigs_ins}")
