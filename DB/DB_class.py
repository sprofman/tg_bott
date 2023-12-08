import sqlalchemy as db

class DB:
    def __init__(self):

        self.engine = db.create_engine('sqlite:///DB/game_db.db', pool_pre_ping=True)
        self.connection = self.engine.connect()
        self.metadata = db.MetaData()

        self.players_table = db.Table('players', self.metadata,
                                 db.Column('ind', db.Integer, primary_key=True, autoincrement=True),
                                 db.Column('chat_id', db.Integer),
                                 db.Column('nikname', db.Text),
                                 db.Column('in_search', db.Boolean),
                                 db.Column('in_game', db.Boolean),
                                 db.Column('wins', db.Integer),
                                 db.Column('loses', db.Integer),
                                 db.Column('stones', db.Integer),
                                 db.Column('scissors', db.Integer),
                                 db.Column('paper', db.Integer),
                                 db.Column('lizard', db.Integer),
                                 db.Column('spock', db.Integer),
                                 db.Column('MMR', db.Text),
                                 )

        self.games_table = db.Table('games', self.metadata,
                                 db.Column('ind', db.Integer, primary_key=True, autoincrement=True),
                                 db.Column('player_1', db.Text),
                                 db.Column('player_2', db.Text),
                                 db.Column('round_1', db.Text),
                                 db.Column('round_2', db.Text),
                                 db.Column('round_3', db.Text)
                                 )

        self.stat_table = db.Table('stat', self.metadata,
                                    db.Column('games', db.Integer),
                                    db.Column('players', db.Text),
                                    db.Column('stones', db.Integer),
                                    db.Column('scissors', db.Integer),
                                    db.Column('paper', db.Integer),
                                    db.Column('lizard', db.Integer),
                                    db.Column('spock', db.Integer),
                                    )
        self.metadata.create_all(self.engine)


    def chat_id_in_DB(self, chat_id):
        poles = self.players_table.c
        selection_query = db.select(poles['chat_id']).where(poles['chat_id'] == chat_id)

        result = self.connection.execute(selection_query).fetchall()

        return True if len(result) != 0 else False


    def nick_in_DB(self, nick):
        poles = self.players_table.c
        selection_query = db.select(poles['nikname']).where(poles['nikname'] == nick)

        result = self.connection.execute(selection_query).fetchall()

        return True if len(result) != 0 else False

    def add_player_in_DB(self, nick, chat_id):
        insertion_query = self.players_table.insert().values([
            {'chat_id': chat_id,
             'nikname': nick,
             'in_search': False,
             'in_game': False,
             'wins': 0,
             'loses': 0,
             'stones': 0,
             'scissors': 0,
             'paper': 0,
             'lizard': 0,
             'spock': 0,
             'MMR': 0,
             }])
        self.connection.execute(insertion_query)
        self.connection.commit()


    def select_info_about_enemy(self, chat_id):
        poles = self.players_table.c
        selection_query = db.select(poles['nikname'],
                                    poles['wins'],
                                    poles['loses']
                                    ).where(poles['chat_id'] == chat_id)

        result = self.connection.execute(selection_query).fetchall()[0]
        names = ['nickname', 'wins', 'loses']
        result = dict(zip(names, result))
        return result