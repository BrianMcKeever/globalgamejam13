import math
def final_score(players, game):
    player = game.max_bpm_player
    bonus = 50
    player.score += bonus
    player.score_summary += "+%s for highest BPM of rounds"%bonus
    player.save()

    player = game.min_bpm_player
    bonus = 50
    player.score += bonus
    player.score_summary += "+%s for lowest BPM of rounds"%bonus
    player.save()

def before_round_score(players, game):
    for player in players:
        pbpm = getattr(player, "round_%s_bpm"%game.round)
        mbpm = getattr(game, "round_%s_master_bpm"%game.round)
        difference = math.fabs(pbpm - mbpm)
        points = 0
        if pbpm == mbpm:
            bonus = 50
            points += bonus
            player.score_summary += "+%s Bullseye!,"%bonus
        elif difference <= 5:
            bonus = 20
            points += bonus
            player.score_summary += "+%s Almost!,"%bonus
        elif difference <= 10:
            bonus = 10
            points += bonus
            player.score_summary += "+%s Close!,"%bonus
        player.score += points
        player.save()

def during_round(player, game):
    pbpm = getattr(player, "round_%s_bpm"%game.round)
    mbpm = getattr(game, "round_%s_master_bpm"%game.round)
    if pbpm == mbpm:
        bonus = 25
        player.score += bonus
        player.score_summary += "+%s Direct hit!,"%bonus
        player.save()

def after_round(players, game):
    players = list(players)
    mbpm = getattr(game, "round_%s_master_bpm"%game.round)
    def key(player):
        pbpm = getattr(player, "round_%s_bpm"%game.round)
        return math.fabs(pbpm - mbpm)
    players.sort(key = key)

    def key(player):
        pbpm = getattr(player, "round_%s_bpm"%game.round)
        return pbpm != mbpm

    players = filter(key, players)
    length = len(players)
    if length >= 1:
        bonus = 20
        players[0].score += bonus
        players[0].score_summary += "+%s Closest not on.,"%bonus
        players[0].save()
    if length >= 2:
        bonus = 10
        players[1].score += bonus
        players[1].score_summary += "+%s Second closest not on.,"%bonus
        players[1].save()
    if length >= 3:
        bonus = 5
        players[2].score += bonus
        players[2].score_summary += "+%s Third closest not on.,"%bonus
        players[2].save()
