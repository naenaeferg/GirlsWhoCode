import school_scores
list_of_record = school_scores.get_all()

print(list_of_record[0]) #printing first element

subdata = list_of_record[0]

for data in list_of_record:  #printing the state name and year
    print("State", data['State']['Name'], "year:", data['Year'] )
    print("Test-Taker", data['Gender']['Female']['Test-takers'])
