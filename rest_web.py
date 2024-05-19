# CNE340 Spring Quarter
# May - 2024
# follow instructions below to complete program
# https://rtc.instructure.com/courses/2471310/assignments/32710446?module_item_id=82125187

# Student name:Van Luong Vuong
# Instrctor: Kim Rhodes

# Import section
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.sql import text
from flask import Flask, render_template, request

# SQL connection and Database
hostname = 'localhost'
uname = 'root'
pwd = ''
dbname = 'zipcodes'

# connect to MySQL on W/LAMP Server
connection_string = f"mysql+pymysql://{uname}:{pwd}@{hostname}/{dbname}"
engine = create_engine(connection_string)

tables = pd.read_csv(r"zip_code_database.csv", dtype={"Population": int})
# The first column name of the zip_code_database.csv is "zip" -> change to "zip_code"
tables.rename(columns={"zip": "zip_code"}, inplace=True)
# The second column name of the zip_code_database.csv is "Population" -> change to "population"
tables.rename(columns={"Population": "population"}, inplace=True)
tables.to_sql('zipcodes', con=engine, if_exists='replace', index=False)

#Flask section
app = Flask(__name__)
app.debug = True

# Setting home.html as homepage
@app.route('/')
def zipcodes_dash():
    return render_template('home.html')

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

# Updates DB if zip and pop are valid arguments. Sends to fail if not
@app.route('/update', methods=['POST'])
def update():
    zip_code = request.form['zipCode']
    population = request.form['population']

    if zip_code.isdigit() and population.isdigit():
        zip_code = int(zip_code)
        population = int(population)
        if 0 <= zip_code <= 99999 and population >= 0:
            connection = engine.connect()
            query = text("UPDATE zipcodes SET population = :population WHERE zip_code = :zip_code")
            connection.execute(query, {"zip_code": zip_code, "population": population})
            connection.close()
            return render_template('update_success.html')
    return render_template('update_fail.html')

# Run Flask
if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5000)







