import discord

intents = discord.Intents.default()
intents.members = True
intents.reactions = True

client = discord.Client(intents=intents)

bot_settings = {
    'ninachannel': 975801486850265150,
    'pedrochannel': 976749934088970271,
    'ninaid': 728547314834341919,
    'pedroid': 506564178845237248,
    'avisos': 978244677801246720,
    'lixo': 978620178394927214,
    'prefix': 'np!'
}

embed = discord.Embed


@client.event
async def on_ready():
    print(f'{client.user} has been turned on.')
    activity = discord.Game(name="Nekopara Vol. 1", type=3)
    await client.change_presence(status=discord.Status.do_not_disturb, activity=activity)


@client.event
async def on_message(message):
    channel = message.channel
    author = message.author
    prefix = bot_settings.get('prefix')
    if author == client.user:
        return

    if message.content.startswith(prefix+'join'):
        if author.voice:
            channel = message.author.voice.channel
            await channel.connect()
            await message.guild.change_voice_state(channel=channel, self_mute=False, self_deaf=True)
        else:
            await message.channel.send("epah yh")

    if message.attachments:
        if channel.id == bot_settings.get('ninachannel'):
            embed = discord.Embed(title=" ", color=0x16d1d4)
            embed.set_thumbnail(url=author.avatar_url)
            embed.add_field(name="Nova imagem NSFW",
                            value="Uma nova mensagem acabou de ser enviada por <@" + str(author.id) + "> para o canal <#" + str(
                                channel.id) + ">\n\nNão te esqueças de reagir à mensagem enviada no canal.",
                            inline=True)
            embed.set_footer(text="enviada por · " + str(author))
            await message.guild.get_channel(bot_settings.get('avisos')).send(embed=embed, content="@everyone")
            count = -1
            async for _ in channel.history(limit=None):
                count += 1
            attachment = await message.attachments[0].save("imagem_"+str(count)+".jpg")

            await message.delete()

            Eembed = discord.Embed(title=str(count)+" - Imagem NSFW ", color=0x16d1d4)
            Eembed.set_image(url="attachment://imagem_"+str(count)+".jpg")
            Eembed.set_footer(text="enviada por · " + str(author))
            messageA = await channel.send(content="", embed=Eembed, file=discord.File("imagem_"+str(count)+".jpg"))
            await messageA.add_reaction('❤️')
            await messageA.add_reaction('😭')
            await messageA.add_reaction('🤮')


    if channel.id == bot_settings.get('pedrochannel'):
        embed = discord.Embed(title=" ", color=0x16d1d4)
        embed.set_thumbnail(url=author.avatar_url)
        embed.add_field(name="Nova pasta NSFW",
                         value="Uma nova mensagem acabou de ser enviada por <@" + str(author.id) + "> para o canal <#" + str(
                              channel.id) + ">", inline=True)
        embed.set_footer(text="enviada por · " + str(author))
        await message.guild.get_channel(bot_settings.get('avisos')).send(embed=embed, content="@everyone")
        count = 0
        async for _ in channel.history(limit=None):
            count += 1
        url_pasta = message.content

        await message.delete()

        Eembed = discord.Embed(title=str(count) + " - Pasta NSFW ", color=0x16d1d4)
        Eembed.set_thumbnail(url="attachment://logo.jpg")
        Eembed.add_field(name="Baixe o arquivo no link abaixo.", value=url_pasta, inline=True)
        Eembed.set_footer(text="enviada por · " + str(author))
        messageA = await channel.send(content="", embed=Eembed, file=discord.File("logo.jpg"))

client.run('OTc2OTIwMjc5NzM5Njk1MTg1.GUpCd2.6UG_Isjz48aODkOvwbkNXn9RoQWOV7LznrbJZk')
