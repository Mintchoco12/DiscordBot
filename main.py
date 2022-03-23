import hikari
import lightbulb
import random
import requests
import json
import os

#Token & Guilds
bot = lightbulb.BotApp(
    token=os.getenv("TOKEN"), 
    default_enabled_guilds=(os.getenv("GUILD")))

#Start event
@bot.listen(hikari.StartedEvent)
async def on_started(event):    
    print("Bot has started")

#Coinflip command
@bot.command
@lightbulb.command("coinflip", "Simple coinflip")
@lightbulb.implements(lightbulb.SlashCommand)
async def coinflip(ctx):
    #Random number generator
    rnd = random.randint(1, 2)
    cf = None
  
    if rnd == 1:
        cf = "Heads"
    elif rnd == 2:
        cf = "Tails"

    await ctx.respond(cf)

#Chooses a random game
@bot.command
@lightbulb.command("game", "chooses a random game to play")
@lightbulb.implements(lightbulb.SlashCommand)
async def game(ctx):
    #Games list
    games = ["Valorant", "Overcooked", "Rainbow Six Siege", "Skribble", "Escape Simulator", "Counter Strike: Global Offensive", "Apex Legends", "Codenames"]
    #Random number generator
    rnd = random.randint(0, len(games))

    await ctx.respond(games[rnd])

#Sends a random gif from tenor
@bot.command
@lightbulb.command("simp", "simping command")
@lightbulb.implements(lightbulb.SlashCommand)
async def simp(ctx):
    apikey = os.getenv("APIKEY")  #Apikey
    limit = 50  #Amount of gif resuslts
    #searchTerm list
    searchTerm = ["Wonyoung", "Chaewon", "Yena", "Yuri", "Minju", "IU", "Sana", "Dahyun", "Jeongyeon", "Tzuyu", "Nayeon", "Momo Twice", "Mina", "Dahyun", "Jihyo", "Chaeyoung", "Taeyeon", "Yihyun", "Yuna", "Ryujin"]
    #Random number generator
    rnd = random.randint(0, len(searchTerm))

    #Gets the anon id
    r = requests.get("https://api.tenor.com/v1/anonid?key=%s" % apikey)
    anonId = json.loads(r.content) ["anon_id"]

    #Gets a limited amount of gifs
    r = requests.get("https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s&anon_id=%s" % (searchTerm[rnd], apikey, limit, anonId))

    gif = json.loads(r.content)
    rnd = random.randint(0, limit - 1)
    url = gif["results"][rnd]["media"][0]["gif"]["url"]

    await ctx.respond(url)

#Valorant parent
@bot.command
@lightbulb.command("valo", "all commands valorant related")
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def valorant(ctx):
    pass


#Chooses between Ranked & Unrated
@valorant.child
@lightbulb.command("gamemode", "chooses either ranked or unrated")
@lightbulb.implements(lightbulb.SlashSubCommand)
async def gamemode(ctx):
    #Random number generator
    gamemodeRnd = random.randint(1, 2)
    gm = None

    if gamemodeRnd == 1:
        gm = "Ranked"
    elif gamemodeRnd == 2:
        gm = "Unrated"
            
    await ctx.respond(gm)

#Chooses a random agent to play
@valorant.child
@lightbulb.command("agent", "randomly chooses an agent")
@lightbulb.implements(lightbulb.SlashSubCommand)
async def agent(ctx):
    #Agent list
    agents = ["Astra", "Breach", "Brimstone", "Chamber", "Cypher", "Jett", "Kay/O", "Killjoy", "Neon", "Omen", "Phoenix", "Raze", "Reyna", "Sage", "Skye", "Sova", "Viper", "Yoru"]
    #Random number generator 
    rnd = random.randint(0, len(agents))

    await ctx.respond(agents[rnd])

# @bot.command
# @lightbulb.option("teams", "amount of teams", type=int)
# @lightbulb.option("players", "amount of players", type=int)
# @lightbulb.command("createteam", "creates random teams")
# @lightbulb.implements(lightbulb.SlashCommand)
# async def create_team(ctx):
#     await ctx.respond(ctx.options.teams + ctx.options.players)

bot.run()