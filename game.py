# Class Definitions
class LandscaperGame:
    def __init__(broke_ass):
        broke_ass.tool = "Teeth"
        broke_ass.money = 0
    def reset(broke_ass):
        broke_ass.tool = "Teeth"
        broke_ass.money = 0
    def cut_lawn(broke_ass):
        if broke_ass.tool == "Teeth":
            broke_ass.money += 1 
            print("Instead of thoughts & prayers, here's $1")
        elif broke_ass.tool == "Scissors":
            broke_ass.money += 5  
            print("I'll pay you $5 if you only trim grass with those scissors")
        elif broke_ass.tool == "Lawnmower":
            broke_ass.money += 50 
            print("$50 to account for inflation")
        elif broke_ass.tool == "Battery-powered lawnmower":
            broke_ass.money += 100  
            print("$100 for innovation")
        elif broke_ass.tool == "Team of starving students":
            broke_ass.money += 250  
            print("It's not a pyramid scheme. You hire a friend who hires a friend and you get $100, they get $50, then the ones they hire get...")

    def buy_scissors(broke_ass):
        if broke_ass.money >= 5 and broke_ass.tool == "Teeth":
            broke_ass.money -= 5  
            broke_ass.tool = "Scissors"  
            print("Your teeth & neighbors can finally breathe a sigh of relief. You're using something other than teeth for business")
        else:
            item_price = 5  # Price of scissors
            item_name = "Scissors"
            print(f"Keep chewing grass with your broke ass. You currently have ${broke_ass.money} and need ${item_price} to buy {item_name}")

    def buy_lawnmower(broke_ass):
        if broke_ass.money >= 25 and broke_ass.tool == "Scissors":
            broke_ass.money -= 25  
            broke_ass.tool = "Lawnmower" 
            print("Moving on up brokie! Good job getting you some REAL blades")
        else:
            item_price = 25  # Price of lawnmower
            item_name = "Lawnmower"
            print(f"Keep snipping pimping! You currently have ${broke_ass.money} and need ${item_price} to buy {item_name}")

    def buy_battery_powered_lawnmower(broke_ass):
        if broke_ass.money >= 250 and broke_ass.tool == "Lawnmower":
            broke_ass.money -= 250  
            broke_ass.tool = "Battery-powered lawnmower"  
            print("Have you ever considered starting an LLC now your business is automated?")
        else:
            item_price = 250  # Price of battery-powered lawnmower
            item_name = "Battery-powered lawnmower"
            print(f"Woah woah woah. You got a lil too much dip on your chip. You currently have ${broke_ass.money} and need ${item_price} to buy {item_name}")

    def buy_team_of_starving_students(broke_ass):
        if broke_ass.money >= 500 and broke_ass.tool == "Battery-powered lawnmower":
            broke_ass.money -= 500  
            broke_ass.tool = "Team of starving students"  
            print("Hire brokies just like you?")
        else:
            item_price = 500  # Price of team of students
            item_name = "Team of starving students"
            print(f"Woah woah woah. You got a lil too much dip on your chip. You currently have ${broke_ass.money} and need ${item_price} to buy {item_name}")

    def play(broke_ass):
        print("From rags to not rags!")
        print("You start by chewing grass cus you'rehungry but some sicko thinks you'd make a good grasscutter so he offers you the job")

        while True:
            choice = input("Ready to make some bands? (Cut/Buy/Reset/Quit): ").lower()

            if choice == "cut":
                broke_ass.cut_lawn()
            elif choice == "buy":
                buy_choice = input("What would you like to buy? (Scissors/Lawnmower/Battery-powered lawnmower/Team of starving students): ")
                if buy_choice == "Scissors":
                    broke_ass.buy_scissors()
                elif buy_choice == "Lawnmower":
                    broke_ass.buy_lawnmower()
                elif buy_choice == "Battery-powered lawnmower":
                    broke_ass.buy_battery_powered_lawnmower()
                elif buy_choice == "Team of starving students":
                    broke_ass.buy_team_of_starving_students()
                else:
                    print("Invalid choice. Please try again.")
            elif choice == "reset":
                game.reset()
                print("Good thing you can reset games unlike life!")
            elif choice == "quit":
                print("Thank you for playing! Your total earnings: $", broke_ass.money)
                break
            else:
                print("Invalid choice. Please try again.")

            # Check if player has won
            if broke_ass.tool == "Team of starving students" and broke_ass.money >= 1000:
                print("Congratulations, you've won!")


# Entry Point
if __name__ == "__main__":
    # Main Program Logic
    game = LandscaperGame()
    game.play()
