class HandEvaluator:
    """
    Clase que evalúa las manos de los jugadores.
    Calcula los puntos y determina el estado de la mano.
    """
    
    @staticmethod
    def get_card_value(card):
        """
        Obtiene el valor numérico de una carta.
        
        Args:
            card (dict): Carta a evaluar.
            
        Returns:
            list: Lista con los posibles valores de la carta.
        """
        value = card['value']
        if value in ['J', 'Q', 'K']:
            return [10]
        elif value == 'A':
            return [1, 11]  # El As puede valer 1 u 11
        else:
            return [int(value)]
    
    @staticmethod
    def calculate_hand_value(hand):
        """
        Calcula el valor de una mano.
        
        Args:
            hand (list): Lista de cartas en la mano.
            
        Returns:
            int: El valor óptimo de la mano.
        """
        # Si no hay cartas, el valor es 0
        if not hand:
            return 0
            
        # Calcular todas las posibles combinaciones de valores
        possible_values = [0]
        
        for card in hand:
            card_values = HandEvaluator.get_card_value(card)
            new_values = []
            
            for card_value in card_values:
                for value in possible_values:
                    new_values.append(value + card_value)
                    
            possible_values = new_values
        
        # Elegir el valor óptimo (el más alto que no supere 21)
        best_value = 0
        for value in possible_values:
            if value <= 21 and value > best_value:
                best_value = value
        
        # Si todas las combinaciones superan 21, tomar el valor más bajo
        if best_value == 0:
            best_value = min(possible_values)
            
        return best_value
    
    @staticmethod
    def is_blackjack(hand):
        """
        Determina si una mano es un blackjack (21 puntos con solo 2 cartas).
        
        Args:
            hand (list): Lista de cartas en la mano.
            
        Returns:
            bool: True si es blackjack, False en caso contrario.
        """
        if len(hand) != 2:
            return False
        
        return HandEvaluator.calculate_hand_value(hand) == 21
    
    @staticmethod
    def is_busted(hand):
        """
        Determina si una mano se ha pasado de 21.
        
        Args:
            hand (list): Lista de cartas en la mano.
            
        Returns:
            bool: True si se ha pasado de 21, False en caso contrario.
        """
        return HandEvaluator.calculate_hand_value(hand) > 21
    
    @staticmethod
    def get_hand_hierarchy(hand):
        """
        Obtiene la jerarquía de la mano para desempates.
        Mayor valor = mayor jerarquía.
        
        Args:
            hand (list): Lista de cartas en la mano.
            
        Returns:
            int: Valor numérico que representa la jerarquía de la mano.
        """
        # Primero, cantidad de cartas (menos cartas = mejor)
        card_count_value = 100 - (len(hand) * 10)
        
        # Segundo, valor de las cartas individuales
        card_hierarchy = {
            'A': 14, 'K': 13, 'Q': 12, 'J': 11, '10': 10,
            '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2
        }
        
        card_values = sorted([card_hierarchy[card['value']] for card in hand], reverse=True)
        
        # Combinar los valores para una puntuación jerárquica
        hierarchy_value = card_count_value
        for i, value in enumerate(card_values):
            hierarchy_value += value * (0.1 ** (i + 1))  # Peso decreciente por posición
            
        return hierarchy_value