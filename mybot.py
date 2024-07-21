from email.mime import message
import discord
import random

facts = [
"Более 1 миллиона видов живых существ находятся на грани исчезновения из-за разрушения их естественной среды.",
"Около 80% мусора в океанах составляют пластиковые отходы, которые представляют угрозу для морской жизни.",
"Одно дерево может поглотить около 22 килограммов углекислого газа в год.",
"Использование электронных устройств в режиме ожидания потребляет до 10% энергии в мире.",
"Повышение температуры на Земле приводит к таянию ледников и поднятию уровня мирового океана.",
]

client = discord.Client()

@client.event
async def on_ready():
 print('Logged on as', client.user)

@client.event
async def on_message(message):
 if message.author == client.user:
  return

if message.content.startswith('!eco_fact'):
 fact = random.choice(facts)
 await message.channel.send(fact)

client.run('YOUR_DISCORD_BOT_TOKEN')


#Замените `'YOUR_DISCORD_BOT_TOKEN'` на токен вашего Discord бота. После запуска бота командой `!eco_fact` он будет отправлять случайный факт об экологии в чат.
