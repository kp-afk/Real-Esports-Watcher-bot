import discord
from discord.ext import commands
import variables
import random
import os
import pymongo
from pymongo import MongoClient
import smtplib, ssl
import datetime
from datetime import datetime, timedelta
import os


mongodb_credentials = os.getenv('mongodb')
cluster = MongoClient(mongodb_credentials)
db = cluster["Real_Esports_Bot"]
collection = db["countr"]

# Returns a colour with a set chance 
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

# send team names with user to the channel
async def update_confirm_teams(ctx, user, *arg1):
  query = {"_id" : "teamcounter"}
  doc = collection.find(query)
  for result in doc:
    score = result["counter"]
  score = score + 1
  collection.update_one({"_id": "teamcounter"},{"$set": {"counter": score}},)
  return score

# returns random emote
def randomemote():
  opemotes = ["<a:yessad:738983674242007140> ",
              "<a:verify:742940239403941930> ",
              "<a:verifykr:763258119169900574> ",
              "<:ATD_vortexScam:801698916373495819> ",
              "<a:tik:746576569652346890> ",
              "<a:emoji_7:790546540217237514> ",
              "<a:safetik:781344436872675339> ",
              "<a:brxpurple:836960052358676480>",
              "<a:op16:789552412260171777> ",
              "<a:yhh:743698122362060810> " ]
  random_emote = random.choice(opemotes)
  return random_emote

def addnewuserinfraction(message):
# ----------------------------------------
  mongodb_credentials = os.getenv('mongodb')
  cluster = MongoClient(mongodb_credentials)
  db = cluster["Real_Esports_Bot"]
  collection = db["watcher_bot_v2"]
# ----------------------------------------
  
  
  post = {
                    "_id": message.author.id,
                    "rajumentions": 1,
                    "name": message.author.name,
                    "time": datetime.now()
        }
  collection.insert_one(post)

def adduserinfraction(message):
# ----------------------------------------
  mongodb_credentials = os.getenv('mongodb')
  cluster = MongoClient(mongodb_credentials)
  db = cluster["Real_Esports_Bot"]
  collection = db["watcher_bot_v2"]
# ----------------------------------------

  query = {"_id": message.author.id}
  user = collection.find(query)
  for result in user:
    score = result["rajumentions"]
  score = score + 1
  collection.update_one(
                    {"_id": message.author.id},
                    {"$set": {
                        "rajumentions": score
                    }},
                )
  collection.update_one(query,
                                      {"$set": {
                                          "time": datetime.now()
                                      }})

 






  