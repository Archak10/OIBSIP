def calculate_bmi(weight, height):
    """Calculate BMI given weight in kilograms and height in meters."""
    return weight / (height ** 2)

def calculator_bmi(bmi):
    """Classify BMI into standard categories."""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def main():
    """Main function to run the BMI calculator."""
    print("Welcome to the BMI Calculator!")
    try:
        # Get user input
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))
        
        if weight <= 0 or height <= 0:
            print("Error: Weight and height must be positive numbers.")
            return
        
        # Calculate BMI
        bmi = calculate_bmi(weight, height)
        category = calculator_bmi(bmi)
        
        # Display results
        print(f"\nYour BMI is: {bmi:.2f}")
        print(f"You are classified as: {category}")
    except ValueError:
        print("Invalid input! Please enter valid numerical values.")

if __name__ == "__main__":
    main()