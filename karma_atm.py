from time import sleep as wait
from karma_funcs import karma_score

print("\n--- Welcome to your karma atm. ---\n\n")
print("Keep track of your deeds and gauge your current karma balance. \n\n")
while True:
    wait(.5)
    print(
    "What have you done today? Choose from the following options...\n\n"
    "1. View current karma score\n"
    "2. Debit 150 karma points (shady act)\n"
    "3. Deposit 150 karma points (act of love)\n"
    "4. Enjoy the rest of my day while focusing on doing good!\n"
    )
    choice = input("Your karma input: \n")
    # if user doesn't choose 1, 2, 3, or 4 they will be prompted again for valid input
    while choice not in "1234":
        print("That is not on the karma scale.\n")
        choice = input("Your karma input: \n")
        continue

    # choice 1 will display the user's current karma score and advice

    if choice == "1":
        wait(1)
        with open("karma_score.txt") as r:
            num = int(r.readline())
            print(f"Your current karma score is k{num}\n")
            print(karma_score(num))
            print(" \n ")
            wait(1)
            #continue

    # choice 2 will debit 150 karma point from the balance and return advice

    elif choice == "2":
        wait(1)
        with open("karma_score.txt", "r") as r:
            balance = r.readline()
            fbalance = int(balance)
            if fbalance >= 250:
                fbalance = fbalance - 150
                with open("karma_score.txt", "w") as w:
                    w.write(str(fbalance))
                print("Your karma deduction is complete! \n")
                wait(1)
            else:
                print("You do not have the karma points to do things like this. Behave! \n")

    # choice 3 will deposit 150 karma point from the balance and return advice

    elif choice == "3":
        wait(1)
        with open("karma_score.txt", "r") as r:
            balance = r.readline()
            fbalance = int(balance)
            if fbalance <= 1600:
                fbalance = fbalance + 150
                with open("karma_score.txt", "w") as w:
                    w.write(str(fbalance))
                print("Your karma deposit is complete! \n")
                wait(1)

    # choice 4 will thank the user and exit while True
    elif choice == "4":
        print("\nThanks for keeping track of your karma. Go do good! \n")
        wait(.5)
        break