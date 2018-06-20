# -*- coding: utf-8 -*-
import curses, time

#    ╔╗
#    ╚╝  

ball = {"x":10, "y":10, "m_x":2, "m_y":2}#sol ust
size_x = 50
size_y = 30
pos_x = 1
pos_y = 1
fps = 35

def init_curses():
    scr = curses.initscr()
    scr.clear()
    
def loop(obj):
    global fps
    global ball
    box = curses.newwin(size_y, size_x, pos_y, pos_x)
    while 1:
        box.clear()
        box.border(0)
        box.addstr(1, int(size_x/2) - 3, "FPS: {}".format(str(fps)))
        box.addstr(ball["y"], ball["x"], "XX")
        box.addstr(ball["y"] + 1, ball["x"], "XX")
        box.addstr(size_y-1, 1, "x:{}, y:{}, m_x:{}, m_y:{}".format(str(ball["x"]), str(ball["y"]), str(ball["m_x"]), str(ball["m_y"]))) 
        box.refresh()
        time.sleep(1/fps)
        obj.move()
        if obj.collusion_detection():
            lock_x = ball["x"]
            lock_y = ball["y"]
            lock_m_x = ball["m_x"]
            lock_m_y = ball["m_y"]
            count = 0
            while ball["x"] <= 1 or ball["x"] >= size_x -2 or ball["y"] <= 1 or ball["y"] >= size_y - 2:
                count += 1
                obj.move()
                
                if count == 3:
                    ball["x"] = lock_x
                    ball["y"] = lock_y
                    ball["m_x"] = -lock_m_x
                    ball["m_y"] = - lock_m_y
                    break
                    
        
        
class maths(object):
    def corner_detection(self):
        global ball
        if ball["x"] <= 1 and ball["y"] <= 1:
            ball["x"] = 1
            ball["y"] = 1
            ball["m_x"] *= -1
            ball["m_y"] *= -1
            return True
            
        if ball["x"] <= 1 and ball["y"] >= size_y - 2:
            ball["x"] = 1
            ball["y"] = size_y - 2
            ball["m_x"] *= -1
            ball["m_y"] *= -1
            return True
            
        if ball["x"] >= size_x - 2  and ball["y"] <= 1:
            ball["x"] = size_x - 2
            ball["y"] = 1
            ball["m_x"] *= -1
            ball["m_y"] *= -1
            return True
            
        if ball["x"] >= size_x - 2 and ball["y"] >= size_y - 2:
            ball["x"] = size_x - 2
            ball["y"] = size_y - 2
            ball["m_x"] *= -1
            ball["m_y"] *= -1
            return True
            
        return False
            
            
    def collusion_detection(self):
        global ball
#        if self.corner_detection():
#            return 0
        calculate_switch = False
        if ball["x"] <= 1 or ball["x"] >= size_x - 2:
            ball["m_x"] *= -1
            calculate_switch = True
            
        if ball["y"] <= 1 or ball["y"] >= size_y - 2:
            ball["m_y"] *= -1
            calculate_switch = True
        if calculate_switch:
            self.calculate_route()
            return 1
        return 0

            
    def calculate_route(self):
        pass
        
    def move(self):
        global ball
        ball["x"] += ball["m_x"]
        ball["y"] -= ball["m_y"]
        
    
        
def main():
    init_curses()
    math_obj = maths()
    loop(math_obj)
    
main()
