tools = ['teeth']
money = 0
prices = {'scissors': 5, 'push lawnmower': 25, 'battery-powered lawnmower': 250, 'team of starving students': 500}
game = True

# Game loop
while game == True:
    print('Your current tools are: ' + str(tools))
    print('The amount of money you have is: $' + str(money))

    if 'team of starving students' in tools and money >= 1000:
        print("Congratulations! You've won the game!")
        game = False

    choice = input("What would you like to do? (cut grass / buy tool / end game): ")

    if choice == "cut grass":
        if 'battery-powered lawnmower' in tools:
            money += 100
        elif 'push lawnmower' in tools:
            money += 50
        elif 'scissors' in tools:
            money += 5
        else:
            money += 1
    elif choice == "buy tool":
        print("Available tools:")
        for tool in prices:
            print(tool + ": $" + str(prices[tool]))
        
        tool_choice = input("Which tool would you like to buy? ")
        
        if tool_choice in prices:
            if money >= prices[tool_choice] and tool_choice not in tools:
                tools.append(tool_choice)
                money -= prices[tool_choice]
                print("Congratulations! You have bought", tool_choice)
            elif tool_choice in tools:
                print("You already own", tool_choice)
            else:
                print("You don't have enough money to buy", tool_choice)
        else:
            print("Invalid choice.")
    else:
        print("Invalid choice.")

