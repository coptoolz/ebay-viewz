import discord
from discord.ext import commands
import requests
from random import randint
import random
import time
import os
import asyncio
import aiohttp



headers1 = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
    }

access_token= os.environ["BOT_TOKEN"]
requests.packages.urllib3.disable_warnings()



TOKEN = access_token
client = discord.Client()

if __name__ == '__main__':
    def main():
        @client.event
        async def on_message(message):
            if message.content.startswith('!ebay'):
                old = message.content
                link = old.replace("!ebay", "").strip()
                embed = discord.Embed(title="Started!", description="Please wait 3 minutes... <:ebay:533696455534444556>", color=0x00ff00)
                await client.send_message(message.channel, embed=embed)
                await views(link)

                await asyncio.sleep(1)
                embed = discord.Embed(title="I've just made 50 views on your item!", description="<:ebay:533696455534444556>", color=0x00ff00)
                await client.send_message(message.channel, embed=embed)
                print("Done")
            if message.content == ('?ebay'):
                embed = discord.Embed(title="Online!", description ="<:ebay:533696455534444556>", color=0x00ff00)
                await client.send_message(message.channel, embed=embed)


async def views(link):
    print("Started")
    for i in range(50):
        async with aiohttp.get(url=link):
            print("Viewed")
    
        
      
main()



@client.event
async def on_ready():
    print("Ready!")
    print(client.user.name)
    print(client.user.id)
    print('------')
    


while True:
    client.run(TOKEN)
