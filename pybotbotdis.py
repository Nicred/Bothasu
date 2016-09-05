import asyncio
import websockets
import aiohttp
import logging
import discord

logging.basicConfig(level=logging.INFO)

client = discord.Client()
global mojnoli
mojnoli = 1

@client.event
async def on_ready():
     print('Logged in as')
     print(client.user.name)
     print(client.user.id)
     print('----------------------')
     print(client)
     client.accept_invite('https://discord.gg/byfXzHt')
     await client.change_status(game=discord.Game(name='Макро'))

@client.event
async def on_message(message):
     s1 = message.content
     s2 = s1.split()
     global announce
     global stk

     global an #= open('anonc.txt', '+')

     def botinvoke(msg):
          if 'бот' in msg or 'Бот' in msg or 'бот,' in msg or 'Бот,' in msg:
               return True
          else:
               return False

     def bgrets(m2):              
          if 'Привет' in m2 or 'привет' in m2 or 'Ку' in m2 or 'ку' in m2 or 'Привет,' in m2 or 'Ку,' in m2 or 'ку,' in m2 or 'Хай' in m2 or 'хай' in m2 or 'хай,' in m2 or 'Хай,' in m2 or 'привет!' in m2 or 'привет,' in m2: 
               return True
          
     def cats(m2):
          if 'кот' in m2 or 'Кот' in m2 or 'Кота' in m2 or 'кота' in m2 or 'Котика' in m2 or 'котика' in m2 or 'котика?' in m2 or 'кота?' in m2:
               return True

     def isboss():
          man = message.author.name
          if man == 'Naxis' or man == 'Nicred' or man == 'VaultBoy' or man == 'YamatoSC':
               return True
          else:
               return False
          

     def info(m2):
          if 'Список' in m2 or 'список' in m2 or 'таблица' in m2 or 'Таблица' in m2 or 'Игроки' in m2 or 'игроки' in m2:
               return True
         
     if botinvoke(s2)== True:
          if bgrets(s2) == True:
               if 'никред' in s2 or 'Никред' in s2 or 'никрид' in s2 or 'Никрид' in s2:
                    return
               respto = message.author.mention
               neim = message.author.name
               if neim == 'FFA':
                    await client.send_file(message.channel, 'peka.jpg', content=('%s бесишь' % respto))
               elif neim == 'VaultBoy':
                    await client.send_message(message.channel, 'Приветствую, владыка всея хасу, успешный предприниматель, ораганизатор и просто хороший человек %s' % respto)
               elif neim == 'WayTeh':
                    await client.send_message(message.channel, 'Евгений Ваганович, здрасте. Опять шутить будете?')
               elif neim == 'Coose':
                    await client.send_file(message.channel, 'peka.jpg', content=('О, привет, %s. Как ты так быстро вырос из бронзы в алмаз? Ты же в школе должен быть!' % respto))
               elif neim == 'Naxis':
                    await client.send_message(message.channel, '%s, ток не чизь(9' % respto)
               elif neim == '#hater':
                    await client.send_file(message.channel, 'peka.jpg', content=('Привет, %s. Го голос?'  % respto))
               elif neim == 'YamatoSC':
                    await client.send_file(message.channel, 'peka.jpg', content=('Привет, %s. Когда ты уже вступишь в хасу ?'  % respto))
               elif neim == 'SlyFox':
                    await client.send_message(message.channel, 'Привет, %s. Ты уже научился строить ццшки ?:D'  % respto)
               elif neim == 'Phoenix':
                    await client.send_message(message.channel, 'Привет, %s. Взял ачивку за командники?'  % respto)
               elif neim == 'AdmiralMer':
                    await client.send_message(message.channel, 'Привет, %s. Всё ещё катаешь в мех ?'  % respto)
                    await client.send_file(message.channel, 'peka.jpg')
               elif neim == 'BolvaX':
                    await client.send_message(message.channel, 'О, %s ты жив О_О'  % respto)
               elif neim == 'azunyashka':
                    await client.send_message(message.channel, 'Два чая господину %s  из клана Houkago Tea Team' % respto)
               elif neim == 'Near':
                    await client.send_message(message.channel, 'Привет, словоопасный %s'  % respto)
               elif neim == 'Nicred':
                    await client.send_file(message.channel, 'peka.jpg', content=('О, привет, %s. Как в школе дела ?' % respto))
               elif neim == 'Kronaz':
                    await client.send_message(message.channel, 'O, %s,привет! Они тут без тебя совсем низуя не могут' % respto)
               else:                    
                    await client.send_message(message.channel, 'Привет, %s' % respto)               

     if message.content == ('таблица') or message.content ==('Таблица'):
          await client.send_message(message.channel, r'Таблица игроков - https://docs.google.com/spreadsheets/d/10-ZIiyvbOcJDxj3Pf9RtlBEx9aTQ7skwiUvDyTiP6-A/edit#gid=2008021498')

     if message.content == ('ссылки') or message.content == ('Cсылки'):
          await client.send_message(message.channel, r'Канал клана "Hasu" на YouTube - https://www.youtube.com/channel/UCmYQiYElhdzp1r-FHK83sKg')
          await client.send_message(message.channel, r'Канал WayTeh на YouTube https://www.youtube.com/channel/UC-xiI_-izDZL6p15fxHTSQg')
          await client.send_message(message.channel, r'Стримы VaultBoy - http://goodgame.ru/channel/Vault2501/ и https://www.twitch.tv/v4u1tboy ')
          await client.send_message(message.channel, r'Стримы SlyFox - http://goodgame.ru/channel/SlyFoxPul/ и https://www.twitch.tv/slyfoxpul')
          await client.send_message(message.channel, r'Стримы MasterPendal - http://goodgame.ru/channel/Pendal/')
          await client.send_message(message.channel, r'Стримы PesheVik - http://goodgame.ru/channel/PesheVik/ Канал YouTube - https://www.youtube.com/channel/UC5TOurQxipkJLt2a9WzyGGA')
     if message.content.startswith('whb'):
          print(isboss())
     if message.content.startswith('setka is'):
          if isboss() == True:              
               stk = open("setka.txt", 'w')
               stk.write(message.content[9:])
               stk.close()
               await client.send_message(message.channel, 'Ок, босс!') 
               print(message.content[9:])
          else:
               print(message.author.name)
               await client.send_message(message.channel, 'Ты не босс!')
     if message.content.startswith('Анонс ='):
          if isboss() == True:              
               anc = open("announce.txt", 'w')
               anc.write(message.content[8:])
               anc.close()
               await client.send_message(message.channel, 'Ок, босс!') 
               print(message.content[9:])
          else:
               print(message.author.name)
               await client.send_message(message.channel, 'Недостаточно минералов')
     
     if message.content.startswith('+pigc'):
          
          if isboss() == True:               
               await client.send_message('general', message.content[6:]) 
               print(message.content[9:])
     if message.content == ('dm'):
          deleted = client.purge_from(message.channel, limit=10)
          await client.send_message(message.channel, 'Deleted {} message(s)'.format(len(deleted)))
          print(deleted)
          #client.delete_messages(td)
     #if message.content == ('!dm %i' %hmtd)
    #delete_messages(messages)
#=================================GET ABOVE=======================================
               
#=================================================================================
               
#===============================POST UNDER========================================
     if message.content == ('Анонс') or message.content == ('анонс'):
          anc = open('announce.txt', 'r')
          msssk2 = anc.read()
          await client.send_message(message.channel, msssk2)   

     if message.content == ('сетка') or message.content == ('Сетка'):          
          stk = open('setka.txt', 'r')
          msssk = stk.read()
          await client.send_message(message.channel, msssk)
          
     if message.content == ('Бот') or message.content == ('бот'):          
          hlp = open('hlp.txt', 'r')
          msdg = hlp.read()
          await client.send_message(message.channel, msdg)
     
     if message.content == ('клан') or message.content == ('Клан'):
          await client.send_message(message.channel, r'Рейтинги игроков клана - http://www.rankedftw.com/clan/H%D0%B0su/played/')

     if ('(peka)') in message.content:
          await client.send_file(message.channel, 'peka.jpg')
    
     if message.content == ('тст'):
          print(message.author.name)
          if message.author.name == ('Nicred'):
               print('yes')
     if message.author == client.user:
          return
#TODO: DELETING
#

client.run('MjEwMDk4NTg5MDgxMjcyMzIw.CoJ1dw.xTAauN-GRTdvq_ccopLtxG3WGbI')


    
