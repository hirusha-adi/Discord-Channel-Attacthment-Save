import os

import discord
import random
from string import ascii_lowercase
from discord.ext import commands

client = commands.Bot(command_prefix=".")


@client.event
async def on_ready():
    print(f"[+] Logged in as {client.user.name}")
    print("[+] Bot is online and ready to be used!")


@client.event
async def on_message(message):
    if client.user == message.author:
        return
    await client.process_commands(message)


@client.command()
async def save(ctx, limit=None):
    if limit == None:
        limit = 9999

    print(
        f"+ Starting to save {limit} messages in {ctx.channel.name} | {ctx.channel.id}")

    iter = 1
    async for message in ctx.channel.history(limit=int(limit)):
        all_attatchments = message.attachments
        if all_attatchments:
            iter_2 = 1
            for attachment in all_attatchments:
                try:
                    if str(attachment.filename) in os.getcwd():
                        extension = str(attachment.filename).split(".")[-1]
                        save_f_name = f"{attachment.filename}.{''.join(random.choice(ascii_lowercase) for x in range(4))}.{extension}"
                    else:
                        save_f_name = str(attachment.filename)

                    await attachment.save(save_f_name)

                    print(
                        f"+ Saved attachment: {iter}-{iter_2} | {save_f_name}")
                except Exception as e:
                    print(
                        f"! Failed to save attatchment {iter}-{iter_2}.\n! Error: {e}")
                iter_2 += 1
            iter_2 = 1
        else:
            with open(f"{iter}.txt", "w", encoding="utf-8") as ftext:
                ftext.write(str(message.content))
            print(f"+ Saved message: {iter}")
        iter += 1


with open("token.txt", "r", encoding="utf-8") as tokenfile:
    token = tokenfile.read()

client.run(token)
