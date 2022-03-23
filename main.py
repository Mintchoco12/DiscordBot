import hikari
import lightbulb
import random
import requests
import json
import os

bot = lightbulb.BotApp(
    token=os.getenv("TOKEN"), 
    default_enabled_guilds=(os.getenv("GUILD")))


@bot.listen(hikari.StartedEvent)
async def on_started(event):    
    print("Bot has started")

@bot.command
@lightbulb.command("coinflip", "Simple coinflip")
@lightbulb.implements(lightbulb.SlashCommand)
async def coinflip(ctx):
    rnd = random.randint(1, 2)
    cf = None
    if rnd == 1:
        cf = "Heads"
    elif rnd == 2:
        cf = "Tails"

    await ctx.respond(cf)

@bot.command
@lightbulb.command("game", "chooses a random game to play")
@lightbulb.implements(lightbulb.SlashCommand)
async def game(ctx):
    games = ["Valorant", "Overcooked", "Rainbow Six Siege", "Skribble", "Escape Simulator", "Counter Strike: Global Offensive", "Apex Legends", "Codenames"]
    rnd = random.randint(0, len(games))

    await ctx.respond(games[rnd])

@bot.command
@lightbulb.command("simp", "simping command")
@lightbulb.implements(lightbulb.SlashCommand)
async def simp(ctx):
    apikey = os.getenv("APIKEY")
    limit = 50
    searchTerm = ["Wonyoung", "Chaewon", "Yena", "Yuri", "Minju", "IU", "Sana", "Dahyun", "Jeongyeon", "Tzuyu", "Nayeon", "Momo Twice", "Mina", "Dahyun", "Jihyo", "Chaeyoung", "Taeyeon", "Yihyun", "Yuna", "Ryujin"]
    rnd = random.randint(0, len(searchTerm))

    r = requests.get("https://api.tenor.com/v1/anonid?key=%s" % apikey)
    anonId = json.loads(r.content) ["anon_id"]
   
    r = requests.get("https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s&anon_id=%s" % (searchTerm[rnd], apikey, limit, anonId))

    gif = json.loads(r.content)
    rnd = random.randint(0, limit - 1)
    url = gif["results"][rnd]["media"][0]["gif"]["url"]

    await ctx.respond(url)

@bot.command
@lightbulb.command("valo", "all commands valorant related")
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def valorant(ctx):
    pass

@valorant.child
@lightbulb.command("gamemode", "chooses either ranked or unrated")
@lightbulb.implements(lightbulb.SlashSubCommand)
async def gamemode(ctx):
    gamemodeRnd = random.randint(1, 2)
    gm = None

    if gamemodeRnd == 1:
        gm = "Ranked"
    elif gamemodeRnd == 2:
        gm = "Unrated"
            
    await ctx.respond(gm)

@valorant.child
@lightbulb.command("agent", "randomly chooses an agent")
@lightbulb.implements(lightbulb.SlashSubCommand)
async def agent(ctx):
    agents = ["Astra", "Breach", "Brimstone", "Chamber", "Cypher", "Jett", "Kay/O", "Killjoy", "Neon", "Omen", "Phoenix", "Raze", "Reyna", "Sage", "Skye", "Sova", "Viper", "Yoru"]
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