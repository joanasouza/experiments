"""
Jokenpo

As regras são as seguintes:
Pedra empata com Pedra e ganha de Tesoura
Tesoura empata com Tesoura e ganha de Papel
Papel empata com Papel e ganha de Pedra

empata ou ganha (False ou True)
"""
def play(player_one, player_two):
    if player_one == 'Pedra' and player_two == 'Tesoura':
        return 'jogador1'
    elif player_one == 'Tesoura' and player_two == 'Papel':
        return 'jogador1'
    return 'empatado'
    
    # return player_one == 'Pedra' and player_two == 'Tesoura'



# TODO: terminar as regras
# TODO: testes do jogador 2


