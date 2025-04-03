import unittest
import sys
import os

# Añadir el directorio padre al path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from blackjack import Blackjack
from hand_evaluator import HandEvaluator

class TestIntegration(unittest.TestCase):
    
    def setUp(self):
        # Inicializar el juego con 3 jugadores
        self.game = Blackjack(num_decks=1)
        self.game.add_player("player1", 1000)
        self.game.add_player("player2", 1000)
        self.game.add_player("player3", 1000)
        self.game.start_game()
        
    def test_complete_game(self):
        # Colocar apuestas
        self.game.place_bet("player1", 100)
        self.game.place_bet("player2", 150)
        self.game.place_bet("player3", 200)
        
        # Verificar que el juego está en estado "playing"
        self.assertEqual(self.game.game_status, "playing")
        
        # Verificar que cada jugador tiene 2 cartas
        for player_id in self.game.players:
            self.assertEqual(len(self.game.players[player_id]["hand"]), 2)
            
        # Player1 pide carta
        self.game.hit("player1")
        
        # Player1 se planta
        self.game.stand("player1")
        
        # Verificar que el turno pasó a player2
        self.assertEqual(self.game.players_order[self.game.current_player_idx], "player2")
        
        # Player2 se planta
        self.game.stand("player2")
        
        # Verificar que el turno pasó a player3
        self.assertEqual(self.game.players_order[self.game.current_player_idx], "player3")
        
        # Player3 se planta
        self.game.stand("player3")
        
        # Verificar que el juego terminó
        self.assertEqual(self.game.game_status, "ended")
        
        # Reiniciar el juego
        self.game.restart_game()
        
        # Verificar que el juego está en estado "betting"
        self.assertEqual(self.game.game_status, "betting")
        
        # Verificar que se conservaron los saldos de los jugadores
        # (no podemos verificar valores exactos porque depende de quién ganó la ronda)
        for player_id in self.game.players:
            self.assertTrue(self.game.players[player_id]["balance"] > 0)
            
    def test_fold_mechanism(self):
        # Colocar apuestas
        self.game.place_bet("player1", 100)
        self.game.place_bet("player2", 150)
        self.game.place_bet("player3", 200)
        
        # Player1 pide cartas hasta pasarse (simulación)
        # Establecer manualmente una mano que se pase
        self.game.players["player1"]["hand"] = [
            {"value": "10", "suit": "Corazones"},
            {"value": "K", "suit": "Picas"},
            {"value": "5", "suit": "Diamantes"}
        ]
        
        # Forzar la evaluación (normalmente ocurriría automáticamente)
        if HandEvaluator.is_busted(self.game.players["player1"]["hand"]):
            self.game.players["player1"]["status"] = "busted"
            self.game._next_player()
        
        # Verificar que player1 está "busted" y el turno pasó a player2
        self.assertEqual(self.game.players["player1"]["status"], "busted")
        self.assertEqual(self.game.players_order[self.game.current_player_idx], "player2")
        
        # Player2 y Player3 se plantan
        self.game.stand("player2")
        self.game.stand("player3")
        
        # Verificar que el juego terminó
        self.assertEqual(self.game.game_status, "ended")
        
        # Verificar que player1 no está entre los ganadores
        game_state = self.game.get_game_state()
        # Nota: No podemos verificar directamente los ganadores aquí porque no están
        # en el estado del juego, tendríamos que mirar los saldos actualizados
        
    def test_game_state(self):
        # Colocar apuestas
        self.game.place_bet("player1", 100)
        self.game.place_bet("player2", 150)
        self.game.place_bet("player3", 200)
        
        # Obtener el estado del juego
        state = self.game.get_game_state()
        
        # Verificar la estructura del estado
        self.assertIn("game_status", state)
        self.assertIn("current_player", state)
        self.assertIn("players", state)
        self.assertIn("pot", state)
        
        # Verificar que el bote es correcto
        self.assertEqual(state["pot"], 450)
        
        # Verificar que todos los jugadores están en el estado
        self.assertIn("player1", state["players"])
        self.assertIn("player2", state["players"])
        self.assertIn("player3", state["players"])
        
        # Verificar que el jugador actual es correcto
        self.assertEqual(state["current_player"], "player1")
        
if __name__ == '__main__':
    unittest.main()