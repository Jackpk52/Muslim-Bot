import discord
from discord.ext import commands
import os
import asyncio
from dotenv import load_dotenv
import colorama
from colorama import Fore, Style, init
import aiohttp
import json
from datetime import datetime

# Initialize Colorama
init(autoreset=True)

# Load environment variables
load_dotenv()

def print_banner():
    """Print a beautiful banner when bot starts"""
    print(Fore.CYAN + "=" * 60)
    print(Fore.GREEN + r"""
    🕌  ____    _   _     _     _       ____        _   
    🕌 |  _ \  | | | |   | |   (_)     |  _ \      | |  
    🕌 | |_) | | | | |   | |    _ ___  | |_) | ___ | |_ 
    🕌 |  _ <  | | | |   | |   | / __| |  _ < / _ \| __|
    🕌 | |_) | | | | |___| |___| \__ \ | |_) | (_) | |_ 
    🕌 |____/  |_| |_____|_____|_|___/ |____/ \___/ \__|
    """ + Fore.RESET)
    print(Fore.CYAN + "=" * 60)
    print(Fore.YELLOW + "🤲 Muslim Bot - Your Islamic Companion")
    print(Fore.CYAN + "=" * 60)

# Bot setup
intents = discord.Intents.all()
bot = commands.Bot(
    command_prefix='!', 
    intents=intents,
    help_command=None  # Disable default help
)

# Simple user data storage
user_regions = {}

def load_user_regions():
    """Load user regions from file"""
    global user_regions
    try:
        with open('user_regions.json', 'r') as f:
            user_regions = json.load(f)
    except FileNotFoundError:
        user_regions = {}

def save_user_regions():
    """Save user regions to file"""
    with open('user_regions.json', 'w') as f:
        json.dump(user_regions, f, indent=2)

@bot.event
async def on_ready():
    print_banner()
    print(Fore.GREEN + f"✅ {bot.user} is online and ready to serve!" + Fore.RESET)
    print(Fore.BLUE + f"📊 Connected to {len(bot.guilds)} server(s)" + Fore.RESET)
    print(Fore.MAGENTA + f"👥 Serving {len(bot.users)} users" + Fore.RESET)
    
    # Load user data
    load_user_regions()
    print(Fore.GREEN + f"✅ Loaded {len(user_regions)} user regions" + Fore.RESET)
    
    # Set bot status
    activity = discord.Activity(type=discord.ActivityType.listening, name="Quran Recitations | !help")
    await bot.change_presence(activity=activity)
    
    print(Fore.CYAN + "🤲 Bot is now listening for Islamic commands..." + Fore.RESET)
    print(Fore.CYAN + "=" * 60 + Fore.RESET)

# ==================== ALL COMMANDS IN MAIN.PY ====================

@bot.command(name='help')
async def help_command(ctx):
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
    print(Fore.GREEN + "✅ Help command executed" + Fore.RESET)

@bot.command(name='convert')
async def convert_command(ctx):
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
    print(Fore.GREEN + "✅ Convert command executed" + Fore.RESET)

@bot.command(name='set-region')
async def set_region_command(ctx, city: str, country: str = None):
    """Set your region for prayer times and weather"""
    
    if not country:
        await ctx.send("Please specify both city and country. Example: `!set-region Mecca Saudi Arabia`")
        return
    
    # Save user's region
    user_id = str(ctx.author.id)
    user_regions[user_id] = {
        'city': city,
        'country': country
    }
    save_user_regions()
    
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
    print(Fore.GREEN + f"✅ Region set for {ctx.author}: {city}, {country}" + Fore.RESET)

@bot.command(name='chk-weather')
async def check_weather_command(ctx):
    """Check weather in your region"""
    
    user_id = str(ctx.author.id)
    if user_id not in user_regions:
        await ctx.send("Please set your region first using `!set-region <city> <country>`")
        return
    
    region = user_regions[user_id]
    api_key = os.getenv('WEATHER_API_KEY')
    
    if not api_key:
        embed = discord.Embed(
            title="🌤️ Weather",
            description="Weather service is currently unavailable.",
            color=0xe74c3c
        )
        await ctx.send(embed=embed)
        return
    
    try:
        async with aiohttp.ClientSession() as session:
            url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={region['city']},{region['country']}&aqi=no"
            async with session.get(url) as response:
                if response.status == 200:
                    data = await response.json()
                    
                    embed = discord.Embed(
                        title=f"🌤️ Weather in {region['city']}, {region['country']}",
                        color=0x3498db
                    )
                    
                    embed.add_field(name="Temperature", value=f"{data['current']['temp_c']}°C", inline=True)
                    embed.add_field(name="Feels Like", value=f"{data['current']['feelslike_c']}°C", inline=True)
                    embed.add_field(name="Condition", value=data['current']['condition']['text'], inline=True)
                    embed.add_field(name="Humidity", value=f"{data['current']['humidity']}%", inline=True)
                    embed.add_field(name="Wind Speed", value=f"{data['current']['wind_kph']} km/h", inline=True)
                    
                    await ctx.send(embed=embed)
                    print(Fore.GREEN + f"✅ Weather checked for {region['city']}" + Fore.RESET)
                else:
                    embed = discord.Embed(
                        title="❌ Weather Error",
                        description="Could not fetch weather data for your region.",
                        color=0xe74c3c
                    )
                    await ctx.send(embed=embed)
    except Exception as e:
        embed = discord.Embed(
            title="❌ Weather Error",
            description="Failed to fetch weather data. Please try again later.",
            color=0xe74c3c
        )
        await ctx.send(embed=embed)

@bot.command(name='chk-namaz-time')
async def check_namaz_time_command(ctx):
    """Check if it's time for prayer in your region"""
    
    user_id = str(ctx.author.id)
    if user_id not in user_regions:
        await ctx.send("Please set your region first using `!set-region <city> <country>`")
        return
    
    region = user_regions[user_id]
    
    try:
        async with aiohttp.ClientSession() as session:
            url = f"http://api.aladhan.com/v1/timingsByCity?city={region['city']}&country={region['country']}&method=4"
            async with session.get(url) as response:
                if response.status == 200:
                    data = await response.json()
                    timings = data['data']['timings']
                    
                    current_time = datetime.now().strftime('%H:%M')
                    
                    # Check if current time matches any prayer time
                    prayer_found = False
                    for prayer, time in timings.items():
                        if prayer in ['Fajr', 'Dhuhr', 'Asr', 'Maghrib', 'Isha']:
                            if current_time == time:
                                embed = discord.Embed(
                                    title="🕌 Prayer Time Alert!",
                                    description=f"**It's time for {prayer} prayer!**\n\nMay Allah accept your prayers! 🤲",
                                    color=0x2ecc71
                                )
                                await ctx.send(embed=embed)
                                prayer_found = True
                                break
                    
                    if not prayer_found:
                        embed = discord.Embed(
                            title="🕌 Prayer Times",
                            description=f"**Current time:** {current_time}\n\nNo prayer time right now. Here are today's prayer times:",
                            color=0x3498db
                        )
                        
                        for prayer in ['Fajr', 'Dhuhr', 'Asr', 'Maghrib', 'Isha']:
                            embed.add_field(name=prayer, value=timings[prayer], inline=True)
                        
                        await ctx.send(embed=embed)
                    
                    print(Fore.GREEN + f"✅ Namaz time checked for {region['city']}" + Fore.RESET)
                else:
                    await ctx.send("❌ Could not fetch prayer times. Please try again later.")
    except Exception as e:
        await ctx.send("❌ Error fetching prayer times. Please try again later.")

@bot.command(name='ping')
async def ping_command(ctx):
    """Check if bot is responsive"""
    latency = round(bot.latency * 1000)
    embed = discord.Embed(
        title="🏓 Pong!",
        description=f"Bot latency: {latency}ms",
        color=0x2ecc71
    )
    await ctx.send(embed=embed)
    print(Fore.GREEN + f"✅ Ping command executed - Latency: {latency}ms" + Fore.RESET)

@bot.command(name='info')
async def info_command(ctx):
    """Show bot information"""
    embed = discord.Embed(
        title="🕌 Muslim Bot Information",
        description="Your Islamic companion on Discord",
        color=0x3498db
    )
    
    embed.add_field(name="Version", value="1.0", inline=True)
    embed.add_field(name="Server Count", value=len(bot.guilds), inline=True)
    embed.add_field(name="User Count", value=len(bot.users), inline=True)
    embed.add_field(name="Developer", value="Mxfil", inline=True)
    embed.add_field(name="Prefix", value="!", inline=True)
    embed.add_field(name="Features", value="Prayer Times, Weather, Islamic Guidance", inline=True)
    
    embed.set_footer(text="Made with ❤️ for the Ummah")
    await ctx.send(embed=embed)
    print(Fore.GREEN + "✅ Info command executed" + Fore.RESET)

@bot.command(name='test')
async def test_command(ctx):
    """Test if bot commands are working"""
    embed = discord.Embed(
        title="🧪 Bot Test",
        description="✅ Bot is working! All systems operational.",
        color=0x00ff00
    )
    embed.add_field(name="Status", value="Online", inline=True)
    embed.add_field(name="Commands Loaded", value=f"{len(bot.commands)}", inline=True)
    embed.add_field(name="Server", value=ctx.guild.name, inline=True)
    
    await ctx.send(embed=embed)
    print(Fore.GREEN + f"✅ Test command executed successfully" + Fore.RESET)

@bot.event
async def on_command_error(ctx, error):
    """Log command errors with colors"""
    if isinstance(error, commands.CommandNotFound):
        print(Fore.RED + f"❌ Command not found: {ctx.message.content}" + Fore.RESET)
        await ctx.send("**Command not found!** Use `!help` to see available commands.")
    elif isinstance(error, commands.MissingRequiredArgument):
        print(Fore.RED + f"❌ Missing argument for {ctx.command}" + Fore.RESET)
        await ctx.send(f"**Missing required argument!** Usage: `!{ctx.command} {ctx.command.signature}`")
    else:
        print(Fore.RED + f"💥 Error in {ctx.command}: {str(error)}" + Fore.RESET)
        await ctx.send(f"**An error occurred:** {str(error)}")

# Run the bot
if __name__ == "__main__":
    token = os.getenv('DISCORD_BOT_TOKEN')
    if token:
        print(Fore.BLUE + "🚀 Starting Muslim Bot..." + Fore.RESET)
        bot.run(token)
    else:
        print(Fore.RED + "❌ ERROR: No DISCORD_BOT_TOKEN found in .env file!" + Fore.RESET)