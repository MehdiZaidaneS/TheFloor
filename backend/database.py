import json
import random
import mysql.connector



# importing os module for environment variables
import os
# importing necessary functions from dotenv library
from dotenv import load_dotenv
# loading variables from .env file
load_dotenv()




## Setting connection with Mysql database
connection = mysql.connector.connect(
    host=os.getenv("HOST"),
    port=int(os.getenv("PORT")),
    user=os.getenv("USER"),
    passwd=os.getenv("PASSWD"),
    database=os.getenv("DATABASE"),
    autocommit=True,
    charset="utf8mb4",
    collation="utf8mb4_general_ci"
)


def getCategories():
    categories = []
    cursor = connection.cursor()
    sql = f"SELECT name FROM categories"
    cursor.execute(sql)
    result = cursor.fetchall()

    for row in result:
        categories.append(row[0])

    return categories  


