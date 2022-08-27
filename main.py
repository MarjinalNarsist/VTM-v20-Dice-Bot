# import discord
from discord.ext import commands
from dice_module import *
import os

client= commands.Bot(command_prefix="&")
bot_token= os.environ.get("DC_TOKEN")


@client.command()
async def r(context, dice, *args):
    user=context.message.author.display_name
    try:
        roll_result=roll(dice)
        result=calculate(roll_result, args)
        roll_reply=f"```Roller: {user} \nRoll Result: {roll_result} \nResult: {result}```"
        await context.message.channel.send(roll_reply)
    except ValueError:
        await context.message.channel.send("```Wrong command! Example:\n&r 5d10 7 sw ```")


@client.command()
async def c(context, *args):
    user = context.message.author.display_name
    try:
        if "reset" in args:
            reset_combat()
            await context.message.channel.send(f"```{user} cleared the order!```")
        else:
            order=combat(modifier=args[0], character=args[1])
            await context.message.channel.send(f"```{order}```")
    except ValueError:
        await context.message.channel.send("```Wrong command! Example:\n&c 4 antonio \nor\n&c reset```")


client.run(bot_token)