from tkinter import * #Comes Defalut With Python3
from tkinter import filedialog as fd
from tkinter import messagebox as ms
import matplotlib.pyplot as plt
import cv2
import numpy as np 
from math import *
import math
from skimage import io, color
import PIL # Install Using PIP
from PIL import ImageTk, Image

class application:
    def __init__(self,master):
        self.master = master
        self.c_size = (700,300)
        self.setup_gui(self.c_size)
        self.img=None
    def setup_gui(self,s):
        Scrollbar(self.master)
        Label(self.master,text = 'Pengolahan Citra Digital',pady=5,bg='white',
            font=('Ubuntu',30)).pack()
        self.canvas = Canvas(self.master,height=s[1],width=700,
            bg='white',bd=10,relief='ridge')
        self.canvas.pack()
        txt = '''
                    Pengolahan Citra Digital
                    Charly Haholongan Situmorang
                    1301150023
        '''
        self.wt = self.canvas.create_text(s[0]/2-270,s[1]/2,text=txt
            ,font=('',12),fill='black')
        f=Frame(self.master,bg='white',padx=10,pady=10)
        bottomframe = Frame(self.master,bg='white',padx=10,pady=10)    
        newFrame =  Frame(self.master,bg='white',padx=10,pady=10)
        newFrame1 =  Frame(self.master,bg='white',padx=10,pady=10)

        Button(f,text='Browse Image',bd=2,fg='white',bg='blue',font=('',15)
            ,command=self.make_image).pack(side=LEFT)
        Button(f,text='Grayscale',bd=2,fg='white',bg='blue',font=('',15)
            ,command=self.grayscaleImage).pack(side=LEFT)
        Button(f,text='Zoom 2x',bd=2,fg='white',bg='blue',font=('',15)
            ,command=self.zoomIn).pack(side=LEFT)
        Button(f,text='ZoomOut 2x',bd=2,fg='white',bg='blue',font=('',15)
            ,command=self.zoomOut).pack(side=LEFT)
        Button(f,text='Geser Atas',bd=2,fg='white',bg='blue',font=('',15)
            ,command=self.geserAtas).pack(side=LEFT)
        f.pack()

        Button(bottomframe,text='Geser Bawah',bd=2,fg='white',bg='blue',font=('',15)
            ,command=self.geserBawah).pack(side=LEFT)
        Button(bottomframe,text='Geser Kanan',bd=2,fg='white',bg='blue',font=('',15)
            ,command=self.geserKanan).pack(side=LEFT)
        Button(bottomframe,text='Geser Kiri',bd=2,fg='white',bg='blue',font=('',15)
            ,command=self.geserKiri).pack(side=LEFT)     
        Button(bottomframe,text='Brightness *3',bd=2,fg='white',bg='blue',font=('',15)
            ,command=self.brightnessKali).pack(side=LEFT)   
        Button(bottomframe,text='Brightness /2',bd=2,fg='white',bg='blue',font=('',15)
            ,command=self.brightnessBagi).pack(side=LEFT)  
        bottomframe.pack() 

        Button(newFrame,text='Brightness +50',bd=2,fg='white',bg='blue',font=('',15)
            ,command=self.brightnessTambah).pack(side=LEFT)  
        Button(newFrame,text='Brightness -1',bd=2,fg='white',bg='blue',font=('',15)
            ,command=self.brightnessKurang).pack(side=LEFT)  
        Button(newFrame,text='Histogram',bd=2,fg='white',bg='blue',font=('',15)
            ,command=self.histogram).pack(side=LEFT)   
        Button(newFrame,text='Histogram Eq',bd=2,fg='white',bg='blue',font=('',15)
            ,command=self.grayscaleImage).pack(side=LEFT)   
        Button(newFrame,text='Kernel Blur',bd=2,fg='white',bg='blue',font=('',15)
            ,command=self.blurkernel).pack(side=LEFT)          
        newFrame.pack()

        Button(newFrame1,text='Kernel Sharp',bd=2,fg='white',bg='blue',font=('',15)
            ,command=self.SharpKernel).pack(side=LEFT)       
        Button(newFrame1,text='Kernel Edge',bd=2,fg='white',bg='blue',font=('',15)
            ,command=self.KernelEdge).pack(side=LEFT)    
        Button(newFrame1,text='Threshold base',bd=2,fg='white',bg='blue',font=('',15)
            ,command=self.SegmentasiThreshold).pack(side=LEFT)    
        Button(newFrame1,text='Region Grow',bd=2,fg='white',bg='blue',font=('',15)
            ,command=self.grayscaleImage).pack(side=LEFT)   
        newFrame1.pack()
        
        self.status=Label(self.master,text = 'Current Image: None',bg='gray',
            font=('Ubuntu',15),bd=2,fg='black',relief='sunken',anchor=W)
        self.status.pack(side=BOTTOM,fill=X)
    def make_image(self):
        try:
            File = fd.askopenfilename()
            self.filename = File
            self.pilImage = Image.open(File)
            re=self.pilImage.resize((500,500),Image.ANTIALIAS)
            self.img = ImageTk.PhotoImage(re)
            self.canvas.delete(ALL)
            self.canvas.create_image(self.c_size[0]/2+10,self.c_size[1]/2+10,
                anchor=CENTER,image=self.img)
            self.status['text']='Current Image:'+File
        except:
            ms.showerror('Error!','File type is unsupported.')
    def changePilImage(self, image):
        im = Image.fromarray(image)
        new_im = im.resize((500,500),Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(new_im)
        self.canvas.delete(ALL)
        self.canvas.create_image(self.c_size[0]/2+10,self.c_size[1]/2+10,
                anchor=CENTER,image=self.img)

    def grayscaleImage(self):
        image = cv2.imread(self.filename)
        b,g,r = cv2.split(image) 
        image = cv2.merge((r,g,b)) #base opencv bgr, must convert to rgb
        gray = image.copy()
        height = image.shape[0]
        width = image.shape[1] 
        for i in range(height):
            for j in range(width):
                value_gray = int((r[i,j]+g[i,j]+b[i,j])/3)
                if(value_gray > 255):
                    value_gray = 255
                elif (value_gray < 0):
                    value_gray = 0
                gray[i,j,2] = value_gray 
                gray[i,j,1] = value_gray 
                gray[i,j,0] = value_gray 
        self.changePilImage(gray)
    def zoomIn(self):
        image = Image.open(self.filename) 
        height,width = image.size 
        newimage = image.resize((math.floor(width*4), math.floor(height*4)), Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(newimage)
        self.canvas.delete(ALL)
        self.canvas.create_image(self.c_size[0]/2+10,self.c_size[1]/2+10,
                anchor=CENTER,image=self.img)        
    def zoomOut(self):
        image = Image.open(self.filename) 
        height,width = image.size 
        newimage = image.resize((math.floor(width/2), math.floor(height/2)), Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(newimage)
        self.canvas.delete(ALL)
        self.canvas.create_image(self.c_size[0]/2+10,self.c_size[1]/2+10,
                anchor=CENTER,image=self.img)
    def geserKiri(self):
        image = cv2.imread(self.filename)
        height = image.shape[0]
        width = image.shape[1] 
        blank_image = np.zeros((width,width,3),np.uint8)
        for i in range(height):
            for j in range(width):
                if(int(j+(width/2)) >= width):
                    blank_image[i,j,2] = 0
                    blank_image[i,j,1] = 0
                    blank_image[i,j,0] = 0
                else:
                    blank_image[i,j,2] = image[i,int(j + (width/2)),2]
                    blank_image[i,j,1] = image[i,int(j + (width/2)),1]
                    blank_image[i,j,0] = image[i,int(j + (width/2)),0]
        b,g,r = cv2.split(blank_image) 
        resultImage = cv2.merge((r,g,b))
        self.changePilImage(resultImage)

    def geserKanan(self):
        image = cv2.imread(self.filename)
        height = image.shape[0]
        width = image.shape[1] 
        blank_image = np.zeros((width,width,3),np.uint8)
        for i in range(height):
            for j in range(width):
                if( j >= width/2):
                    blank_image[i,j,2] = image[i,int(j - (width/2)),2]
                    blank_image[i,j,1] = image[i,int(j - (width/2)),1]
                    blank_image[i,j,0] = image[i,int(j - (width/2)),0]
                else:
                    blank_image[i,j,2] = 0
                    blank_image[i,j,1] = 0
                    blank_image[i,j,0] = 0
        b,g,r = cv2.split(blank_image) 
        resultImage = cv2.merge((r,g,b))
        self.changePilImage(resultImage)
    def geserAtas(self):
        image = cv2.imread(self.filename)
        height = int(image.shape[0]*2)
        width = int(image.shape[1]*2)
        geserAtas = int(image.shape[0]/2)
        R = np.array(image[:, :,2])
        G = np.array(image[:, :,1])
        B = np.array(image[:, :,0])  
        mid= image.shape[0]/2
        blank_image = np.zeros((width,width,3),np.uint8)
        print(blank_image.shape)
        for i in range(int(image.shape[0]),1,-1):
            for j in range(int(image.shape[0]),1,-1):
                blank_image[i,j+geserAtas,0] = B[i-1,j-1]
                blank_image[i,j+geserAtas,1] = G[i-1,j-1]
                blank_image[i,j+geserAtas,2] = R[i-1,j-1]
        b,g,r = cv2.split(blank_image) 
        resultImage = cv2.merge((r,g,b))
        self.changePilImage(resultImage)

    def geserBawah(self):
        image = cv2.imread(self.filename)
        height = image.shape[0]
        width = image.shape[1] 
        blank_image = np.zeros((width,width,3),np.uint8)
        for i in range(height):
            for j in range(width):
                if( i >= width/2):
                    blank_image[i,j,2] = image[int(i - (width/2)),j,2]
                    blank_image[i,j,1] = image[int(i - (width/2)),j,1]
                    blank_image[i,j,0] = image[int(i - (width/2)),j,0]
                else:
                    blank_image[i,j,2] = 0
                    blank_image[i,j,1] = 0
                    blank_image[i,j,0] = 0
        b,g,r = cv2.split(blank_image) 
        resultImage = cv2.merge((r,g,b))
        self.changePilImage(resultImage)
    def brightnessTambah(self):
        image = cv2.imread(self.filename)
        height = image.shape[0]
        width = image.shape[1] 
        blank_image = np.zeros((width,width,3),np.uint8)
        for i in range(height):
            for j in range(width):
                # print("before "+str(image[i,j,2])+" after "+str(math.floor(image[i,j,2] + 10)))
                blank_image[i,j,2] = math.floor(image[i,j,2] + 50)
                blank_image[i,j,1] = math.floor(image[i,j,1] + 50)
                blank_image[i,j,0] = math.floor(image[i,j,0] + 50)
        b,g,r = cv2.split(blank_image) 
        resultImage = cv2.merge((r,g,b))
        self.changePilImage(resultImage)

    def brightnessKurang(self):
        image = cv2.imread(self.filename)
        height = image.shape[0]
        width = image.shape[1] 
        blank_image = np.zeros((width,width,3),np.uint8)
        for i in range(height):
            for j in range(width):
                if(math.floor(image[i,j,2]-1) <= 0):
                    blank_image[i,j,2] = 0
                elif(math.floor(image[i,j,1]-1) <= 0):
                    blank_image[i,j,1] = 0
                elif(math.floor(image[i,j,0]-1) <= 0):
                    blank_image[i,j,0] = 0
                else:    
                    blank_image[i,j,2] = math.floor(image[i,j,2]-1)
                    blank_image[i,j,1] = math.floor(image[i,j,1]-1)
                    blank_image[i,j,0] = math.floor(image[i,j,0]-1)
        b,g,r = cv2.split(blank_image) 
        resultImage = cv2.merge((r,g,b))
        self.changePilImage(resultImage)

    def brightnessKali(self):
        image = cv2.imread(self.filename)
        height = image.shape[0]
        width = image.shape[1] 
        blank_image = np.zeros((width,width,3),np.uint8)
        for i in range(height):
            for j in range(width):
                blank_image[i,j,2] = math.floor(image[i,j,2] * 3)
                blank_image[i,j,1] = math.floor(image[i,j,1] * 3)
                blank_image[i,j,0] = math.floor(image[i,j,0] * 3)
                if(blank_image[i,j,0] <= 0):
                    blank_image[i,j,0] = 0
                elif(blank_image[i,j,1] <= 0):
                    blank_image[i,j,1] = 0
                elif(blank_image[i,j,2] <= 0):
                    blank_image[i,j,2] = 0
                elif(blank_image[i,j,0] >= 255 ):
                    blank_image[i,j,0] = 255
                elif(blank_image[i,j,1] >= 255):
                    blank_image[i,j,1] = 255
                elif(blank_image[i,j,2] >= 255):
                    blank_image[i,j,2]  = 255
        b,g,r = cv2.split(blank_image) 
        resultImage = cv2.merge((r,g,b))
        self.changePilImage(resultImage)

    def brightnessBagi(self):
        image = cv2.imread(self.filename)
        height = image.shape[0]
        width = image.shape[1] 
        blank_image = np.zeros((width,width,3),np.uint8)
        for i in range(height):
            for j in range(width):
                blank_image[i,j,2] = math.floor(image[i,j,2] / 2)
                blank_image[i,j,1] = math.floor(image[i,j,1] / 2)
                blank_image[i,j,0] = math.floor(image[i,j,0] / 2)
                if(blank_image[i,j,0] <= 0):
                    blank_image[i,j,0] = 0
                elif(blank_image[i,j,1] <= 0):
                    blank_image[i,j,1] = 0
                elif(blank_image[i,j,2] <= 0):
                    blank_image[i,j,2] = 0
                elif(blank_image[i,j,0] >= 255 ):
                    blank_image[i,j,0] = 255
                elif(blank_image[i,j,1] >= 255):
                    blank_image[i,j,1] = 255
                elif(blank_image[i,j,2] >= 255):
                    blank_image[i,j,2]  = 255
        b,g,r = cv2.split(blank_image) 
        resultImage = cv2.merge((r,g,b))
        self.changePilImage(resultImage)

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
        n, bins, patches = plt.hist(gray_array, num_bins, facecolor='blue', alpha=0.5)
        print("check value "+str(np.unique(gray_array)))
        plt.show()

    def blurkernel(self):
        img = cv2.imread(self.filename)
        image = color.rgb2gray(img) 
        kernel_blur = np.array([[1,1,1],[1,1,1],[1,1,1]])
        new_kernel = np.flipud(np.fliplr(kernel_blur))
        output = np.zeros_like(image) 
        image_padded = np.zeros((image.shape[0] + 2, image.shape[1] + 2))
        image_padded[1:-1, 1:-1] = image
        for x in range(image.shape[1]):     # Loop over every pixel of the image
            for y in range(image.shape[0]):
                # element-wise multiplication of the kernel and the image
                output[y,x]=(kernel_blur*image_padded[y:y+3,x:x+3]).sum()     
        plt.imshow(output, cmap=plt.cm.gray)
        plt.show()   

    def SharpKernel(self):
        img = cv2.imread(self.filename) 
        image = color.rgb2gray(img) 
        kernel_sharp = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])
        new_kernel = np.flipud(np.fliplr(kernel_sharp))
        output = np.zeros_like(image) 
        image_padded = np.zeros((image.shape[0] + 2, image.shape[1] + 2))
        image_padded[1:-1, 1:-1] = image
        for x in range(image.shape[1]):     # Loop over every pixel of the image
            for y in range(image.shape[0]):
                # element-wise multiplication of the kernel and the image   
                output[y,x]=(kernel_sharp*image_padded[y:y+3,x:x+3]).sum()        
        plt.imshow(output, cmap=plt.cm.gray)
        plt.show() 

    def KernelEdge(self):
        img = cv2.imread(self.filename) 
        image = color.rgb2gray(img) 
        kernel_edge = np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]])
        new_kernel = np.flipud(np.fliplr(kernel_edge))
        output = np.zeros_like(image) 
        image_padded = np.zeros((image.shape[0] + 2, image.shape[1] + 2))
        image_padded[1:-1, 1:-1] = image
        for x in range(image.shape[1]):     # Loop over every pixel of the image
            for y in range(image.shape[0]):
                # element-wise multiplication of the kernel and the image
                output[y,x]=(kernel_edge*image_padded[y:y+3,x:x+3]).sum()        
        plt.imshow(output, cmap=plt.cm.gray)
        plt.show() 
    def SegmentasiThreshold(self):
        image = cv2.imread(self.filename)
        threshold = image.copy()
        imgToGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
        for x in range(imgToGray.shape[0]):
            for y in range(imgToGray.shape[1]):
                if(imgToGray[x,y] < 60):
                    threshold[x,y] = 0
                else:
                    threshold[x,y] = 255 
        self.changePilImage(threshold)                   
root=Tk()
root.configure(bg='white')
root.title('Pengolahan Citra Digital')
application(root)
root.resizable(0,0)
root.mainloop()
# template GUI by https://pastebin.com/b7Hy33ra 
#creating object of class and tk window-