import os
from flask_restful import Api, Resource
from flask import Flask, request
from db import DB
from datetime import datetime

app = Flask(__name__)
api = Api(app)

# Make it so Products and Purchases have a search functionality, like url args. For example /product?date=21122015
class Weather (Resource):
    def get(self):
        weather_list = []
        if request.args.items() == []:
            return [weather.to_dict() for weather in DB.WeatherVar.get_all()]

        city_id = request.args.get("city_id")
        from_date = request.args.get("from")
        to_date = request.args.get("to")
        date = request.args.get("date")

        if from_date is None and date is None:
            return "ERROR: Please choose either arg date or arg from"

        if from_date:
            try:
                from_date = datetime.strptime(from_date, "%m-%d-%y")
            except ValueError:
                return "ERROR: from date incorrect format: %m-%d-%y"

            if to_date:
                try:
                    to_date = datetime.strptime(to_date, "%m-%d-%y")
                except ValueError:
                    return "ERROR: to date incorrect format: %m-%d-%y"
            else:
                to_date = datetime.now()

            weather_list = [weather.to_dict() for weather in DB.session.query(DB.WeatherVar).filter(
                DB.WeatherVar.date.between(from_date, to_date))]


        else:
            date = datetime.strptime(date, "%m-%d-%y")
            weather_list = [weather.to_dict() for weather in DB.session.query(DB.WeatherVar).filter(DB.WeatherVar.date==date).all()]

        if city_id != None:
            return [weather for weather in weather_list if weather["city_id"] == int(city_id)]
        return weather_list


class Products (Resource):
    def get(self):
        products = DB.Product.get_all()
        return [product.to_dict() for product in products]

class Product (Resource):

    def get(self, id):
        pass

class Purchases (Resource):
    def get(self):
        purchases = []
        if request.args.items() == []:
            print "args are empty"
            return [purchase.to_dict() for purchase in DB.Purchase.get_all()]

        if request.args.items()[0][0] == "return":
            purchases = [purchase.to_dict() for purchase in DB.Purchase.get_all()]

        else:
            search_vars = {}
            customer_id = request.args.get("customer_id")
            company_id = request.args.get("company_id")

            if customer_id is not None:
                search_vars["customer_id"] = customer_id

            if company_id is not None:
                #search_vars["product_id"] = 
                products = DB.search(DB.Product, {"company_id": company_id})

                if not products == []:
                    products = [product.id for product in products]

                    if customer_id is not None:
                        purchases = DB.session.query(DB.Purchase).filter(
                                DB.Purchase.product_id.in_(products),
                                DB.Purchase.customer_id == customer_id)
                        purchases = [purchase.to_dict() for purchase in purchases]

                    else:
                        purchases = DB.session.query(DB.Purchase).filter( DB.Purchase.product_id.in_(products))
                        purchases = [purchase.to_dict() for purchase in purchases]


            if not search_vars == {} and not company_id:
                print search_vars
                print 'got search vars'
                purchases = [purchase.to_dict() for purchase in DB.search(DB.Purchase, search_vars)]

            #if company_id == None and customer_id == None:
            #    print 'no correct search_vars'
            #    return []

        returnargs = request.args.get("return")

        customer_args = {}
        product_args = {}
        company_args = {}

        if returnargs is not None:
            returnargs = returnargs.split(",")

            for arg in returnargs:
                if arg == "customer_name":
                    customer_args[arg] = DB.Customer.name

                elif arg == "customer_cc":
                    customer_args[arg] = DB.Customer.cc

                elif arg == "product_name":
                    product_args[arg] = DB.Product.name

                elif arg == "product_price":
                    product_args[arg] = DB.Product.price

                elif arg == "company_name":
                    company_args[arg] = DB.Company.name

                elif arg == "company_city":
                    company_args[arg] = DB.Company.city_id


        if purchases == []:
            return []

        if customer_args != {} or product_args != {} or company_args != {}:
            for purchase in purchases:
                if customer_args != {}:
                    values = DB.session.query(DB.Customer, *customer_args.values()).filter(DB.Customer.id==purchase["customer_id"]).first()[1:]
                    for i, arg in enumerate(customer_args):
                        purchase[arg] = values[i]

                if product_args != {}:
                    values = DB.session.query(DB.Product, *product_args.values()).filter(DB.Product.id==purchase["product_id"]).first()[1:]

                    for i, arg in enumerate(product_args):
                        purchase[arg] = values[i]

                #if company_args != {}:
                    #vales = DB.session.query(DB.Company, *company_args.values()).filter(DB.Company==)

        return purchases


class Purchase (Resource):
    def get(self, id):
        pass

if __name__ == "__main__":

    api.add_resource(Weather, '/weather')

    api.add_resource(Products, '/product')
    api.add_resource(Product, '/product/<int:id>')

    api.add_resource(Purchases, '/purchase')
    api.add_resource(Purchase, '/purchase/<int:id>')


    app.run(debug=True,host='0.0.0.0',port=5000)

