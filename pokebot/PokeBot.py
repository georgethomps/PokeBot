# import packages
import discord
from discord.ext import commands
from PokeList import PokeList
from DataManager import DataManager
from random import choice
from re import compile

# define the TOKEN (needed to connect to Discord)
TOKEN = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

# store missing argument error
missing_arg = discord.ext.commands.MissingRequiredArgument

# instantiate the DataManager and PokeList
dm = DataManager()
pl = PokeList()

# instantiate the bot
description = 'Send comments/jokes to users mentioned in Discord messages!'
bot = commands.Bot(command_prefix='$', description=description)

# TODO: notify users bot is ready (FUTURE RELEASE)


# allow user to print the PokeList
@bot.command()
async def pokelist(ctx):
    await ctx.send(pl.print_list())


# TODO: must implement error handling for all commands that have arguments!!!!!!!!!! (line 50)
# allow user to add a user to the PokeList
@bot.command()
async def load(ctx, user):

    # add error handling in case a user isn't specified
    try:
        # add the user and send a notification
        await ctx.send(pl.load_user(user))

    # print an error notification
    except missing_arg:
        await ctx.send('You must specify a user to load!')


# allow user to remove a user from the PokeList
# TODO: simplify command name (same for loaduser)
@bot.command()
async def unload(ctx, user):
    try:
        await ctx.send(pl.unload_user(user))

    except missing_arg:
        await ctx.send('You must specify a user to unload!')


# allow user to clear the PokeList
@bot.command()
async def clearlist(ctx):
    await ctx.send(pl.clear_list())


# allow user to create a user profile
@bot.command()
async def createprofile(ctx, user, file):
    try:
        await ctx.send(dm.create_user(user, file))

    except missing_arg:
        await ctx.send('You must specify a user and text file!')


# allow user to delete a user profile (FEATURE)
# TODO: need to check user exists
@bot.command()
async def deleteprofile(ctx, user):
    try:
        pl.unload_user(user)
        await ctx.send(dm.delete_profile(user))

    except missing_arg:
        await ctx.send('You must specify a user to delete!')


# allow user to delete all user profiles
@bot.command()
async def clearprofiles(ctx):
    pl.clear_list()
    await ctx.send(dm.delete_all_profiles())


# allow user to print user profile settings
# TODO: formatting issues (col headers) (FUTURE RELEASE)
@bot.command()
async def userprofiles(ctx):
    await ctx.send(dm.print_users())


# allow user to terminate bot from Discord
@bot.command()
async def terminate(ctx):
    await ctx.send('Terminating PokeBot!')
    await bot.close()


# roast Noah if message contain's "Noah"
@bot.event
async def on_message(message):

    # process commands (prevents commands from being disabled)
    # TODO: break if command is found
    await bot.process_commands(message)

    # use a conditional to prevent pokes from being sent if a command is run
    if not message.content.startswith('$'):

        # store lower case message variable
        msg_lower = message.content.lower()

        # store data manager settings in a list
        profiles = dm.user_profiles

        # create a regex to search for all loaded users
        regex_string = '|'.join(pl.poke_list)
        regex = compile(regex_string)

        # store all matches and count of matches (set removes duplicates)
        matches = list(set(regex.findall(msg_lower)))

        # send out pokes if there are matches
        if matches:

            # prevent bot from responding to itself
            if message.author == bot.user:
                return

            # list to gather all relevant profile settings
            profile_dicts = [user for user in profiles if user['user'] in matches]

            # compile a list of all the comments to send
            msgs = [choice(comments) for comments in
                    [value for user in profile_dicts for key, value in user.items() if key == 'comments']]

            # send comments
            [await message.channel.send(comment) for comment in msgs]

# run bot with token
bot.run(TOKEN)

# TODO: safely terminate bot when terminating script
