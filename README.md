# Population by zipcode

This repository contains data of the Zipcode and the population in the United States.

## Overview

The crime rate dataset provides information on various types of crimes reported across different states in the USA for the year 2024. The data includes details such as crime type, location, and frequency of occurrence.

## Dataset

The dataset used in this analysis can be found in the project folder. It includes the following files:

- `crime-rate-by-state-2024.csv`: Contains the raw data on crime rates for each state in the USA for the year 2024.

## Analysis

The analysis of the crime rates is performed by this program and explores the dataset, performs data cleaning and preprocessing using Python, and provides visualizations and insights into the crime trends across different states.

## Results

The analysis reveals trends and patterns in crime rates across different states in the USA for the year 2024. Key findings and visualizations are presented in Python.
This program reads a CSV file from https://worldpopulationreview.com/state-rankings/crime-rate-by-state and tranfers it to a local phpadmin database, which is included in the project folder.  
The program also plots figure for analytics for crime rate of States and the District of Columbia in the USA, based on crime per 100,000 people.

![figure #3.jpg](figure%20%233.jpg)
## Usage

To use this repository:

1. Install Python 3 and dependencies

In order to run this program you must install python 3.11, as your interpreter, https://www.python.org/downloads/
The following python packages must also be installed, pandas, matplotlib, SQLAlchemy, pymysql

2. Clone the repository:

```sh
git clone https://github.com/luongvv-rtc/USA_Crime_Rate_2024.git

    Navigate to the cloned directory:

sh

cd USA_Crime_Rate_2024

    Explore the dataset and analysis in the data and files, respectively.

3. Create Local database

You will also need to create your own local phpadmin database and modify the SQL connection and database in the main.py file for your connection

License

This project is licensed under the MIT License. 
