"""
Program: csv_import.py
Author: Andy Volesky
Last date modified: 11/17/2021

The purpose of this program:

For this assignment, you'll be importing the full list of counties of Iowa and their demographics,
creating a dictionary of objects from the data, and applying some methods and math to the data.
"""

import csv

county_list = []

with open('Iowa 2010 Census Data Population Income.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=',')
    for row in csv_reader:
        if row['Rank'] != '':
            county_list.append(row)



class CountyDemos:

    def __init__(self, county, per_cap, med_house, med_fam, population, num_households):
        self.county = county
        self.per_cap = per_cap
        self.med_house = med_house
        self.med_fam = med_fam
        self.population = population
        self.num_households = num_households

    def county_pop(county):
        for x in county_list:
            if x['County'] == county:
                print(f'{x["Population"]}')

    def iowa_pop():
        pop = 0
        for x in county_list:
            pop = int(x['Population'].replace(',', '')) + pop
        print(pop)

CountyDemos.county_pop('Dallas')
CountyDemos.iowa_pop()

