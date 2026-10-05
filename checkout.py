def checkout_total(price,qty,tax_rate):

    subtotal = price*qty
    return subtotal - (subtotal*tax_rate)

print ("Total:", checkout_total(15,5,0.065))


    