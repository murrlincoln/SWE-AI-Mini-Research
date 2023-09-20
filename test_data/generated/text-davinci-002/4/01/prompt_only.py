def max_product(list): 

max_product = 1

for i in range(len(list)):
    for j in range(i+1, len(list)):
        product = list[i] * list[j]

if product > max_product:
    max_product = product

return max_product