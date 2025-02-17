from settings import *
from pytmx.util_pygame import load_pygame

class Game:
	# general 
	def __init__(self):
		pygame.init()
		self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
		pygame.display.set_caption('Monster Hunter')
		self.clock = pygame.time.Clock()
		
        # groups 
		self.all_sprites = AllSprites()
		
		self.import_assets()
		self.setup(self.tmx_maps['world'], 'house')
    
def import_assets(self):
    self.tmx_maps = {'world': load_pygame(join('..', 'data', 'maps', 'world.tmx'))}
	
def setup(self, tmx_map, player_start_pos):
	# terrain
    for x, y, surf in tmx_map.get_layer_by_name('Terrain').tiles():
        Sprite((x * TILE_SIZE, y * TILE_SIZE), surf, self.all_sprites)