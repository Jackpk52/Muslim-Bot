# 🕌 Muslim Bot - Your Islamic Discord Companion

A comprehensive Discord bot designed to serve the Muslim community with Islamic features, prayer times, Quran verses, and daily reminders.

![Discord](https://img.shields.io/badge/Discord-7289DA?style=for-the-flat&logo=discord&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-flat&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Link[(https://jackpk52.github.io/Muslim-Bot/)

## 🌟 Features

### 🤲 Islamic Commands
- **Shahada Guide**: Learn how to become Muslim
- **Prayer Times**: Accurate prayer times based on location
- **Quran Verses**: Access Quranic verses and translations
- **Islamic Reminders**: Daily duas and Islamic knowledge

### 🕋 Prayer Management
- **Auto Region Detection**: Set your location for accurate prayer times
- **Namaz Reminders**: Get notified when it's prayer time
- **Prayer Time Check**: Instantly check if it's time for prayer

### 🌤️ Utility Features
- **Weather Integration**: Check weather conditions for your region
- **Multi-language Support**: Arabic, English, and more
- **Beautiful Embeds**: Color-coded Islamic messages

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- Discord Bot Token
- Discord Server with Admin permissions

### Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/muslim-bot.git
   cd muslim-bot
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Setup Environment**
   - Rename `.env.example` to `.env`
   - Add your Discord bot token:
     ```env
     DISCORD_BOT_TOKEN=your_bot_token_here
     WEATHER_API_KEY=your_weather_api_key_optional
     ```

4. **Configure Bot**
   - Edit `config.txt` to customize settings
   - Add your server-specific configurations

5. **Run the Bot**
   ```bash
   python main.py
   ```

## 📋 Command List

### 🕋 Core Commands
| Command | Description | Example |
|---------|-------------|---------|
| `!convert` | Learn how to become Muslim | `!convert` |
| `!set-region` | Set your location | `!set-region Mecca Saudi Arabia` |
| `!chk-namaz-time` | Check prayer times | `!chk-namaz-time` |
| `!chk-weather` | Check local weather | `!chk-weather` |
| `!help` | Show all commands | `!help` |

### 📖 Islamic Commands
| Command | Description | Example |
|---------|-------------|---------|
| `!quran <surah:verse>` | Get Quran verse | `!quran 1:1` |
| `!hadith <collection>` | Random hadith | `!hadith bukhari` |
| `!dua <occasion>` | Get specific dua | `!dua morning` |
| `!islamic-date` | Current Islamic date | `!islamic-date` |

## 🛠️ Setup Guide

### Creating Discord Bot

1. Go to [Discord Developer Portal](https://discord.com/developers/applications)
2. Click "New Application" and name it "Muslim Bot"
3. Go to "Bot" section and click "Add Bot"
4. Copy the bot token and add to `.env` file
5. Enable these Privileged Gateway Intents:
   - ✅ PRESENCE INTENT
   - ✅ SERVER MEMBERS INTENT
   - ✅ MESSAGE CONTENT INTENT

### Inviting Bot to Server

Use this invite URL (replace YOUR_CLIENT_ID):
```
https://discord.com/oauth2/authorize?client_id=YOUR_CLIENT_ID&permissions=8&scope=bot%20applications.commands
```

### Required Permissions
- 📝 Read Messages/View Channels
- 📢 Send Messages
- 📋 Embed Links
- 👥 Manage Roles (for reminders)
- ⏰ Use External Emojis

## 📁 Project Structure

```
Muslim-bot/
├── main.py                 # Main bot file
├── .env                    # Environment variables (SECRET)
├── config.txt              # Bot configuration
├── requirements.txt        # Python dependencies
├── Duas/                   # Islamic prayers database
│   └── duas.json          # Collection of duas
├── Namaz_Reminder/         # Prayer management
│   ├── namaz_times.json   # Prayer time data
│   └── reminder_system.py # Reminder logic
└── Commands/              # All bot commands
    ├── convert.py         # Shahada guide
    ├── help.py           # Help system
    ├── set_region.py     # Location setting
    ├── chk_weather.py    # Weather checks
    └── chk_namaz_time.py # Prayer time checks
```

## ⚙️ Configuration

### Environment Variables (.env)
```env
DISCORD_BOT_TOKEN=your_discord_bot_token
WEATHER_API_KEY=your_openweather_api_key
```

### Bot Settings (config.txt)
```txt
BOT_PREFIX=!
DEFAULT_CITY=Mecca
DEFAULT_COUNTRY=Saudi Arabia
PRAYER_METHOD=4
```

## 🎨 Features in Detail

### 🤲 Conversion Guide
- Step-by-step Shahada process
- Welcome message for new Muslims
- Basic Islamic knowledge

### 🕌 Prayer Times
- Accurate calculation based on location
- Multiple calculation methods
- Automatic timezone detection
- Beautiful prayer time displays

### 📖 Quran & Hadith
- Multiple translation support
- Easy verse lookup
- Authentic hadith collections
- Proper referencing

### 🌤️ Weather Integration
- Local weather conditions
- Prayer time adjustments
- Seasonal reminders

## 🔧 Troubleshooting

### Common Issues

1. **Bot not starting**
   - Check if token is correct in `.env`
   - Verify Python version (3.8+ required)
   - Ensure all dependencies are installed

2. **Commands not working**
   - Check bot permissions in server
   - Verify message content intent is enabled
   - Ensure bot has proper role hierarchy

3. **Prayer times inaccurate**
   - Verify city/country spelling
   - Check timezone settings
   - Try different calculation methods

### Support
For issues and questions:
1. Check this README
2. Review error logs in console
3. Create an issue on GitHub

## 🤝 Contributing

We welcome contributions from the community!

### How to Contribute
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

### Areas for Contribution
- 📚 Additional Quran translations
- 🕌 More prayer calculation methods
- 🌍 Support for more regions
- 📱 Mobile optimization
- 🎨 Improved embeds and UI

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Aladhan API** for prayer times
- **AlQuran Cloud API** for Quran data
- **OpenWeather API** for weather data
- The Muslim community for inspiration and support

## 🎯 Roadmap

- [ ] Auto-prayer reminders
- [ ] Ramadan features
- [ ] Zakat calculator
- [ ] Islamic calendar
- [ ] Mobile app version
- [ ] Multi-language support
- [ ] Voice prayer alerts

---

<div align="center">

**Made with ❤️ for the Ummah**

*May Allah accept our deeds and make this bot beneficial for the Muslim community*

**Assalamu Alaikum Warahmatullahi Wabarakatuh** 🤲

</div>

## 📞 Support Server

Join our Discord server for support and updates: [Invite Link](https://discord.gg/)

---


*Note: This bot is a tool to assist Muslims in their daily Islamic practices. Always verify important religious matters with knowledgeable scholars.*

