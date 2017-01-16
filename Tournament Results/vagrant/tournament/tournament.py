#!/usr/bin/env python
# tournament.py -- implementation of a Swiss-system tournament
"""
Functions that tournament_test.py will run unit tests on.
This program represents the first two rounds of a Swiss Tournament.
"""


import psycopg2




def deleteMatches():

    """Removes all results records such as wins, lossses and match
    id's from the database.
    'query' stores the postgresql commands to be executed by the
    cursor object which wipes the table.
    db_connect() commits changes and closes the database.
    """

    DB = psycopg2.connect("dbname=tournament")
    c = DB.cursor()
    c.execute("DELETE FROM results")
    DB.commit()
    DB.close()


def deletePlayers():

    """Removes all the player records from the database.
    'query' stores the posgresql commands to be executed by the
    cursor object which wipes the table.
    db_connect() commits changes and closes the database.
    """

    DB = psycopg2.connect("dbname=tournament")
    c = DB.cursor()
    query = ("DELETE FROM players;")
    c.execute(query)
    DB.commit()
    DB.close()


def countPlayers():

    """Returns the number of players ready to play a match.
    'query' stores the postgresql commands to be executed by the
    cursor object which will return a count of all the players
    in the players table.
    'player_count' stores the list of  players tuples
    returned by database.
    db_connect() closes the database.
    """

    DB = psycopg2.connect("dbname = tournament")
    c = DB.cursor()
    c.execute("SELECT count(players.player_id) AS player_count FROM players")
    player_count = c.fetchone()[0]
    DB.close()
    return player_count


def registerPlayer(name):

    """Adds a player to the tournament database.
    Args:
      name: the player's full name (need not be unique).
      player_id is set by the database.
    'query' stores the postgresql commands to be executed by the
    cursor object which inserts a new player name and id into the
    table.
    query parameter 'name' is used to protect the database from
    sql based attacks.
    db_connect() commits changes and closes the database.
    """

    DB = psycopg2.connect("dbname = tournament") 
    c = DB.cursor()
    query = ("INSERT INTO players(player_id, name) VALUES (default, %s);")
    c.execute(query, (name,))
    DB.commit()
    DB.close()


def playerStandings():

    """Returns a list of the players and their win records, sorted by wins.
    The first entry in the list should be the player in first place,
    or a player tied for first place if there is currently a tie.
    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    'query' stores the postgresql commands to be executed by the
    cursor object which selects all the data from the
    standings view.
    'matches' collects the data as a list of tuples and returns it.
    db_connect() commits changes and closes the database.
    """

    DB = psycopg2.connect("dbname = tournament") 
    c = DB.cursor()
    c.execute("SELECT * FROM position")
    matches = c.fetchall()
    DB.close()
    return matches


def reportMatch(winner, loser):

    """Records the outcome of a single match between two players.
    Args:
      winner:  player_id of the player who won
      loser:  player_id of the player who lost
    'query' stores the postgresql commands to be executed by the
    cursor object which inserts a player name and id as winner
    and loser, into the results table.
    query parameters 'winner' and 'loser' are used to protect the database from
    sql based attacks.
    db_connect() commits changes and closes the database.
    """

    DB = psycopg2.connect("dbname = tournament") 
    c = DB.cursor()
    query = ("INSERT INTO results(match_id, winner, loser) VALUES (default, %s, %s);")
    c.execute(query, (winner, loser,))
    DB.commit()
    DB.close()


def swissPairings():

    """Returns a list of pairs of players for the next round of a match.
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's player_id
        name1: the first player's name
        id2: the second player's player_id
        name2: the second player's name
    'query' stores the postgresql commands to be executed by the
    c object which collects a list of players tuples ordered
    by total_wins column.
    'win_pair_list' stores the list of tuples returned by c execution.
        eg: [(5202, 'Twilight Sparkle'), (5204, 'Applejack'),
             (5203, 'Fluttershy'), (5205, 'Pinkie Pie')]
    The 'if' statement will check to make sure there are is an even number
    of tuples in the tournament list.
    The 'for' loop will loop over the list of tuples for the length of the list
    making 2 steps for each loop.
    'collect_players' is assigned the value of 1st and 3rd, 2 and 4th players
     to create a list of at least two tuples of player pairings.
        eg: win_pair_list[i][0]:   player 1,3 ids
            win_pair_list[i][1]:   player 1,3 names
            win_pair_list[i+1][0]: player 2,4 ids
            win_pair_list[i+1][1]: player 2,4 names
    The loop will return a pair of tuples for the unit test to unpack:
        eg: [(5232, 'Twilight Sparkle', 5234, 'Applejack'),
             (5233, 'Fluttershy', 5235, 'Pinkie Pie')]
    """

    pair = []

    DB = psycopg2.connect("dbname = tournament")
    c = DB.cursor()
    c.execute("SELECT player_id, name FROM position ORDER BY wins DESC")
    win_pair_list = c.fetchall()

    for i in range(0, len(win_pair_list), 2):
        collect_players = win_pair_list[i][0], win_pair_list[i][1], \
                              win_pair_list[i+1][0], win_pair_list[i+1][1]
        pair.append(collect_players)
    return pair

    
    DB.close()