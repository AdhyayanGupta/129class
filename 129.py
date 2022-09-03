from email import header
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
import requests


data = []
with open("archive_dataset.csv","r") as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        data.append(row)

headers = data[0]
planet_data= data[1:]


# coverting all planet name to lowercase
for data_point in planet_data:
    data_point[2].lower()

# sorting planet name in order

planet_data.sort(key = lambda planet_data:planet_data[2])
with open("archive_dataset_sorted.csv", "a+") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(planet_data)
 #remove blank lines
with open("archive_dataset_sorted.csv") as input, open("archive_dataset_sorted1.csv", "w", newline='') as output:
    writer = csv.writer(output)
    for row in csv.reader(input):
        if any(field.strip() for field in row):
            writer.writerow(row)   