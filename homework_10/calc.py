import logging
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, ConversationHandler)

# Логирование
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

CHOICE, RATIONAL_ONE, RATIONAL_TWO, OPERATIONS_RATIONAL, OPERATIONS_COMPLEX, COMPLEX_ONE, COMPLEX_TWO = range(7)

def start(update, _):
    update.message.reply_text(f'Привет, {update.effective_user.first_name}, это - калькулятор.\nВыберите пожалуйста команду:\n')
    update.message.reply_text('1 - считаем рациональные числа \n2 - считаем комплесные числа\n')
    return CHOICE

def choice(update, context):
    user = update.message.from_user
    logger.info("%s выбрал %s", user.first_name, update.message.text)
    user_choice = update.message.text
    if user_choice in '12':
        if user_choice == '1':
            update.message.reply_text('Введите число:\n ')
            return RATIONAL_ONE
        if user_choice == '2':
            context.bot.send_message(update.effective_chat.id, 'Введите Re и Im первого числа через ПРОБЕЛ: ')
            return COMPLEX_ONE    
    else:
        update.message.reply_text('Ошибка ввода. Введите цифру операции: \n1 - считаем рациональные числа \n2 - считаем комплесные числа')

def rational_one(update, context):
    user = update.message.from_user
    logger.info("%s ввел число: %s", user.first_name, update.message.text)
    get_rational = update.message.text
    if get_rational.isdigit():
        get_rational = float(get_rational)
        context.user_data['rational_one'] = get_rational
        update.message.reply_text('Введите второе число:')
        return RATIONAL_TWO

    else:
        update.message.reply_text('Ошибка ввода. Введите рациональное число!')


def rational_two(update, context):
    user = update.message.from_user
    logger.info("%s ввел число: %s", user.first_name, update.message.text)
    get_rational = update.message.text
    if get_rational.isdigit():
        get_rational = float(get_rational)
        context.user_data['rational_two'] = get_rational
        update.message.reply_text('Выберите действие: \n\n\"+\" - для сложения; \n\"-\" - для вычетания; \n\"*\" - для умножения; \n\"/\" - для деления. \n')
        return OPERATIONS_RATIONAL
    else:
        update.message.reply_text('Ошибка ввода! Выберите действие: \n+ - для сложения; \n- - для вычетания; \n* - для умножения; \n/ - для деления. \n')


def operatons_rational(update, context):
    user = update.message.from_user
    logger.info(
        "%s выбрал операцию: \"%s\"", user.first_name, update.message.text)
    rational_one = context.user_data.get('rational_one')
    rational_two = context.user_data.get('rational_two')
    user_choice = update.message.text
    if user_choice in '+-/*':
        if user_choice == '+':
            result = rational_one + rational_two
        if user_choice == '-':
            result = rational_one - rational_two
        if user_choice == '*':
            result = rational_one * rational_two
        if user_choice == '/':
            try:
                result = rational_one / rational_two
            except:
                update.message.reply_text('Деление на ноль запрещено')
        update.message.reply_text(f'Результат = {result}\nПосчитать еще? /start')
        return ConversationHandler.END
    else:
        update.message.reply_text('Ошибка ввода. Выберите действие: \n+ - для сложения; \n- - для вычетания; \n* - для умножения; \n/ - для деления. \n' )

def complex_one(update, context):
    user = update.message.from_user
    logger.info(
        "%s ввел число: %s", user.first_name, update.message.text)
    user_choice = update.message.text
    test = user_choice.replace('-', '')
    if ' ' in test and (test.replace(' ', '')).isdigit():
        user_choice = user_choice.split(' ')
        complex_one = complex(int(user_choice[0]), int(user_choice[1]))
        context.user_data['complex_one'] = complex_one
        update.message.reply_text(f'Первое число {complex_one},  Введите Re и Im второго числа через ПРОБЕЛ: ')
        return COMPLEX_TWO
    else:
        update.message.reply_text('Ошибка ввода. Введите Re и Im первого числа через ПРОБЕЛ')


def complex_two(update, context):
    user = update.message.from_user
    logger.info(
        "%s ввел число: %s", user.first_name, update.message.text)
    user_choice = update.message.text
    test = user_choice.replace('-', '')
    if ' ' in test and (test.replace(' ', '')).isdigit():
        user_choice = user_choice.split(' ')
        complex_two = complex(int(user_choice[0]), int(user_choice[1]))
        context.user_data['complex_two'] = complex_two
        update.message.reply_text(
            f'Второе число {complex_two}, Выберите действие: \n\n\"+\" - для сложения; \n\"-\" - для вычетания; \n\"*\" - для умножения; \n\"/\" - для деления. \n')
        return OPERATIONS_COMPLEX
    else:
        update.message.reply_text('Ошибка ввода. Введите Re и Im второго числа через ПРОБЕЛ')

def operatons_complex(update, context):
    user = update.message.from_user
    logger.info(
        "%s выбрал операцию: \"%s\"", user.first_name, update.message.text)
    complex_one = context.user_data.get('complex_one')
    complex_two = context.user_data.get('complex_two')
    user_choice = update.message.text
    if user_choice in '+-/*':
        if user_choice == '+':
            result = complex_one + complex_two
        if user_choice == '-':
            result = complex_one - complex_two
        if user_choice == '*':
            result = complex_one * complex_two
        if user_choice == '/':
            try:
                result = complex_one / complex_two
            except:
                update.message.reply_text('Деление на ноль запрещено')
        update.message.reply_text(f'Результат = {result}\nПосчитать еще? /start')
        return ConversationHandler.END
    else:
        update.message.reply_text('Ошибка ввода. \n"+\" - для сложения; \n\"-\" - для вычетания; \n\"*\" - для умножения; \n\"/\" - для деления. \n')

def cancel(update, _):
    user = update.message.from_user
    logger.info("Пользователь %s отменил разговор.", user.first_name)
    update.message.reply_text('Спасибо, до свидания!')
    return ConversationHandler.END

if __name__ == '__main__':
    updater = Updater('5955516969:AAGI_AYviS6ddMTFrNo2SWs9VvvKI-iNGSg')
    dispatcher = updater.dispatcher

    conversation_handler = ConversationHandler(  
    
        entry_points=[CommandHandler('start', start)],
    
        states={
            CHOICE: [MessageHandler(Filters.text, choice)],
            RATIONAL_ONE: [MessageHandler(Filters.text, rational_one)],
            RATIONAL_TWO: [MessageHandler(Filters.text, rational_two)],
            OPERATIONS_RATIONAL: [MessageHandler(Filters.text, operatons_rational)],
            OPERATIONS_COMPLEX: [MessageHandler(Filters.text, operatons_complex)],
            COMPLEX_ONE: [MessageHandler(Filters.text, complex_one)],
            COMPLEX_TWO: [MessageHandler(Filters.text, complex_two)],
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    dispatcher.add_handler(conversation_handler)
    print('server start')
    updater.start_polling()
    updater.idle()