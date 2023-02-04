milk = input("how many liters of milk do you have?")
eggs = input("how many eggs do you have?") 
flour = input("how many kg of flour do you have?")

# 12 pancakes = 0,1kg flour, 2 eggs, 0,3l milk

pc_milk = int(milk) / 0.3 * 12 
pc_eggs = int(eggs) / 2 * 12
pc_flour = int(flour) / 0.1 * 12 

result = [pc_milk, pc_eggs, pc_flour] 

print ("you can make: ", int(min(result)), " pancakes")