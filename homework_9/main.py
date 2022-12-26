import random

from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters

def isWin(arr, who):
    if (((arr[0] == who) and (arr[4] == who) and (arr[8] == who)) or
            ((arr[2] == who) and (arr[4] == who) and (arr[6] == who)) or
            ((arr[0] == who) and (arr[1] == who) and (arr[2] == who)) or
            ((arr[3] == who) and (arr[4] == who) and (arr[5] == who)) or
            ((arr[6] == who) and (arr[7] == who) and (arr[8] == who)) or
            ((arr[0] == who) and (arr[3] == who) and (arr[6] == who)) or
            ((arr[1] == who) and (arr[4] == who) and (arr[7] == who)) or
            ((arr[2] == who) and (arr[5] == who) and (arr[8] == who))):
        return True
    return False

def countUndefinedCells(cellArray):
    counter = 0
    for i in cellArray:
        if i == '❄':
            counter += 1
    return counter

def game(callBackData):
    message = 'Ваш ход'  
    alert = None

    buttonNumber = int(callBackData[0])  
    if not buttonNumber == 9: 
        charList = list(callBackData)  
        charList.pop(0)  
        if charList[buttonNumber] == '❄':  
            charList[buttonNumber] = '❎' 
            if isWin(charList, '❎'):  
                message = 'Вы победили'
            else:  
                if countUndefinedCells(charList) != 0: 
                    isCycleContinue = True
                    while (isCycleContinue):
                        rand = random.randint(0, 8)  
                        if charList[rand] == '❄':  
                            charList[rand] = '⭕'
                            isCycleContinue = False  
                            if isWin(charList, '⭕'):  
                                message = 'Победил maxiRage'
        else:
            alert = 'Нажимать можно только на ' + '❄'

        if countUndefinedCells(charList) == 0 and message == 'Ваш ход':
            message = 'Ничья'

        callBackData = ''
        for c in charList:
            callBackData += c

    if message == 'Вы победили' or message == 'Победил maxiRage' or message == 'Ничья':
        message += '\n'
        for i in range(0, 3):
            message += '\n | '
            for j in range(0, 3):
                message += callBackData[j + i * 3] + ' | '
        callBackData = None  

    return message, callBackData, alert

def getKeyboard(callBackData):
    keyboard = [[], [], []]  

    if callBackData != None:  
        for i in range(0, 3):
            for j in range(0, 3):
                keyboard[i].append(InlineKeyboardButton(callBackData[j + i * 3], callback_data=str(j + i * 3) + callBackData))

    return keyboard

def newGame(update, _):
    data = ''
    for i in range(0, 9):
        data += '❄'

    update.message.reply_text('Ваш ход', reply_markup=InlineKeyboardMarkup(getKeyboard(data)))

def button(update, _):
    query = update.callback_query
    callbackData = query.data 

    message, callbackData, alert = game(callbackData)
    if alert is None:  
        query.answer()  
        query.edit_message_text(text=message, reply_markup=InlineKeyboardMarkup(getKeyboard(callbackData)))
    else: 
        query.answer(text=alert, show_alert=True)

def help_command(update, _):
    update.message.reply_text('Играем в крестики-нолики\n' \
            'Команда /start или /new_game для новой игры')

if __name__ == '__main__':
    updater= Updater(token='5955516969:AAGI_AYviS6ddMTFrNo2SWs9VvvKI-iNGSg', use_context=True) 

    updater.dispatcher.add_handler(CommandHandler('start', newGame))
    updater.dispatcher.add_handler(CommandHandler('new_game', newGame))
    updater.dispatcher.add_handler(CommandHandler('help', help_command))
    updater.dispatcher.add_handler(MessageHandler(Filters.text, help_command))  
    updater.dispatcher.add_handler(CallbackQueryHandler(button))  
    print('server start')
    updater.start_polling()
    updater.idle()