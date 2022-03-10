# Imports
# May require you to install: discord.py, python-dotenv, dotenv, promise
import os
import discord
import re
import asyncio
import random
import subprocess
from time import sleep
from discord.ext import commands
from threading import Thread


with open("/tmp/token.env", "r") as file:
    # Env token loading
    TOKEN = file.readline()

os.remove("/tmp/token.env")

# Bot Strings
prefix = "ms!"

# client = discord.Client()
client = commands.Bot(command_prefix=prefix)
# client.add_cog("test")


@client.event
async def on_ready():
    print(f"{client.user} has connected to Discord!")
    await client.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching, name="for ms!help to list commands!"
        )
    )


# Ping Command - see if bot is currently alive
@client.command(
    brief="Check bot latency",
    description="The bot pings the server to check response time. The lower, the faster the response.",
    commands_heading="Tools",
)
async def ping(ctx):
    await ctx.send(
        f"{ctx.message.author.mention}, pong! `({round(client.latency*1000)}ms)`"
    )


# Test
@client.command(
    brief="Perform math calculations",
    description="Send the bot an equation for it to be performed. First argument must be operator (*, /, + or -) and second two arguments must be numbers. Example:\nms!calc + 1 5",
    commands_heading="Tools",
)
async def calc(ctx):
    args = ctx.message.content.split(" ")
    try:
        if args[1] == "*":
            await ctx.send(str(int(args[2]) * int(args[3])))
        elif args[1] == "/":
            await ctx.send(str(int(args[2]) / int(args[3])))
        elif args[1] == "+":
            await ctx.send(str(int(args[2]) + int(args[3])))
        elif args[1] == "-":
            await ctx.send(str(int(args[2]) - int(args[3])))
        else:
            await ctx.send("Invalid operator detected!")
    except Exception as err:
        await ctx.send("EXCEPTION RAISED: " + str(err))


@client.command(
    brief="Randomly selects famous monkey quotes.",
    description="Chooses a famous quote said by a monkey at random from a premade database.",
    commands_heading="Tools",
)
async def quotes(ctx):
    quoteList = [
        '"Give orange me give eat orange me eat give me eat give me eat orange give me you."\n-Nim.',
        '"NOOO!"\n-Caesar.',
        '"Give orange me give eat orange me eat give me eat give me eat orange give me you."\n-Nim.',
        '"You are right, I have always known about man. From the evidence, I believe his wisdom must walk hand and hand with his idiocy. His emotions must rule his brain. He must be a warlike creature who gives battle to everything around him, even himself."\n-Dr. Zaius.',
        '"Apes together strong."\n-Caesar.',
        "\"Beware the beast Man, for he is the Devil's pawn. Alone among God's primates, he kills for sport, or lust or greed. Yea, he will murder his brother to possess his brother's land. Let him not breed in great numbers, for he will make a desert of his home and yours. Shun him. Drive him back into his jungle liar, for he is the harbinger of death.\"\n-Cornelius.",
        '"Enough! From humans, Koba learned hate. But nothing else."\n-Caesar.',
        "\"I've never known any problem that couldn't be solved with a little nap.\"\n-Donkey Kong.",
        '"If you beat me, I will go. If not, then it is you who must leave - without your pants!."\n-Monkey.',
        '"Help Earth. Hurry!"\n-Koko.',
        '"ONE EGG LEFT?! For a nutritious breakfast, TWO eggs is the minimum requirement!"\n-Mojo Jojo.',
        '"I must remember to destroy those kids after my breakfast has been eaten."\n-Mojo Jojo.',
        '"Apes not kill apes."\n-Koba.',
        '"Betcha won\'t get much further than this..."\n-Cranky Kong.',
        '"So you found me, did ya?! What do you want?!"\n-Cranky Kong.',
        '"I\'m bailing out, dudes!"\n-Funky Kong.',
        "\"Lookin' good, Kongs! Belt up. Blast off. You're outta sight!\"\n-Funky Kong.",
    ]
    selectedQuote = random.choice(quoteList)
    await ctx.send(f"```{selectedQuote}```")


@client.command(
    brief="Play rock, paper, scissors with me!",
    description="By using 'ms!rps <option>', you can play RPS against me. Your options are rock, paper or scissors.",
    commands_heading="Tools",
)
async def rps(ctx):
    options = ["rock", "paper", "scissors"]
    monkeysee = random.choice(options)
    opponent = ctx.message.content.split("ms!rps ")[1].strip().lower()

    output = ""

    if (
        opponent == "gun"
        or opponent == "shoot"
        or opponent == "stab"
        or opponent == "shank"
    ):
        output = "https://cdn.discordapp.com/attachments/757138782167236648/948734039328686130/arrrgghhhh.mp4"

    elif opponent == monkeysee:
        output = "A draw?! You won't win the next one!"

    elif (
        (opponent == "rock" and monkeysee == "scissors")
        or (opponent == "scissors" and monkeysee == "paper")
        or (opponent == "paper" and monkeysee == "rock")
    ):
        output = "I lost?! You've must cheated - I demand a rematch!"

    elif (
        (monkeysee == "rock" and opponent == "scissors")
        or (monkeysee == "scissors" and opponent == "paper")
        or (monkeysee == "paper" and opponent == "rock")
    ):
        output = "Of course I won. You can't possibly win against me."

    else:
        output = "What were you trying to accomplish?"

    await ctx.send(f"{output}")


@client.command(brief="???", description="???", commands_heading="Tools")
async def flag(ctx):
    await ctx.send("mookeyCTF{1t_s4ys_gu11ibl3_0n_th3_cei1ing!}")


# Command that is vulnerable to CLI injection
@client.command(
    brief="Repeats text given to it",
    description="Using state-of-the-art cowsay technology, the bot will send you a text file back with a funny monkey repeating what you said. Example:\nms!monkeydo Hello, World!",
    commands_heading="Tools",
)
async def monkeydo(ctx):
    global prefix
    args = ctx.message.content.split("ms!monkeydo ")
    try:
        args[1]
    except:
        await ctx.send("Not enough arguments!")
        return 0

    for x in [">", "<", "%"]:
        args[1] = args[1].replace(x, "")

    # runCommand = str(f'printf {(args[1])} > /tmp/{args[2]}.txt')
    # print(runCommand)
    print(str(args[1]))
    # TRY TO MAKE RAW
    # Need to bring a monkey.cow file into /usr/share/cowsay/cows
    try:
        open("/tmp/output.txt", "x")
    except FileExistsError:
        pass
    vuln = str(args[1])
    if vuln[0] == '"':
        vuln = " " + vuln
    lister = [f'/usr/games/cowsay -f monkey "{vuln}" > /tmp/output.txt']
    remove = ['echo "" > /tmp/output.txt']
    lister[0] = lister[0].replace(r"\\", r"\0".replace("0", ""))
    print(lister)
    subprocess.call(lister, shell=True)
    await ctx.send(file=discord.File("/tmp/output.txt"))
    subprocess.call(remove, shell=True)


client.run(TOKEN)
