import csv
f1 = open("Booking.csv",'r')
Seat_no = []
Pick_up_point = []
Drop_point = []
Dates = []
Travelers = []
Traveler_company = {}
gender = {}

d1 = list(csv.reader(f1,delimiter = ','))
print("Booking Data:")
print(d1)
print("\n")

for i in range(len(d1)):
    Seat_no.append(d1[i][0])
    Travelers.append(d1[i][1])
    Pick_up_point.append(d1[i][4])
    Drop_point.append(d1[i][5])
    Dates.append(d1[i][3])
    Traveler_company.update({d1[i][0]:d1[i][2]})
    gender.update({d1[i][1]:d1[i][6]})

print("Seat No.:")
print(Seat_no)
print("\n")
print("Name of Travelers:")
print(Travelers)
print("\n")
print("Pick_up_Points:")
print(set(Pick_up_point))
print("\n")
print("Drop_Points:")
print(set(Drop_point))
print("\n")
print("Name of Traveler_companies:")
print(set(Traveler_company.values()))
print("\n")
print("Dates:")
print(set(Dates))
print("\n")
print("Travelers and there gender:")
print(gender)
print("\n")


# Most People travel on Which date : 
frequency = {}
for item in Dates:
    if item in frequency:
        frequency[item] = frequency[item]+1
    else:
        frequency[item] = 1
print("Frequency of Dates:")
print(frequency)

marklist=sorted(frequency.items(),key = lambda x:x[1],reverse=True)
sortdict = dict(marklist)
print(marklist)
print("The Most People travel on this date = ",list(sortdict.keys())[0], "; No. of Peeople is =",list(sortdict.values())[0])
print("\n")

# Finding Most Popular Traveler company and no. of its customer :
frequency = {}
for item in Traveler_company.values():
    if item in frequency:
        frequency[item] = frequency[item]+1
    else:
        frequency[item] = 1
print("Frequency of Traveler_company:")
print(frequency)

marklist=sorted(frequency.items(),key = lambda x:x[1],reverse=True)
sortdict = dict(marklist)
print(marklist)
print("The Most Popular Traveler company is",list(sortdict.keys())[0], "use",list(sortdict.values())[0],"times.")
print("\n")

# Finding Most People Travel from which place and there no. :
frequency = {}
for item in Pick_up_point:
    if item in frequency:
        frequency[item] = frequency[item]+1
    else:
        frequency[item] = 1
print("Frequency of Pick_up_points:")
print(frequency)

marklist=sorted(frequency.items(),key = lambda x:x[1],reverse=True)
sortdict = dict(marklist)
print(marklist)
print("The Most People Travel from",list(sortdict.keys())[0], "and thier no. is =",list(sortdict.values())[0])
print("\n")

# Finding Most People Travel to reach which place and there no. :
frequency = {}
for item in Drop_point:
    if item in frequency:
        frequency[item] = frequency[item]+1
    else:
        frequency[item] = 1
print("Frequency of Drop_points:")
print(frequency)

marklist=sorted(frequency.items(),key = lambda x:x[1],reverse=True)
sortdict = dict(marklist)
print(marklist)
print("The Most People Travel to reach",list(sortdict.keys())[0], "and thier no. is =",list(sortdict.values())[0])
print("\n")

# Calculating no. of Males and Females Traveler.
male = 0
female = 0

for item in gender.keys():
    if gender[item] == "Male":
        male = male + 1
    else:
        female = female + 1
 
print("No. of Males Travel : ",male)
print("No. of Females Travel : ",female)

print("\n")
print("******************************* Thank You! ******************************")
