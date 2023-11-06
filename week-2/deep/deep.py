# Get input from user

answer=input("What is the answer to the Great Question of Life, the Universe and Everything?\n")

# Print Yes if the user inputs 42 or forty-two or Forty Two

if answer.strip() == ("42"): # We use ".strip()" to delete spaces from around of the input
    print("Yes")
elif answer.lower().strip() == ("forty-two"): # We use to ".lower()" to make lower everything in input
    print("Yes")
elif answer.lower().strip() == ("forty two"):
    print("Yes")

# Otherwise output

else:
    print("No")