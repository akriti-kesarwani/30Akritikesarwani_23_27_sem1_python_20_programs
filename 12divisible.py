class DivisibleBySevenGenerator:
    def __init__(self, n):
        self.n = n

    def generate_divisible_by_seven(self):
        for num in range(0, self.n + 1):
            if num % 7 == 0:
                yield num

# Take user input for the range
try:
    n_value = int(input("Enter the value of n: "))
except ValueError:
    print("Please enter a valid integer.")
    exit()

# Create an instance of the class and iterate through the generated numbers
divisible_by_seven_instance = DivisibleBySevenGenerator(n_value)

print(f"Numbers divisible by 7 in the range 0 to {n_value}:")
for num in divisible_by_seven_instance.generate_divisible_by_seven():
    print(num)
