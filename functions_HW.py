# The Area and Perimeter App

def get_length():
    length = float(input("Please enter the length: "))
    return length

def get_width():
    width = float(input("Please enter the width: "))
    return width

def calculate_area(length, width):
    area = length * width
    return area

def calculate_perimeter(length, width):
    perimeter = 2 * (length + width)
    return perimeter

def main():
    print("The Area and Perimeter App")
    length = get_length()
    width = get_width()
    area = calculate_area(length, width)
    perimeter = calculate_perimeter(length, width)
    print("Area = " + str(area))
    print("Perimeter = " + str(perimeter))

def Bye():
    print()
    print("Bye!")
  
if __name__ == "__main__":
    main()
    Bye()


# score App
def get_test_scores():
    print("Welcome to the Test Scores application")
    print("Enter 'X' to end input")
    print("======================")
    print()
    test_scores = []

    while True:
        score = input("Enter test score ( or x to quit ): ")
        if score.lower() == "x":
            break
        else:
            score = int(score)
            while score < 0 or score > 100:
                print("Test score must be from 0 through 100. Please try again.")
                score = int(input("Enter test score (or x to quit): "))
            test_scores.append(score)
    return test_scores

def calculate_scores(test_scores):
    if test_scores:
        total_score = sum(test_scores)
        average_score = round(total_score / len(test_scores))
    else:
        total_score = 0
        average_score = 0
    return total_score, average_score

def display_result(total_score, average_score):
    print("======================")
    print("Total Score:", total_score)
    print("Average Score:", average_score)

def main():
    scores = get_test_scores()
    total, average = calculate_scores(scores)
    display_result(total, average)

if __name__ == "__main__":
    main()