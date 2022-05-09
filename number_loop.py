#!/usr/bin/env python3

# Created by: Jackson Naufal
# Created on: March 2022
# This is whats your grade level


def grade_function(grade_level):
    
    
    
    if grade_level == "4+":
        grade_percentage = 97.5

    elif grade_level == "4":
        grade_percentage = 90.5

    elif grade_level == "4-":
        grade_percentage = 83  

    elif grade_level == "3+":
        grade_percentage = 78

    elif grade_level == "3":
        grade_percentage = 74.5

    elif grade_level == "3-":
        grade_percentage = 71

    elif grade_level == "2+":
        grade_percentage = 68

    elif grade_level == "2":
        grade_percentage = 65.5

    elif grade_level == "2-":
        grade_percentage = 61

    elif grade_level == "1+":
        grade_percentage = 58

    elif grade_level == "1":
        grade_percentage = 54.5

    elif grade_level == "1-":
        grade_percentage = 51

    elif grade_level == "R":
        grade_percentage = 39.5
    else:
        grade_percentage = -1

    return grade_percentage


    # output


def main():

    # call function

    level_grade = input("Enter Your grade (4+, 4, 4-, etc): ")
    

    function_grade = grade_function(level_grade)
    
    
    if function_grade == -1:
        print("Invalid Input")
    else:
        print ("The {0} level is a {1}%.".format(level_grade, function_grade))


    print("\nDone.")


if __name__ == "__main__":
    main()
