import requests
from discord.ext import commands
from datetime import datetime

##################################################################################################################
# Cloud Bot
# Hi I am Cloud Bot. I can retrieve weather data from any city.

# SETUP
# 1. Generate your own api key at https://api.openweathermap.org
# 2. Generate a discord token for your channel at https://discordapp.com/developers/applications
# 3. Copy your api key and discord token into code lines 20 and 21 respectively
# 4. Run this script and your bot should be ready and come online in a few seconds!

# COMMANDS
# Type .weather followed by any city location
# Eg .weather Calgary
##################################################################################################################

user_api = 'YOUR API KEY'
discord_token = 'YOUR DISCORD TOKEN'
client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
    print('Cloud Bot is Online!')

@client.command()
async def weather(ctx, location=None):
    try:
        complete_api_link = 'https://api.openweathermap.org/data/2.5/weather?q=' + location + '&appid=' + user_api
        api_link = requests.get(complete_api_link)
        api_data = api_link.json()

        if api_data['cod'] == '404':
            await ctx.send('\'' + location + '\' is not a valid city')
        else:
            # create variables to store weather statistics
            city = api_data['name']
            date_time = datetime.now().strftime('%b %d, %Y | %I:%M %p')
            temperature = 'Temp: ' + str(round((api_data['main']['temp']) - 273.15)) + ' deg C'
            humidity = 'Humidity: ' + str(api_data['main']['humidity']) + '%'
            wind_speed = 'Wind: ' + str(api_data['wind']['speed']) + ' mph'

            # assemble strings for output
            weather_summary = city + '\n' + date_time + '\n' + temperature + '\n' + humidity + '\n' + wind_speed

            # display summary in discord
            await ctx.send(weather_summary)
    except:
        await ctx.send('Error: please check API key and commands in the instructions.')

try:
    client.run(discord_token)
except:
    print("Invalid token, please see setup instructions above.")