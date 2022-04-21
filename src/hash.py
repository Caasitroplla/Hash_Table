def number_hash(number: int) -> int:
    # Turning the number into an array of digits
    number_arr = [i for i in str(number)]
    # Sorting the array to find the samllest number possible
    number_arr.sort()
    smallest_value = "".join(number_arr)
    # Sorting the array to find the largest number possible
    number_arr.sort(reverse=True)
    largest_value = "".join(number_arr)

    # Turning both into integers then subtracting them
    return int(largest_value) - int(smallest_value)

def char_to_int(char: str) -> int:
    # Turning the character into an integer
    return ord(char)

def hash_string(string: str) -> int:
    # Turning the string into an array of characters
    string_arr = [i for i in string]
    # Turning each character in the array into a numerical value
    string_arr = [char_to_int(i) for i in string_arr]
    # Hashing each character in the array
    string_arr = [number_hash(i) for i in string_arr]
    # Summing the array
    return sum(string_arr)
