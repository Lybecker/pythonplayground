# Run below command before running this file:
# pip install python-dotenv

import os
from dotenv import load_dotenv

load_dotenv()

MY_ENV_VAR = os.getenv('MYPROJECT_APIENDPOINT')


print(MY_ENV_VAR)
print("Hello World")
