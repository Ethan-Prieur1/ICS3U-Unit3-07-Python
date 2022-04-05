#!/usr/bin/env python3

# Created by Ethan Prieur
# Created on March 2022
# This is a program that checks to see if you are allowed to date a granddaughter


def main():
    # This function is the main program

    # Input
    print("Answer Yes/No to see if you can date the granddaughter.")
    rich = input("Are you rich?: ")
    handsome = input("are you handsome?: ")

    # Process and Output

    if rich == "yes" or handsome == "yes":
        print("You can date the GrandDaughter")
    elif rich == "no" and handsome == "no":
        print("\nYou are forbidden from dating the GrandDaughter >:(")
    else:
        print("I Don't Know?")
    print("\nDone")


if __name__ == "__main__":
    main()
