import telebot
from telebot.types import CallbackQuery
from config import token
from start_dir.start_func import start_func, nickname_input_func
from DB.DB_class import DB
from next_steps import next_step_continue, next_step_repeat
from start_dir.start_clb import search_for_players_clb
from game_dir.game_clb import repeat_search_clb, menu_clb
from game_dir.game_func import search_game_func, back_to_menu_func


bot = telebot.TeleBot(token)
db = DB()

players_in_search = []
players_in_game = {}

@bot.message_handler(commands=["start"])
def start_hand(message):
    msg, next_step = start_func(bot, message, db)
    if next_step == next_step_continue:
        bot.register_next_step_handler(msg, nickname_input_hand)

def nickname_input_hand(message):
    msg, next_step = nickname_input_func(bot, message, db)
    if next_step == next_step_repeat:
        bot.register_next_step_handler(msg, nickname_input_hand)


@bot.callback_query_handler(func=lambda call: call.data in [search_for_players_clb, repeat_search_clb])
def search_player_hand(call:CallbackQuery):
    search_game_func(bot,
                     call,
                     db,
                     players_in_game,
                     players_in_search)

@bot.callback_query_handler(func=lambda call: call.data == menu_clb)
def back_to_menu_hand(call:CallbackQuery):
    back_to_menu_func(bot, call)

if __name__ == "__main__":
    bot.polling(none_stop=True)

