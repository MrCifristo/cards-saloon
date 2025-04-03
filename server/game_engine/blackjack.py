from deck_manager import DeckManager
from hand_evaluator import HandEvaluator
from bet_manager import BetManager
import json
import sys

class Blackjack:
    """
    Clase principal que maneja la lógica del juego de Blackjack.
    """
    
    def __init__(self, num_decks=1):
        """
        Inicializa el juego de Blackjack.
        
        Args:
            num_decks (int): Número de mazos a utilizar.
        """
        self.deck_manager = DeckManager(num_decks)
        self.bet_manager = BetManager()
        self.players = {}  # {player_id: {"hand": [], "status": "playing"}}
        self.game_status = "waiting"  # waiting, betting, playing, ended
        self.current_player_idx = 0
        self.players_order = []
        
    def add_player(self, player_id, initial_balance=1000):
        """
        Añade un jugador al juego.
        
        Args:
            player_id: Identificador único del jugador.
            initial_balance (float): Saldo inicial del jugador.
            
        Returns:
            bool: True si el jugador se añadió correctamente, False en caso contrario.
        """
        if player_id in self.players:
            return False
            
        self.players[player_id] = {
            "hand": [],
            "status": "waiting",
            "balance": initial_balance
        }
        self.players_order.append(player_id)
        return True
        
    def remove_player(self, player_id):
        """
        Elimina un jugador del juego.
        
        Args:
            player_id: Identificador único del jugador.
            
        Returns:
            bool: True si el jugador se eliminó correctamente, False en caso contrario.
        """
        if player_id not in self.players:
            return False
            
        del self.players[player_id]
        self.players_order.remove(player_id)
        return True
        
    def start_game(self):
        """
        Inicia una nueva ronda de juego.
        
        Returns:
            bool: True si el juego se inició correctamente, False en caso contrario.
        """
        if len(self.players) < 2:
            return False
            
        # Reiniciar el estado del juego
        self.deck_manager.reset()
        self.bet_manager.reset()
        
        for player_id in self.players:
            self.players[player_id]["hand"] = []
            self.players[player_id]["status"] = "betting"
            
        self.game_status = "betting"
        return True
        
    def place_bet(self, player_id, amount):
        """
        Registra la apuesta de un jugador.
        
        Args:
            player_id: Identificador único del jugador.
            amount (float): Cantidad apostada.
            
        Returns:
            bool: True si la apuesta es válida, False en caso contrario.
        """
        if player_id not in self.players:
            return False
            
        if self.game_status != "betting":
            return False
            
        player = self.players[player_id]
        
        if amount > player["balance"]:
            return False
            
        success = self.bet_manager.place_bet(player_id, amount)
        
        if success:
            player["balance"] -= amount
            player["status"] = "ready"
            
            # Verificar si todos los jugadores han apostado
            all_ready = all(p["status"] == "ready" for p in self.players.values())
            if all_ready:
                self._deal_initial_cards()
                self.game_status = "playing"
                self.current_player_idx = 0
                
        return success
        
    def _deal_initial_cards(self):
        """Reparte las cartas iniciales a cada jugador."""
        # Repartir 2 cartas a cada jugador
        for _ in range(2):
            for player_id in self.players_order:
                card = self.deck_manager.deal_card()
                self.players[player_id]["hand"].append(card)
                
        # Actualizar el estado de los jugadores
        for player_id in self.players:
            self.players[player_id]["status"] = "playing"
            
    def hit(self, player_id):
        """
        Solicita una carta adicional para el jugador.
        
        Args:
            player_id: Identificador único del jugador.
            
        Returns:
            dict: Estado actualizado del jugador, o None si la acción no es válida.
        """
        if not self._is_valid_action(player_id, "hit"):
            return None
            
        player = self.players[player_id]
        card = self.deck_manager.deal_card()
        player["hand"].append(card)
        
        # Verificar si el jugador se ha pasado de 21
        if HandEvaluator.is_busted(player["hand"]):
            player["status"] = "busted"
            self._next_player()
            
        return {
            "player_id": player_id,
            "card": card,
            "hand_value": HandEvaluator.calculate_hand_value(player["hand"]),
            "status": player["status"]
        }
        
    def stand(self, player_id):
        """
        El jugador se planta con su mano actual.
        
        Args:
            player_id: Identificador único del jugador.
            
        Returns:
            dict: Estado actualizado del jugador, o None si la acción no es válida.
        """
        if not self._is_valid_action(player_id, "stand"):
            return None
            
        player = self.players[player_id]
        player["status"] = "stand"
        
        self._next_player()
        
        return {
            "player_id": player_id,
            "hand_value": HandEvaluator.calculate_hand_value(player["hand"]),
            "status": player["status"]
        }
        
    def _next_player(self):
        """Pasa al siguiente jugador o finaliza el juego si todos han jugado."""
        self.current_player_idx += 1
        
        # Si todos los jugadores han jugado, finalizar la ronda
        if self.current_player_idx >= len(self.players_order):
            self._end_round()
        
    def _is_valid_action(self, player_id, action):
        """
        Verifica si una acción es válida en el estado actual del juego.
        
        Args:
            player_id: Identificador único del jugador.
            action (str): Acción a verificar ('hit' o 'stand').
            
        Returns:
            bool: True si la acción es válida, False en caso contrario.
        """
        if player_id not in self.players:
            return False
            
        if self.game_status != "playing":
            return False
            
        if self.players_order[self.current_player_idx] != player_id:
            return False
            
        player = self.players[player_id]
        
        if player["status"] != "playing":
            return False
            
        return True
        
    def _end_round(self):
        """Finaliza la ronda actual y determina al ganador."""
        self.game_status = "ended"
        winners = self._determine_winners()
        
        # Distribuir las ganancias
        winnings = self.bet_manager.distribute_winnings(winners)
        
        # Actualizar saldos
        for player_id, amount in winnings.items():
            self.players[player_id]["balance"] += amount
            
        return {
            "winners": winners,
            "winnings": winnings
        }
        
    def _determine_winners(self):
        """
        Determina los ganadores de la ronda.
        
        Returns:
            list: Lista de identificadores de los jugadores ganadores.
        """
        valid_players = []
        
        # Filtrar jugadores que no se han pasado de 21
        for player_id, player in self.players.items():
            if not HandEvaluator.is_busted(player["hand"]):
                valid_players.append(player_id)
        
        # Si no hay jugadores válidos, no hay ganadores
        if not valid_players:
            return []
            
        # Buscar el valor más alto entre los jugadores válidos
        max_value = 0
        for player_id in valid_players:
            hand_value = HandEvaluator.calculate_hand_value(self.players[player_id]["hand"])
            if hand_value > max_value:
                max_value = hand_value
        
        # Filtrar jugadores con el valor más alto
        highest_players = []
        for player_id in valid_players:
            hand_value = HandEvaluator.calculate_hand_value(self.players[player_id]["hand"])
            if hand_value == max_value:
                highest_players.append(player_id)
        
        # Si hay solo un jugador con el valor más alto, es el ganador
        if len(highest_players) == 1:
            return highest_players
            
        # Si hay empate, desempatar por jerarquía de manos
        best_hierarchy = -1
        winners = []
        
        for player_id in highest_players:
            hierarchy = HandEvaluator.get_hand_hierarchy(self.players[player_id]["hand"])
            
            if hierarchy > best_hierarchy:
                best_hierarchy = hierarchy
                winners = [player_id]
            elif hierarchy == best_hierarchy:
                winners.append(player_id)
        
        return winners
    
    def get_game_state(self):
        """
        Obtiene el estado actual del juego.
        
        Returns:
            dict: Estado completo del juego.
        """
        return {
            "game_status": self.game_status,
            "current_player": self.players_order[self.current_player_idx] if self.game_status == "playing" and self.current_player_idx < len(self.players_order) else None,
            "players": {
                player_id: {
                    "hand": player["hand"],
                    "hand_value": HandEvaluator.calculate_hand_value(player["hand"]),
                    "status": player["status"],
                    "balance": player["balance"],
                    "bet": self.bet_manager.get_player_bet(player_id)
                }
                for player_id, player in self.players.items()
            },
            "pot": self.bet_manager.get_total_pot()
        }
    
    def restart_game(self):
        """
        Reinicia el juego para una nueva ronda manteniendo los saldos.
        
        Returns:
            bool: True si el juego se reinició correctamente.
        """
        # Conservar los saldos de los jugadores
        balances = {player_id: player["balance"] for player_id, player in self.players.items()}
        
        # Reiniciar el juego
        self.start_game()
        
        # Restaurar saldos
        for player_id, balance in balances.items():
            if player_id in self.players:
                self.players[player_id]["balance"] = balance
                
        return True

def main():
    # Crear una instancia del juego
    game = Blackjack()
    
    # Obtener los argumentos de la línea de comandos
    args = sys.argv[1:]
    
    if not args:
        print(json.dumps({"error": "No se proporcionó ninguna acción"}))
        return
        
    action = args[0]
    
    try:
        if action == "start":
            # Iniciar un nuevo juego con 3 jugadores por defecto
            game.add_player("player1", 1000)
            game.add_player("player2", 1000)
            game.add_player("player3", 1000)
            game.start_game()
            result = game.get_game_state()
            
        elif action == "hit":
            player_id = args[1]
            result = game.hit(player_id)
            
        elif action == "stand":
            player_id = args[1]
            result = game.stand(player_id)
            
        elif action == "bet":
            player_id = args[1]
            amount = float(args[2])
            success = game.place_bet(player_id, amount)
            result = {
                "success": success,
                "game_state": game.get_game_state() if success else None
            }
            
        else:
            result = {"error": f"Acción desconocida: {action}"}
            
        # Imprimir el resultado en formato JSON
        print(json.dumps(result))
        
    except Exception as e:
        print(json.dumps({"error": str(e)}))
        
if __name__ == "__main__":
    main()