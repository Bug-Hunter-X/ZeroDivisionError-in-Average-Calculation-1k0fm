def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    return sum(numbers) / len(numbers)

# Example usage
numbers1 = [10, 20, 30]
average1 = calculate_average(numbers1)
print(f"Average of {numbers1}: {average1}")

numbers2 = []
average2 = calculate_average(numbers2)
print(f"Average of {numbers2}: {average2}")
