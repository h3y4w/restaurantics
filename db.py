import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, String, ForeignKey, Float, DateTime
from pprint import pprint
from datetime import datetime
import sys
import csv

class DB(object):
    Base = declarative_base()

    @staticmethod
    def configure():
        Session = sessionmaker()
        DB.engine = sqlalchemy.create_engine("sqlite:///master.db")
        Session.configure(bind=DB.engine)
        DB.session = Session()

    @staticmethod
    def create_tables():
        DB.Base.metadata.create_all(DB.engine)

    @staticmethod
    def add(obj):
        DB.session.add(obj)
        DB.session.commit()
        return obj

    @staticmethod
    def delete(obj):
        DB.session.delete(obj)
        DB.session.commit()

    @staticmethod
    def dump_table_to_json(table):
        records = []
        for record in table.get_all():
            records.append(record.convert_to_json())
        return records

    @staticmethod
    def search(table, search_vars):
        for var in search_vars:
            return DB.session.query(table).filter_by(**search_vars).all()


    @staticmethod
    def write_to_csv(fn, records):
        f = open(fn, 'wb')
        _csv = csv.writer(f)
        headers = records[0].keys()
        _csv.writerow(headers)
        for i in range(len(records)):
            items = records[i].items()
            values = []

            if records[i].keys() != headers:
                raise Exception("Different records are in list")

            for key, value in items:
                values.append(value)
            _csv.writerow(values)
        f.close()

    class WeatherVar(Base):
        __tablename__ = "weathervar"
        id = sqlalchemy.Column(Integer, primary_key=True)
        city_id = sqlalchemy.Column(Integer, nullable=False)
        temp = sqlalchemy.Column(Integer, nullable=False)
        date = sqlalchemy.Column(DateTime, nullable=False)


        def __init__(self, info):
            self.temp = info['temp']
            self.date = info['date']
            self.city_id = info['city_id']

        def delete(self):
            DB.delete(self)

        def to_dict(self):
            return {"id": self.id, "date": self.date.strftime("%m/%d/%y"), "temp": self.temp, "city_id": self.city_id}

        @staticmethod
        def create(info):
            obj = DB.WeatherVar(info)
            DB.add(obj)
            return obj

        @staticmethod
        def get_all():
            return DB.session.query(DB.WeatherVar).all()


        @staticmethod
        def find_record_by_id(id):
            return DB.session.query(DB.WeatherVar).filter_by(id=id).first()

    class City(Base):
        __tablename__ = 'city'
        id = sqlalchemy.Column(Integer, primary_key=True)
        name = sqlalchemy.Column(String)

        def __init__(self, info):
            self.name = info['name']

    class Company(Base):
        __tablename__ = 'company'
        id = sqlalchemy.Column(Integer, primary_key=True)
        name = sqlalchemy.Column(String)
        city_id = sqlalchemy.Column(Integer)

        def __init__(self, info):
            self.name = info['name']
            self.city_id = info['city_id']

        @staticmethod
        def create(info):
            obj = DB.Company(info)
            DB.add(obj)
            return obj

        @staticmethod
        def get_all():
            return DB.session.query(DB.Company).all()


    class Customer(Base):
        __tablename__ = 'customer'
        id = sqlalchemy.Column(Integer, primary_key=True)
        name = sqlalchemy.Column(String)
        cc = sqlalchemy.Column(Integer)

        def __init__(self, info):
            self.name = info['name']
            self.cc = info['cc']

        def to_dict(self):
            return {"id": self.id, "name": self.name, "cc": self.cc}


        @staticmethod
        def create(info):
            obj = DB.Customer(info)
            DB.add(obj)
            return obj

        @staticmethod
        def get_all():
            return DB.session.query(DB.Customer).all()

    class Product(Base):
        __tablename__ = 'product'
        id = sqlalchemy.Column(Integer, primary_key=True)
        name = sqlalchemy.Column(String)
        company_id = sqlalchemy.Column(Integer)
        price = sqlalchemy.Column(Integer)

        def __init__(self, info):
            self.name = info['name']
            self.company_id = info['company_id']
            self.price = info['price']

        def to_dict(self):
            return {"id": self.id, "company_id": self.company_id, "price": self.price, "name": self.name}


        @staticmethod
        def create(info):
            obj = DB.Product(info)
            DB.add(obj)
            return obj

        @staticmethod
        def get_all():
            return DB.session.query(DB.Product).all()

    class Purchase(Base):
        __tablename__ = 'purchase'
        id = sqlalchemy.Column(Integer, primary_key=True)
        product_id = sqlalchemy.Column(Integer)
        customer_id = sqlalchemy.Column(Integer)
        date = sqlalchemy.Column(DateTime)

        def __init__(self, info):
            self.product_id = info['product_id']
            self.customer_id = info['customer_id']
            self.date = info['date']


        def to_dict(self):
            return {"id": self.id, "customer_id": self.customer_id, "product_id": self.product_id, "date": self.date.strftime("%m/%d/%y")}

        @staticmethod
        def find_record_by_id(id):
            pass


        @staticmethod
        def create(info):
            obj = DB.Purchase(info)
            DB.add(obj)
            return obj

        @staticmethod
        def get_all():
            return DB.session.query(DB.Purchase).all()




DB.configure()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == 'create':
            DB.create_tables()
    #records = DB.dump_table_to_json(DB.StockInput)
    #DB.write_to_csv('out.csv', records)

