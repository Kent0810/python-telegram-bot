
from typing import Final
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, filters, MessageHandler


class Expend:
    def __init__(self) -> None:
        self.expendType = ""
        self.name = ""
        self.price = 0
        self.description = ""

    def set_expend_info(self, type, name, price, description) -> None:
        self.expendType = type
        self.name = name
        self.price = price
        self.description = description

    def print_expend_info(self) -> None:
        print(self.expendType, self.name, self.price, self.description)


Token: Final = "6619084343:AAHG8Qv0NGjEVULXclR2Z3XwhIoDLB2_E0c"

BOT_USERNAME: Final = "@KentExpendBot"


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! Thanks for using ExpendBot! I am Kent!")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Yes, I am Kent! Please type in your expend in this form: /ex [IN_OUT], [EXPEND_NAME], [EXPEND_PRICE], [ADDITION_INFO]")


def handle_response(text: str) -> str:
    processed: str = text.lower()

    if 'em iu anh' in processed:
        return 'Anh chi iu minh Khanh Phuong thui!'
    return "Sorry, I didn't understand what you just said T.T"


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    response: str = handle_response(text)
    print('Bot:', response)
    await update.message.reply_text(response)


async def send_expend(update: Update, context: ContextTypes.DEFAULT_TYPE):
    expend = Expend()

    responseArray = ' '.join(context.args).split(',')
    responseArray = [value.strip() for value in responseArray]

    if (len(responseArray) != 4):
        await update.message.reply_text("Please fill in all the infomation, or type /help to get help, Thank You :>")
        return

    expend.set_expend_info(
        responseArray[0], responseArray[1], responseArray[2], responseArray[3])

    expend.print_expend_info()

    await update.message.reply_text("Thank You, I got it!")


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')

if __name__ == '__main__':
    print("STARTING BOT")
    app = ApplicationBuilder().token(Token).build()

    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('ex', send_expend))

    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    app.add_error_handler(error)

    app.run_polling(poll_interval=2)
