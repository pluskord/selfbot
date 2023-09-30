import discord, asyncio, inspect, io; from discord.ext import commands
plus=commands.Bot(command_prefix="$", intents=discord.Intents.all(), self_bot=True)
@plus.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name=f"pluscord", url="https://www.youtube.com/watch?v=0eicfJ1MKJk"))
@plus.command()
async def ping(ctx):
    ms = round(plus.latency * 1000)
    await ctx.reply(content=f'**{ms}** ms', mention_author=False)
@plus.command(aliases=["src"])
async def source(ctx, cmd: str):
    command = plus.get_command(cmd)
    if command:
        src = inspect.getsource(command.callback); cox = io.BytesIO(src.encode("utf-8"))
        await ctx.reply(file=discord.File(cox, filename=f"{cmd}.py"), mention_author=False)
    else:
        await ctx.reply(f"**{cmd}** isn't a valid cmd", mention_author=False)
plus.run("token", bot=False)

