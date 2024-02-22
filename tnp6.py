def generate_inverse_pattern(input_value):
    if input_value < 1:
        print("Input value must be greater than 0. Exiting...")
        return

    max_number = (input_value * (input_value + 1)) // 2

    current_number = 1
    for i in range(input_value, 0, -1):
        for j in range(1, i * 2 + 1):
            print(f"{current_number}", end="")
            if j < i * 2:
                print("*", end="")
            current_number += 1
        print()

# Get user input
user_input = int(input("Enter a positive integer: "))
generate_inverse_pattern(user_input)
