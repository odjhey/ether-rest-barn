import mss, pyautogui
import pygetwindow as gw
import time
import collections

titles = gw.getAllTitles()
title = "Etheria:Restart"

def print_titles():
  for title in titles:
      if title.strip():   # ignore empty titles
          print(title)

windows = gw.getWindowsWithTitle(title)
win = windows[0]

def activate_win():
    top, left = win.top, win.left
    print(f"top, left {(top, left)}")
    pyautogui.click(left+10, top+10 )

activate_win()

def get_module_stat_subscreen():
    top = win.top
    right = win.right
    Offset = collections.namedtuple("Offset", ["from_right", "from_top"])
    offset = Offset(503, 135)
    subscr_width = 400
    subscr_height = 440
    return top+offset.from_top, right-offset.from_right, subscr_width, subscr_height


with mss.mss() as sct:
    top, left, width, height = get_module_stat_subscreen()
    region = {'top': top, 'left': left, 'width': width, 'height': height}
    sct_img = sct.grab(region)
    mss.tools.to_png(sct_img.rgb, sct_img.size, output='shot.png')

#pyautogui.click(500, 500)
#pyautogui.dragTo(600, 600, duration=0.4)
#pyautogui.scroll(-200)
