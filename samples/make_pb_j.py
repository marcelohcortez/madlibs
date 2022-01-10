def madlib():
    color = input("Color: ")
    noun1 = input("Noun: ")
    food = input("Food: ")
    adjective1 = input("Adjective: ")
    adjective2 = input("Adjective: ")
    number = input("Number: ")
    noun2 = input("Noun: ")
    verb1 = input("Verb: ")
    verb2 = input("Verb: ")
    noun3 = input("Noun: ")

    madlib = f"1. Select the type of bread you want to use. Many prefer the taste of {color} bread, while others prefer {noun1} bread because it is healthy. \n \
    2. Choose the flavor of Jam/Jelly. I personally prefer {food} jam, but you can use whatever you want. \n \
    3. Choose the type of penut butter - either {adjective1} or {adjective2}. \n \
    4. Take out {number} slice(s) of bread. \n \
    5. Use a {noun2} to {verb1} the jam all over on of the pieces of bread. \n \
    6. Now {verb2} the penut butter on the other piece of bread. \n \
    7. Put them together, and you have a PB&J {noun3}."

    print(madlib)