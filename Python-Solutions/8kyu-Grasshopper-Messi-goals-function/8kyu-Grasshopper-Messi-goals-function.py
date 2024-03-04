#Solutions

def goals (laLiga, copaDelRey, championsLeagues):
    return laLiga + copaDelRey + championsLeagues

# Alternate Solutions

def goals(*a):
    return sum(a)
