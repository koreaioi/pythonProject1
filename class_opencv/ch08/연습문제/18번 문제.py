import numpy as np, cv2

def draw_bar(img, pt, w, bars):
    pt = np.array(pt, np.int)
    for bar in bars:
        (x,y), h = pt, w*6
        cv2.rectangle(img, (x,y,w,h), (0,0,0),-1)
        if bar == 0:
            y = (y + w * 3 - w // 4)
            h = (w // 2)
            cv2.rectangle(img, (x,y,w,h), (255,255,255),-1)
        pt += (int(w*1.5),0)
