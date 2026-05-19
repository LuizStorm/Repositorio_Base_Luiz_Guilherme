import pyautogui as pg
import time

pg.FAILSAFE = True

time.sleep(2)

pg.press("win")
time.sleep(1)

pg.write("chrome", interval=0.05)
time.sleep(1)

pg.press("enter")

time.sleep(3)

pg.write("https://www.youtube.com", interval=0.03)
pg.press("enter")

time.sleep(5)

video = "bob esponja"

pg.click(x=650, y=130)

time.sleep(1)

pg.write(video, interval=0.05)
pg.press("enter")

time.sleep(5)

pg.moveTo(x=500, y=500, duration=1)

time.sleep(1)

pg.click()