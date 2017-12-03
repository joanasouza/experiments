def test_returns_false_when_tie():
    player_one = 'Pedra'
    player_two = 'Pedra'
    result = jokenpo_play(player_one, player_two)
    
    assert result == 'empatado'

def test_returns_true_when_rock_wins_scissors():
    player_one = 'Pedra'
    player_two = 'Tesoura'
    result = jokenpo_play(player_one, player_two)

    assert result == 'jogador1'

def test_returns_true_when_scissors_wins_paper():
    player_one = 'Tesoura'
    player_two = 'Papel'
    result = jokenpo_play(player_one, player_two)

    assert result == 'jogador1'
