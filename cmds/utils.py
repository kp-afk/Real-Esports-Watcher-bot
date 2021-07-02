import discord
from discord.ext import commands
import variables
import random
import os
import pymongo
from pymongo import MongoClient

mongodb_credentials = os.getenv('mongodb')
cluster = MongoClient(mongodb_credentials)
db = cluster["Real_Esports_Bot"]
collection = db["countr"]

def randomc():
      chance = random.randint(0, 100) 
      if chance <= 10:
        randomcolour = 0x800080 #purple
        return randomcolour
      elif chance <= 20:
        randomcolour = 0xFFFF00 #yellow
        return randomcolour
      elif chance <= 30:
        randomcolour = 0x00FFFF #cyan
        return randomcolour
      elif chance <= 40:
        randomcolour = 0xFF0000 #red
        return randomcolour
      elif chance <= 50:
        randomcolour = 0xFFFFFF # white
        return randomcolour
      else:
        randomcolour = 0x00FF00 #green
        return randomcolour

async def update_confirm_teams(ctx, user, *arg1):
  query = {"_id" : "teamcounter"}
  doc = collection.find(query)
  for result in doc:
    score = result["counter"]
  score = score + 1
  collection.update_one({"_id": "teamcounter"},{"$set": {"counter": score}},)
  return score
