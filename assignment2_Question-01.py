# Question 01. Interactive Terminal E-Commerce Cart & Inventory Tracker
catalog ={"laptop":800, "mouse":20, "keyboard":50, "monitor":150}

grand_total = 0
discount = 0
final_total = 0

# Interactive Command Loop
while True:
    item = input("Enter an item to add to your cart or 'checkout' to finish or 'exit' to clear the cart):").lower()
    
    if item == "checkout":
        break
    elif item == "exit":
        grand_total = 0
        break
    elif item in catalog:
        price = catalog[item]
        grand_total = grand_total + price
        print(f"Added {item} (${price}) to your cart. Current total: ${grand_total}")
    else:
        print(f"Item '{item}' not found in catalog. Please try again.")

        # Checkout and Conditional Discount Process
        
        if grand_total > 0:
            if grand_total >= 500:
                discount = grand_total*0.10
            elif grand_total >= 200:
                discount = grand_total*0.05
            else:
                discount = 0

            final_total = grand_total - discount

# Final Receipt Print Output
print("\nCHECKOUT RECEIPT ")
print("========================================")
print(f"Subtotal: ${grand_total:.1f}")
print(f"Discount: ${discount:.1f}")
print(f"Final Total: ${final_total:.1f}")
print("========================================")



