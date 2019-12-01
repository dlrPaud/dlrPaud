import asyncio

import discord

client = discord.Client()
@client.event
async def on_member_join(member):
    await member.send("--------------------------------------")
    await member.send("**Welcome! to our server**\nwatch our guide video\n https://youtu.be/a_1E0yctOxE ")
    await member.send("*check our #guide-bot-system text channel*")


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("SCUM -skeleton server-")
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    id = client.get_guild(619565463386456065)

    if message.content.startswith("!members"):
        await message.channel.send(f"""number of Members: {id.member_count}""")

    if message.content.startswith("!server"):
        embed = discord.Embed(title="NEW SKELETON ISLAND!", description="45.35.136.226:28202", color=0x00ff00)
        embed.set_footer(text="have fun playing!")
        await message.channel.send(embed=embed)

    if message.content.startswith('!commands'):
        embed = discord.Embed(title="skeleton server commands", description="*use it in server*", color=0x6A97D7)
        embed.add_field(name="!discord", value="shows discord link", inline=False)
        embed.add_field(name="!bank", value="shows your bitscum", inline=False)
        embed.add_field(name="!kd", value="shows your kd", inline=False)
        embed.add_field(name="!ranking", value="shows your ranking", inline=False)
        embed.add_field(name="!online", value="shows number of players online", inline=False)
        await message.channel.send(embed=embed)

    if message.content.startswith('!list'):
        embed = discord.Embed(title="known problems and solutions", description="scum server", color=0x6A97D7)
        embed.add_field(name="**getting kicked out of server**", value="trying restarting steam or scum", inline=False)
        embed.add_field(name="**i bought stuff but its not coming**", value="bot might be offline OR wait", inline=False)
        embed.add_field(name="**it says im offline!**", value="server needs to restart dm @sdu342 or admin", inline=False)
        embed.add_field(name="**if you still need help contact admins**", value="sorry!", inline=False)
        await message.channel.send(embed=embed)

    if message.content.find('help') != -1 and message.content.find("any")==-1 and message.content.find("do")==-1:
        await message.channel.send("are you having problem? watch our tutorial video in #rule")
        await asyncio.sleep(2)
        await message.channel.send("If your problem isn't solved  **type !list**")

    if message.content.find("kit") != -1 and message.content.find("not") != -1 or message.content.find("starter kit") != -1 and message.content.find("need") != -1:
        await message.channel.send("did you write !kit on #starter-kit?")

    if message.content.find("bot") != -1 and message.content.find("not") != -1 or message.content.find("bot") != -1 and message.content.find("work") != -1:
        await message.channel.send("do you think bots aren't working? DM @sdu342 to restart the bot")
        await message.channel.send("sorry for inconvenient")

    if message.content.startswith('!kit'):
        await message.channel.send("type !kit in #starter-kit")

    if message.content.find("car") != -1 and message.content.find("spawn") != -1:
        await message.channel.send("vehicles don't spawn in this server you need to buy it on Eshop")

    if message.content.find("you") != -1 and message.content.find("offline") != -1 or message.content.find("i") != -1and message.content.find("offline") != -1:
        await message.channel.send("Bot need reboot DM @sdu")
        await message.channel.send("sorry for inconvenient")


client.run("NjQ3Nzc0NTc1NDY3Mjk4ODE2.Xdkl9w.XxEeHAkIV6NHGcCGN_RPv7GhqZI")
