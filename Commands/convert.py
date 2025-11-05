import discord
from discord.ext import commands

class ConvertCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='convert')
    async def convert_to_islam(self, ctx):
        """Guide someone to convert to Islam"""
        shahada = "**Ash-hadu an la ilaha illa Allah, wa ash-hadu anna Muhammadan rasulu Allah**"
        meaning = "*I bear witness that there is no god but Allah, and I bear witness that Muhammad is the Messenger of Allah*"
        
        embed = discord.Embed(
            title="🕋 Shahada - Declaration of Faith",
            description="To become Muslim, sincerely say:",
            color=0x2ecc71
        )
        
        embed.add_field(name="Arabic", value=shahada, inline=False)
        embed.add_field(name="English Meaning", value=meaning, inline=False)
        embed.add_field(
            name="Steps to Convert", 
            value="1. Believe in your heart\n2. Say the Shahada sincerely\n3. Learn to pray\n4. Continue learning Islam", 
            inline=False
        )
        
        embed.add_field(
            name="Welcome Message",
            value="**Assalamu Alaikum!** Welcome to Islam, brother/sister! May Allah guide and bless you.",
            inline=False
        )
        
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(ConvertCommand(bot))