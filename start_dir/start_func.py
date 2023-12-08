from start_dir.start_inl_kb import inl_kb_for_player_menu
from start_dir.start_messages import player_menu_msg, nickname_query_msg, nickname_repeat_msg
from next_steps import next_step_continue, next_step_repeat




def start_func(bot, message, DB):
    chat_id = message.chat.id
    user_in_DB = DB.chat_id_in_DB(chat_id)
    if user_in_DB:
        bot.send_message(chat_id=chat_id,
                         text=player_menu_msg,
                         reply_markup=inl_kb_for_player_menu)
        return None, None
    else:
        msg = bot.send_message(chat_id=chat_id,
                         text=nickname_query_msg)
        return msg, next_step_continue

def nickname_input_func(bot, message, DB):
    chat_id = message.chat.id
    nick = message.text
    nick_in_DB = DB.nick_in_DB(nick)
    if nick_in_DB:
        msg = bot.send_message(chat_id=chat_id,
                               text=nickname_repeat_msg)
        return msg, next_step_repeat
    else:
        DB.add_player_in_DB(nick, chat_id)
        bot.send_message(chat_id=chat_id,
                         text=player_menu_msg,
                         reply_markup=inl_kb_for_player_menu)
        return None, None
