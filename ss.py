# game config
# 16:9, 1600*900
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

Offset = collections.namedtuple("Offset", 
                                ["from_right", "from_top","from_left"],
                                defaults=[0,0,0])
def get_module_stat_subscreen():
    top = win.top
    right = win.right
    offset = Offset(from_right=503, from_top=135)
    subscr_width = 400
    subscr_height = 440
    return top+offset.from_top, right-offset.from_right, subscr_width, subscr_height

def get_module_grid_subscreen():
    top = win.top
    left = win.left
    offset = Offset(from_left=165, from_top=132)
    subscr_width = 855
    subscr_height = 712
    return top+offset.from_top, left+offset.from_left, subscr_width, subscr_height

def get_module_center_by_idx(idx, grid_cols=7):
    """get x,y of the center of a module by idx in grid, idx starts at 0"""
    top, left, _, _ = get_module_grid_subscreen()
    subscr_width = 139
    subscr_height = subscr_width
    # x,y in grid
    grid_col,grid_row= idx%grid_cols,idx//grid_cols

    # row scrolls on 5, then for >5 clamp due to game auto scroll behaviour
    offset_top=0
    # clamp
    if grid_row >= 4:
        grid_row = 4
        if grid_col != 0:
            offset_top=-80
        else:
            offset_top=80

    subscr_top, subscr_left = top+(grid_row*subscr_height), left+(grid_col*subscr_width)
    center_top, center_left = subscr_top+(subscr_height//2)+offset_top, subscr_left+(subscr_width//2)

    return center_left, center_top

for idx in range(6002):
    time.sleep(0.050)
    x,y = get_module_center_by_idx(idx)
    pyautogui.click(x, y)
    with mss.mss() as sct:
        top, left, width, height = get_module_stat_subscreen()
        region = {'top': top, 'left': left, 'width': width, 'height': height}
        sct_img = sct.grab(region)
        mss.tools.to_png(sct_img.rgb, sct_img.size, output=f"outs/xshot_{idx}.png")

