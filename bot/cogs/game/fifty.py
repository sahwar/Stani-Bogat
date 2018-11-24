from discord.ext import commands

from bot.core.embeds import QuestionEmbed, JokersEmbed


class Fifty:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='50:50', aliases=['50/50', '5050', '50%50'])
    async def cut_2_answers(self, ctx):
        game = self.bot.games[str(ctx.author.id)]

        if game.fifty:
            game.remove_2_choices()
            embed = QuestionEmbed(**game.last_question)

            await game.last_embed.edit(embed=embed)
            game.fifty = False
        else:
            await ctx.send(f'<@{ctx.author.id}>, използвал си 50:50.')
            embed = JokersEmbed(game.user.name,
                                game.user.avatar_url,
                                game.jokers_left())
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Fifty(bot))