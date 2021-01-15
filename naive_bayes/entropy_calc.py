import math
def entropy_calc(p1, p2):
    entropy = (-(p1)*math.log((p1) , 2) - (p2)*math.log((p2) ,2))
    return entropy
entrop = entropy_calc(1/3 , 2/3)
print(entrop)
