
print("Welcome to NutriBot! 🥗")
print("Ask me about nutrition. Type 'exit' to stop.")

while True:
    user = input("You: ").lower()

    if user == "exit":
        print("NutriBot: Goodbye! Stay healthy! 😊")
        break

    elif "hello" in user or "hi" in user:
        print("NutriBot: Hello! How can I help you?")

    elif "protein" in user:
        print("NutriBot: Eggs, beans, lentils, milk, and paneer are good protein sources.")

    elif "vitamin" in user:
        print("NutriBot: Fruits and vegetables provide many essential vitamins.")

    elif "calorie" in user:
        print("NutriBot: Calories measure the energy provided by food.")

    elif "water" in user:
        print("NutriBot: Drink water regularly throughout the day.")

    elif "healthy food" in user:
        print("NutriBot: Eat fruits, vegetables, whole grains, and protein-rich foods.")
    
    elif "fruit" in user:
    print("NutriBot: Fruits provide vitamins, minerals, and fiber. Try eating apples, bananas, and oranges!")
    
    else:
        print("NutriBot: Sorry, I don't know that yet. Ask me about protein, vitamins, calories, or water.")
        
