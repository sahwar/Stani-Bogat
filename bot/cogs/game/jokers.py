from discord.ext import commands

from bot.core.constants import Cogs
from bot.core.embeds import JokersEmbed
from bot.core.replies import Reply


class Jokers(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.user_id = str()

    @commands.guild_only()
    @commands.command(name=Cogs.Game.jokers, aliases=[Cogs.Game.joker])
    async def jokers(self, ctx):
        self.user_id = str(ctx.author.id)

        if self.user_id not in self.bot.games.keys():
            await ctx.send(Reply.not_in_game(self.user_id))
            return

        player_id = self.user_id

        game = self.bot.games[player_id]
        embed = JokersEmbed(game.user.name,
                            game.user.avatar_url,
                            game.jokers_left())
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Jokers(bot))
