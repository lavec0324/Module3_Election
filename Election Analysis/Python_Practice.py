# How many votes did you get?
# my_votes = int(input("How many votes did you get in the election? "))
#  Total votes in the election
# total_votes = int(input("What is the total votes in the election? "))
# Calculate the percentage of votes you received.
# percentage_votes = round((my_votes / total_votes),2)*100
# print("I received " + str(percentage_votes)+"% of the total votes.")
# percentage_votes = int(percentage_votes)
#if percentage_votes > "50"
#    print ("You won the election :) ")
#    print ("You lost the election :( ")
# counties = ["Arapahoe","Denver","Jefferson"]
# if counties[0] == 'Denver':
#    print(counties[0])
# else:
#    print(counties[2])
# temperature = int(input("What is the temperature outside? "))

# if temperature >= 80:
#     print("Turn on the AC.")
# else:
#     print("Open the windows.")        
# What is the score
# score = int(input("What was the score you received?"))
#print(score)
# if score >= 90:
#     print("You receive an 'A'")
# else:
#         if score >= 80:
#             print("You receive an 'B'")
#         else:
#             if score >= 70:
#                 print("You receive an 'C'")
#             else:
#                 if score >= 60:
#                     print("You receive an 'D'")
#                 else:
#                         print("You receive an 'F'")
# score = int(input("What was the score you received?"))
# if score >= 90:
#     print("You receive an 'A'")
# elif score >= 80:
#     print("You receive an 'B'")
# elif score >= 70:
#     print("You receive an 'C'")
# elif score >= 60:
#     print("You receive an 'D'")
# else:
#     print("You receive an 'F'")

#Using If and In
#counties = ["Arapahoe","Denver","Jefferson"] 
# if "Arapahoe" in counties: 
#     print("True") 
# else: print("False")

#Using If and Not in
# if "El Paso" not in counties:
#         print("True")
# else: print("False")

# if "El Paso" in counties:
#     print("El Paso is in the list of counties.")
# else:
#     print("El Paso is not in the list of counties.")
  
#Use in & And

#WHile loops
# x = 0
# while x <=5:
#     print(x)
#     x= x + 1 

#For loops

#counties = ["Arapahoe","Denver","Jefferson"] 
# for county in counties:
#     print(county)

#Range of numbers
# for numbers in range(1,11):
#     print(numbers)
    
# for i in range(len(counties)):
#         print(i)
#         print(len(counties))
#         print(counties[i])
        
# counties_tuple = ("Arapahoe","Denver","Jefferson")
# for county in counties_tuple:
#    print(county)
# for i in range(len(counties_tuple)):
#     print(counties_tuple[i])

#iterate dictionary
#counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
# for county in counties_dict.values():
#     print(county)
# for county in counties_dict:
#     print(counties_dict.get(county))

#gets keys and values using items

# for county, voters in counties_dict.items():
#     print(county, voters)


candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

print(message_to_candidate)