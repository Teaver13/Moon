import os
import dotenv
dotenv.load_dotenv()
PWord = os.getenv("pass")

print(f"The password is: {PWord}")
