from pyrogram import Client, filters
from utils import check_user, multi_rec, getChannels

app = Client(
    "http://t.me/Free_de_la_hoya_Recording_bot",
    bot_token = "5628562557:AAFPXFDiast8O37JVvO_rtWxs-3t9vXeboc",
    api_id = 17038143,
    api_hash = "c1705f4cf711329ea025772dfd7057e0"
)



@app.on_message(filters.incoming & filters.command(['multirec']) & filters.incoming & filters.text)
def multirec_handler(app, message):

    auth_user = check_user(message)
    if auth_user is None:
        return

    if len(message.text.split()) < 3:
        message.reply_text("<b>Syntax: </b>`/multirec [channelName] [duration] | [filename]`")
        return

    multi_rec(app, message)

@app.on_message(filters.incoming & filters.command(['channels']) & filters.text)
def show_channels_handler(app, message):

    auth_user = check_user(message)
    if auth_user is None:
        return


    getChannels(app, message)


@app.on_message(filters.command(['start']) & filters.text)
def start_handler(app, message):

    if len(message.text.split()) < 3:
        message.reply_text("<b>A Multi Mega Recording Telegram bot by Team Disney Cartoons</b>\n\n<b>Made with Love by @Free_De_La_Hoya_Official</b>")
        return
    # Don't remove Conan76 from here, Resepct the Developer...
    
app.run()
