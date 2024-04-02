#Создай собственный Шутер!

from random import *
from pygame import *
window = display.set_mode((700, 500))
display.set_caption("Космос")
background = transform.scale(image.load("123.png"), (700, 500))

run = True
clock = time.Clock()
FPS = 120

font.init()
font2 = font.Font(None, 36)
font3 = font.Font(None, 56)

score = 0
lost = 0                

class Game(sprite.Sprite):
    def __init__(self,pimage, x, y, speed):
        super().__init__()
        self.image = transform.scale(image.load(pimage), (50,50))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(Game):
    def update(self):
        keys = key.get_pressed()
        if keys [K_RIGHT] and self.rect.x <= 640:
            self.rect.x += self.speed
        if keys [K_LEFT] and self.rect.x >= 5:
            self.rect.x -= self.speed
    def fire(self):
        bullet = Bullet('123451.png', tester.rect.x, tester.rect.y,5)
        bullets.add(bullet) 

lost = 0
class Enemy(Game):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > 500:
            self.rect.y = 0
            lost += 1

class Enemy2(Game):
    def update(self):
        self.rect.y += self.speed
        
        self.rect.x -= self.speed
        if self.rect.y > 500:
            self.rect.y = 0
            

class Enemy2(Game):
    def update(self):
        self.rect.y += self.speed
        
        self.rect.x -= self.speed

        
        global lost
        if self.rect.y > 500:
            self.rect.y = 0
           
            
class Bullet(Game):
    def update(self):
        
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill()     


tester = Player('golub.png', 330, 440, 10)


mixer.init()
mixer.music.load('space.ogg')
monsters = sprite.Group()
bullets = sprite.Group()
asteroids = sprite.Group()

for i in range(0,6):
    test1 = Enemy('333.png', randint(0,650), 0, randint(1,4) )
    test2 = Enemy2('121.png', randint(0,650), 0, randint(1,4))
    monsters.add(test1)
    asteroids.add(test2)
    

top = 0
mixer.music.play()
finish = False
while run: 
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                tester.fire()
                
    window.blit(background,(0, 0))

    text = font2.render('Пропущено:' + str(lost), True,(255,255,255))
    window.blit(text, (0,0))
    if lost >= 25:
        finish = True
        text3 = font3.render('Проигрыш', True, (255,255,255))
        window.blit(text3, (50,50))
    
    text2 = font2.render('Поймано:' + str(score), True,(255,255,255))
    window.blit(text2, (40,80))
    if score >= 25:
        finish = True
        text4 = font3.render('Победа!!!', True,(255,255,255))
        window.blit(text4, (50,50))    

    if not finish:
        monsters.update()      
        monsters.draw(window)
        bullets.update()
        bullets.draw(window)
        tester.reset()
        asteroids.update()
        asteroids.draw(window)

    sprites_list = sprite.spritecollide(tester,monsters, True)
    if sprites_list:
        test2 = Enemy2('121.png', randint(0,650), 0, randint(1,4))
        test1 = Enemy('333.png', randint(0,650), 0, randint(1,4) )
        monsters.add(test1,test2)
    sprites_list2 = sprite.groupcollide(monsters, bullets, True, True)
    
    if sprites_list2:
        
        test1 = Enemy('333.png', randint(0,650), 0, randint(1,4) )
        monsters.add(test1)
        score += 1
        if top <= score:
            top+=1
        print(score)

    sprites_list3 = sprite.groupcollide(asteroids, bullets, False, True)

    if sprites_list3:
        test2 = Enemy2('121.png', randint(0,650), 0, randint(1,4))
        test1 = Enemy('333.png', randint(0,650), 0, randint(1,4) )
        monsters.add(test1)
        score += 1
        if top <= score:
            top+=1
        print(score)



   

    tester.update()
    display.update()
    clock.tick(FPS)

'''
1/ Цель - Выявить ошибки(можно ли еще раз наччать игру, после проигрыша или выйгрыша. Есть ли стрельба зажимом клавиши?)
2/ Действия - Дойти до конца, как либо способом. Зажать клавишу стрельбы.
3/ Результат -  В результате окончяния игры выявлено - продолжения нету, как и стрельбы после  зажатия клавиши.

'''