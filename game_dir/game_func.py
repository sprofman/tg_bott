from datetime import datetime
from class_game import Game
from game_dir.game_messages import begin_game_msg, choose_item_msg, create_info_message_about_enemy, bad_search_msg,\
    begin_search_msg, player_menu_msg
from game_dir.game_inl_kb import game_kb, timeout_kb, inl_kb_for_player_menu


def search_game_func(bot, call, db, players_in_game, players_in_search):
    chat_id = call.message.chat.id
    msg_id = call.message.message_id
    bot.edit_message_text(chat_id=chat_id,
                          message_id=msg_id,
                          text=begin_search_msg)
    bot.answer_callback_query(callback_query_id=call.id,
                              text=begin_search_msg)
    players_in_search.append(chat_id)

    begin = datetime.now()
    end = begin

    while (end - begin).total_seconds() < 10 and chat_id not in players_in_game:
        end = datetime.now()
        len_list = len(players_in_search)
        B = players_in_search[:len_list // 2]
        if len_list % 2 == 0:
            C = players_in_search[len_list // 2:]
        else:
            C = players_in_search[len_list // 2:-1]

        for i in range(len(B)):
            first_player = B[i]
            second_player = C[i]
            if first_player not in players_in_game and second_player not in players_in_game:
                players_in_game[first_player] = Game(first_player, second_player)
                players_in_game[second_player] = Game(second_player, first_player)
                players_in_search.remove(first_player)
                players_in_search.remove(second_player)
                bot.send_message(chat_id=first_player,
                                 text=begin_game_msg)
                bot.send_message(chat_id=first_player,
                                 text=create_info_message_about_enemy(db,second_player))
                bot.send_message(chat_id=first_player,
                                 text=choose_item_msg,
                                 reply_markup=game_kb)

                bot.send_message(chat_id=second_player,
                                 text=begin_game_msg)
                bot.send_message(chat_id=second_player,
                                 text=create_info_message_about_enemy(db, first_player))
                bot.send_message(chat_id=second_player,
                                 text=choose_item_msg,
                                 reply_markup=game_kb)

                if chat_id not in players_in_search:
                    return None
    if chat_id not in players_in_search:
        return None
    players_in_search.remove(chat_id)
    bot.send_message(chat_id=chat_id,
                     text=bad_search_msg,
                     reply_markup=timeout_kb)


def back_to_menu_func(bot, call):
    chat_id = call.message.chat.id
    msg_id = call.message.message_id
    bot.edit_message_text(chat_id=chat_id,
                          message_id=msg_id,
                     text=player_menu_msg,
                     reply_markup=inl_kb_for_player_menu)
