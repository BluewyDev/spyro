import discord, config
from discord.ext import commands

class sugg(commands.Cog, name="Suggestions"):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        channel = self.bot.get_channel(817714676934377504)
        if message.channel != channel:
            return
        user = self.bot.fetch_user(805872242184683551)
        if message.author == user:
            return
        await message.delete()
        await channel.send(message.content)

def setup(bot):
    bot.add_cog(sugg(bot))
