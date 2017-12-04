import unittest 
from jokenpo import play

class JokenpoTest(unittest.TestCase):

    def test_returns_false_when_tie(self):
        self.assertEqual('empatado', play('Pedra', 'Pedra'))
    
    def test_returns_true_when_rock_wins_scissors(self):
        self.assertEqual('jogador1',play('Pedra','Tesoura'))


    def test_returns_true_when_scissors_wins_paper(self):
        self.assertEqual('jogador1',play('Tesoura','Papel'))

   
