import unittest
import sys
import os

# Añadir el directorio padre al path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from hand_evaluator import HandEvaluator

class TestHandEvaluator(unittest.TestCase):
    
    def test_get_card_value(self):
        # Probar cartas numéricas
        self.assertEqual(HandEvaluator.get_card_value({"value": "2", "suit": "Corazones"}), [2])
        self.assertEqual(HandEvaluator.get_card_value({"value": "10", "suit": "Diamantes"}), [10])
        
        # Probar figuras
        self.assertEqual(HandEvaluator.get_card_value({"value": "J", "suit": "Tréboles"}), [10])
        self.assertEqual(HandEvaluator.get_card_value({"value": "Q", "suit": "Picas"}), [10])
        self.assertEqual(HandEvaluator.get_card_value({"value": "K", "suit": "Corazones"}), [10])
        
        # Probar As
        self.assertEqual(HandEvaluator.get_card_value({"value": "A", "suit": "Diamantes"}), [1, 11])
        
    def test_calculate_hand_value(self):
        # Mano vacía
        self.assertEqual(HandEvaluator.calculate_hand_value([]), 0)
        
        # Mano simple
        hand1 = [
            {"value": "10", "suit": "Corazones"},
            {"value": "K", "suit": "Picas"}
        ]
        self.assertEqual(HandEvaluator.calculate_hand_value(hand1), 20)
        
        # Mano con As (valor óptimo)
        hand2 = [
            {"value": "A", "suit": "Corazones"},
            {"value": "10", "suit": "Diamantes"}
        ]
        self.assertEqual(HandEvaluator.calculate_hand_value(hand2), 21)
        
        # Mano con As (valor 1 para no pasarse)
        hand3 = [
            {"value": "A", "suit": "Corazones"},
            {"value": "10", "suit": "Diamantes"},
            {"value": "J", "suit": "Tréboles"}
        ]
        self.assertEqual(HandEvaluator.calculate_hand_value(hand3), 21)
        
        # Mano con As (valor 1 para minimizar puntos al pasarse)
        hand4 = [
            {"value": "A", "suit": "Corazones"},
            {"value": "10", "suit": "Diamantes"},
            {"value": "J", "suit": "Tréboles"},
            {"value": "5", "suit": "Picas"}
        ]
        self.assertEqual(HandEvaluator.calculate_hand_value(hand4), 26)
        
    def test_is_blackjack(self):
        # Blackjack (21 con 2 cartas)
        hand1 = [
            {"value": "A", "suit": "Corazones"},
            {"value": "K", "suit": "Picas"}
        ]
        self.assertTrue(HandEvaluator.is_blackjack(hand1))
        
        # 21 puntos pero con más de 2 cartas (no es blackjack)
        hand2 = [
            {"value": "A", "suit": "Corazones"},
            {"value": "10", "suit": "Diamantes"},
            {"value": "10", "suit": "Tréboles"}
        ]
        self.assertFalse(HandEvaluator.is_blackjack(hand2))
        
        # 2 cartas pero menos de 21 puntos (no es blackjack)
        hand3 = [
            {"value": "A", "suit": "Corazones"},
            {"value": "9", "suit": "Diamantes"}
        ]
        self.assertFalse(HandEvaluator.is_blackjack(hand3))
        
    def test_is_busted(self):
        # Mano que no se pasa
        hand1 = [
            {"value": "10", "suit": "Corazones"},
            {"value": "K", "suit": "Picas"}
        ]
        self.assertFalse(HandEvaluator.is_busted(hand1))
        
        # Mano que se pasa
        hand2 = [
            {"value": "10", "suit": "Corazones"},
            {"value": "K", "suit": "Picas"},
            {"value": "5", "suit": "Diamantes"}
        ]
        self.assertTrue(HandEvaluator.is_busted(hand2))
        
        # Mano con As que se pasa
        hand3 = [
            {"value": "A", "suit": "Corazones"},
            {"value": "10", "suit": "Picas"},
            {"value": "K", "suit": "Diamantes"},
            {"value": "5", "suit": "Tréboles"}
        ]
        self.assertTrue(HandEvaluator.is_busted(hand3))
        
    def test_get_hand_hierarchy(self):
        # Mano con menos cartas debe tener mayor jerarquía
        hand1 = [
            {"value": "10", "suit": "Corazones"},
            {"value": "K", "suit": "Picas"}
        ]
        
        hand2 = [
            {"value": "6", "suit": "Diamantes"},
            {"value": "7", "suit": "Tréboles"},
            {"value": "7", "suit": "Corazones"}
        ]
        
        # Ambas manos valen 20, pero hand1 tiene más jerarquía por tener menos cartas
        self.assertGreater(HandEvaluator.get_hand_hierarchy(hand1), HandEvaluator.get_hand_hierarchy(hand2))
        
        # Manos con misma cantidad de cartas pero cartas de mayor valor
        hand3 = [
            {"value": "A", "suit": "Corazones"},
            {"value": "9", "suit": "Picas"}
        ]
        
        hand4 = [
            {"value": "K", "suit": "Diamantes"},
            {"value": "J", "suit": "Tréboles"}
        ]
        
        # Ambas manos tienen 2 cartas, pero hand3 tiene As (valor más alto)
        self.assertGreater(HandEvaluator.get_hand_hierarchy(hand3), HandEvaluator.get_hand_hierarchy(hand4))
        
if __name__ == '__main__':
    unittest.main()