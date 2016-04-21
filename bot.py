import discord, asyncio, time,youtube_dl
invite = r'https://discord.gg/0YEQ1VcAC52WYL1y' #manolos dorgados
#invite = r'https://discord.gg/0ZccGQBTU46tz803' # test server

client = discord.Client()
#discord.utils.oauth_url('168201768554070017','')
listword = ['!burl','!saindo da jaula','!13','!hora do show','!jc','!miau']

@client.event
async def on_message(message):

    if message.content.startswith("oi bot"):
        author = message.author
        authorstr = str(message.author)
        await client.send_message(message.channel,"Olá "+authorstr[0:-5]+" :-)", tts=False)
        await client.send_message(message.channel, "Curte esse som ai", tts=False)
        voice = await client.join_voice_channel(message.author.voice_channel)
        player = await voice.create_ytdl_player("https://www.youtube.com/watch?v=xv6yW8PuvJw")
        player.start()

    if message.content.startswith('!play'):
        link = str(message.content)[6:]
        list = ['youtube','yt','twitch']
        for i in list:
            if i in link:
                channelV = message.author.voice_channel
                voice = await client.join_voice_channel(channelV)
                player = await voice.create_ytdl_player(link)
                player.start()
                client.change_status(game=str(player.title),idle=False)

    if message.content.startswith('!stop'):
        if client.is_voice_connected():
            await client.voice.disconnect()


    if '@' in message.content:
        #await client.send_message(message.channel, 'Alguma pessoa foi mencionada', tts=False)
        pessoa = message.author
        mencoes = message.mentions  #lista com as menções
        for i in mencoes:
            if str(i.status) == 'offline':
                await client.send_message(i,'Vcoê foi mencionado enquanto estava offline por '+str(pessoa)+'\nMensagem recebida:',tts=False)
                await client.send_message(i,message.content,tts=False)
                print('Mensagem enviada para '+str(i))

    if message.content.startswith("!botcomandos"):
        await client.send_message(message.channel, 'Os comandos atuais são: %s' %listword, tts=False)

    if message.content.startswith("tchau bot"):
        await client.send_message(message.channel, 'Adeus humanos!.', tts=False)

    if message.content.startswith("!logar"):
        await client.send_message(message.channel, 'Entrando no canal', tts=False)
        channelV = message.author.voice_channel
        voice = await client.join_voice_channel(channelV)


    #if message.content.startswith('!deslogar'):
    #    if client.is_voice_connected():
    #        await client.voice.disconnect()
    #    else:
    #        await client.send_message(message.channel,'Não estou conectado ao chat de voz', tts=False)


    if message.content.startswith(listword[0]):
        if not (client.is_voice_connected()):
            channelV = message.author.voice_channel #channelV = objeto do canal em que a pessoa que mandou a mensagem esta
            print("ENCONTRADO")
            voice = await client.join_voice_channel(channelV)
            player = voice.create_ffmpeg_player('burl.mp3')
            player.start()
            time.sleep(1)
            await client.voice.disconnect()
        else:
            player = client.voice.create_ffmpeg_player('burl.mp3')
            player.start()
            time.sleep(1)
            await client.voice.disconnect()

    if message.content.startswith(listword[1]):
        if not (client.is_voice_connected()):
            channelV = message.author.voice_channel
            print("ENCONTRADO")
            voice = await client.join_voice_channel(channelV)
            player = voice.create_ffmpeg_player('saindodajaula.mp3')
            player.start()
            time.sleep(6)
            await client.voice.disconnect()
        else:
            player = client.voice.create_ffmpeg_player('saindodajaula.mp3')
            player.start()
            time.sleep(1)
            await client.voice.disconnect()

    if message.content.startswith(listword[2]) or (' 13 ' in message.content):
        if not (client.is_voice_connected()):
            channelV = message.author.voice_channel
            print("ENCONTRADO")
            voice = await client.join_voice_channel(channelV)
            player = voice.create_ffmpeg_player('13-memo.mp3')
            player.start()
            time.sleep(3.7)
            await client.voice.disconnect()
        else:
            player = client.voice.create_ffmpeg_player('13-memo.mp3')
            player.start()
            time.sleep(3.7)
            await client.voice.disconnect()

    if message.content.startswith(listword[3]):
        if not (client.is_voice_connected()):
            channelV = message.author.voice_channel
            print("ENCONTRADO")
            voice = await client.join_voice_channel(channelV)
            player = voice.create_ffmpeg_player('hora-do-show-porra.mp3')
            player.start()
            time.sleep(4.5)
            await client.voice.disconnect()
        else:
            player = client.voice.create_ffmpeg_player('hora-do-show-porra.mp3')
            player.start()
            time.sleep(4.5)
            await client.voice.disconnect()

    if message.content.startswith(listword[4]):
        if not (client.is_voice_connected()):
            channelV = message.author.voice_channel
            print("ENCONTRADO")
            voice = await client.join_voice_channel(channelV)
            player = voice.create_ffmpeg_player('hisnamejohncena.mp3')
            player.start()
            time.sleep(7)
            await client.voice.disconnect()
        else:
            player = client.voice.create_ffmpeg_player('hisnamejohncena.mp3')
            player.start()
            time.sleep(7)
            await client.voice.disconnect()

    if message.content.startswith(listword[5]):
        if not (client.is_voice_connected()):
            channelV = message.author.voice_channel
            print("ENCONTRADO")
            voice = await client.join_voice_channel(channelV)
            player = voice.create_ffmpeg_player('miau.mp3')
            player.start()
            time.sleep(3)
            await client.voice.disconnect()
        else:
            player = client.voice.create_ffmpeg_player('miau.mp3')
            player.start()
            time.sleep(3)
            await client.voice.disconnect()



    if message.content.startswith("!listar"):
        lista = list(client.get_all_channels())
        print (lista)

    if message.content.startswith("!teste"):
        channelV = message.author.voice_channel
        print(type(channelV))



@client.event
async def on_ready():
    print('logou como')
    print(client.user.name)
    print(client.user.id)
    discord.opus.load_opus('opus.dll')#carrega dll que permite executar sons
    if (discord.opus.is_loaded() == True):
        print("Opus loaded.")
    channels = client.get_all_channels()
    print(type(channels))
    for i in channels:
        if str(i.type) == 'text':
            await client.send_message(i,'Bot conectando',tts=False)
            time.sleep(1)

   # await client.get_invite(invite)
    #await client.accept_invite(invite)

client.run('botmanolosdorgados@gmail.com','arroz333')
#client.login('MTY4MjAxNzY4NTU0MDcwMDE3.CesC5g.XzplnNWl0KNhDUzWnWc9m0ogjAc')
