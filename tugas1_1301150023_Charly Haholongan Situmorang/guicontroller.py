from tkinter import filedialog
import cv2
class GuiController:
    def browse_photoButton(self):
        self.filename = filedialog.askopenfilename(
            initialdir="/", title="Select file", filetypes=(("jpeg files", "*.jpg", ".gif"), ("all files", "*.*")))
        img = cv2.imread(self.filename)
        cv2.imshow('image', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
