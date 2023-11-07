# tutorial/tables.py
import django_tables2 as tables
from .models import *
import numpy as np
class RestaurantTable(tables.Table):
    class Meta:
        model = Restaurant
        #template_name = "django_tables2/bootstrap.html"
        attrs = {"class":"w3-table-all"}
        fields = ("name", "neighborhood", "cuisine", "price", "rating", "comments")
    def render_price(self, value):
        return "$"*value
    def render_rating(self, value):
        return "★"*value
    def render_comments(self, value): #would like to keep this actually empty instead a string sometime
        if value == 'nan':
            return ""     
        else:
            return value