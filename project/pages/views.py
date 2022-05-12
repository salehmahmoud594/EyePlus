from django.shortcuts import render
import os
import glob
import ntpath
import sys


# Create your views here.

def index(request):
    files = list()
    last = list()
    rec_path  = os.path.join(os.path.abspath(os.getcwd()),'project\\static\\recordings')
    output_directory = os.path.join(rec_path , 'mp4Videos\\')

    input_directory = output_directory
    aviFiles = glob.glob(rec_path + '/*.avi')
    # print(aviFiles)
    # print('#'*50)

    for rec in aviFiles:
        try:
            avi2mp4(rec, output_directory)
        except:
            raise

    # print('#'*50)
    # print(output_directory)
    # print('#'*50)
    recs =os.listdir(output_directory) 
    draw_img(len(recs))
    
    for counter , rec in enumerate(recs):
        record = {rec:os.path.join(output_directory,rec)}
        # record = {rec:os.path.join(output_directory,rec) , 'counter':counter}
        files.append(record)
        # print('#'*50)
        # print(counter)
        # print('#'*50)
    # print(files)
    # print('*'*50)
    # last_videos(output_directory)
    # print()
    # print('#'*50)
    # print(files)
    # print('#'*50)
    return render(request, 'pages/index.html',{"files":files , "last":last_videos(output_directory)})
    
def last_videos(path):
    last = list()
    files = os.listdir(path)
    paths = [os.path.join(path, basename) for basename in files]
    for i in range(3):
        last.append(paths[i])
    return last


def avi2mp4(file_name, output_directory):
    input_name = file_name
    output_name = ntpath.basename(file_name)
    output = output_directory + output_name.replace('.avi', '.mp4', 1)
    cmd = 'ffmpeg -i "{input}"  -c:a copy -c:v vp9 -b:v 100K "{output}"'.format(input = input_name, output = output)
    # print('#'*20)
    # print(output)
    # print('#'*20)
    # cmd = 'ffmpeg -i "{input}" -c:v copy -c:a copy -y  "{output}"'.format(input = input_name, output = output)
    return os.popen(cmd)


def draw_img(num):
    from PIL import Image
    from PIL import ImageFont
    from PIL import ImageDraw

    # Plot question mark:

    img = Image.new('RGB', (300,300), (17,29,70))  #! Color
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("OpenSans-Regular.ttf", 400)
    draw.text((180, -30),"?",(250,250,250),font=font)     #! Color

    # plot digit numbers (from 0 to ...):
    for i in range(num):
        img = Image.new('RGB', (300,300), (17,29,70))   #! Color
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("OpenSans-Regular.ttf", 200)
        draw.text((150, -30),str(i),(250,250,250),font=font)    #! Color
        savefile = os.path.join(os.path.abspath(os.getcwd()),'project\\static\\images\\')
        # print(savefile)
        # print(savefile + 'num '+str(i)+'.jpg')
        # print('#'*50)
        img.save(savefile +str(i)+'.jpg')

