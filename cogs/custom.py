import discord, config, asyncio, datetime
from discord.ext import commands
from discord_slash import cog_ext, SlashContext

class custom(commands.Cog, name="Custom"):
    def __init__(self, bot):
        self.bot = bot
        self.suggestion_channel = 820259145830760449# Suggestion Channel

    @commands.Cog.listener('on_message')
    async def suggestions(self, message):
        if message.channel.id != self.suggestion_channel or message.author.id in [self.bot.user.id, 620990340630970425]:
            return
        elif message.author.bot is True:
            return await message.delete()
        elif message.content.startswith('! ') and message.author.guild_permissions.administrator is True:
            return
        await message.delete()
        channel = self.bot.get_channel(self.suggestion_channel)
        embed = discord.Embed(description=str(message.content), color=config.green)
        embed.set_author(name=str(message.author), icon_url=str(message.author.avatar_url))
        if message.attachments != []:
            embed.set_image(url=message.attachments[0].url)
        embed2 = await channel.send(embed=embed)
        await embed2.add_reaction('👍')
        await embed2.add_reaction('🤷')
        await embed2.add_reaction('👎')

def setup(bot):
    bot.add_cog(custom(bot))
