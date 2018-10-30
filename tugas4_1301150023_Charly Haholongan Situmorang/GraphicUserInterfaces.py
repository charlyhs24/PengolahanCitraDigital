from tkinter import * #Comes Defalut With Python3
from tkinter import filedialog as fd
from tkinter import messagebox as ms
import numpy as np
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import PIL # Install Using PIP
from PIL import ImageTk, Image
import matplotlib.mlab as mlab
import math
from skimage import exposure

class application:
    def __init__(self,master):
        self.master = master
        self.c_size = (700,300)
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
        f.pack()
        bottomframe = Frame(self.master,bg='white',padx=10,pady=10)
        bottomframe.pack()
        newFrame =  Frame(self.master,bg='white',padx=10,pady=10)
        newFrame.pack()
        Button(f,text='Browse Image',bd=2,fg='white',bg='blue',font=('',15)
            ,command=self.make_image).pack(side=LEFT)

        Button(f,text='Grayscale',bd=2,fg='white',bg='blue',font=('',15)
            ,command=self.grayscaleImage).pack(side=LEFT)
        
        Button(f,text='Perbesar',bd=2,fg='white',bg='blue',font=('',15)
            ,command=self.perbesarImage).pack(side=LEFT)

        Button(f,text='Perkecil',bd=2,fg='white',bg='blue',font=('',15)
            ,command=self.perkecilImage).pack(side=LEFT)

        Button(f,text='Geser Atas',bd=2,fg='white',bg='blue',font=('',15)
            ,command=self.geseratas).pack(side=LEFT)

        Button(f,text='Geser Bawah',bd=2,fg='white',bg='blue',font=('',15)
            ,command=self.geserbawah).pack(side=LEFT)                
   
        Button(bottomframe,text='Geser <=',bd=2,fg='white',bg='blue',font=('',15)
            ,command=self.geserkiri).pack(side=LEFT)   

        Button(bottomframe,text='Geser =>',bd=2,fg='white',bg='blue',font=('',15)
            ,command=self.geserkanan).pack(side=LEFT)                

        Button(bottomframe,text='Brightness *',bd=2,fg='white',bg='blue',font=('',15)
            ,command=self.brightnessKali).pack(side=LEFT)                

        Button(bottomframe,text='Brightness +',bd=2,fg='white',bg='blue',font=('',15)
            ,command=self.brightnessTambah).pack(side=LEFT)   

        Button(bottomframe,text='Brightness -',bd=2,fg='white',bg='blue',font=('',15)
            ,command=self.brightnessKurang).pack(side=LEFT)   

        Button(bottomframe,text='Brightness "/"',bd=2,fg='white',bg='blue',font=('',15)
            ,command=self.brightnessBagi).pack(side=LEFT)    

        Button(newFrame,text='Histogram',bd=2,fg='white',bg='blue',font=('',15)
            ,command=self.histogram).pack(side=LEFT)

        Button(newFrame,text='Histeq',bd=2,fg='white',bg='blue',font=('',15)
            ,command=self.histogramEqualisasi).pack(side=LEFT)        
        Button(newFrame,text='VAlue Image',bd=2,fg='white',bg='blue',font=('',15)
            ,command=self.valueArray).pack(side=LEFT)                
        self.status=Label(self.master,text = 'Current Image: None',bg='gray',
            font=('Ubuntu',15),bd=2,fg='black',relief='sunken',anchor=W)
        self.status.pack(side=BOTTOM,fill=X)
    def valueArray(self):
        image = mpimg.imread(self.filename) 
        print(image.shape)
    def perbesarImage(self):
        ms.showinfo("gambar diproses", "Proses Perbesar gambar memakan waktu cukup lama, silahkan ditunggu")
        image = Image.open(self.filename) 
        height,width = image.size
        zeroimage = np.zeros((width,width,3),np.uint8)
        newimage = image.resize((int(width*2), int(height*2)), Image.ANTIALIAS)
        # R = np.array(image[:, :,0])
        # G = np.array(image[:, :,1])
        # B = np.array(image[:, :,2])
        # for i  in range(width):
        #     for j in range(height):
        #         zeroimage[i,j,0] = image[int(math.floor(i/10)),int(math.floor(j/10)),0] 
        #         zeroimage[i,j,1] = image[int(math.floor(i/10)),int(math.floor(j/10)),1]
        #         zeroimage[i,j,2] = image[int(math.floor(i/10)),int(math.floor(j/10)),2]  
        # ms.showinfo("Title", "Ukuran Gambar Setelah diperbesar"+str(zeroimage.shape))      
        plt.imshow(newimage)
        plt.show()

    def geserkanan(self):
        image = mpimg.imread(self.filename) 
        height = image.shape[0]*2
        width = image.shape[1]*2
        geserKanan = image.shape[0]
        R = np.array(image[:, :,2])
        G = np.array(image[:, :,1])
        B = np.array(image[:, :,0])        
        blank_image = np.zeros((width,width,3),np.uint8)
        for i in range(image.shape[0]):
            for j in range(image.shape[0]):
                blank_image[i,j+geserKanan,0] = R[i,j]
                blank_image[i,j+geserKanan,1] = G[i,j]
                blank_image[i,j+geserKanan,2] = B[i,j] 
        plt.imshow(blank_image)
        plt.show()        

    def geserkiri(self):
        image = cv2.imread(self.filename)
        height = image.shape[0]*2
        width = image.shape[1]*2
        geserKanan = image.shape[0]
        R = np.array(image[:, :,2])
        G = np.array(image[:, :,1])
        B = np.array(image[:, :,0])          
        blank_image = np.zeros((width,width,3),np.uint8)
        for i in range(image.shape[0]):
            for j in range(image.shape[1]):
                blank_image[i+int(geserKanan/2),j,0] = R[i,j]
                blank_image[i+int(geserKanan/2),j,1] = G[i,j]
                blank_image[i+int(geserKanan/2),j,2] = B[i,j]
        plt.imshow(blank_image)
        plt.show()      

    def geserbawah(self):
        image = cv2.imread(self.filename)
        height = image.shape[0]*2
        width = image.shape[1]*2
        geserBawah = image.shape[0]
        R = np.array(image[:, :,2])
        G = np.array(image[:, :,1])
        B = np.array(image[:, :,0])  
        blank_image = np.zeros((width,width,3),np.uint8)
        for i in range(image.shape[0]):
            for j in range(image.shape[0]):
                blank_image[i+geserBawah,j,0] = R[i,j]
                blank_image[i+geserBawah,j,1] = G[i,j]
                blank_image[i+geserBawah,j,2] = B[i,j]
        plt.imshow(blank_image)
        plt.show()   

    def geseratas(self):
        image = cv2.imread(self.filename)
        newheight = image.shape[0]
        newwidth = image.shape[1]
        height = int(image.shape[0]*2)
        width = int(image.shape[1]*2)
        geserAtas = int(image.shape[0])
        R = np.array(image[:, :,2])
        G = np.array(image[:, :,1])
        B = np.array(image[:, :,0])  
        mid= image.shape[0]/2
        blank_image = np.zeros((width,width,3),np.uint8)
        print(blank_image.shape)
        for i in range(newheight),1,-1):
            for j in range(newwidth),1,-1):
                blank_image[i,j+geserAtas,0] = R[i-1,j-1]
                blank_image[i,j+geserAtas,1] = G[i-1,j-1]
                blank_image[i,j+geserAtas,2] = B[i-1,j-1]
        plt.imshow(blank_image)
        plt.show()                

    def perkecilImage(self):
        image = Image.open(self.filename) 
        height,width = image.size
        # blank_image = np.zeros((int(height * 0.5),int(width * 0.5),3), np.uint8)
        image3 = image.resize((int(width*0.5), int(height*0.5)), Image.ANTIALIAS)
        # for i in range(int(blank_image.shape[0])):
        #     for j in range(int(blank_image.shape[1])):
        #         datar = image[i,j,0]*0.5
        #         datag = image[i,j,1]*0.5
        #         datab = image[i,j,2]*0.5
        #         blank_image[i,j,0] = datar
        #         blank_image[i,j,1] = datag
        #         blank_image[i,j,2] = datab
        plt.imshow(image3)
        plt.show()
    def grayscaleImage(self):
        image = mpimg.imread(self.filename) 
        gray = image.copy()
        print(image.shape)
        for i in range(int(image.shape[0])):
            for j in range(int(image.shape[1])):
                value_gray = (image[i,j,0]+image[i,j,1]+image[i,j,2])/3
                gray[i,j,0] = value_gray 
                gray[i,j,1] = value_gray 
                gray[i,j,2] = value_gray 
        plt.imshow(gray)
        plt.show()
    def brightnessBagi(self):
        image = cv2.imread(self.filename)
        bright = image.copy()
        R = np.array(image[:, :,2])
        G = np.array(image[:, :,1])
        B = np.array(image[:, :,0])  
        for i in range(int(image.shape[0])):
            for j in range(int(image.shape[0])):
                bright[i,j,0] = R[i,j]/2
                bright[i,j,1] = G[i,j]/2
                bright[i,j,2] = B[i,j]/2
        plt.imshow(bright)
        plt.show()    
    def brightnessKurang(self):
        image = cv2.imread(self.filename)
        bright = image.copy()
        R = np.array(image[:, :,2])
        G = np.array(image[:, :,1])
        B = np.array(image[:, :,0])  
        for i in range(int(image.shape[0])):
            for j in range(int(image.shape[0])):
                bright[i,j,0] = R[i,j]-10
                bright[i,j,1] = G[i,j]-10
                bright[i,j,2] = B[i,j]-10
        plt.imshow(bright)
        plt.show()    

    def brightnessKali(self):
        image = cv2.imread(self.filename)
        bright = image.copy()
        R = np.array(image[:, :,2])
        G = np.array(image[:, :,1])
        B = np.array(image[:, :,0])  
        for i in range(int(image.shape[0])):
            for j in range(int(image.shape[0])):
                # print(image[i,j,0],image[i,j,1],image[i,j,2])
                bright[i,j,0] = R[i,j]*1.2
                bright[i,j,1] = G[i,j]*1.2
                bright[i,j,2] = B[i,j]*1.2
        plt.imshow(bright)
        plt.show()
    def brightnessTambah(self):
        image = cv2.imread(self.filename)
        bright = image.copy()
        R = np.array(image[:, :,2])
        G = np.array(image[:, :,1])
        B = np.array(image[:, :,0])  
        for i in range(int(image.shape[0])):
            for j in range(int(image.shape[0])):
                bright[i,j,0] = R[i,j]+10
                bright[i,j,1] = G[i,j]+10
                bright[i,j,2] = B[i,j]+10
        plt.imshow(bright)
        plt.show()       
    def histogram(self):
        image = cv2.imread(self.filename)
        gray_array = []
        gray = image.copy()
        print(image.shape)
        for i in range(int(image.shape[0])):
            for j in range(int(image.shape[1])):
                value_gray = int((image[i,j,0]+image[i,j,1]+image[i,j,2])/3) #convert to grayscale
                gray[i,j,0] = value_gray 
                gray[i,j,1] = value_gray 
                gray[i,j,2] = value_gray 
                gray_array.append(value_gray)
                gray_array.sort()
        num_bins = 256
        n, bins, patches = plt.hist(gray.ravel(), num_bins, facecolor='blue', alpha=0.5)
        print("check value "+str(np.unique(gray_array)))

        plt.show()
        
    def histogramEqualisasi(self):
        image = cv2.imread(self.filename)
        img_eq = exposure.equalize_hist(image)
        img_adapteq = exposure.equalize_adapthist(image, clip_limit=0.03)
        num_bins = 256
        plt.hist(img_adapteq.ravel(), num_bins, facecolor='blue', alpha=0.5)
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
