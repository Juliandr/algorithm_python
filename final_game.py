import pygame
import random
from os import path

WIDTH, HEIGHT = 600, 800
NEW_ENEMY_GENERATE_INTERVAL = 50 
MISSILE_LIFETIME = 10000
MISSILE_INTERVAL = 500

pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.mixer.init()

pygame.init()#13min
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()


last_enemy_generate_time = 0
class Player(pygame.sprite.Sprite):
	"""docstring for Player"""
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.transform.flip(player_img, False, True)
		self.image = pygame.transform.scale(self.image, (53, 40))
		self.image.set_colorkey((0, 0, 0))
		self.rect = self.image.get_rect()#获取地址 
		self.rect.centerx =  300
		self.rect.bottom = HEIGHT
		self.radius = 20
		self.hp = 100
		self.lives = 3
		self.score = 0
		self.hidden = False
		self.hide_time = 0
		self.is_missile_firing = False
		self.start_missile_time = 0
		self.last_missile_time = 0

	def update(self):
		key_state = pygame.key.get_pressed()
		if key_state[pygame.K_LEFT]:
			self.rect.x -= 5
		if key_state[pygame.K_RIGHT]:
			self.rect.x += 5
		if key_state[pygame.K_UP]:
			self.rect.y -= 5
		if key_state[pygame.K_DOWN]:
			self.rect.y +=5
		if self.rect.left < 0:
			self.rect.left = 0
		if self.rect.right > WIDTH:
			self.rect.right = WIDTH
		if self.rect.top < 0:
			self.rect.top = 0
		if self.rect.bottom > HEIGHT:
			self.rect.bottom = HEIGHT
		now = pygame.time.get_ticks()
		if self.hidden and now -self.hide_time > 1000:
			self.hp = self.old_hp

		if self.is_missile_firing:
			if now - self.start_missile_time <= MISSILE_LIFETIME:
				if now - self.last_missile_time > MISSILE_INTERVAL:
					missile = Missile(self.rect.center)
					missiles.add(missile)
					self.last_missile_time = now
			else:
				self.is_missile_firing = False

		

	def shoot(self):
		bullet = Bullet(self.rect.centerx, self.rect.centery)
		bullets.add(bullet)
		shoot_sound.play()


	def fire_missile(self):
		self.is_missile_firing = True
		self.start_missile_time = pygame.time.get_ticks()


	# def hide(self):
	# 	self.hidden = True
	# 	self.old_hp = self.hp
	# 	self.hide_time = pygame.time.get_ticks()
class Enemy(pygame.sprite.Sprite):
	"""docstring for Enemy"""
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.transform.flip(enemy_img, False, False)
		img_width = random.randint(20, 120)
		self.image = pygame.transform.scale(enemy_img, (img_width, img_width))
		self.image.set_colorkey((0, 0, 0))
		self.image_origin = self.image.copy()
		self.rect = self.image.get_rect()
		self.rect.bottom = 0#从上面飞下来
		
		self.radius = img_width // 2

		# pygame.draw.circle(self.image, (255,0,0), self.rect.center, self.radius)
		self.rect.x = random.randint(0, WIDTH - self.rect.w)#宽度减敌人的宽度
		self.vx = random.randint(-2, 5)
		self.vy = random.randint(2, 10)

		self.last_time = pygame.time.get_ticks()
		self.rotate_speed = random.randint(-5, 5)
		self.rotate_angle = 0
	
	def rotate(self):
		now = pygame.time.get_ticks()
		if now - self.last_time > 30:
			self.rotate_angle = (self.rotate_angle + self.rotate_speed) % 360
			x, y = self.rect.center
			self.image = pygame.transform.rotate(self.image_origin, self.rotate_angle)
			self.rect = self.image.get_rect()
			self.rect.centerx = x
			self.rect.centery = y
			self.last_time = now
	def update(self):
		self.rect.x += self.vx
		self.rect.y += self.vy
		self.rotate()

	def enemy_break(self, x, y):
		enemy = Enemy()
		enemy.rect.x = x
		enemy.rect.y = y
		enemys.add(enemy)
class Bullet(pygame.sprite.Sprite):
	"""docstring for Bullets"""
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.transform.scale(bullet_img, (20, 35))
		self.image.set_colorkey((0, 0, 0))
		self.rect = self.image.get_rect()
		self.rect.centerx = x
		self.rect.centery = y

	def update(self):
		self.rect.y -= 10
		if self.rect.bottom < 0:
			self.kill

class Explosion(pygame.sprite.Sprite):
	"""docstring for Explosion"""
	def __init__(self, center):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.transform.scale(explosion_animation[0], (80, 80))
		self.image.set_colorkey((0, 0, 0))
		self.rect = self.image.get_rect()
		self.rect.center = center
		self.frame = 0
		self.last_time = pygame.time.get_ticks()
	def update(self):
		now = pygame.time.get_ticks()
		if now - self.last_time > 30:
			if self.frame < len(explosion_animation):
				self.image = pygame.transform.scale(explosion_animation[self.frame], (80, 80))
				self.image.set_colorkey((0, 0, 0))
				self.frame += 1
				self.last_time = now
			else:
				self.kill()

class PowerUP(pygame.sprite.Sprite):
	"""docstring for PowerUP"""
	def __init__(self, center):
		pygame.sprite.Sprite.__init__(self)
		random_num = random.random()
		if random_num < 0.5:
			self.type = 'add_hp'
		elif random_num < 0.8:
			self.type = 'add_missile'
		else:
			self.type = 'add_life'
		self.image = powerup_imgs[self.type]
		self.rect = self.image.get_rect()
		self.image.set_colorkey((0, 0, 0))
		self.rect.center = center

	def update(self):
		self.rect.x += random.randint(-2, 3)
		self.rect.y += 3
class Missile(pygame.sprite.Sprite):
	"""docstring for Missiles"""
	def __init__(self, center):
		pygame.sprite.Sprite.__init__(self)
		self.image = missile_img
		self.rect = self.image.get_rect()
		self.image.set_colorkey((0, 0, 0))
		self.rect.center = center

	def update(self):
		self.rect.y -= 5
		

def draw_ui():
	pygame.draw.rect(screen, (0, 255, 0), (10, 10, player.hp, 15))#在（10，10）的位置创建一个（50，15）的框
	pygame.draw.rect(screen, (255, 255, 255), (10, 10, 100, 15), 2) #2是边框粗细
	img_rect = player_img_small.get_rect()
	img_rect.right = WIDTH - 10
	img_rect.top = 10
	for _ in range(player.lives):
		screen.blit(player_img_small, img_rect)
		img_rect.x -= img_rect.width + 10



def draw_text(text,  surface, color, font_size, x, y):
	font_name = pygame.font.match_font('arial')
	font = pygame.font.Font(font_name, font_size)
	text_surface = font.render(text, True, color)
	text_rect = text_surface.get_rect()
	text_rect.midtop = (x, y)
	surface.blit(text_surface, text_rect)


def show_menu():
	global game_state, screen, game_over
	screen.blit(background_img, background_rect)

	draw_text('Space shooter!', screen, (255, 255, 255), 40,WIDTH/2, 100)
	draw_text('Press Space to start', screen, (255, 255, 255), 20,WIDTH/2, 300)
	draw_text('Press ESC key to quit', screen, (255, 255, 255), 20,WIDTH/2, 350)




# class God(object): 
# 	"""docstring for God"""
# 	def __init__(self, arg):
# 		pygame.sprite.Sprite.__init__(self)
		

		
img_dir = path.join(path.dirname(__file__), 'img')
background_dir = path.join(img_dir, 'background.png')
background_img = pygame.image.load(background_dir).convert()
background_rect = background_img.get_rect()
player_dir = path.join(img_dir, 'spaceShips_001.png')
player_img = pygame.image.load(player_dir).convert()
player_img_small = pygame.transform.scale(player_img, (27, 20))
player_img_small.set_colorkey((0, 0, 0))
enemy_dir = path.join(img_dir, 'enemy_009.png')
enemy_img = pygame.image.load(enemy_dir).convert()
bullet_dir = path.join(img_dir, 'spaceMissiles_001.png')
bullet_img = pygame.image.load(bullet_dir).convert()
# god_dir = path.join(img_dir, 'god.png')
# god_img = pygame.image.load(god_dir).convert()
sound_dir = path.join(path.dirname(__file__), 'sound')
shoot_sound = pygame.mixer.Sound(path.join(sound_dir, 'Laser_Shoot23.wav'))
pygame.mixer.music.load(path.join(sound_dir, 'background.ogg'))
missile_dir = path.join(img_dir, 'spaceMissiles_021.png')
missile_img = pygame.image.load(missile_dir).convert()


explosion_animation = []
for i in range(9):
	explosion_dir = path.join(img_dir, f'regularExplosion0{i}.png')
	explosion_img = pygame.image.load(explosion_dir).convert()
	explosion_animation.append(explosion_img)

powerup_imgs = {}
power_add_hp_dir = path.join(img_dir, 'gem_red.png')
powerup_imgs['add_hp'] = pygame.image.load(power_add_hp_dir).convert()
power_add_hp_dir = path.join(img_dir, 'heartFull.png')
powerup_imgs['add_life'] = pygame.image.load(power_add_hp_dir).convert()
power_add_hp_dir = path.join(img_dir, 'gem_yellow.png')
powerup_imgs['add_missile'] = pygame.image.load(power_add_hp_dir).convert()



			

player = Player()
enemys = pygame.sprite.Group()
bullets = pygame.sprite.Group()
missiles = pygame.sprite.Group()
explosions = pygame.sprite.Group()
powerups = pygame.sprite.Group()

for i in range(10):
	enemy = Enemy()
	enemys.add(enemy)
game_over = False
game_state = 0
pygame.mixer.music.play(loops=-1)
while not game_over:
	clock.tick(60)
	if game_state == 0:
		event_list = pygame.event.get()
		for event  in event_list:
			if event.type == pygame.QUIT:
				game_over = True
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					game_over = True
				if event.key == pygame.K_SPACE:
					game_state = 1
			if event.type == pygame.MOUSEMOTION:
				mouse_pos = event.pos
		show_menu()
		pygame.display.flip()
	else:
		event_list = pygame.event.get()
		for event  in event_list:
			if event.type == pygame.QUIT:
				game_over = True
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					game_over = True
				if event.key == pygame.K_SPACE:
					player.shoot()
			if event.type == pygame.MOUSEMOTION:
				mouse_pos = event.pos
				print(event.pos)
		now = pygame.time.get_ticks()
		if now - last_enemy_generate_time > NEW_ENEMY_GENERATE_INTERVAL:
			enemy = Enemy()
			enemys.add(enemy)
			last_enemy_generate_time = now
		screen.fill((255, 255, 255))
		player.update()
		enemys.update()
		bullets.update()
		missiles.update()
		explosions.update()
		powerups.update()
		
		# hits = pygame.sprite.spritecollide(player, enemys, False, pygame.sprite.collide_rect_ratio(0.7)矩形检测)#false是保留，ture是删除
		hits = pygame.sprite.spritecollide(player, enemys, True, pygame.sprite.collide_circle)
		for hit in hits:
			player.hp -= hit.radius
			if player.hp < 0:
				player.lives -= 1
				player.hp = 100
				# player.hide()
				if player.lives == 0:
					game_over = True

		
		hit_bullets = pygame.sprite.groupcollide(enemys, bullets , True, True)
		hits_missiles = pygame.sprite.groupcollide(enemys, missiles , True, True)
		hits = {}
		hits.update(hit_bullets)
		hits.update(hits_missiles)
		for hit in hits:
			enemy = Enemy()
			enemys.add(enemy)
			explosion = Explosion(hit.rect.center)
			explosions.add(explosion)
			player.score +=100 - hit.radius
			if random.random() > 0.7:
				powerup = PowerUP(hit.rect.center)
				powerups.add(powerup)

		# hits = pygame.sprite.groupcollide(enemys, missiles , True, True)
		# for hit in hits:
		# 	enemy = Enemy()
		# 	enemys.add(enemy)
		# 	explosion = Explosion(hit.rect.center)
		# 	explosions.add(explosion)
		# 	player.score +=100 - hit.radius
		# 	if random.random() > 0.9:
		# 		powerup = PowerUP(hit.rect.center)
		# 		powerups.add(powerup)

		hits = pygame.sprite.spritecollide(player, powerups, True)
		for hit in hits:
			if hit.type == 'add_hp':
				player.hp += 50
				if player.hp > 100:
					player.hp = 100
			elif hit.type == 'add_life':
				player.lives += 1
				if player.lives > 3:
					player.lives = 3
			else:
				player.fire_missile()
				

			

		# screen.blit(enemy.image, enemy.rect)不需要这样画了
		screen.blit(background_img, background_rect)
		enemys.draw(screen)
		bullets.draw(screen)
		missiles.draw(screen)
		explosions.draw(screen)
		powerups.draw(screen)

		draw_ui()
		draw_text(str(player.score), screen, (255, 255, 255), 20, WIDTH / 2, 10)

		screen.blit(player.image, player.rect)
		pygame.display.flip()
