# How well do you know the United States capitals

name = input('Hello, what is your name?: ')
print("Hello, " + name + "." + " Are you ready to see how well you know your capitals? There are 10 questions.")


def Capital_Questions():
    correct = 0
    incorrect = 0
    AQs = ('A', 'a', 'B', 'b', 'C', 'c', 'D', 'd')

    print("")
    print("1. What is the capital of Alabama?")
    print("A. Monte")
    print("B. Montgomery")
    print("C. Georgia")
    print("D. Little Rock")
    AQ1 = input("Your answer: ")
    while AQ1 not in AQs:
        AQ1 = input("Your answer: ")
    if AQ1.lower() == 'b':
        print('Correct')
        correct += 1
    else:
        print('Incorrect')
        incorrect += 1

    print("")
    print("2. What is the capital of Idaho?")
    print("A. Raleigh")
    print("B. Columbia")
    print("C. Boise")
    print("D. Frankfort")
    AQ2 = input("Your answer: ")
    while AQ2 not in AQs:
       AQ2 = input("Your answer: ")
    if AQ2.lower() == 'c':
        print('Correct')
        correct += 1
    else:
        print('Incorrect')
        incorrect += 1

    print("")
    print("3. What is the capital of Delaware?")
    print("A. Dover")
    print("B. Salem")
    print("C. Bismarck")
    print("D. York")
    AQ3 = input("Your answer: ")
    while AQ3 not in AQs:
       AQ3 = input("Your answer: ")
    if AQ3.lower() == 'a':
        print('Correct')
        correct += 1
    else:
        print('Incorrect')
        incorrect += 1

    print("")
    print("4. What is the capital of New Mexico?")
    print("A. Des Moines")
    print("B. Santa Barbara")
    print("C. Santa Fe")
    print("D. Augusta")
    AQ4 = input("Your answer: ")
    while AQ4 not in AQs:
        AQ4 = input("Your answer: ")
    if AQ4.lower() == 'c':
       print('Correct')
       correct += 1
    else:
        print('Incorrect')
        incorrect += 1

    print("")
    print("5. What is the capital of Florida?")
    print("A. Tallahassee")
    print("B. Orlando")
    print("C. Miami")
    print("D. Topeka")
    AQ5 = input("Your answer: ")
    while AQ5 not in AQs:
        AQ5 = input("Your answer: ")
    if AQ5.lower() == 'a':
        print('Correct')
        correct += 1
    else:
        print('Incorrect')
        incorrect += 1

    print("")
    print("6. What is the capital of Nebraska?")
    print("A. Ohmaha")
    print("B. Jackson")
    print("C. Charleston")
    print("D. Lincoln")
    AQ6 = input("Your answer: ")
    while AQ6 not in AQs:
        AQ6 = input("Your answer: ")
    if AQ6.lower() == 'd':
        print('Correct')
        correct += 1
    else:
        print('Incorrect')
        incorrect += 1

    print("")
    print("7. What is the capital of Arkansas?")
    print("A. Madison")
    print("B. Harrisburg")
    print("C. Little Rock")
    print("D. Providence")
    AQ7 = input("Your answer: ")
    while AQ7 not in AQs:
        AQ7 = input("Your answer: ")
    if AQ7.lower() == 'c':
        print('Correct')
        correct += 1
    else:
        print('Incorrect')
        incorrect += 1

    print("")
    print("8. What is the capital of Illinois?")
    print("A. Chicago")
    print("B. Springfield")
    print("C. Baton Rouge")
    print("D. Montpelier")
    AQ8 = input("Your answer: ")
    while AQ8 not in AQs:
        AQ8 = input("Your answer: ")
    if AQ8.lower() == 'b':
        print('Correct')
        correct += 1
    else:
        print('Incorrect')
        incorrect += 1

    print("")
    print("9. What is the capital of Texas?")
    print("A. Austin")
    print("B. Dallas")
    print("C. St. Paul")
    print("D. Cheyenne")
    AQ9 = input("Your answer: ")
    while AQ9 not in AQs:
        AQ9 = input("Your answer: ")
    if AQ9.lower() == 'a':
        print('Correct')
        correct += 1
    else:
        print('Incorrect')
        incorrect += 1

    print("")
    print("10. What is the capital of New York?")
    print("A. Long Island")
    print("B. York")
    print("C. New York City")
    print("D. Albany")
    AQ10 = input("Your answer: ")
    while AQ10 not in AQs:
        AQ10 = input("Your answer: ")
    if AQ10.lower() == 'd':
        print('Correct')
        correct += 1
    else:
        print('Incorrect')
        incorrect += 1

    print("")
    print("Thank you for playing, " + str(name) + "." + " Here are your results:")
    print("Correct: " + str(correct))
    print("Incorrect: " + str(incorrect))


Capital_Questions()