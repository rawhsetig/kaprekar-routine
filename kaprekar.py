from math import factorial

def kaprekar_routine(n):
    if n < 0 or n > 9999:
        raise ValueError("Input must be a non-negative integer less than or equal to 9999.")
    
    # Pad the number with leading zeros to ensure it has 4 digits
    n_str = str(n).zfill(4)
    
    # Create the largest and smallest numbers from the digits
    largest = int(''.join(sorted(n_str, reverse=True)))
    smallest = int(''.join(sorted(n_str)))
    
    # Perform the Kaprekar routine
    result = largest - smallest
    
    return result

# Example usage:
number = int(input("Enter a non-negative integer (0 to 9999): "))
while number != 6174:
    result = kaprekar_routine(number)
    print(f"{largest} - {smallest} = {result}")
    number = result
print("Congratulations! You've reached 6174, the Kaprekar's constant.")
