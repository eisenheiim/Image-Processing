inp_filename, operation, out_filename = input().split()
# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

height=0
width=0
max_pixel=0
mode=""
def read_imagefile(f):
    global max_pixel
    global mode
    variables=f.readline().strip().split()
    mode=(variables[0]) #assigning the picture's properties.
    height=int(variables[1])
    width=int(variables[2])
    max_pixel=int(variables[3])

    image_matrix=[]
    rest=f.read()#taking rest of the picture
    rest_file=rest.split()
  
    i=0
    for row in range(height):

        row_i=[]
        for column in range(width):
            row_i.append(int(rest_file[i])) #appending each row the the list
            i+=1
        image_matrix.append(row_i)

    return image_matrix

def write_imagefile(f,img_matrix):
    height=len(img_matrix)
    width=len(img_matrix[0])
    f.write(f"{mode} {height} {width} {max_pixel}\n")
    for row in range(height): #writing rows into the file

        for column in range(width):
            f.write(f"{img_matrix[row][column]} ")
        f.seek(f.tell()-1)
        f.write("\n")
def convolution(img_matrix, kernel):
    height=len(img_matrix)
    width=len(img_matrix[0])
    img_matrix.insert(0,[0]*(width+2)) #adding the paddings to calculate values.
    img_matrix.append([0]*(width+2))
    for i in range(1,len(img_matrix)-1):
        img_matrix[i].insert(0,0)
        img_matrix[i].append(0)
  
    
   
    kernel_width=width
    kernel_height=height
    reskernel=[]
    for i in range(kernel_height):
        reskernel.append([])
    
    for i in range(kernel_height):
        for j in range(kernel_width): #calculating the values.
            num1=img_matrix[i][j]*kernel[0][0]
            num2=img_matrix[i][j+1]*kernel[0][1]
            
            num3=img_matrix[i][j+2]*kernel[0][2]
            num4=img_matrix[i+1][j]*kernel[1][0]
            num5=img_matrix[i+1][j+1]*kernel[1][1]
            num6=img_matrix[i+1][j+2]*kernel[1][2]
            num7=img_matrix[i+2][j]*kernel[2][0]
            num8=img_matrix[i+2][j+1]*kernel[2][1]
            num9=img_matrix[i+2][j+2]*kernel[2][2]
           
            res=num1+num2+num3+num4+num5+num6+num7+num8+num9
            res = 0 if res < 0 else 255 if res > 255 else res #limiting result.
            reskernel[i].append(res) #inserting the values
    
    return reskernel





def misalign(img_matrix):
    height=len(img_matrix)
    width=len(img_matrix[0])
    for column in range(1,width,2): 
        for row in range(height//2):
            img_matrix[row][column],img_matrix[height-1-row][column]=img_matrix[height-1-row][column],img_matrix[row][column]#mutually changing value of the pixel with the one at corresponding bottom positin

    return img_matrix


def sort_columns(img_matrix):
    height=len(img_matrix)
    width=len(img_matrix[0])
   
    for i in range(width):
        res=[]
        for j in range(height):
            res.append(img_matrix[j][i])#appending each column into res list.
        res.sort()#sorting columns
        for row in range(height):
            img_matrix[row][i]=res[row]#reappending columns.
        
   
    return img_matrix


    
def sort_rows_border(img_matrix):
    height=len(img_matrix)
    width=len(img_matrix[0])
    for row in range(height):
        start=0
        row_i=img_matrix[row].copy() #taking each row.
       
    
        for pixel in range(width) :
            if pixel==width-1 and row_i[pixel]!=0: #when we are at the end if pixel is not black we are sorting
                img_matrix[row][start:width]=sorted(img_matrix[row][start:width])
            if row_i[pixel]==0: # if pixel is black
                if pixel>0 :#and not the first pixel
                        if row_i[pixel-1]!=0: #and not a following black pixel
                    
                            img_matrix[row][start:pixel]=sorted(img_matrix[row][start:pixel])
                            start=pixel                    
            else: #if it is not black.
                if pixel>0:
                    if row_i[pixel-1]==0:#after passing the border checking if it is another start position.
                        start=pixel
                else:continue
    return img_matrix
                
            
# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
f = open(inp_filename, "r")
img_matrix = read_imagefile(f)
f.close()

if operation == "misalign":
    img_matrix = misalign(img_matrix)

elif operation == "sort_columns":
    img_matrix = sort_columns(img_matrix)

elif operation == "sort_rows_border":
    img_matrix = sort_rows_border(img_matrix)

elif operation == "highpass":
    kernel = [
        [-1, -1, -1],
        [-1, 9, -1],
        [-1, -1, -1]
    ]
    img_matrix = convolution(img_matrix, kernel)

f = open(out_filename, "w")
write_imagefile(f, img_matrix)
f.close()