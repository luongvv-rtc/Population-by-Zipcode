# CNE340 Spring Quarter
# May - 2024
# follow instructions below to complete program
# https://rtc.instructure.com/courses/2471310/assignments/32710446?module_item_id=82125187

# Student name:Van Luong Vuong
# Instrctor: Kim Rhodes

# Import section
import pandas as pd
from sqlalchemy import create_engine
from flask import Flask, render_template, request
import socket


# SQL connection and Database
hostname = 'localhost'
uname = 'root'
pwd = ''
dbname = 'zipcodes'

# connect to MySQL on W/LAMP Server
connection_string = f"mysql+pymysql://{uname}:{pwd}@{hostname}/{dbname}"
engine = create_engine(connection_string)

# opens csv file from GitHub Project Folder
with open('zip_code_database.csv') as file_path:
    df = pd.read_csv(file_path)

# table name
table_name = 'zip_code'
df.to_sql(table_name, engine, if_exists='replace', index=False)

# query from table from our database
query = f"SELECT * FROM {table_name} ORDER BY zip DESC"  # pulling data from table in db
db_sorted = pd.read_sql(query, engine)

print(db_sorted)

# close connection made by engine
engine.dispose()

#Flask section

# Establishing Flask
app = Flask(__name__)

# Setting home.html as homepage
@app.route('/')
def zipcodes_dash():
    return render_template('home.html')
    app.debug = True

# Using GET for /search argument
@app.route('/search', methods=['GET'])
def search():
    zip_code = request.args.get('zipCode')

    data = get_zip_results(zip_code)
    population = data.population if data is not None else None

    return render_template('gofecth.html', zipCode=zip_code, population=population)

# Queries the DB using input from zipCode
def get_zip_results(zip_code):
    connection = engine.connect()
    query = text("SELECT * FROM zipcodes WHERE zip_code = :zip_code")
    result = connection.execute(query, {"zip_code": zip_code}).fetchone()
    connection.close()
    return result



# Run Flask
if __name__ == '__main__':
    #Start the Flask development server
    app.run(host='0.0.0.0', port=5000)







