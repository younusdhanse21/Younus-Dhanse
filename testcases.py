
test_cases = [ 
    (15 , 12),       # both > 10 
    (12 , 8),        # one <= 10
    (10 , 11),       # one is exactly 10 (not greater than)
    (20 , 6),        # one is > 5 but <=10
    (4 ,4 ),         # neither >5 
]

print(f"{'pair':<10} | {'Condition Met?'}")
print("-" * 30)

for v1, v2 in test_cases:
    
    is_met = (v1 > 10 and v2 > 10 ) and (v1 > 5 or v2 > 5)
    
    result  = "yes" if is_met else "no"
    print(f"{v1}, {v2}):<10 | {result}")
