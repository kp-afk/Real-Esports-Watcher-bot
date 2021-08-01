import discord
from discord.ext import commands, tasks
import pymongo
from pymongo import MongoClient
import variables
import asyncio
import datetime
from datetime import datetime, timedelta
import os
from cmds import utils

mongodb_credentials = os.getenv('mongodb')
cluster = MongoClient(mongodb_credentials)
db = cluster["Real_Esports_Bot"]
collection = db["watcher_bot_v2"]


class antiping(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
    # -----------------------------------------------------------------------------------------
        guild = self.client.guilds[0]
        content_creator_role = guild.get_role(706016926475747349)
        raju = self.client.get_user(788868444325543977)
        chiripto = self.client.get_user(511965562457423902)
        rajoo = self.client.get_user(550948377148522498)
    # -----------------------------------------------------------------------------------------
        if raju.mentioned_in(message) or chiripto.mentioned_in(message) or rajoo.mentioned_in(message) and not message.author.bot:

            myquery = {"_id": message.author.id}
            if (collection.count_documents(myquery) == 0):

                utils.addnewuserinfraction(message)

                if not message.author.guild_permissions.view_audit_log and content_creator_role not in message.author.roles:
                    await message.reply(content=
                        "Don't mention the server owner again! \nWait for response from <@&746822303584878672> ",
                        mention_author=False)
                else:
                    return

            else:
                utils.adduserinfraction(message)

                if not message.author.guild_permissions.view_audit_log and content_creator_role not in message.author.roles:
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
                            }}, {"$set": {
                                "time": datetime.now()
                            }})

                        await message.author.remove_roles(muterole,
                                                          reason="Time over!",
                                                          atomic=True)

                    else:
                        await message.reply(content=
                            "Don't mention the server owner again! \nWait for response from <@&746822303584878672> ",
                            mention_author=False)

                else:
                    return
        else:
            return

    @tasks.loop(seconds=2)
    async def autodeleter():
        for x in collection.find({}, {"_id": 0, "rajumentions": 0, "name": 0}):
            y = x.get("time")
            z = datetime.now() - timedelta(hours=8)
            if y < z:
                myquery = {"time": y}
                opbolte = collection.find_one(myquery)
                name = opbolte.get("name")
                collection.delete_one(myquery)
                print(f"Document for {name} deleted (time over)")

            else:
                pass
    autodeleter.start()

    
        

def setup(client):
    client.add_cog(antiping(client))
