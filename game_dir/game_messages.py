begin_game_msg = "Начало игры"
choose_item_msg = "Выбирете предмет"
bad_search_msg = "Не удалось найти соперника"
begin_search_msg = "Поиск соперника"
player_menu_msg = "Меню игрока, выберите действие"
def create_info_message_about_enemy(db, chat_id):
    infodict = db.select_info_about_enemy(chat_id)
    text = f'Ваш соперник {infodict["nickname"]}\nКоличество побед {infodict["wins"]}\nКоличество поражений {infodict["loses"]}'
    return text