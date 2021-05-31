import discord
from discord.ext import commands

client = commands.Bot(command_prefix = ".")

@client.command()
async def role(ctx, member: discord.Member = None, *, role_name = None):
    if member is None:
        await ctx.send("Mention a member")
        return
    if role_name is None:
        await ctx.send("Make sure you type in the name of the role")
        return
    

    try:
        role = await commands.RoleConverter().convert(ctx, argument = role_name)
    except commands.ConversionError:
        await ctx.send("Make sure you type the role name correctly")
        return
    except commands.RoleNotFound:
        await ctx.send("Make sure you type the role name correctly, its case sensitive")
        return
    
    if member in role.members:
        await member.remove_roles(role)
        await ctx.send(f"{role.name} has been removed from {member.mention}")
        return
    await member.add_roles(role)
    await ctx.send(f"{role.name} has been added to {member.mention}")

client.run("TOKEN")