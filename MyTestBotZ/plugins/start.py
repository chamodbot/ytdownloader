from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    
    welcomed = f""""""
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
