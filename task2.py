
def main():

    while True:
        try:
            input_value = int(input("Input number in range 50 - 150: "))
        except ValueError:
            print("Enter an integer")
            continue
        if input_value < 50:
            print("Value must be greater than or equal to 50")
        elif input_value > 150:
            print("Value must be less than or equal to 150")
        else:
            print("Your value: " + str(input_value))
            break


if __name__ == '__main__':
    main()
