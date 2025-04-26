from pygame import *
#создай окно игры
window = display.set_mode((700, 500))
display.set_caption("Догонялки")

mixer.init()
mixer.music.load('povezlo-povezlo.ogg')
mixer.music.play(-1)

#задай фон сцены
background = transform.scale(image.load("back.jpg"), (700, 500))
#создай 2 спрайта и размести их на сцене
sprite1 = transform.scale(image.load("flag.png"), (50, 50))
sprite2 = transform.scale(image.load("vladimir.png"), (50, 50))
x1 = 100
y1 = 100
x2 = 150
y2 = 50
speed = 10

clock = time.Clock()
game = True
while game:
    window.blit(background,(0, 0))
    window.blit(sprite1,(x1,y1))
    window.blit(sprite2,(x2, y2))

    keys_pressed = key.get_pressed()
    if keys_pressed[K_LEFT] and x1 > 5:
        x1 -= speed
    if keys_pressed[K_RIGHT] and x1 < 650:
        x1 += speed
    if keys_pressed[K_UP] and y1 > 5:
        y1 -= speed
    if keys_pressed[K_DOWN] and y1 < 450:
        y1 += speed
    if keys_pressed[K_a] and x2 > 5:
        x2 -= speed
    if keys_pressed[K_d] and x2 < 650:
        x2 += speed
    if keys_pressed[K_w] and y2 > 5:
        y2 -= speed
    if keys_pressed[K_s] and y2 < 450:
        y2 += speed


    #обработай событие «клик по кнопке "Закрыть окно"»
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    clock.tick(60)
    display.update()


