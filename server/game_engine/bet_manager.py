class BetManager:
    """
    Clase que maneja las apuestas del juego.
    """
    
    def __init__(self):
        """Inicializa el gestor de apuestas."""
        self.player_bets = {}  # {player_id: bet_amount}
        self.pot = 0
        
    def place_bet(self, player_id, amount):
        """
        Registra la apuesta de un jugador.
        
        Args:
            player_id: Identificador único del jugador.
            amount (float): Cantidad apostada.
            
        Returns:
            bool: True si la apuesta es válida, False en caso contrario.
        """
        if amount <= 0:
            return False
        
        self.player_bets[player_id] = amount
        self.pot += amount
        return True
    
    def get_player_bet(self, player_id):
        """
        Obtiene la apuesta de un jugador.
        
        Args:
            player_id: Identificador único del jugador.
            
        Returns:
            float: Cantidad apostada por el jugador o 0 si no ha apostado.
        """
        return self.player_bets.get(player_id, 0)
    
    def get_total_pot(self):
        """
        Obtiene el total de apuestas.
        
        Returns:
            float: Total de apuestas acumuladas.
        """
        return self.pot
    
    def distribute_winnings(self, winner_ids):
        """
        Distribuye las ganancias entre los ganadores.
        
        Args:
            winner_ids (list): Lista de identificadores de los jugadores ganadores.
            
        Returns:
            dict: Diccionario con las ganancias de cada jugador.
        """
        if not winner_ids or len(winner_ids) == 0:
            return {}
        
        winnings_per_player = self.pot / len(winner_ids)
        result = {player_id: winnings_per_player for player_id in winner_ids}
        
        # Reiniciar las apuestas
        self.player_bets = {}
        self.pot = 0
        
        return result
    
    def reset(self):
        """Reinicia todas las apuestas."""
        self.player_bets = {}
        self.pot = 0