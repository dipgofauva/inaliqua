def my_generator():
    # This line yields a list with three elements
    yield [12, 11, 0.0026713408791001632]

# Create a generator object
gen = my_generator()

# Retrieve the next item from the generator
result = next(gen)
print(result)  # Output: [12, 11, 0.0026713408791001632]

# Alternatively, you can use a for loop to iterate over the generator
for item in my_generator():
    print(item)
