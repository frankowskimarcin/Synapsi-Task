import random


def main():

    while True:
        min_value = random.randint(0, 150)
        max_value = random.randint(75, 200)
        if min_value < max_value:
            break

    while True:
        try:
            input_value = int(input("Input number in range {} - {}: ".format(min_value, max_value)))
        except ValueError:
            print("Enter an integer")
            continue
        if input_value < min_value:
            print("Value must be greater than or equal to {}".format(min_value))
        elif input_value > max_value:
            print("Value must be less than or equal to {}".format(max_value))
        else:
            print("Your value: " + str(input_value))
            break


if __name__ == '__main__':
    main()
