# This function returns a list of skills.
# This is the list that the user will choose from
# Add at least 3 random skills for the user to select from
def get_skills():
    return["Python","C++","Javascript","Juggling", "Running","Eating"]


# This function pretty prints the skills to the user
# It takes the list of skills as an argument and prints them numbered
# This function doesn't return anything
def show_skills(skills):

    
    for number, skill in enumerate(skills,1):
        print(number, skill)





# Shows the available skills and have user pick from them two skills
# HINT: Use previous built functions to show the skills
# For example, if the user enters 1, the first skill in your list of skills will be added to the list
# Return a list of the two skills that the user inputted
def get_user_skills(skills):

    users_list=[]
    option1 = skills[int(input("Please choose the first skill:"))-1]
    option2 = skills[int(input("Please choose the second skill:"))-1]

    users_list.append(option1)
    users_list.append(option2)

    return users_list


    





# This function will get the user's cv from their inputs
# HINT: Use previous built functions to get the skills from the user
def get_user_cv(skills):
    cv ={}
    users_name = input("What's your name?: ")
    users_age = int(input("How old are you?: "))
    users_xp = int(input("How many years of experience do you have?: "))

    cv["name"] = users_name
    cv["age"] = users_age
    cv["experience"] = users_xp
    show_skills(get_skills())
    cv["skills"] = get_user_skills(skills)


    return cv




# This functions checks if the cv is acceptable or not, by checking the age, experience and skills and return a boolean (True or False) based on that
def check_acceptance(cv, desired_skill):
    
    return ( 40 > cv["age"] > 25 and  desired_skill in cv["skills"] and cv["experience"] > 3 )




def main():
    # Write your main logic here by combining the functions above into the
    # desired outcome
    print("Welcome to the special recruitment program, please answer the following questions:")
    skills = get_skills()
    desired_skill = skills[2]
    
    cv = get_user_cv(skills)
    if check_acceptance(cv, desired_skill):
        print(f"You have been accepted")
    else:
        print("You have been rejected")
        
        


    

    
    


if __name__ == "__main__":
    main()

