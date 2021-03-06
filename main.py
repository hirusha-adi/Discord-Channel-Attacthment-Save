import os
import random
import sys
import json
from string import ascii_lowercase
from datetime import datetime

import discord
from discord.ext import commands

if ("config.json" in os.listdir(os.getcwd())):
    with open(os.path.join(os.getcwd(), "config.json"), "r", encoding="utf-8") as jsonfile:
        datajson = json.load(jsonfile)
        prefix = datajson["prefix"]
        token = datajson["token"]
else:
    datajson = None

if datajson is None:
    if ("prefix.txt" in os.listdir(os.getcwd())):
        with open(os.path.join(os.getcwd(), "prefix.txt"), "r", encoding="utf-8") as prefixfile:
            prefix = prefixfile.read()
    else:
        prefix = '.'

    if ("token.txt" in os.listdir(os.getcwd())):
        with open("token.txt", "r", encoding="utf-8") as tokenfile:
            token = tokenfile.read()
    else:
        token = None


client = commands.Bot(command_prefix=prefix)

client.remove_command('help')


@client.event
async def on_ready():
    print(
        f"[+] Logged in!\n\tName: {client.user.name}\n\tID: {client.user.id}\n\tPrefix: {prefix}")
    print("[+] Bot is online and ready to be used!")


@client.event
async def on_message(message):
    if client.user == message.author:
        return
    await client.process_commands(message)


@client.command()
async def help(ctx):
    print("[+] Invoked `help` command")
    embed = discord.Embed(title="Discord Channel Saver",
                          url="https://hirusha-adi.github.io/Discord-Channel-Attacthment-Save",
                          description="Save all messages and attachments sent in a channel ",
                          color=0x00e1ff,
                          timestamp=datetime.utcnow()
                          )
    embed.set_author(name=f"{client.user.name}",
                     url="http://hirusha.xyz",
                     icon_url=f"{client.user.avatar_url}")
    embed.add_field(name=f"{prefix}save [limit=9999]",
                    value="Save all messages and attachments sent in the channel with the given limit. `limit` will default to 9999",
                    inline=False)
    embed.set_footer(text=f"Requested by {ctx.author.name}")
    await ctx.send(embed=embed)


@client.command()
async def save(ctx, limit=None):
    if limit == None:
        limit = 9999

    print(
        f"[!] Starting to save {limit} messages in {ctx.channel.name} | {ctx.channel.id}")

    iter = 1
    try:
        async for message in ctx.channel.history(limit=int(limit)):
            all_attatchments = message.attachments
            if all_attatchments:
                iter_2 = 1
                for attachment in all_attatchments:
                    try:
                        if str(attachment.filename) in os.listdir(os.getcwd()):
                            extension = str(attachment.filename).split(".")[-1]
                            save_f_name = f"{attachment.filename}.{''.join(random.choice(ascii_lowercase) for x in range(4))}.{extension}"
                        else:
                            save_f_name = str(attachment.filename)

                        await attachment.save(save_f_name)

                        print(
                            f"[+] Saved attachment: {iter}-{iter_2} | {save_f_name}")
                    except Exception as e:
                        print(
                            f"[-] Failed to save attatchment {iter}-{iter_2}.\n[-] Error: {e}")
                    iter_2 += 1
                iter_2 = 1

            else:
                with open(f"{iter}.txt", "w", encoding="utf-8") as ftext:
                    ftext.write(str(message.content))
                print(f"[+] Saved message: {iter} | {iter}.txt")

            iter += 1

        print(f"[+] Saved all attacthments and messages\n\tTo: {os.getcwd()}")
        await ctx.send(f"[+] Saved all attacthments and messages to `{os.getcwd()}`")

    except Exception as e:
        print(f"[-] Failed to run command\n[-] Error: {e}")
        await ctx.send(f"[+] Saved all attacthments and messages to ```{e}```")

if token is None:
    sys.exit("[-] Invalid bot token. Please refer the documentation")
else:
    client.run(token)
