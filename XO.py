#!/usr/bin/python3

import Telibrary

bot = Telibrary.bot('708650236:AAEkwbbaJlE4rGPqRO7wh2j_kAs9I0FZO-s','136172699',{'https': 'socks5h://127.0.0.1:9050'})

def Getit(Message):
    if Message['message']['text'] == '/start':
        bot.SendText(Message['message']['chat']['id'],
        'created by amoo amir.\nhttps://github.com/amooamirxd\nstart talking!',
        0,0,Message['message']['message_id'])
    elif Message['message']['text'][0] == '/':
        bot.SendText(Message['message']['chat']['id'],
        'DO NOT TRY TO SPAM! XD\n(messages shouldn\'t be started with "/" )',
        0,0,Message['message']['message_id'])
    else:
        bot.SendText(Message['message']['chat']['id'],
        'Sent! :)',
        0,0,Message['message']['message_id'])
        bot.Forward(bot.AdminID,
        Message['message']['chat']['id'],
        Message['message']['message_id'])

def Bemessenger(Message):
    bot.SendText(Message['message']['reply_to_message']['forward_from']['id'],
    Message['message']['text'])

updater = open('/home/amoooamir/github/TG-messenger/tmp.txt','r')
updateid = updater.readline()

while True:
    res = bot.Update(updateid)
    if res.json()['result'] != 0:
        for i in res.json()['result']:
            if i['message']['from']['id'] != int(bot.AdminID):
                Getit(i)
                updateid = i['update_id'] + 1
            else:
                try:
                    Bemessenger(i)
                        updateid = i['update_id'] + 1
                except:
                    pass
            updater.close()
            updater = open('/home/amoooamir/github/TG-messenger/tmp.txt','w')
            updater.writelines(str(updateid))
            updater.close()
