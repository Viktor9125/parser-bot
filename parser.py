import telebot
import parser_functions as ps

TOKEN = ''
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Добро пожаловать в бота для новостей!")


@bot.message_handler(commands=['articles_by_flows'])
def get_flow_for_article(message):
    bot.send_message(message.chat.id, 'Напиши поток.')
    bot.register_next_step_handler_by_chat_id(message.chat.id, get_articles_by_flows)


def get_articles_by_flows(message):
    flow = message.text.lower()
    flows_names = ['develop', 'admin', 'design', 'management', 'marketing', 'popsci']
    flows = {'разработка': flows_names[0],
             'администрирование': flows_names[1],
             'дизайн': flows_names[2],
             'менеджмент': flows_names[3],
             'маркетинг': flows_names[4],
             'научпоп': flows_names[5]}
    if flow in flows.keys():
        articles = ps.articles_by_flows(flows.get(flow))
        for article in articles:
            bot.send_message(message.chat.id, f'Название: {article}. Сылка: {articles[article]}.')
    else:
        bot.send_message(message.chat.id, f'Поток {flow} не найден.')


@bot.message_handler(commands=['articles'])
def get_articles(message):
    articles = ps.articles()
    for article in articles:
        bot.send_message(message.chat.id, f'Название: {article}. Сылка: {articles[article]}.')


@bot.message_handler(commands=['complaint'])
def get_text_for_complaint(message):
    bot.send_message(message.chat.id, 'Введите текст.')
    bot.register_next_step_handler_by_chat_id(message.chat.id, get_complaint)


def get_complaint(message):
    ps.complaint(message.chat.id, message.text)
    bot.send_message(message.chat.id, 'Текст сохранен.')


bot.polling()
