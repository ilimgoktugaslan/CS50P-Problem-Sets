def main():
    # Get input from user
    message = input("What's your emoji?\n")

    # Use convert function
    result = convert(message)

    # Print result
    print(result)

def convert(message):
    # Replace :) happy emoji
    m1=message.replace(":)",'🙂')
    # Replace :( sad emoji
    m2=m1.replace(":(",'🙁')
    # Return string
    return m2
main()