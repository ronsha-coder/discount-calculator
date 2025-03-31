def calculate_discount(price, discount_percent):
    """Calculates the final price after applying a discount if it's 20% or higher."""
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Example values
price = 1000  # Original price
discount_percent = 20  # Discount is exactly 20%

# Calculate the final price
final_price = calculate_discount(price, discount_percent)

# Print the result
print(f"The final price after a {discount_percent}% discount on {price} is: {final_price}")
