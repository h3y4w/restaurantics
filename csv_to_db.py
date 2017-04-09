import csv
import random
from db import DB
from datetime import datetime, timedelta
import os
import time

def weather_data():
    city_map = {"722950": 1, "724937":3, "994016":2} #LA, Palo Alto, SF
    with open("weather_data.csv", "rb") as csv_f:
        csv_reader = csv.reader(csv_f, delimiter=',')
        headers = csv_reader.next()
        for row in csv_reader:
            s = row[0].replace(" ", "")

            d = datetime.strptime(row[2].replace(" ", ""), "%Y%m%d")

            t =  row[3].replace(" ", "")

            weather = {"date": d, "temp": t, "city_id": city_map[s]}
            DB.WeatherVar.create(weather)

def company_data():
    DB.Company.create({"name": "VENDBLEND", "city_id": 1})
    DB.Company.create({"name": "KOFFEE", "city_id": 2})
    DB.Company.create({"name": "SNACKTION", "city_id": 3})

def customer_data():
    with open("customers.csv", "rb") as csv_f:
        csv_reader = csv.reader(csv_f, delimiter=",")
        headers = csv_reader.next()
        print headers
        for row in csv_reader:
            customer = {"name": row[0], "cc": row[1]}
            print customer
            DB.Customer.create(customer)

def food_data():
    csv_f1 = open("food_prices.csv", "rb")
    csv_f2 = open("food_names.csv", "rb")
    csv_reader1 = csv.reader(csv_f1, delimiter=",")
    csv_reader2 = csv.reader(csv_f2, delimiter=",")

    headers1 = csv_reader1.next()
    headers2 = csv_reader2.next()

    ran = random.sample(range(1,100), 50)
    d1 = list(csv_reader1)
    d2 = list(csv_reader2)

    for n in ran:
        food = {"name": d2[n][0], "price": d1[n][0], "company_id": d1[n][1] }
        DB.Product.create(food)


    csv_f1.close()
    csv_f2.close()



def purchase_data():
    files = ["purchases.csv", "purchases2.csv", "purchases3.csv"]
    for f in files:
        with open(f, "rb") as csv_f:
            csv_reader = csv.reader(csv_f, delimiter=",")
            headers = csv_reader.next()
            date = datetime(2015, 1, 1, 0, 0)
            d = list(csv_reader)
            i = 0
            while (date < datetime(2016, 12, 31, 0, 0) and i < 999):
                x = 3
                while (random.randrange(0, 10)>x and i< 999):
                    purchase = {"date": date, "customer_id": d[i][0], "product_id": d[i][1]}
                    DB.Purchase.create(purchase)

                    x+=1
                    i+=1

                date = date+timedelta(days=1)
if __name__ == "__main__":
    if os.path.isfile("master.db"):
        print "DB ALREADY EXISTS...  STARTING IN 5 SECS..."
        time.sleep(5)

