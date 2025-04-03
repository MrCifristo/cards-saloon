import unittest
import sys
import os

# Añadir el directorio padre al path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from deck_manager import DeckManager

class TestDeckManager(unittest.TestCase):
    
    def test_init_single_deck(self):
        # Probar la inicialización con un solo mazo
        deck_manager = DeckManager(num_decks=1)
        
        # Un mazo estándar tiene 52 cartas
        self.assertEqual(deck_manager.cards_remaining(), 52)
        
    def test_init_multiple_decks(self):
        # Probar la inicialización con múltiples mazos
        deck_manager = DeckManager(num_decks=3)
        
        # 3 mazos tienen 156 cartas (52 * 3)
        self.assertEqual(deck_manager.cards_remaining(), 156)
        
    def test_deal_card(self):
        deck_manager = DeckManager()
        
        # Cantidad inicial de cartas
        initial_count = deck_manager.cards_remaining()
        
        # Repartir una carta
        card = deck_manager.deal_card()
        
        # Verificar que se redujo la cantidad de cartas
        self.assertEqual(deck_manager.cards_remaining(), initial_count - 1)
        
        # Verificar que la carta es un diccionario con las claves correctas
        self.assertIsInstance(card, dict)
        self.assertIn('value', card)
        self.assertIn('suit', card)
        
    def test_deal_all_cards(self):
        deck_manager = DeckManager()
        
        # Repartir todas las cartas
        for _ in range(52):
            card = deck_manager.deal_card()
            self.assertIsNotNone(card)
            
        # Verificar que no quedan cartas
        self.assertEqual(deck_manager.cards_remaining(), 0)
        
        # Intentar repartir otra carta debe devolver None
        card = deck_manager.deal_card()
        self.assertIsNone(card)
        
    def test_reset(self):
        deck_manager = DeckManager()
        
        # Repartir algunas cartas
        for _ in range(10):
            deck_manager.deal_card()
            
        # Verificar que quedan menos cartas
        self.assertEqual(deck_manager.cards_remaining(), 42)
        
        # Reiniciar el mazo
        deck_manager.reset()
        
        # Verificar que se restauró la cantidad de cartas
        self.assertEqual(deck_manager.cards_remaining(), 52)
        
    def test_shuffle(self):
        deck_manager1 = DeckManager()
        deck_manager2 = DeckManager()
        
        # Asegurarse de que ambos mazos tengan las mismas cartas inicialmente
        # (aunque pueden estar en orden diferente debido a la mezcla automática en el constructor)
        deck_manager1.reset()
        deck_manager2.reset()
        
        # Guardar el orden inicial del primer mazo
        initial_cards = deck_manager1.cards.copy()
        
        # Mezclar el primer mazo
        deck_manager1.shuffle()
        
        # Verificar que el orden de las cartas cambió
        # Nota: hay una pequeña posibilidad de que la mezcla resulte en el mismo orden,
        # pero es extremadamente improbable
        self.assertNotEqual(initial_cards, deck_manager1.cards)
        
if __name__ == '__main__':
    unittest.main()