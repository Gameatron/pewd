import discord
from discord.ext import commands
from discord.utils import get

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_member_join(self, ctx):
        channel = get(ctx.guild.channels, name="welcome")
        await channel.send(f"Welcome dumdum ({ctx.mention}), this is a new server and it is still in construction. If you stay you will be part if a great disfunctional disc family, and if you leave ur a fag. Now introduce yourself")
    
def setup(bot):
    bot.add_cog(Events(bot))