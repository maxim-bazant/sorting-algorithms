# sorting algorithms - HW


def create_list():
    list_of_numbers = list()
    numbers = input("type numbers separated by comma and space (example: 1, 5, 6): ")

    for number in numbers.split(", "):
        list_of_numbers.append(float(number))

    return list_of_numbers


def bubble_sort(numbers_: list):
    already_sorted = 0
    for row in range(len(numbers_)):
        for index in range(len(numbers_) - (already_sorted + 1)):
            if numbers_[index] > numbers_[index + 1]:
                numbers_[index], numbers_[index + 1] = numbers_[index + 1], numbers_[index]

        already_sorted += 1

    print(numbers_)


def selection_sort(numbers_: list):
    already_sorted = 0
    for row in range(len(numbers_)):
        min_number_index = already_sorted
        for index in range(already_sorted, len(numbers_)):
            if numbers_[index] < numbers_[min_number_index]:
                min_number_index = index

        numbers_[min_number_index], numbers_[already_sorted] = numbers_[already_sorted], numbers_[min_number_index]

        already_sorted += 1

    print(numbers_)


def insertion_sort(numbers_: list):
    already_sorted = 0

    for row in range(len(numbers_)):
        index = already_sorted
        while numbers_[index - 1] > numbers_[index] and index > 0:
            numbers_[index], numbers_[index - 1] = numbers_[index - 1], numbers_[index]
            index -= 1

        already_sorted += 1

    print(numbers_)


problem_occurred = True

choice = input("What sort do you want to use, type s for selection sort, b for bubble sort, i for insertions sort: ")

while problem_occurred:
    try:
        if choice == "b":
            print("Ok, bubble sort")
            bubble_sort(create_list())
        elif choice == "s":
            print("Ok, selection sort")
            selection_sort(create_list())
        elif choice == "i":
            print("Ok, insertion sort")
            insertion_sort(create_list())
        elif choice == "m":
            print("Ok, merge sort")
            merge_sort(create_list())
        else:
            print("Oops something went wrong")
    except Exception:
        print("Oops something went wrong, try again")
    else:
        problem_occurred = False
