def calculate_discount(price,discount_percent):
    price=float(input("Enter the price: "))
    discount_percent=float(input("Enter the discount received: "))
    if discount_percent >=20:
        new_price = price-(price*discount_percent/100)
        print(new_price)
    else :
        new_price =price
        print(f"Your price is {price} no discount included.")
    return new_price,discount_percent
calculate_discount("price","discount_percent")

    

