import telebot
import requests
from bs4 import BeautifulSoup

API_TOKEN = '2061280843:AAFzQI78qrLmgP1CFPYBf8Qjb5X4d17INU0'

bot = telebot.TeleBot(API_TOKEN)


list = []
r = requests.get('https://www.skysports.com/serie-a-table')
soup = BeautifulSoup(r.text, 'html.parser')

league_table = soup.find('table', class_ = 'standing-table__table callfn')
id = 1
for team in league_table.find_all('tbody'):
    rows = team.find_all('tr')
    for row in rows:
        pl_team = row.find('td', class_ ='standing-table__cell standing-table__cell--name')
        pl_team = pl_team['data-long-name']
        points = row.find_all('td', class_ = 'standing-table__cell')[9].text
        played = row.find_all('td', class_ = 'standing-table__cell')[2].text
        text = str(id)+'   '+pl_team+'   '+played+'   '+str(points)+'\n'
        id += 1
        list.append(text)

txt = '\n'.join(list)
text = "O'rin | Klub nomi | O'yinlar soni | Ochko\n\n"+txt+'\n\nAdmin: Raxmatjon { @xc_ho }'
# print(text)
    



@bot.message_handler(commands=['help', 'start'])
def hello(message):
    bot.reply_to(message, "Jadvalni ko'rish uchun /show ni bosing: /show\n\nAdmin: Raxmatjon { @xc_ho }")

@bot.message_handler(commands=['show'])
def helloo(message):
    bot.reply_to(message, text)

bot.enable_save_next_step_handlers(delay=2)
bot.load_next_step_handlers()
bot.infinity_polling()