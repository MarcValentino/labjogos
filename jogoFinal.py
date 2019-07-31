
def registrarPontuacao(score, dict, n):
    dict[str(n)] = int(score)

def setcoins(lis1, lis2, lis3, posinit):
    from random import randint
    for j in range(22):
        novospr = Sprite("cointest.png", 4)
        novospr.set_total_duration(700)
        initpos = randint(0, 1)
        if initpos == 0:
            novospr.x = posinit + (600 + (200 * j))
        elif initpos == 1:
            novospr.x = posinit + (500 + (200 * j))
        colocado = False
        for platform in lis2:
            if platform.x <= novospr.x <= platform.x + platform.width:
                colocado = True
                novospr.y = platform.y - novospr.height
                lis3.append(novospr)
        for ground in lis1:
            if ground.x <= novospr.x <= ground.x + ground.width and not colocado:
                novospr.y = ground.y - novospr.height
                lis3.append(novospr)

def setobstacles(lis1, lis2, lis3, posinit):
    from random import randint
    numobstacles = randint(3, 12)
    for j in range(numobstacles):
        novospr = Sprite("spikes.png")
        #initpos = randint(0, 1)
        #if initpos == 0:
            #novospr.x = posinit + (520 + (randint(400,600) * j))
        #elif initpos == 1:
        novospr.x = posinit + (750 + (randint(400, 600) * j))
        colocado = False
        for platform in lis2:
            if platform.x <= novospr.x <= platform.x + platform.width:
                novospr.y = platform.y - novospr.height
                novospr.x = platform.x
                lis3.append(novospr)
                colocado = True
        for ground in lis1:
            if ground.x <= novospr.x <= ground.x + ground.width and not colocado:
                novospr.y = ground.y - novospr.height
                lis3.append(novospr)

def movercenario(f1,f2,ms,win):
    f1.y = win.height - f1.height
    f2.y = win.height - f2.height
    f1.x -= ms * win.delta_time()
    f2.x -= ms * win.delta_time()
    if f2.x <= 0:
        f1.x = 0
        f2.x = f1.width
    f1.draw()
    f2.draw()
    return None

def areaplatforms(lis, spr):
    if lis != []:
        for obj in lis:
            if obj.x +30 <= spr.x <= (obj.x + obj.width) -30:
                return True
    else:
        return False

    return False

def moverObjetos(ms,lis,win,lis2, lis3, lis4):
    for bloco in lis:
        bloco.move_x(-ms * janela.delta_time())
        if bloco.x < - win.width:
            lis.remove(bloco)
            #bloco.x = 2 * win.width
        bloco.draw()
    if lis2 != []:
        for obj in lis2:
            obj.move_x(-ms * win.delta_time())
            if obj.x < - win.width:
                lis2.remove(obj)
                #obj.x = 2 * win.width
            obj.draw()
    if lis3 != []:
        for obs in lis3:
            obs.move_x(-ms * win.delta_time())
            if obs.x < - win.width:
                lis3.remove(obs)
                #obs.x = 2 * win.width
            obs.draw()
    for coin in lis4:
        coin.move_x(-ms * win.delta_time())
        if coin.x < - win.width:
            lis4.remove(coin)
            #coin.x = 2 * win.width
        coin.draw()
        coin.update()

def areafloor(lis, spr):
    for obj in lis:
        if obj.x <= spr.x <= (obj.x + obj.width):
            return True
    return False

def acessarDict(win, dict):
    y = 50
    x = 200
    cont = 0
    for item in sorted(dict.items(), key=lambda t: t[1], reverse=True):
        if cont < 10:
            win.draw_text(str(item[0]) + ".: " + str(item[1]),x, y, size=50, color=(182,163,124), font_name="Shumi", bold=False, italic=False)
            y += 40
        cont += 1

def generateScenario(posInit):
    somaPos = 0
    numplats = randint(1,5)
    if numplats != 0:
        counter = 0
        for i in range(numplats):
            plataforma = Sprite("plataforma.png")
            plataforma.y = janela.height - 4.2 * plataforma.height
            plataforma.x = posInit + 400
            if i == 0:
                platforms.append(plataforma)
            else:
                dist = randint(0, 1)
                if dist == 0:
                    intervalo = 900
                else:
                    intervalo = 1200
                plataforma.x = plataforma.x + (intervalo * counter)
                platforms.append(plataforma)
            counter += 1
    contador = 0
    numsprites = 23
    primeiro = True
    while contador < numsprites:
        chao = Sprite("Chao.png")
        chao.y = janela.height - chao.height
        chao.x = posInit
        if primeiro:
            floor.append(chao)
            primeiro = False
        else:
            chao.x = posInit + (chao.width * contador)
            floor.append(chao)
            for plat in platforms:
                if (plat.x <= chao.x  <= (plat.x + plat.width)) or (plat.x <= (chao.x + chao.width) <= (plat.x + plat.width)):
                    if chao not in floor:
                        floor.append(chao)
                    floor.remove(chao)
        somaPos += chao.width
        contador += 1
    setobstacles(floor, platforms, obstacles, posInit)
    setcoins(floor, platforms, coins, posInit)

    return somaPos

import pygame
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.window import *
from PPlay.mouse import *
from PPlay.keyboard import *
from PPlay.sound import *
janela = Window(800, 600)
jogar = Sprite("jogar.png")
fundo = GameImage("cenario.png")
sair = Sprite("sairC.png")
ranking = Sprite("ranking.png")
back = Sprite("voltar.png")
janela.set_background_color((0,0,0))
jogar.x = 300
teclado = Keyboard()
sair.x = 300
fundo.x = 0
fundo.y = janela.height - (fundo.height)
jogar.y = 140
ranking.x = 300
ranking.y = 280
sair.y = 420
mouse = Mouse()
musica = Sound("musica.ogg")
musica.set_volume(25)
menu = True
game = False
rank = False
highscore = dict()
n = 0

while menu:
    fundo.draw()
    janela.draw_text("Cheese Thief", 200, 40, size=65, color=(182, 163, 124), font_name="Shumi", bold=False,
                     italic=False)
    janela.draw_text("Seta pra cima para pular! ", 550, 450, size=15, color=(182, 163, 124), font_name="Shumi",
                     bold=False, italic=False)
    jogar.draw()
    sair.draw()
    ranking.draw()
    janela.update()

    if mouse.is_over_object(sair):
        if mouse.is_button_pressed(1):
            menu = False
    if mouse.is_over_object(ranking):
        if mouse.is_button_pressed(1):
            rank = True
            back.x = 20
            back.y = janela.width - 2*back.height
            while rank:
                if mouse.is_over_object(back):
                    if mouse.is_button_pressed(1):
                        rank = False
                fundo.draw()
                acessarDict(janela, highscore)
                back.draw()
                janela.update()
                if teclado.key_pressed("esc"):
                    rank = False

    if mouse.is_over_object(jogar):
        if mouse.is_button_pressed(1):
            game = True
            from random import randint
            espinho = Sprite("spikes.png")
            plataforma = Sprite("plataforma.png")
            fundo = GameImage("cenario.png")
            fundo2 = GameImage("cenario.png")
            janela.set_background_color((50, 50, 50))
            mockey = Sprite("Mockey.png")
            mockey.x = 40
            time_elapsed = 0
            verificador = 1700
            fundo.x = 0
            perdeu = False
            obstacles = []
            fundo2.x = janela.width
            movspeed = 140
            vely = 260 * 1.2
            fallspeed = 100
            score = 0
            grav = 10
            floor = []
            coins = []
            primeiro = True
            cair = False
            contador = 0
            finalposition = 0
            numplats = randint(1, 5)
            platforms = []
            chao = Sprite("Chao.png")
            numsprites = (janela.width * 2.5)//chao.width
            relogio = 0
            mockey.y = janela.height - (mockey.height + chao.height)//1.1
            comprimentoFase = generateScenario(0)
            pular = False

            while game:
                if not musica.is_playing():
                    musica.play()
                movercenario(fundo, fundo2, movspeed, janela)
                nochao = areafloor(floor, mockey)
                naplataforma = areaplatforms(platforms, mockey)
                teclado = Window.get_keyboard()
                time_elapsed += janela.delta_time()
                if (teclado.key_pressed("up")) and not cair:
                    pular = True

                if pular:
                    mockey.y -= vely * janela.delta_time()
                    vely -= 300 * janela.delta_time()
                    if mockey.y + (mockey.height * 0.8) > floor[0].y and nochao:
                        mockey.y = floor[0].y - mockey.height * 0.8
                        pular = False
                        vely = 260 * 1.2
                    else:
                        if platforms != []:
                            if mockey.y + (mockey.height * 0.8) > platforms[0].y and naplataforma:
                                mockey.y = platforms[0].y - mockey.height * 0.8
                                pular = False
                                vely = 260 * 1.2

                if not nochao and not naplataforma and not pular and not cair:
                    vely = 0
                    cair = True

                if cair:
                    vely += 300 * janela.delta_time()
                    mockey.y += vely * janela.delta_time()
                    if mockey.y + (mockey.height * 0.8) > floor[0].y and nochao:
                        mockey.y = floor[0].y - mockey.height * 0.8
                        vely = 260 * 1.2
                        queda = True
                        cair = False
                relogio += janela.delta_time()
                moverObjetos(movspeed, floor, janela, platforms, obstacles, coins)
                for moeda in coins:
                    if mockey.collided_perfect(moeda):
                        score += 10
                        coins.remove(moeda)
                comprimentoFase -= movspeed * janela.delta_time()

                if relogio > 17 * janela.delta_time():
                    score += 1
                    relogio = 0
                    movspeed += 0.15
                janela.draw_text("Pontos: " + str(score), 20, 20, size=20, color=(100, 100, 100), font_name="Shumi",
                                 bold=False, italic=False)
                if comprimentoFase <= 810:
                   comprimentoFase += generateScenario(810)
                mockey.draw()
                for spike in obstacles:
                    if mockey.collided_perfect(spike):
                        musica.stop()
                        game = False
                        fundo.x = 0
                        n += 1
                        registrarPontuacao(score, highscore, n)
                janela.update()
                if teclado.key_pressed("esc"):
                    musica.stop()
                    game = False
                    n += 1
                    registrarPontuacao(score, highscore, n)
                if mockey.y > janela.height:
                    musica.stop()
                    game = False
                    n += 1
                    registrarPontuacao(score, highscore, n)

