def calculate_average(numbers):
    try:
        total = 0
        for i in range(len(numbers)):
            total += numbers[i]

        return total / len(numbers)

    except ZeroDivisionError:
        print("Cannot calculate average of an empty list.")
        return None
data1 = [10, 20, 30]
data2 = [5, 15, 25]
data3 = []

print(calculate_average(data1))
print(calculate_average(data2))
print(calculate_average(data3))

def get_list_element(my_list, index):
    try:
        return my_list[index]
    except IndexError:
        print("Error: Index is out of bounds.")
        return None
    except TypeError:
        print("Error: The input must be a list.")
        return None
    print(get_list_element([10, 20, 30], 1))
print(get_list_element([10, 20, 30], 5))
print(get_list_element("Hello", 1))