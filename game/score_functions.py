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

def round_score(players, game):
    smallest_difference = 10000000000
    closest_player = []
    for player in players:
        points = 0
        pbpm = getattr(player, "round_%s_bpm"%game.round)
        difference = math.abs(pbpm - game.master_bpm)
        if smallest_difference > difference:
            smallest_difference = difference
            closest_players = [player]
        elif smallest_difference == difference:
            closest_players.append(player)

        if game.round == 0:
            if pbpm == game.master_bpm:
                points += 30
                player.score_summary += "+30 Bullseye!,"
            elif difference <= 5:
                points += 10
                player.score_summary += "+10 Almost!,"
            elif difference <= 10:
                points += 5
                player.score_summary += "+5 Close!,"
        else:
            if pbpm == game.master_bpm:
                points += 60
                player.score_summary += "+60 Bullseye!,"
            elif difference <= 5:
                points += 25
                player.score_summary += "+25 Almost!,"
            elif difference <= 10:
                points += 20
                player.score_summary += "+20 Close!,"
        player.score += points
        player.save()

    for player in closest_players:
        player.score += 10
        player.score_summary += "+10 Closest in round %s"%game.round
        player.save()
