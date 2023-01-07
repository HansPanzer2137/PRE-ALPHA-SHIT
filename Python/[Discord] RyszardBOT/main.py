# IMPORT DISCORD.PY. ALLOWS ACCESS TO DISCORD'S API.
import discord

# GETS THE CLIENT OBJECT FROM DISCORD.PY. CLIENT IS SYNONYMOUS WITH BOT.
intents = discord.Intents.all()
bot = discord.Client(intents=intents)

# EVENT LISTENER FOR WHEN THE BOT HAS SWITCHED FROM OFFLINE TO ONLINE.
@bot.event
async def on_ready():
	# CREATES A COUNTER TO KEEP TRACK OF HOW MANY GUILDS / SERVERS THE BOT IS CONNECTED TO.
	guild_count = 0

	# LOOPS THROUGH ALL THE GUILD / SERVERS THAT THE BOT IS ASSOCIATED WITH.
	for guild in bot.guilds:
		# PRINT THE SERVER'S ID AND NAME.
		print(f"- {guild.id} (name: {guild.name})")

		# INCREMENTS THE GUILD COUNTER.
		guild_count = guild_count + 1

	# PRINTS HOW MANY GUILDS / SERVERS THE BOT IS IN.
	print("SampleDiscordBot is in " + str(guild_count) + " guilds.")

# EVENT LISTENER FOR WHEN A NEW MESSAGE IS SENT TO A CHANNEL.
@bot.event
async def on_message(message):
	# CHECKS IF THE MESSAGE THAT WAS SENT IS EQUAL TO "HELLO".
    if message.content == "hitler nie wiedzial":
        print("ale pedal")
        await message.channel.send("Więc jeszcze raz mówię, nic takiego nie robię. Po prostu nie ma żadnego dowodu, czy Hitler wiedział o holokauście, czy nie wiedział. Jeżeli ktoś miałby taki dowód, to jest nagroda 175 tysięcy funtów za taki dowód, niech zatem leci do Londynu i odbiera nagrodę.Takiego dowodu nie ma, a ponieważ sądy nie skazują ludzi bez dowodów, na podstawie pomówień, to niestety istnieje bardzo poważne przypuszczenie, że świętej pamięci Himmler nie raczył poinformować Hitlera o tym, że urządza holokaust, i tyle.")
    if message.content=="Stekus":
        print("We has got him")
        await message.channel.send(
            "Stekus is wanted by CIA and FBI by folowing acts\n-Child Abusement\n-Murder of approximately 60 people (including 40 children)\n-Possession and distribution of illegal files(CP, GORE)\nParticipation in organized criminal structures (al-Qaeda, Wagner group)\nWarcrimes on Ukraine territory during Russia-Ukraine war\nSupporting Russian power in the Kremlin, helping Vladimir Vladimirovich Putin in planning an attack on civilian structures/entities \n\nhttps://media.discordapp.net/attachments/992389207257522326/1060967391082860635/wanted.jpg?width=845&height=222"
        )


# EXECUTES THE BOT WITH THE SPECIFIED TOKEN. TOKEN HAS BEEN REMOVED AND USED JUST AS AN EXAMPLE.
bot.run("")
print(discord.Intents.message_content in discord.Intents.default())