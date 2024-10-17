from langchain_community.utilities import SQLDatabase

import logging
import mysql.connector.connection
import traceback

logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

db_user = "sa"
db_password = "abc123"
db_host = "localhost"
db_name = ""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access the variables 
# mysql+mysqlconnector://root:admin@localhost:3306/ecommerce"
#db_url = "mysql+mysqlconnector://your_username:your_password@your_host:3306/your_database"

my_variable = os.getenv('GOOGLE_API_KEY')
another_variable = os.getenv('ANOTHER_VARIABLE')
print(my_variable)
print(another_variable)


try:
    ## generate code langchain connnect to MySQL database


    db_url = "mysql+mysqlconnector://root:admin@localhost:3306/mydatabase"
    print(db_url)
    db = SQLDatabase.from_uri(db_url)
    #print(f"get tables {db.get_table_names()}")
    #result = db.execute('select count(*) from mydatabase.athlete')
    #print(f"type {result.data[0][0]}")
except Exception as e:
    print("Error connecting to the database:")
    print(e.with_traceback())
    print(traceback.format_exc())
except ConnectionRefusedError  as e:
    print("runtime error")
    print(e.with_traceback())
except NameError  as e:
    print("Name error")    