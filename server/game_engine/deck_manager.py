import random

class DeckManager:
    """
    Clase que maneja las cartas del juego.
    Se encarga de crear, mezclar y repartir cartas.
    """
    
    def __init__(self, num_decks=1):
        """
        Inicializa el manejador de mazos.
        
        Args:
            num_decks (int): Número de mazos a utilizar.
        """
        self.num_decks = num_decks
        self.cards = []
        self.init_deck()
        
    def init_deck(self):
        """Inicializa y mezcla los mazos de cartas."""
        suits = ['Corazones', 'Diamantes', 'Tréboles', 'Picas']
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        
        # Crear el mazo con la cantidad especificada de barajas
        for _ in range(self.num_decks):
            for suit in suits:
                for value in values:
                    self.cards.append({'value': value, 'suit': suit})
        
        self.shuffle()
        
    def shuffle(self):
        """Mezcla las cartas."""
        random.shuffle(self.cards)
        
    def deal_card(self):
        """
        Reparte una carta del mazo.
        
        Returns:
            dict: Carta repartida o None si no hay más cartas.
        """
        if len(self.cards) > 0:
            return self.cards.pop()
        return None
    
    def cards_remaining(self):
        """
        Devuelve el número de cartas restantes en el mazo.
        
        Returns:
            int: Número de cartas restantes.
        """
        return len(self.cards)
    
    def reset(self):
        """Reinicia el mazo."""
        self.cards = []
        self.init_deck()