import math

def calculate_circle_area(radius):
    pi = math.pi
    return pi * (radius ** 2)

def calculate_total_due(money, tax_rate):
    return money + (money * tax_rate)

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * (5 / 9)

# 1. Circle Area Input
print("--- Circle Area Calculation ---")
radius_input = float(input("Enter the radius: "))
area_result = calculate_circle_area(radius_input)
print(f"Output: {area_result:.2f}\n")

# 2. Taxes Input
print("--- Total Due Calculation ---")
money_input = float(input("Enter the money amount: "))
tax_input = float(input("Enter the tax rate as a whole number: ")) / 100
total_result = calculate_total_due(money_input, tax_input)
print(f"Output: {total_result:.2f}\n")

# 3. Temperature Input
print("--- Temperature Conversion ---")
fah_input = float(input("Enter Fahrenheit temperature: "))
cel_result = fahrenheit_to_celsius(fah_input)
print(f"Output: {cel_result:.4f}\n")