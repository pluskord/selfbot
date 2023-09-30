import discord, asyncio, inspect, io; from discord.ext import commands
plus=commands.Bot(command_prefix="$", intents=discord.Intents.all(), self_bot=True)
@plus.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandError):
        await ctx.reply(f"```fix\n{error}\n```", mention_author=False)
    else:
        raise error
@plus.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name=f"pluscord", url="https://www.youtube.com/watch?v=0eicfJ1MKJk"))
@plus.command(aliases=["p"])
async def ping(ctx):
    ms = round(plus.latency * 1000)
    await ctx.reply(content=f'**{ms}** ms', mention_author=False)
@plus.command(aliases=["src"])
async def source(ctx, cmd: str):
    command = plus.get_command(cmd)
    if command:
        src = inspect.getsource(command.callback); x = io.BytesIO(src.encode("utf-8"))
        await ctx.reply(file=discord.File(x, filename=f"{cmd}.py"), mention_author=False)
    else:
        await ctx.reply(f"**{cmd}** isn't a valid cmd", mention_author=False)
@plus.command(aliases=["av"])
async def avatar(ctx, *, member: discord.User = None):
    if member is None:
        member = ctx.author
    await ctx.reply(f"{member.avatar_url if member.avatar else member.default_avatar_url}", mention_author=False)
@plus.command(aliases=["enc"])
async def encode(ctx, *, message: str):
    await ctx.reply(content=f"> original content\n```\n{message}\n```\n> encoded as\n```{base64.b64encode(message.encode()).decode('utf-8')}\n```", mention_author=False)
@plus.command(aliases=["dcd"])
async def decode(ctx, *, message: str):
    await ctx.reply(content=f"> encoded content as\n```\n{message}\n```\n> original content\n```{base64.b64decode(message).decode('utf-8')}\n```", mention_author=False)
plus.run("token", bot=False) #replace token with your discord client token
