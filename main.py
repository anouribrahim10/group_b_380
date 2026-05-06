from cipher import encrypt, decrypt


def main():
    while True:
        print("\n=== Cipher Menu ===")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "3":
            print("Exit Complete.")
            break

        elif choice == "1" or choice == "2":
            message = input("Enter your message: ")
            sequence_string = input("Enter sequence (ex. C1 C2 C2 C1): ")
            sequence_list = sequence_string.split()
            unique_words = []

            for word in sequence_list:
                if word not in unique_words:
                    unique_words.append(word)
            word_to_number = {}
            for word in unique_words:
                shift_value = input(f"Enter a number for {word}: ")
                shift_value = int(shift_value)
                word_to_number[word] = shift_value
            final_integer_list = []
            for word in sequence_list:
                number = word_to_number[word]
                final_integer_list.append(number)
           
            if choice == "1":
                result = encrypt(message, final_integer_list)
                print("\nEncrypted message:")
                print(result)

            elif choice == "2":
                result = decrypt(message, final_integer_list)
                print("\nDecrypted message:")
                print(result)

        else:
            print("Invalid choice. Please choose 1, 2, or 3.")


if __name__ == "__main__":
    main()