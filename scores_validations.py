
print("The Test Scores application")
print()
print("Enter 3 test scores")
print("======================")
# initialize variables
counter = 0
score_total = 0
test_score = [0]

while test_score != 999:
    try:
        test_score = int(input("Enter test score or 999 to exit: "))
        if test_score >= 0 and test_score <= 100:
            score_total += test_score
            counter += 1
        elif test_score != 999:
            print("Test score must be from 0 through 100. Score discarded. Try again.")
    except ValueError:
        print("Invalid input. Please enter a valid test score.")

# calculate average score
if counter != 0:
    average_score = round(score_total / counter)
else:
    average_score = 0
# format and display the result
print("======================")

print("Total Score:", score_total)
print("Average Score:", average_score)
