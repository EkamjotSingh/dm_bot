import discord
from discord.ext import commands
from discord.ext.commands import Bot

client = commands.Bot(command_prefix="d!")



@client.remove_command("help")

@client.event
async def on_ready():
	print("I am ready!")

@client.command()

async def send(ctx ,* , message : str):
	for member in ctx.guild.members:
		total = ctx.guild.members
		await member.send(message)
		await ctx.send(f"DM sent to {member} :white_check_mark:")
	await ctx.send('''
	Process Finished!
        Made by Ekamjot#9133''')

	            
			
			



client.run("NzM5MDYzODA2MTk3NzYwMDYz.XyVAzg.kuSRV3UTifJ6BKHm57NmwK4XByY")

