import os
from flask_restful import Api, Resource
from flask import Flask, request
from db import DB
from datetime import datetime

app = Flask(__name__)
api = Api(app)

tags = []
class TweetData(Resource):

    def get(self):
        return 
    """
    [
      {
          "name": "@Scott",
              "tag": "PaneraSJ",
                  "picture": "http://placehold.it/32x32",
                      "company": "PAPRICUT",
                          "msg": "",
                              "date": "2014-05-27T04:21:28 +07:00",
                                  "latitude": 0.807814,
                                      "longitude": 58.372797
                                        
      },
        {
                    "name": "@Pugh",
                        "tag": "Togos-sf,Togos-SV",
                            "picture": "http://placehold.it/32x32",
                                "company": "ELENTRIX",
                                    "msg": "",
                                        "date": "2015-06-12T09:07:05 +07:00",
                                            "latitude": -49.230133,
                                                "longitude": -100.773617
                                                  
                },
        {
                    "name": "@Marshall",
                        "tag": "PaneraSJ",
                            "picture": "http://placehold.it/32x32",
                                "company": "ISOPLEX",
                                    "msg": "",
                                        "date": "2016-03-28T06:37:21 +07:00",
                                            "latitude": -71.581145,
                                                "longitude": -20.269433
                                                  
                },
        {
                    "name": "@Ross",
                        "tag": "PaneraSF",
                            "picture": "http://placehold.it/32x32",
                                "company": "IMMUNICS",
                                    "msg": "",
                                        "date": "2015-03-20T06:12:56 +07:00",
                                            "latitude": 86.912537,
                                                "longitude": 108.116276
                                                  
                },
        {
                    "name": "@Ruiz",
                        "tag": "Togos-sf,Togos-SV",
                            "picture": "http://placehold.it/32x32",
                                "company": "KONNECT",
                                    "msg": "",
                                        "date": "2015-03-11T04:30:45 +07:00",
                                            "latitude": 25.430992,
                                                "longitude": -147.273856
                                                  
                },
        {
                    "name": "@Bradford",
                        "tag": "PaneraSF",
                            "picture": "http://placehold.it/32x32",
                                "company": "PLASMOSIS",
                                    "msg": "",
                                        "date": "2015-09-30T09:57:47 +07:00",
                                            "latitude": 57.134624,
                                                "longitude": 27.461671
                                                  
                },
        {
                    "name": "@Miles",
                        "tag": "Togos-sf,Togos-SV",
                            "picture": "http://placehold.it/32x32",
                                "company": "IDEALIS",
                                    "msg": "",
                                        "date": "2016-06-27T04:22:18 +07:00",
                                            "latitude": -51.50928,
                                                "longitude": -25.095389
                                                  
                },
        {
                    "name": "@Dotson",
                        "tag": "PaneraSF",
                            "picture": "http://placehold.it/32x32",
                                "company": "MANTRO",
                                    "msg": "",
                                        "date": "2016-08-18T12:56:01 +07:00",
                                            "latitude": -4.03804,
                                                "longitude": 171.913534
                                                  
                },
        {
                    "name": "@Green",
                        "tag": "Togos-sf,Togos-SV",
                            "picture": "http://placehold.it/32x32",
                                "company": "ENERSOL",
                                    "msg": "",
                                        "date": "2014-04-22T01:32:23 +07:00",
                                            "latitude": -38.977971,
                                                "longitude": 170.71633
                                                  
                },
        {
                    "name": "@Hodge",
                        "tag": "PaneraSJ",
                            "picture": "http://placehold.it/32x32",
                                "company": "CORECOM",
                                    "msg": "",
                                        "date": "2015-11-16T02:18:24 +08:00",
                                            "latitude": -81.044554,
                                                "longitude": 102.338197
                                                  
                },
        {
                    "name": "@Gilliam",
                        "tag": "PaneraSF",
                            "picture": "http://placehold.it/32x32",
                                "company": "ZANITY",
                                    "msg": "",
                                        "date": "2015-02-23T01:24:04 +08:00",
                                            "latitude": 19.229023,
                                                "longitude": -113.076739
                                                  
                },
        {
                    "name": "@Blake",
                        "tag": "PaneraSJ",
                            "picture": "http://placehold.it/32x32",
                                "company": "GOLOGY",
                                    "msg": "",
                                        "date": "2015-04-04T02:29:33 +07:00",
                                            "latitude": 37.83198,
                                                "longitude": 139.295984
                                                  
                },
        {
                    "name": "@Mcfarland",
                        "tag": "PaneraSF",
                            "picture": "http://placehold.it/32x32",
                                "company": "SHOPABOUT",
                                    "msg": "",
                                        "date": "2016-12-07T09:06:45 +08:00",
                                            "latitude": -30.245091,
                                                "longitude": -15.097872
                                                  
                },
        {
                    "name": "@Goodwin",
                        "tag": "Togos-sf,Togos-SV",
                            "picture": "http://placehold.it/32x32",
                                "company": "ROOFORIA",
                                    "msg": "",
                                        "date": "2014-05-03T07:42:58 +07:00",
                                            "latitude": -85.970203,
                                                "longitude": -162.539126
                                                  
                },
        {
                    "name": "@Yates",
                        "tag": "PaneraSF",
                            "picture": "http://placehold.it/32x32",
                                "company": "EMTRAK",
                                    "msg": "",
                                        "date": "2014-06-04T01:55:36 +07:00",
                                            "latitude": 50.988983,
                                                "longitude": 125.811832
                                                  
                },
        {
                    "name": "@Shepherd",
                        "tag": "PaneraSJ",
                            "picture": "http://placehold.it/32x32",
                                "company": "DIGIQUE",
                                    "msg": "",
                                        "date": "2015-03-24T05:52:08 +07:00",
                                            "latitude": -6.598973,
                                                "longitude": 114.744186
                                                  
                },
        {
                    "name": "@Rios",
                        "tag": "PaneraSF",
                            "picture": "http://placehold.it/32x32",
                                "company": "BIZMATIC",
                                    "msg": "",
                                        "date": "2016-02-22T09:26:52 +08:00",
                                            "latitude": -35.349969,
                                                "longitude": -130.118016
                                                  
                },
        {
                    "name": "@Arnold",
                        "tag": "PaneraSF",
                            "picture": "http://placehold.it/32x32",
                                "company": "REALYSIS",
                                    "msg": "",
                                        "date": "2014-03-03T12:00:45 +08:00",
                                            "latitude": -30.177156,
                                                "longitude": 153.563403
                                                  
                },
        {
                    "name": "@Holt",
                        "tag": "PaneraSF",
                            "picture": "http://placehold.it/32x32",
                                "company": "DUFLEX",
                                    "msg": "",
                                        "date": "2014-09-01T06:09:37 +07:00",
                                            "latitude": -10.745241,
                                                "longitude": 112.31502
                                                  
                },
        {
                    "name": "@Mcpherson",
                        "tag": "PaneraSJ",
                            "picture": "http://placehold.it/32x32",
                                "company": "CONFERIA",
                                    "msg": "",
                                        "date": "2015-07-16T08:19:11 +07:00",
                                            "latitude": -28.504638,
                                                "longitude": -9.419378
                                                  
                }

    ]
    """

    def post(self):
        data = request.get_json(force=True)
        tweet = DB.Tweet.create(data['tweet'])
        DB.Hashtag.create(data['hashtag'].update({"tweet_id":tweet.id}))
        return 'OK'

class Tag (Resource):
    def get(self):
        return tags

    def post(self):
        global tags
        tags_ = request.args.get("tags")
        if tags_ != None:
            tags = tags_.split(",")
            return "SET"

        return "ERROR NOT SET"


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

            if request.args.get("from") != None and request.args.get("to") != None:
                #try:
                from_date = request.args.get("from")
                to_date = request.args.get("to")

                to_date = datetime.strptime(to_date, "%m/%d/%y")
                from_date = datetime.strptime(from_date, "%m/%d/%y")

                    #return "ERROR PARSING DATE RANGE"
                company_id = request.args.get("company_id")

                products = DB.search(DB.Product, {"company_id": company_id})
                products = [product.id for product in products]

                purchases = DB.session.query(DB.Purchase).filter(
                        DB.Purchase.product_id.in_(products),
                        DB.Purchase.date.between(from_date, to_date)).all()

                purchases = [purchase.to_dict() for purchase in purchases]

                return purchases

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


        return purchases


class Purchase (Resource):
    def get(self, id):
        pass

if __name__ == "__main__":

    api.add_resource(TweetData, "/tweet")

    api.add_resource(Tag, "/tag")

    api.add_resource(Weather, '/weather')

    api.add_resource(Products, '/product')
    api.add_resource(Product, '/product/<int:id>')

    api.add_resource(Purchases, '/purchase')
    api.add_resource(Purchase, '/purchase/<int:id>')


    app.run(debug=True,host='0.0.0.0',port=5000)

