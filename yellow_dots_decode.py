import cv2 
import numpy as np
import sys
def yellow_dots(image_path):
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError("Image not found or unable to load.")
    else :
        pass 
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower_yellow = np.array([20, 100, 100]) # Min yellow
    upper_yellow = np.array([40, 255, 255]) # Max yellow
    mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
    height, width = mask.shape[:2]  
    scale = 0.5                   
    resized_mask = cv2.resize(mask, (int(width*scale), int(height*scale)))
    cv2.imshow("Yellow Mask", resized_mask)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python yellow_dots_decode.py <image_path>")
        print("Example: python yellow_dots_decode.py C:\\CTF\\ch18.png")
        sys.exit(1)
    
    img_path = sys.argv[1]
    yellow_dots(img_path)