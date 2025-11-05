import discord
from discord.ext import commands
import aiohttp
import os

class CheckWeatherCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.reminder_system = None

    def set_reminder_system(self, reminder_system):
        self.reminder_system = reminder_system

    @commands.command(name='chk-weather')
    async def check_weather(self, ctx):
        """Check weather in your region"""
        
        user_id = str(ctx.author.id)
        if user_id not in self.reminder_system.user_regions:
            await ctx.send("Please set your region first using `!set-region <city> <country>`")
            return
        
        region = self.reminder_system.user_regions[user_id]
        api_key = os.getenv('WEATHER_API_KEY')
        
        if not api_key:
            await ctx.send("Weather service is currently unavailable.")
            return
        
        async with aiohttp.ClientSession() as session:
            url = f"http://api.openweathermap.org/data/2.5/weather?q={region['city']},{region['country']}&appid={api_key}&units=metric"
            async with session.get(url) as response:
                if response.status == 200:
                    data = await response.json()
                    
                    embed = discord.Embed(
                        title=f"🌤️ Weather in {region['city']}, {region['country']}",
                        color=0x3498db
                    )
                    
                    embed.add_field(name="Temperature", value=f"{data['main']['temp']}°C", inline=True)
                    embed.add_field(name="Feels Like", value=f"{data['main']['feels_like']}°C", inline=True)
                    embed.add_field(name="Humidity", value=f"{data['main']['humidity']}%", inline=True)
                    embed.add_field(name="Condition", value=data['weather'][0]['description'].title(), inline=True)
                    embed.add_field(name="Wind Speed", value=f"{data['wind']['speed']} m/s", inline=True)
                    
                    await ctx.send(embed=embed)
                else:
                    await ctx.send("Could not fetch weather data for your region.")