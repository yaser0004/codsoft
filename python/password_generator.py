import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

while True:
    length = int(input("\nEnter the desired password length (1-100): "))
    if length > 100:
        print("\nError: Password length cannot exceed 100. Please try again.")
        continue
    password = generate_password(length)
    print(f"\nGenerated Password:-\n{password}")
    choice = input("\nDo you want to generate another password? (yes/no): ").strip().lower()
    if choice != "yes":
        print("Exiting Password Generator. Goodbye!")
        break
