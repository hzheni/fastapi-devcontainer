#!/usr/bin/env python3
import mysql.connector

from fastapi import Request, FastAPI
from typing import Optional
from pydantic import BaseModel
#import pandas as pd
import json
import os

api = FastAPI()

@api.get("/")  # zone apex
def zone_apex():
    return {"Hello": "Hello APIIdodododoIII"}

#@api.get("/add/{a}/{b}")
#def add(a: int, b: int):
#    return {"sum": a + b}

#@api.get("/customer/{idx}")
#def get_customer(idx: int):
    # Read the data from the CSV file
#    df = pd.read_csv("../customers.csv")
    # Filter the data based on the index
#    customer = df.iloc[idx]
    # Return the data as a dictionary
#    return customer.to_dict()

#@api.post("/get_payload")
#async def get_payload(request: Request):
#    response = await request.json()
    #num1 = response.get("num1")
    #num2 = response.get("num2")
    #sum = num1 + num2
    #return {"sum": sum}
    #geo = response.get("geo")
    #url = "https://maps.google.com/?q={geo}".format(geo=geo)
    # return await request.json()

# ------- data project 1
DBHOST = "ds2022.cqee4iwdcaph.us-east-1.rds.amazonaws.com"
DBUSER = "admin"
DBPASS = os.getenv('DBPASS')
DB = "dkh8my"

db = mysql.connector.connect(user=DBUSER, host=DBHOST, password=DBPASS, database=DB)
cur=db.cursor()

# ---------------

@api.get('/genres')
def get_genres():
    query = "SELECT * FROM genres ORDER BY genreid;"
    try:    
        cur.execute(query)
        headers=[x[0] for x in cur.description]
        results = cur.fetchall()
        json_data=[]
        for result in results:
            json_data.append(dict(zip(headers,result)))
        return(json_data)
    except Error as e:
        print("MySQL Error: ", str(e))
        return None
    cur.close()

@api.get('/songs')
def get_songs():
    query = """SELECT songs.title, songs.album, songs.artist, songs.year, songs.file, songs.image,
           genres.genre 
           FROM songs JOIN genres ON songs.genre = genres.genreid;"""
    try:    
        cur.execute(query)
        headers=[x[0] for x in cur.description]
        results = cur.fetchall()
        json_data=[]
        for result in results:
            json_data.append(dict(zip(headers,result)))
        return(json_data)
    except Error as e:
        print("MySQL Error: ", str(e))
        return None
    cur.close()