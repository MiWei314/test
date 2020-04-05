import cv2
import numpy as np

while True :
    NoiseTV = np.random.random((600, 800))
    NoiseTV *= 50
    NoiseTV = NoiseTV.round()
    cv2.imshow("NoiseTV", NoiseTV)
    if cv2.waitKey(1) & 0xff == ord('q') :
        break

    
