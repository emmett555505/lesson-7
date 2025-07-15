#take input for the student that he can take the exam or not
medical_cause = input("did you have a medical cause Y or N :")
#take input of the attendance
attendance = int(input("enter the attendance of the student :"))

#checking the user input predicting outpur accordingly 
if medical_cause == 'Y' or medical_cause == 'y':
    print("you are allowed")
else:
    if attendance>=75:
        print("allowed")
    else:
        print("not allowed")
