# Define a function calculate_item_total(quantity, unit_price) 
# that returns the total price for an item

def calculate_item_total(quantity, unit_price):
    total = quantity * unit_price
    return total
    


def apply_bulk_discount(total, quantity):
    if quantity >= 10:
        return total * 0.1
    elif quantity >= 5:
        return total * 0.05
    else:
        return total * 0
    



# Define a function calculate_tax(subtotal, tax_rate) that calculates tax amount
def calculate_tax(subtotal, tax_rate):
    return subtotal * tax_rate

# Define a function is_eligible_for_free_shipping(subtotal) that returns True if subtotal >= 50
def is_eligible_for_free_shipping(subtotal):
    if subtotal>=50:
        return True
# Define a function process_order(item_name, quantity, unit_price, tax_rate)
# Calculates item total
# Applies bulk discount
# Calculates tax
# Checks shipping eligibility
# Prints a formatted receipt

def process_order(item_name, quantity, unit_price, tax_rate):
    print(item_name)
    item_total = calculate_item_total(quantity, unit_price)
    discount_amount = apply_bulk_discount(item_total, quantity)
    subtotal= item_total-discount_amount
    tax_amount = calculate_tax(subtotal, tax_rate)
    free_shipping = 50 - subtotal
    print("="*20)
    print('SHOPPING CART CALCULATOR')
    # Order Receipt for: Notebooks
    print(f"Order Receipt for: {item_name} @ ${unit_price:.2f} each")
    # Quantity: 12 @ $3.50 each
    print(f'Quantity: {quantity}')
    # Item Total: $42.00
    print(f'Item Total: ${item_total:.2f}')
    # Bulk Discount: -$4.20
    print(f'Bulk Discount: ${discount_amount:.2f}')
    # Subtotal: $37.80
    print(f'Suntotal: ${subtotal:.2f}')
    # Tax (8%): $3.02
    print(f'Tax: ${tax_amount:.2f}')
    # Final Total: $40.82
    print(f"Final Total: ${subtotal:.2f}")
    # Need $12.20 more for free shipping
    print(f'Need ${free_shipping:.2f} more for free shipping!')
    print('-'*20)
process_order("notebook", 12, 3.5, 0.08)

