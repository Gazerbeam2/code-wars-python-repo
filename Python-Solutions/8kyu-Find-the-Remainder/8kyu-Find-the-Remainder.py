def remainder(a,b):
    if min(a,b) == 0:
        return None
    else:
        return max(a,b) % min(a,b)
