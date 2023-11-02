# Python Image Stegangraphy project
from tkinter import *
import tkinter.filedialog
from tkinter import messagebox
from PIL import ImageTk
from PIL import Image
from io import BytesIO
import os
import binascii
class IMG_Stegno:
    
    def main(self, root):
       
        root.title('Mendel Osdoba')
        root.geometry('500x650')
        root.iconphoto(False, PhotoImage(file='../assets/security.png'))

        root.resizable(width =False, height=False)
        root.config(bg = '#a0d0c0')
        frame = Frame(root)
        frame.grid()

        title = Label(frame, text=' Image Steganography')
        title.config(font=('Times new roman',25, 'bold'),bg = '#e3f4f1')
        title.grid(pady=10)
        title.grid(row=1)

        encode = Button(frame,text="Encode",command= lambda :self.encode_frame1(frame), padx=14,bg = '#e3f4f1' )
        encode.config(font=('Helvetica',15),bg = '#D2B48C')
        encode.grid(row=2)
        decode = Button(frame, text="Decode",command=lambda :self.decode_frame1(frame), padx=14,bg = '#e3f4f1')
        decode.config(font=('Helvetica',15), bg = '#D2B48C')
        decode.grid(pady = 19)
        decode.grid(row=3)

        root.grid_rowconfigure(1, weight=1)
        root.grid_columnconfigure(0, weight=1)
        #function to go back to the main frame
        #frame for encode page


    
    #Back function to loop back to main screen
    def back(self,frame):
        frame.destroy()
        self.main(root)   


    def encode_frame1(self,F):
        F.destroy()
        F2 = Frame(root)
        label1= Label(F2,text='Select the image in which \n you want to hide text :')
        label1.config(font=('Times new roman',25, 'bold'),bg = '#e3f4f1')
        label1.grid()
 
        button_bws = Button(F2, text='Select',command=lambda : self.encode_frame2(F2))
        button_bws.config(font=('Helvetica',15), bg = '#D2B48C')
        button_bws.grid()
        button_back = Button(F2, text='Cancel', command=lambda : IMG_Stegno.back(self,F2))
        button_back.config(font=('Helvetica',15),bg = '#D2B48C')
        button_back.grid(pady=15)
        button_back.grid()
        F2.grid()
 
    #frame for decode page
    def decode_frame1(self,F):
        F.destroy()
        d_f2 = Frame(root)
        label1 = Label(d_f2, text='Select image with Hidden text:')
        label1.config(font=('Times new roman',25,'bold'),bg = '#e3f4f1')
        label1.grid()
        label1.config(bg = '#e3f4f1')
        button_bws = Button(d_f2, text='Select', command=lambda :self.decode_frame2(d_f2))
        button_bws.config(font=('Helvetica',15), bg='#e8c1c7')
        button_bws.grid(pady=15)
        button_back = Button(d_f2, text='Cancel', command=lambda : IMG_Stegno.back(self,d_f2))
        button_back.config(font=('Helvetica',15), bg='#e8c1c7')
        button_back.grid(pady=15)
        button_back.grid()
        d_f2.grid()
    # function to encode image,
    # setting up an encoding interface
    # step 5 
    def encode_frame2(self,e_F2):
        e_pg= Frame(root)
        myfile = tkinter.filedialog.askopenfilename(filetypes = ([('png', '*.png'),('jpeg', '*.jpeg'),('jpg', '*.jpg'),('All Files', '*.*')]))
        if not myfile:
            messagebox.showerror("Error","You have selected nothing !")
        else:
            my_img = Image.open(myfile)
            new_image = my_img.resize((180,180))
            img = ImageTk.PhotoImage(new_image)
            label3= Label(e_pg,text='Selected Image')
            label3.config(font=('Helvetica',14,'bold'))
            label3.grid() 
            board = Label(e_pg, image=img)
            board.image = img
            self.output_image_size = os.stat(myfile)
            self.o_image_w, self.o_image_h = my_img.size
            board.grid()
            label2 = Label(e_pg,text='Enter Data')
            label2.config(font=('Helvetica',14,'bold'))
            label2.grid(pady=15)
            text_a = Text(e_pg, width=50, height=10)
            text_a.grid()
            encode_button = Button(e_pg, text='Cancel', command=lambda: self.back(e_pg))
            encode_button.config(font=('Helvetica',14), bg='#e8c1c7')
            data = text_a.get("1.0", "end-1c")

            button_back = Button(e_pg, text='Encode', command=lambda : [self.enc_fun(text_a,my_img)])
            button_back.config(font=('Helvetica',14), bg='#e8c1c7')
            button_back.grid(pady=15)
            encode_button.grid()
            e_pg.grid(row=1)
            e_F2.destroy()

            
          
        # function to decode image
        #step 6
    def decode_frame2(self,d_F2):
        #attaching new frame to program 
        d_F3 = Frame(root)
        myfiles = tkinter.filedialog.askopenfilename(filetypes = ([('png', '*.png'),('jpeg', '*.jpeg'),('jpg', '*.jpg'),('All Files', '*.*')]))
        if not myfiles:
            messagebox.showerror("You have selected nothing !")
        else:
            my_img = Image.open(myfiles, 'r')
            my_image = my_img.resize((300, 200))
            img = ImageTk.PhotoImage(my_image)
            label4= Label(d_F3,text='Selected Image :')
            label4.config(font=('Helvetica',14,'bold'))
            label4.grid()
            board = Label(d_F3, image=img)
            board.image = img
            board.grid()
            hidden_data = self.decode(my_img)
            print('Hidden Data:', hidden_data)
            label2 = Label(d_F3, text='Hidden data is :')
            label2.config(font=('Helvetica',14,'bold'))
            label2.grid(pady=10)
            text_a = Text(d_F3, width=50, height=10)
            text_a.insert(INSERT, hidden_data)
            text_a.configure(state='disabled')
            text_a.grid()
            button_back = Button(d_F3, text='Cancel', command=lambda: self.frame_3(root, d_F3))
            button_back.config(font=('Helvetica',14),bg='#e8c1c7')
            button_back.grid(pady=15)
            button_back.grid()
            d_F3.grid(row=1)
            d_F2.destroy()    
    #function to decode data
    # at this point we have to take out data from the image to replace with data from text
    
   
    

    def decode(self, image):
        #iterates one element at a time
        image_data = iter(image.getdata())
        print(image_data)
        #empty data object
        data = ''
        char_index = 0
 
        while (True):
            pixels = [value for value in image_data.__next__()[:3] +
                      image_data.__next__()[:3] +
                      image_data.__next__()[:3]]
        
            print("Original Pixels:", pixels)
            for index, pixel_value in enumerate(pixels):
                binary_pixel = format(pixel_value, '08b')
                print(f"Pixel {index + 1}: {binary_pixel}")
            # string of binary data
            binary_str = ''
            for i in pixels[:8]:
                if i % 2 == 0:
                    binary_str += '0'
                else:
                    binary_str += '1'
              # Print the binary string
            char_decoded = chr(int(binary_str, 2))
            print(f"Decoded Character {char_index + 1}: {char_decoded} ({binary_str})")  
            
            data += chr(int(binary_str, 2))
            if pixels[-1] % 2 != 0:
                print("Binary Data:", data)
                print("Modified Pixels:", pixels)  # Print the pixels after modification
                for index, pixel_value in enumerate(pixels):
                    binary_pixel = format(pixel_value, '08b')
                    print(f"Modified Pixel {index + 1}: {binary_pixel}")
                return data
                
    
            char_index += 1
    #function to generate data into zeroes and ones
    def generate_Data(self,data):
        # list of binary codes of given data
        binary_data = []
 
        for i in data:
            binary_data.append(format(ord(i), '08b'))
        return binary_data            
    

    # Function to modify the pixels of the image
    def modify_Pix(self, pix, data):
        print('mp', pix)
        dataList = self.generate_Data(data)
        dataLen = len(dataList)
        print(dataLen)
        imgData = iter(pix)
        #iterate over every character
        for i in range(dataLen):
            #extracts pixel values
            pix = [value for value in imgData.__next__()[:3] +
                imgData.__next__()[:3] +
                imgData.__next__()[:3]]
            print(f"Modifying pixel for character: {data[i]}")
            character_in_binary = format(ord(data[i]), '08b')
            print(character_in_binary)
            print("pixels initially")
            DEBUG = True
            binary_counter = 1
            for value in pix:
                binary_value = format(value, '08b')
                if DEBUG:
                    print(f'Binary {binary_counter}: {binary_value}')
                    binary_counter += 1
            print('pix', pix)    

            #This loop iterates through the 8 bits of binary data to be hidden in pixel.
            for j in range(0, 8):
                # compares every bit in i, our character index,
                # with corresponding bit in pixel
                
                if (dataList[i][j] == '0') and (pix[j] % 2 != 0):
                        pix[j] -= 1
                elif (dataList[i][j] == '1') and (pix[j] % 2 == 0):
                    if(pix[j] != 0):
                        pix[j] -= 1
                    else:
                        pix[j] += 1
                #special case     
            if (i == dataLen - 1):
                if (pix[-1] % 2 == 0):
                    if(pix[-1] != 0):
                        pix[-1] -= 1
                else:
                    pix[-1] += 1
 
            else:
                if (pix[-1] % 2 != 0):
                    pix[-1] -= 1
            print("pixels modified")    
            binary_counter = 1

            for value in pix:
                binary_value = format(value, '08b')
                DEBUG = True
                if DEBUG:
                    print(f'Binary {binary_counter}: {binary_value}')
                    binary_counter += 1        

            pix = tuple(pix)
            print("pix", pix)
            yield pix[0:3]
            yield pix[3:6]
            yield pix[6:9]
            
            
            
    
    # function to enter the data pixels in image
    # it calls modify_pix which loops through list of new pixels
    def encode_enc(self,newImg, data):
        width = newImg.size[0]
        print(width)
        (x, y) = (0, 0)

        for pixel in self.modify_Pix(newImg.getdata(), data):

            # Putting modified pixels in the new image
            newImg.putpixel((x, y), pixel)
            if (x == width - 1):
                x = 0
                y += 1
            else:
                x += 1        

    # function to enter hidden text
    def enc_fun(self,text_a,myImg):
        data = text_a.get("1.0", "end-1c")
        
        if (len(data) == 0):
            messagebox.showinfo("Please enter text")
            
        else:
            
            newImg = myImg.copy()
            self.encode_enc(newImg, data)
            my_file = BytesIO()
            temp=os.path.splitext(os.path.basename(myImg.filename))[0]
            newImg.save(tkinter.filedialog.asksaveasfilename (initialfile=temp, filetypes = ([('png', '*.png')]), defaultextension=".png"))
            self.d_image_size = my_file.tell()
            self.d_image_w,self.d_image_h = newImg.size
            messagebox.showinfo("Success","Encoding Successful\nFile is saved as Image_with_hiddentext.png in the same directory")
            
            binary_data = binascii.b2a_hex(data.encode()).decode()
            print("input text:", data)
            print('length of text', len(data))
            binary_data = ' '.join(format(ord(char), '08b') for char in data)
            print("binary_representation:", binary_data)
    def frame_3(self,root,frame):
        frame.destroy()
        self.main(root)     

#GUI loop
root = Tk()
o = IMG_Stegno()
o.main(root)
root.mainloop()                  