import math
def final_score(players, game):
    """
    game.master_bpm
    game.round
    player.round_0_bpm
    player.round_1_bpm
    player.round_2_bpm
    player.round_3_bpm
    player.score
    player.score_summary 
    """
    player = max(players, lambda player: player.round_3_bpm)
    player.score += 10
    player.score_summary += "+10 for highest BPM"
    player.save()

    player = min(players, lambda player: player.round_3_bpm)
    player.score += 10
    player.score_summary += "+10 for lowest BPM"
    player.save()

def before_round_score(players, game):
    for player in players:
        if pbpm == game.master_bpm:
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
    if pbpm == game.master_bpm:
        bonus = 25
        player.score += bonus
        player.score_summary += "+%s Ding!,"%bonus
        player.save()

def after_round(players, game):
    players = list(players)
    def key(player):
        pbpm = getattr(player, "round_%s_bpm"%game.round)
        return math.abs(pbpm - game.master_bpm)
    players.sort(key = key)

    def key(player):
        pbpm = getattr(player, "round_%s_bpm"%game.round)
        return pbpm == game.master_bpm

    #players = filter(players, lambda player: player
    for player in players:
        bonus = 20
        player.score += bonus
        player.score_summary += "+%s Closest not on %s"%(bonus, game.round)
        player.save()
