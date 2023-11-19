import unittest
import pygame
import random
import math
from pygame import mixer

class PygameTest(unittest.TestCase):
   def setUp(self):
       pygame.init()
       self.screen = pygame.display.set_mode((800, 600))
       self.running = True

   def test_screen_initialization(self):
       self.assertEqual(self.screen.get_width(), 800)
       self.assertEqual(self.screen.get_height(), 600)

   def test_running_variable(self):
       self.assertTrue(self.running)

   def tearDown(self):
       pygame.quit()
 


class TestGameFunctions(unittest.TestCase):
   def test_show_score(self):
       # You need to mock the screen and font objects, and the score_value variable
       # Then you can call the show_score function and check if it behaves as expected
       pass

   def test_game_over_text(self):
       # Similar to test_show_score, you need to mock the screen and over_font objects
       # Then you can call the game_over_text function and check if it behaves as expected
       pass

   def test_player(self):
       # You need to mock the screen and playerImg objects
       # Then you can call the player function and check if it behaves as expected
       pass

   def test_enemy(self):
       # You need to mock the screen, enemyImg, and i objects
       # Then you can call the enemy function and check if it behaves as expected
       pass
class TestBulletFunctions(unittest.TestCase):
    def test_fire_bullet(self):
        global bullet_state
        bullet_state = "idle"
        

   

if __name__ == '__main__':
   unittest.main()
