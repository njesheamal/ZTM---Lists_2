# using this list, 
basket = ["Banana", "Apples", "Oranges", "Blueberries"];

# 1. Remove the Banana from the list
basket.pop(0)
print(basket)
print("--------------------")

# 2. Remove "Blueberries" from the list.
basket.remove("Blueberries")
print(basket)
print("--------------------")
# 3. Put "Kiwi" at the end of the list.
basket.append('Kiwi')
print(basket)
print("--------------------")

# 4. Add "Apples" at the beginning of the list
basket.insert(0, "Apples")
print(basket)
print("--------------------")

# 5. Count how many apples in the basket
print(basket.count("Apples"))
print("--------------------")

# 6. empty the basket

basket.clear()
print(basket)



































#Solution:
#1 - basket.remove('Banana')
#2 - basket.pop()
#3 - basket.append('Kiwi')
#4 - basket.insert(0, 'Apples')
#5 - basket.count('Apples')
#6 - basket.clear()