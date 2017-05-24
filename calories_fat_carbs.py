#S.McDonald 11/5/2016
#calories_fat_carbs
#This program takes the number of fat and carbohydrate grams entered by the user and
#calculates the number of calories from both the fat and carbohydrates that the user has
#consumed that day.


#input
#obtain grams of fat consumed and calculate calories consumed from said fat
def calories_fat():
    print("Please enter the amount of grams of fat you have consumed today: ")
    grams_fat = int(input(">>"))
    return grams_fat * 9 #grams_fat*9 to find calories from fat

#obtain carbohydrates consumed and calculate calories consumed from said carbohydrates
def calories_carbs():
    print("Please enter the amount of grams of carbohydrates that you have consumed today: ")
    grams_carbs = int(input(">>"))
    return grams_carbs * 4 #grams_carbs*4 to find calories from carbohydrates


#create a main function
def main():
    #call calories_fat
    fat = calories_fat() #return the value from the function
    #call calories_carbs
    carbs = calories_carbs() #return the value from the function
    print("Calories from fat: ", fat) #display calories from fat
    print("Calories from carbohydrates: ", carbs) #display calories from carbohydrates
    

#call the main()
main()


