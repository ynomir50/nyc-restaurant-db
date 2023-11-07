from restaurants.models import *
import pandas as pd
from django.core.exceptions import ObjectDoesNotExist

def run(): #currently deletes all data and then reimports from csv
    Restaurant.objects.all().delete()
    inDF = pd.read_csv('import/import.csv')
    print(inDF)
    for obj in inDF.itertuples():
        try:
            if Restaurant.objects.filter(name=obj.Name).count() == 0: #check if entry exists before inserting
                newentry = Restaurant(name=obj.Name, neighborhood=Neighborhood.objects.get(name=obj.Neighborhood), cuisine = obj.Cuisine, price = obj.Price, rating = obj.Rating, comments = obj.Comments)
                newentry.save()
            else:
                print(f"Item not Inserted due to redundancy: {obj.Name}")
        except ObjectDoesNotExist:
            print(f"Item not Inserted due to error: {obj.Name}")
            pass
