import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")#表示画像
    bg_img2 = pg.transform.flip(bg_img,True,False)#練8
    kk_img = pg.transform.flip(pg.image.load("fig/3.png"),True,False)#練3
    kk_rct = kk_img.get_rect()#練10
    kk_rct.center = 300, 200#練10
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        x = tmr % 3200 #練習9
        screen.blit(bg_img, [-x, 0])#背景画像Surfaceをスクリーンにblit
        screen.blit(bg_img, [-x+1600, 0])#練7
        screen.blit(bg_img2, [-x+1600, 0])#練8
        screen.blit(bg_img, [-x+3200, 0])

        key_lst = pg.key.get_pressed()#練10↓
        if key_lst[pg.K_UP]:#演習1
            kk_rct.move_ip((-1,-1))
        if key_lst[pg.K_DOWN]:
            kk_rct.move_ip((-1,+1))
        if key_lst[pg.K_LEFT]:
            kk_rct.move_ip((-1,0))
        if key_lst[pg.K_RIGHT]:
            kk_rct.move_ip((+1,0))
        else:
            kk_rct.move_ip((-1,0))
        screen.blit(kk_img, kk_rct)#練4、練10↑
        pg.display.update()
        tmr += 1        
        clock.tick(200)#練6


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()