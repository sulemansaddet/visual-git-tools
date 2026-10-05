def checkout_total(price,qty,tax_rate, discount=0.0):

    subtotal = (price*qty) - discount
    return subtotal + (subtotal*tax_rate)

print ("Total:", checkout_total(15,5,0.065))


    