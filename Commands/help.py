import discord
from discord.ext import commands

class HelpCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='help')
    async def help_command(self, ctx):
        """Show all available Islamic commands"""
        embed = discord.Embed(
            title="🕌 Muslim Bot - Islamic Commands",
            description="**Assalamu Alaikum!** Here are all available Islamic commands:",
            color=0x3498db
        )
        
        commands_list = {
            "!convert": "Learn how to become Muslim",
            "!set-region <city> <country>": "Set your location for prayer times",
            "!chk-weather": "Check weather in your region", 
            "!chk-namaz-time": "Check if it's prayer time",
            "!ping": "Check bot responsiveness",
            "!info": "Show bot information",
            "!test": "Test if bot is working",
            "!help": "Show this help menu"
        }
        
        for cmd, desc in commands_list.items():
            embed.add_field(name=cmd, value=desc, inline=False)
        
        embed.set_footer(text="May Allah accept our deeds 🤲")
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(HelpCommand(bot))