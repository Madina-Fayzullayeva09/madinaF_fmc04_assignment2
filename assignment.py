total_volume = 0 
below_range = 0 
in_range = 0 
above_range = 0 
 
def classify(value): 
    if value < 248: 
        return "Below range" 
    elif 248 <= value <= 252: 
        return "In range" 
    elif value > 252: 
        return "Above range" 
def calculate_average(total, count): 
    average = total / count 
    return average      
 
number_jars = int(input("Enter the number of jars: ")) 
 
for i in range(number_jars): 
    jar_volume = int(input("Enter the jar volume: ")) 
    total_volume = total_volume + jar_volume 
 
    category = classify(jar_volume) 
    print(category) 
 
    if category == "Below range": 
        below_range += 1 
    elif category == "In range": 
        in_range += 1 
    elif category == "Above range": 
        above_range += 1 
 
average_volume = total_volume / number_jars 
 
print(f"Total volume: {total_volume} ml") 
print(f"Average volume: {average_volume} ml") 
 
print(f"Below range: {below_range}") 
print(f"In range: {in_range}") 
print(f"Above range: {above_range}")