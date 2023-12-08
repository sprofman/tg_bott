from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from start_dir.start_btn import search_for_players_btn, change_nickname_btn, games_statistics_btn,\
    invite_a_friend_btn
from start_dir.start_clb import change_nickname_clb, games_statistics_clb, invite_a_friend_clb,\
    search_for_players_clb









inl_kb_for_player_menu = InlineKeyboardMarkup()
inl_kb_for_player_menu.add(InlineKeyboardButton(text=invite_a_friend_btn, callback_data=invite_a_friend_clb))
inl_kb_for_player_menu.add(InlineKeyboardButton(text=search_for_players_btn, callback_data=search_for_players_clb))
inl_kb_for_player_menu.add(InlineKeyboardButton(text=games_statistics_btn, callback_data=games_statistics_clb))
inl_kb_for_player_menu.add(InlineKeyboardButton(text=change_nickname_btn, callback_data=change_nickname_clb))
