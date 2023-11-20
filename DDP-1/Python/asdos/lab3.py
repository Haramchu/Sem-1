line1 = "cupcake,katsu,perkedel,kwetiau"
line2 = "katsu,muffin,pempek,sushi"

result1 = ""
current_item = ""
item_same = ""

for char in line1:
    if char == ',':
        if current_item not in line2:
            result1 += current_item + ', '
        current_item = ""
    else:
        current_item += char

if current_item not in line2:
    result1 += current_item + ', '

current_item = ""

for char in line2:
    if char == ',': 
        if current_item not in line1:
            result1 += current_item + ', '
        current_item = ""
    else:
        current_item += char

if current_item not in line1:
    result1 += current_item + ', '

print(result1)