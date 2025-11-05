import discord
from discord.ext import commands
import json

class SetRegionCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.reminder_system = None  # Will be set from main

    def set_reminder_system(self, reminder_system):
        self.reminder_system = reminder_system

    @commands.command(name='set-region')
    async def set_region(self, ctx, city: str, country: str = None):
        """Set your region for prayer times and weather"""
        
        if not country:
            await ctx.send("Please specify both city and country. Example: `!set-region Mecca Saudi Arabia`")
            return
        
        # Save user's region
        user_id = str(ctx.author.id)
        self.reminder_system.user_regions[user_id] = {
            'city': city,
            'country': country
        }
        self.reminder_system.save_user_regions()
        
        embed = discord.Embed(
            title="📍 Region Set Successfully",
            description=f"Your region has been set to:\n**{city}, {country}**",
            color=0x27ae60
        )
        
        embed.add_field(
            name="Prayer Times", 
            value="Now you can use `!chk-namaz-time` to check prayer times for your location.",
            inline=False
        )
        
        embed.add_field(
            name="Weather", 
            value="Use `!chk-weather` to check weather in your region.",
            inline=False
        )
        
        await ctx.send(embed=embed)