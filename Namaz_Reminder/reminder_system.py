import discord
import asyncio
import aiohttp
import json
from datetime import datetime, timedelta

class NamazReminder:
    def __init__(self, bot):
        self.bot = bot
        self.user_regions = self.load_user_regions()
        
    def load_user_regions(self):
        try:
            # Fixed path - using correct folder name
            with open('Namaz_Reminder/namaz_times.json', 'r') as f:
                data = json.load(f)
                return data.get('user_regions', {})
        except FileNotFoundError:
            return {}
    
    def save_user_regions(self):
        # Fixed path
        with open('Namaz_Reminder/namaz_times.json', 'r') as f:
            data = json.load(f)
        data['user_regions'] = self.user_regions
        with open('Namaz_Reminder/namaz_times.json', 'w') as f:
            json.dump(data, f, indent=2)
    
    async def get_prayer_times(self, city, country):
        async with aiohttp.ClientSession() as session:
            url = f"http://api.aladhan.com/v1/timingsByCity?city={city}&country={country}&method=4"
            async with session.get(url) as response:
                data = await response.json()
                return data['data']['timings']
    
    async def check_namaz_time(self, user_id):
        user_id = str(user_id)  # Ensure it's string
        if user_id not in self.user_regions:
            return "Please set your region first using !set-region"
        
        region = self.user_regions[user_id]
        timings = await self.get_prayer_times(region['city'], region['country'])
        
        current_time = datetime.now().strftime('%H:%M')
        
        for prayer, time in timings.items():
            if prayer in ['Fajr', 'Dhuhr', 'Asr', 'Maghrib', 'Isha']:
                if current_time == time:
                    return f"🕌 It's time for {prayer} prayer! 🕌"
        
        return f"Current time: {current_time}. No prayer time right now."