import cv2
import tkinter as tk
from tkinter import messagebox
from time import sleep
import os
key = cv2.waitKey(1)
webcam = cv2.VideoCapture(0)
sleep(2)
root = tk.Tk()
root.withdraw()
messagebox.showinfo("Instructions!", "Click \"S\" Capturing \n Click \"Q\" = Quit")
path = os.getcwd()
try:
    while True:

        try:
            check, frame = webcam.read()
            cv2.imshow("Capturing", frame)
            key = cv2.waitKey(1)
            if key == ord('s'): 
                cv2.imwrite(os.path.join(path , 'Saved Picture\saved_img.jpg'), img=frame)
                webcam.release()
                print("Processing image...")
                img_ = cv2.imread(os.path.join(path , 'Saved Picture\saved_img.jpg'), cv2.IMREAD_ANYCOLOR)
                print("Image saved!")
                webcam.release()
                cv2.destroyAllWindows()
                
                break
            
            elif key == ord('q'):
                webcam.release()
                cv2.destroyAllWindows()
                break
        
        except(KeyboardInterrupt):
            print("Turning off camera.")
            webcam.release()
            print("Camera off.")
            print("Program ended.")
            cv2.destroyAllWindows()
            break
except:
    messagebox.showinfo("Warning!!!", "Webcam not found",icon = 'warning')


webcam.release()
cv2.destroyAllWindows()