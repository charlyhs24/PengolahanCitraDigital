from tkinter import * #Comes Defalut With Python3
from tkinter import filedialog as fd
from tkinter import messagebox as ms
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import PIL # Install Using PIP
from PIL import ImageTk, Image
import math

class application:
    def __init__(self,master):
        self.master = master
        self.c_size = (700,500)
        self.setup_gui(self.c_size)
        self.img=None
 
    def setup_gui(self,s):
        Label(self.master,text = 'Pengolahan Citra Digital',pady=5,bg='white',
            font=('Ubuntu',30)).pack()
        self.canvas = Canvas(self.master,height=s[1],width=s[0],
            bg='black',bd=10)
        self.canvas.pack()
        txt = '''
                    Pengolahan Citra Digital
                    Charly Haholongan Situmorang
                    1301150023
        '''
        self.wt = self.canvas.create_text(s[0]/2-270,s[1]/2,text=txt
            ,font=('',15),fill='white')
        f=Frame(self.master,bg='white',padx=10,pady=10)
        Button(f,text='Browse Image',bd=2,fg='white',bg='blue',font=('',15)
            ,command=self.make_image).pack(side=LEFT)
        f.pack()
        Button(f,text='Grayscale',bd=2,fg='white',bg='blue',font=('',15)
            ,command=self.grayscaleImage).pack(side=LEFT)
        f.pack()
        Button(f,text='Perbesar',bd=2,fg='white',bg='blue',font=('',15)
            ,command=self.perbesarImage).pack(side=LEFT)

        Button(f,text='Perkecil',bd=2,fg='white',bg='blue',font=('',15)
            ,command=self.perkecilImage).pack(side=LEFT)
        f.pack()
        f.pack()        
        self.status=Label(self.master,text = 'Current Image: None',bg='gray',
            font=('Ubuntu',15),bd=2,fg='black',relief='sunken',anchor=W)
        self.status.pack(side=BOTTOM,fill=X)

    def perbesarImage(self):
        ms.showinfo("gambar diproses", "Proses Perbesar gambar memakan waktu cukup lama, silahkan ditunggu")
        image = mpimg.imread(self.filename) 
        img = image.shape
        width = img[0]*10
        height = img[1]*10
        plt.imshow(image)
        zeroimage = np.zeros((width,height,3))
        R = np.array(image[:, :,0])
        G = np.array(image[:, :,1])
        B = np.array(image[:, :,2])
        for i  in range(width):
            for j in range(height):
                zeroimage[i,j,0] = image[math.floor(i/10),math.floor(j/10),0] 
                zeroimage[i,j,1] = image[math.floor(i/10),math.floor(j/10),1]
                zeroimage[i,j,2] = image[math.floor(i/10),math.floor(j/10),2]  
        ms.showinfo("Title", "Ukuran Gambar Setelah diperbesar"+str(zeroimage.shape))      
        plt.imshow(zeroimage)
        plt.show()
        
    def perkecilImage(self):
        ms.showinfo("Info","fungsi belum ada")
        data = Image.new("RGB", (int(self.img.size[0]/2), int(self.img.size[1]/2)))
        print(self.img.size)
        widthImage = self.img.size[0]/2
        heightImage = self.img.size[1]/2
        # for i in range(width):
        #     for j in range(height):


    def grayscaleImage(self):
        image = mpimg.imread(self.filename) 
        x = self.pilImage.size[0]
        y = self.pilImage.size[1]
        
        grayImage = np.zeros((image.shape))
        R = np.array(image[:, :, 0])
        G = np.array(image[:, :, 1])
        B = np.array(image[:, :, 2])
        
        for i in range(x):
            for j in range(y):
                gray = (R[i, j] * 0.5) + (G[i, j] * 0.25) + (B[i, j] * 0.25)
                grayImage[i, j,0] = gray
                grayImage[i, j,1] = gray
                grayImage[i, j,2] = gray
        plt.imshow(grayImage)
        plt.show()

    def make_image(self):
        ms.showinfo("Info","format gambar yang bisa di proses hanya .PNG")
        try:
            File = fd.askopenfilename(initialdir="/")
            self.filename = File
            self.pilImage = Image.open(File)
            image = mpimg.imread(self.filename) 
            self.img = ImageTk.PhotoImage(self.pilImage)
            self.canvas.delete(ALL)
            self.canvas.create_image(self.c_size[0]/2+10,self.c_size[1]/2+10,
                anchor=CENTER,image=self.img)
            self.status['text']='Current Image:'+File
            ms.showinfo("Informasi Gambar", "Ukuran Gambar Original"+str(image.shape))
        except:
            ms.showerror('Error!','File type is unsupported.')
            
# template GUI by https://pastebin.com/b7Hy33ra 
#creating object of class and tk window-
root=Tk()
root.configure(bg='white')
root.title('Image Viewer')
application(root)
root.resizable(0,0)
root.mainloop()
