#9_1
def good():
    
    list = ['Harry', 'Ron','Hermione']
    return print(list)

good()


#9_2
def get_odds():
    for num in range(10):
        if num % 2 != 0:
            yield num

odds = get_odds() 
count = 0
for odd in odds:
    count += 1
    if count == 3:
        print(odd)
        break