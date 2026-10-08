def filter_and_sort_evens(numbers):
    even_numbers = [number for number in numbers if number % 2 == 0]
    return sorted(even_numbers)
def count_character_frequency(text):
    frequency = {}
    for character in text.lower():
        frequency[character] = frequency.get(character, 0) + 1
    return frequency
print(filter_and_sort_evens([5, 2, 8, 1, 4]))
print(count_character_frequency("Hello"))