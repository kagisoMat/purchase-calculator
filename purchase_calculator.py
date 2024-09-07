import os

# Define a named constant for the sales tax rate
SALES_TAX_RATE = 0.08  # 8% tax rate


def get_item_price():
    """Get the price of the item from the user."""
    while True:
        try:
            price = float(input("Enter the price of the item: R"))
            if price < 0:
                raise ValueError("Price cannot be negative.")
            return price
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a valid number.")


def get_quantity():
    """Get the quantity of items from the user."""
    while True:
        try:
            quantity = int(input("Enter the quantity of items: "))
            if quantity < 0:
                raise ValueError("Quantity cannot be negative.")
            return quantity
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a valid number.")


def calculate_total(item_price, quantity):
    """Calculate total before tax, sales tax, and final total."""
    total_before_tax = item_price * quantity
    sales_tax = total_before_tax * SALES_TAX_RATE
    total_after_tax = total_before_tax + sales_tax
    return total_before_tax, sales_tax, total_after_tax


def display_summary(item_price, quantity, total_before_tax, sales_tax, total_after_tax):
    """Display the purchase summary."""
    print("\n--- Purchase Summary ---")
    print(f"Item price: R{item_price:.2f}")
    print(f"Quantity: {quantity}")
    print(f"Total before tax: R{total_before_tax:.2f}")
    print(f"Sales tax: R{sales_tax:.2f}")
    print(f"Total after tax: R{total_after_tax:.2f}")


def save_receipt(item_price, quantity, total_before_tax, sales_tax, total_after_tax):
    """Save the purchase summary to a text file."""
    with open("receipt.txt", "w") as file:
        file.write("--- Purchase Summary ---\n")
        file.write(f"Item price: R{item_price:.2f}\n")
        file.write(f"Quantity: {quantity}\n")
        file.write(f"Total before tax: R{total_before_tax:.2f}\n")
        file.write(f"Sales tax: R{sales_tax:.2f}\n")
        file.write(f"Total after tax: R{total_after_tax:.2f}\n")
    print("Receipt saved as 'receipt.txt'.")


def main():
    """Main program loop."""
    while True:
        print("\nWelcome to the Purchase Calculator!")
        item_price = get_item_price()
        quantity = get_quantity()
        total_before_tax, sales_tax, total_after_tax = calculate_total(item_price, quantity)

        display_summary(item_price, quantity, total_before_tax, sales_tax, total_after_tax)

        save_choice = input("Would you like to save the receipt to a file? (yes/no): ").lower()
        if save_choice == 'yes':
            save_receipt(item_price, quantity, total_before_tax, sales_tax, total_after_tax)

        another_calculation = input("\nDo you want to perform another calculation? (yes/no): ").lower()
        if another_calculation != 'yes':
            print("Thank you for using the Purchase Calculator!")
            break


if __name__ == "__main__":
    main()
