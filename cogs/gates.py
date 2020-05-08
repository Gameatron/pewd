import discord
from discord.ext import commands
from discord.utils import get as discget

class Gate(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.admins = (334393879258202113, 653983428785733652, 494175763541786634)

    @commands.command()
    async def accept(self, ctx, user:discord.Member):
        await ctx.message.delete()
        role = discget(ctx.guild.roles, id=708176852925284396)
        channel = discget(ctx.guild.channels, id=708171327848185896)
        if ctx.author.id in self.admins:
            await user.add_roles(role)
            await channel.send(f"{user.mention} has been accepted. Welcome.")
        else:
            await ctx.send("You do not have the permission to use this command", delete_after=5)
        
def setup(bot):
    bot.add_cog(Gate(bot))