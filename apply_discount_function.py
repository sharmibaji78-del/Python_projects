def apply_discount(price,discount):
    if not isinstance(price,(int,float)):
        return "The price should be a number"
    if not isinstance(discount,(int,float)):
        return "The discount should be a number"
    if price<=0 :
        return "The price should be greater than 0"
    if discount<0 or discount>100:
        return "The discount should be between 0 and 100"
    final_price=price-(price*discount/100)
    return final_price
d=apply_discount(100,20)
d1=apply_discount(200,50)
d2=apply_discount(50,0)
print(d)
print(d1)
print(d2)

