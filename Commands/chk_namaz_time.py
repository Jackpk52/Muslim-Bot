import discord
from discord.ext import commands

class CheckNamazTimeCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.reminder_system = None

    def set_reminder_system(self, reminder_system):
        self.reminder_system = reminder_system

    @commands.command(name='chk-namaz-time')
    async def check_namaz_time(self, ctx):
        """Check if it's time for prayer in your region"""
        
        user_id = str(ctx.author.id)
        result = await self.reminder_system.check_namaz_time(user_id)
        
        embed = discord.Embed(
            title="🕌 Prayer Time Check",
            description=result,
            color=0x2ecc71
        )
        
        await ctx.send(embed=embed)