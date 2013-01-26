def final_score(player, game):
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
    player.save()

def round_score(player, game):
    player.score += 40
    player.score_summary += "+40 points for great justice"
    player.save()

