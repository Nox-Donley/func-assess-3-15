
def calculate_health(current_health, damage_received, armor):
    redamage = damage_received * armor
    rehealth = current_health - redamage
    print(rehealth)
    return rehealth
calculate_health(100,10,0.5)

def average_of_5(num1, num2, num3, num4, num5):
    print((num1+num2+num3+num4+num5)/5)
print(average_of_5(10,20,30,40,50))
