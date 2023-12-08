from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from game_dir.game_btn import stone_btn, leave_btn, paper_btn, spock_btn, lizard_btn, scissors_btn, menu_btn, repeat_search_btn,\
    invite_a_friend_btn, change_nickname_btn, games_statistics_btn, search_for_players_btn
from game_dir.game_clb import stone_clb, leave_clb, paper_clb, spock_clb, lizard_clb, scissors_clb, menu_clb, repeat_search_clb,\
    search_for_players_clb,change_nickname_clb,games_statistics_clb,invite_a_friend_clb




game_kb = InlineKeyboardMarkup()
game_kb.row(InlineKeyboardButton(text=stone_btn, callback_data=stone_clb))
game_kb.row(InlineKeyboardButton(text=scissors_btn, callback_data=scissors_clb))
game_kb.row(InlineKeyboardButton(text=paper_btn, callback_data=paper_clb))
game_kb.row(InlineKeyboardButton(text=lizard_btn, callback_data=lizard_clb))
game_kb.row(InlineKeyboardButton(text=spock_btn, callback_data=spock_clb))
game_kb.row(InlineKeyboardButton(text=leave_btn, callback_data=leave_clb))

timeout_kb = InlineKeyboardMarkup()
timeout_kb.row(InlineKeyboardButton(text=menu_btn, callback_data=menu_clb))
timeout_kb.row(InlineKeyboardButton(text=repeat_search_btn, callback_data=repeat_search_clb))


inl_kb_for_player_menu = InlineKeyboardMarkup()
inl_kb_for_player_menu.add(InlineKeyboardButton(text=invite_a_friend_btn, callback_data=invite_a_friend_clb))
inl_kb_for_player_menu.add(InlineKeyboardButton(text=search_for_players_btn, callback_data=search_for_players_clb))
inl_kb_for_player_menu.add(InlineKeyboardButton(text=games_statistics_btn, callback_data=games_statistics_clb))
inl_kb_for_player_menu.add(InlineKeyboardButton(text=change_nickname_btn, callback_data=change_nickname_clb))
