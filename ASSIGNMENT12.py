print("Arcade Game Center Calculator")
print("Enter game type: classic, modern, or premium")
print("Type 'done' when finish play")
total = 0
while True:
    game = input("Enter game type: ")
    if game == "classic":
        price = 0.50
    elif game == "modern":
        price = 1.50
    elif game == "premium":
        price = 2.50
    elif game == "done":
        break
    else:
        print("Invalid game type. Please enter classic, modern, premium, or done.")
        continue
    total = total + price
    print(f"Price: ${price:}")
    print(f"Current total: ${total:}")
bonus = 0
if total >= 10:
    bonus = 1.50
final_total = total - bonus
print("Game Summary")
print(f"Subtotal: ${total:}")
print(f"Token Bonus Credit: -${bonus:}")
print(f"Final Total: ${final_total:}")
print("Thank you for playing!")