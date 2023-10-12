from restaurants.models import *
import pandas as pd

def run():
    inDF = pd.read_csv('import/import.csv')
    print(inDF)
    restaurantimport = [Restaurant(name=obj.Name, neighborhood=Neighborhood.objects.get(name=obj.Neighborhood), cuisine = obj.Cuisine, price = obj.Price, rating = obj.Rating) for obj in inDF.itertuples()]
    for i in restaurantimport:
        i.save()
    # ------can add in filtering to ensure no duplicates later, once I find some criteria to differentiate between entries
    #for i in restaurantimport:
    #    if Restaurant.objects.filter(official=i.official).count() == 0: #check if entry exists
    #        i.save()
