import unittest
import sys
import os

# Añadir el directorio padre al path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from bet_manager import BetManager

class TestBetManager(unittest.TestCase):
    
    def setUp(self):
        # Crear una instancia nueva para cada prueba
        self.bet_manager = BetManager()
        
    def test_place_bet(self):
        # Probar colocar una apuesta válida
        result = self.bet_manager.place_bet("player1", 100)
        self.assertTrue(result)
        self.assertEqual(self.bet_manager.get_player_bet("player1"), 100)
        self.assertEqual(self.bet_manager.get_total_pot(), 100)
        
    def test_place_invalid_bet(self):
        # Probar colocar una apuesta inválida (cantidad negativa)
        result = self.bet_manager.place_bet("player1", -50)
        self.assertFalse(result)
        self.assertEqual(self.bet_manager.get_player_bet("player1"), 0)
        self.assertEqual(self.bet_manager.get_total_pot(), 0)
        
        # Probar colocar una apuesta de cero
        result = self.bet_manager.place_bet("player1", 0)
        self.assertFalse(result)
        self.assertEqual(self.bet_manager.get_player_bet("player1"), 0)
        self.assertEqual(self.bet_manager.get_total_pot(), 0)
        
    def test_multiple_bets(self):
        # Probar múltiples apuestas de diferentes jugadores
        self.bet_manager.place_bet("player1", 100)
        self.bet_manager.place_bet("player2", 200)
        self.bet_manager.place_bet("player3", 150)
        
        self.assertEqual(self.bet_manager.get_player_bet("player1"), 100)
        self.assertEqual(self.bet_manager.get_player_bet("player2"), 200)
        self.assertEqual(self.bet_manager.get_player_bet("player3"), 150)
        self.assertEqual(self.bet_manager.get_total_pot(), 450)
        
    def test_get_player_bet_nonexistent(self):
        # Probar obtener la apuesta de un jugador que no ha apostado
        self.assertEqual(self.bet_manager.get_player_bet("nonexistent"), 0)
        
    def test_distribute_winnings_single_winner(self):
        # Configurar algunas apuestas
        self.bet_manager.place_bet("player1", 100)
        self.bet_manager.place_bet("player2", 200)
        self.bet_manager.place_bet("player3", 150)
        
        # Distribuir ganancias a un solo ganador
        winnings = self.bet_manager.distribute_winnings(["player1"])
        
        # Verificar que el ganador recibe todo el bote
        self.assertEqual(winnings["player1"], 450)
        
        # Verificar que el bote y las apuestas se reiniciaron
        self.assertEqual(self.bet_manager.get_total_pot(), 0)
        self.assertEqual(self.bet_manager.get_player_bet("player1"), 0)
        self.assertEqual(self.bet_manager.get_player_bet("player2"), 0)
        self.assertEqual(self.bet_manager.get_player_bet("player3"), 0)
        
    def test_distribute_winnings_multiple_winners(self):
        # Configurar algunas apuestas
        self.bet_manager.place_bet("player1", 100)
        self.bet_manager.place_bet("player2", 200)
        self.bet_manager.place_bet("player3", 150)
        
        # Distribuir ganancias a múltiples ganadores
        winnings = self.bet_manager.distribute_winnings(["player1", "player3"])
        
        # Verificar que los ganadores reciben partes iguales del bote
        self.assertEqual(winnings["player1"], 225)  # 450 / 2
        self.assertEqual(winnings["player3"], 225)  # 450 / 2
        
    def test_distribute_winnings_no_winners(self):
        # Configurar algunas apuestas
        self.bet_manager.place_bet("player1", 100)
        self.bet_manager.place_bet("player2", 200)
        
        # Intentar distribuir ganancias sin ganadores
        winnings = self.bet_manager.distribute_winnings([])
        
        # Verificar que no se distribuyen ganancias
        self.assertEqual(winnings, {})
        
        # Las apuestas y el bote deben permanecer intactos
        self.assertEqual(self.bet_manager.get_total_pot(), 300)
        self.assertEqual(self.bet_manager.get_player_bet("player1"), 100)
        self.assertEqual(self.bet_manager.get_player_bet("player2"), 200)
        
    def test_reset(self):
        # Configurar algunas apuestas
        self.bet_manager.place_bet("player1", 100)
        self.bet_manager.place_bet("player2", 200)
        
        # Reiniciar el gestor de apuestas
        self.bet_manager.reset()
        
        # Verificar que se reiniciaron las apuestas y el bote
        self.assertEqual(self.bet_manager.get_total_pot(), 0)
        self.assertEqual(self.bet_manager.get_player_bet("player1"), 0)
        self.assertEqual(self.bet_manager.get_player_bet("player2"), 0)
        
if __name__ == '__main__':
    unittest.main()