import discord
import dataman

bot_token_file = open('DISCORD TOKEN_test.txt', 'r')
GUILD = 'Fax'
bot_token = bot_token_file.readline()
client = discord.Client()


@client.event
async def on_ready():
    guild = discord.utils.find(lambda g: g.name == GUILD, client.guilds)
    print(
        f'{client.user} is connected to {guild.name} (id: {guild.id})')


@client.event
async def on_message(message):
    username = message.author
    if message.author == client.user:
        return

    channel = message.channel
    if message.content.startswith('..ao_hello'):
        await channel.send('AO Season points counter bot greetings you!')

    if message.content.startswith('..add'):
        msg = message.content.split(' ')
        ign = msg[1]
        points = msg[2]
        emote = dataman.points_add(ign, points)
        await message.add_reaction(emote)

    if message.content.startswith('..leaderboard'):
        lb = dataman.leaderboard_show()
        embed_msg = discord.Embed(
            description=lb[1],
            color=discord.Color.gold()
        )
        embed_msg.set_image(
            url='https://cdna.artstation.com/p/assets/images/images/002/921/302/large/'
                'maximilian-degen-albion-splash-overpaint-02-final-02-upload.jpg?1467290849')
        embed_msg.set_footer(text='OopsieDoopsie#0412')
        await channel.send(embed=embed_msg)

    if message.content.startswith('..delete'):
        msg = message.content.split(' ')
        ign = msg[1]
        if discord.utils.get(username.roles, name='Mechanic') is None:
            await message.add_reaction('💢')
            await channel.send('😡 Insufficient rights. 😡')
        else:
            dataman.ign_delete(ign)
            await message.add_reaction('💔')
            await channel.send(f'🦀 {ign} is gone! 🦀')

    if message.content.startswith('..help'):
        embed_msg = discord.Embed(
            title='**AVAILABLE COMMANDS**',
            description='**..ao_hello** - Sends hello message, just for testing if bot is online.\n'
                        '\n'
                        '**..add** - (ex: ..add Carl 200) Adds points to chosen participant.\n'
                        '*If negative value will be given, it will be substracted from saved value*\n'
                        '\n'
                        '**..leaderboard** - Shows Top 20 leaderboard.\n'
                        '\n'
                        '**..delete** - (ex: ..delete Carl) Deletes participant from database.\n'
                        'Requiers discord role **Mechanic**\n'
                        '*CAUTION: THERE IS NO WAY TO RECOVER DELETED DATA*',
            color=discord.Color.green()
        )
        embed_msg.set_footer(text='OopsieDoopsie#0412')
        embed_msg.set_image(url='https://yt3.ggpht.com/ooDmRtyMCL1W6SJyqsPRoJD6ag63CqYGD0FPMDmGhvvga4'
                                '6HrHgeCiBCvMxl-OpBkagBBYShfA=w640-fcrop64=1,32b75a57cd48a5a8-nd-c0xffffffff-rj-k-no')
        await channel.send(embed=embed_msg)


client.run(bot_token)
