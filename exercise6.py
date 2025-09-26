def ordinalSuffix(number):
    
    ns = str(number)
    
    if ns[-2:] in ("11", "12", "13"):
        return ns + "th"
    
    if ns in "1" or ns[-1] == "1":
        return ns + "st"
    elif ns in "2" or ns[-1] == "2":
        return ns + "nd"
    elif ns in "3" or ns[-1] == "3":
        return ns + "rd"
    else:
        return ns + "th"
            
assert ordinalSuffix(0) == '0th' 
assert ordinalSuffix(1) == '1st' 
assert ordinalSuffix(2) == '2nd' 
assert ordinalSuffix(3) == '3rd' 
assert ordinalSuffix(4) == '4th' 
assert ordinalSuffix(10) == '10th' 
assert ordinalSuffix(11) == '11th' 
assert ordinalSuffix(12) == '12th' 
assert ordinalSuffix(13) == '13th' 
assert ordinalSuffix(14) == '14th' 
assert ordinalSuffix(101) == '101st'