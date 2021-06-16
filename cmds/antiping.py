import discord
from discord.ext import commands
import pymongo
from pymongo import MongoClient
import variables
import asyncio
import datetime
from datetime import datetime, timedelta
import os

mongodb_credentials = os.getenv('mongodb')
cluster = MongoClient(mongodb_credentials)
db = cluster["Real_Esports_Bot"]
collection = db["watcher_bot_v2"]


class antiping(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):

        raju = self.client.get_user(788868444325543977)
        chiripto = self.client.get_user(511965562457423902)

        if raju.mentioned_in(message) or chiripto.mentioned_in(
                message) and message.author.bot == False:

            myquery = {"_id": message.author.id}
            if (collection.count_documents(myquery) == 0):
                post = {
                    "_id": message.author.id,
                    "rajumentions": 1,
                    "name": message.author.name,
                    "time": datetime.now()
                }
                collection.insert_one(post)
                if not message.author.guild_permissions.view_audit_log:
                    await message.reply(
                        "Don't mention the server owner again! \nWait for response from <@&746822303584878672> ",
                        mention_author=False)
                else:
                    return

            else:
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

                if not message.author.guild_permissions.view_audit_log:
                    userdocument = collection.find_one(
                        {"_id": message.author.id})
                    infractions_count = userdocument.get("rajumentions")
                    if infractions_count >= 3:
                        guild = self.client.guilds[0]
                        muterole = guild.get_role(variables.muterole)
                        await message.author.add_roles(
                            muterole,
                            reason=
                            f"{message.author.name} Muted for 10 mins (Pinging Owner)",
                            atomic=True)
                        await message.channel.send(
                            f"{message.author.mention} Muted from the Text for 10 Minutes :zipper_mouth:"
                        )
                        await asyncio.sleep(600)
                        query = {"_id": message.author.id}
                        user = collection.find(query)
                        for result in user:
                            score = result["rajumentions"]
                        score = score - 2
                        collection.update_one(
                            {"_id": message.author.id},
                            {"$set": {
                                "rajumentions": score
                            }},
                        )

                        await message.author.remove_roles(muterole,
                                                          reason="Time over!",
                                                          atomic=True)

                    else:
                        await message.reply(
                            "Don't mention the server owner again! \nWait for response from <@&746822303584878672> ",
                            mention_author=False)

                else:
                    return
        else:
            return


def setup(client):
    client.add_cog(antiping(client))
