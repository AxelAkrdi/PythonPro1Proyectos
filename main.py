from pygame import*
#clase padre para otros objetos
class GameSprite(sprite.Sprite):
  #constructor de clase
  def __init__(self, player_image, player_x, player_y, player_speed):
      # Llama el constructor de la clase (Sprite):
      sprite.Sprite.__init__(self)
 
      # cada objeto debe almacenar la propiedad image
      self.image = transform.scale(image.load(player_image), (80, 80))
      self.speed = player_speed
 
      # cada objeto debe almacenar la propiedad rect (rectángulo) en la cual es ingresada
      self.rect = self.image.get_rect()
      self.rect.x = player_x
      self.rect.y = player_y
   #método para dibujar el personaje en la ventana
  def reset(self):
      window.blit(self.image, (self.rect.x, self.rect.y))
#clase del jugador principal
class Player(GameSprite):
  #método que implementar el control de objetos usando los botones de flechas del teclado
  def update(self):
      keys = key.get_pressed()
      if keys[K_LEFT] and self.rect.x > 5:
          self.rect.x -= self.speed
      if keys[K_RIGHT] and self.rect.x < win_width - 80:
          self.rect.x += self.speed
      if keys[K_UP] and self.rect.y > 5:
          self.rect.y -= self.speed
      if keys[K_DOWN] and self.rect.y < win_height - 80:
          self.rect.y += self.speed
#clase del objeto del enemigo    
class Enemy(GameSprite):
  side = "left"
   #movimiento del enemigo
  def update(self):
      if self.rect.x <= 410:
          self.side = "right"
      if self.rect.x >= win_width - 85:
          self.side = "left"
      if self.side == "left":
          self.rect.x -= self.speed
      else:
          self.rect.x += self.speed
#clase del elemento de la pared
class Wall(sprite.Sprite):
  def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
       sprite.Sprite.__init__(self)
       self.color_1 = color_1
       self.color_2 = color_2
       self.color_3 = color_3
       self.width = wall_width
       self.height = wall_height
 
       # imagen de la pared – un rectángulo del tamaño y color deseado
       self.image = Surface([self.width, self.height])
       self.image.fill((color_1, color_2, color_3))
 
       # cada objeto debe almacenar la propiedad rect (rectángulo)
       self.rect = self.image.get_rect()
       self.rect = Rect(wall_x, wall_y, wall_width, wall_height)
  def draw_wall(self):
      draw.rect(window, (self.color_1, self.color_2, self.color_3), (self.rect.x, self.rect.y, self.width, self.height))
#Crear una ventana
win_width = 700
win_height = 500
display.set_caption("Labyrinth")
window = display.set_mode((win_width, win_height))
#Crear paredes
w1 = Wall(0, 0, 0, win_width / 2 - win_width / 3, win_height / 2, 300, 10)
w2 = Wall(0, 0, 0, 410, win_height / 2 - win_height / 4, 10, 350)
#Crear objetos
packman = Player('hero.png', 5, win_height - 80, 5)
monster = Enemy('cyborg.png', win_width - 80, 200, 5)
final_sprite = GameSprite('pac-1.png', win_width - 85, win_height - 100, 0)
 
#ciclo de juego
run = True
while run:
    #el ciclo se ejecuta cada 0.05 segundos
    time.delay(50)
    #Se comprueban todos los eventos que pueden suceder
    for e in event.get():
        #evento de clic del botón “cerrar”  
        if e.type == QUIT:
            run = False
 
    #Se actualiza el fondo con cada iteración
    
    
 
    #dibuja las paredes
    w1.draw_wall()
    w2.draw_wall()
 
    #ejecuta el movimiento del objeto
    packman.update()
    monster.update()
 
    #los actualiza en una nueva ubicación con cada iteración del ciclo
    packman.reset()
    monster.reset()
    final_sprite.reset()
 
    display.update()
 
 







