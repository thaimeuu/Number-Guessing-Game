import random


def main():
    print("Welcome to Number Guessing Game!")

    is_playing = input("Are you ready? (y/n) : ")
    if is_playing != "y":
        print("See you again!")
        quit()

    record = []
    while True:
        counter = 0

        left = random.randint(1, 50)
        right = random.randint(50, 100)
        target = random.randint(left, right)
        print(f"\nYour number is in range [{left}, {right}]\n")

        while True:
            guess = input("Guess: ")
            counter += 1

            if not guess.isdigit():
                print("Invalid Value!!!")
                continue
            if not int(guess) in range(left, right + 1):
                print("Out of range!!!")
                continue

            if int(guess) > target:
                print("Try smaller")
            elif int(guess) < target:
                print("Try larger")
            else:
                record.append(counter)
                print(f"Well done, you got it in {counter} guesses\n")
                break

        print(f"Current Best Record: {min(record)} guesses\n")

        keep_playing = input("Play again? (y/n): ")
        if keep_playing != "y":
            print("See you again!")
            quit()


if __name__ == "__main__":
    main()
