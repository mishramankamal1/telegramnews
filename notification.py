import telegram
import constant


def send_to_telegram(news):
    bot = telegram.Bot(token=constant.BOT_API_KEY)
    status = bot.send_message(chat_id=constant.MY_CHANNEL_NAME, text=news,
                              parse_mode=telegram.ParseMode.HTML, disable_web_page_preview=True)
