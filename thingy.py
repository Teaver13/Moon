import os
import dotenv
dotenv.load_dotenv()
PWord = os.getenv("pass")

print(
    f"The password is: {PWord} and this will not show on github the env file is ignored\n\n")


real_token = os.getenv("TOKEN")


def load_token():
    global my_token
    # Load token from .env into the variable
    my_token = os.getenv("TOKEN")


def verify_token():
    env_token = os.getenv("TOKEN")  # load again or reuse my_token

    if my_token == env_token:
        print("Verified Successfully, Access Granted\n\n")
        secret_area()
    else:
        print("Verification Failed")


def secret_area():
    print("Welcome to the Secret Area! Type 'exit' to leave.")
    while True:
        math_input = input("Enter a Number (Adds 10): ")
        if math_input.isdigit():
            number = int(math_input)
            result = number + 10  # Simple addition operation
            print(f"Result after adding 10: {result}")

        if math_input.lower() == "exit":
            print("Exiting Secret Area.")
            break


load_token()
verify_token()
