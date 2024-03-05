# Solution
def combat(health, damage):
    remaningHealth = (health - damage)
    if (remaningHealth > 0):
        return remaningHealth
    else: return 0
    #your code here

# Solution

def combat(health, damage):
    return max(0, health-damage)
