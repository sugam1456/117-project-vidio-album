import os
import cv2


path = "Images"

images = []


for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file

        print(file_name)
               
        images.append(file_name)
        
print(len(images))
count = len(images)

frame=cv2.imread(images[1])

height,width,channel = frame.shape

video=cv2.VideoWriter("Video.mp4", cv2.VideoWriter_fourcc(*'DIVX'),1,(width,height))

for i in range(count-1,0,-1):
    frame=cv2.imread(images[i])
    video.write(frame)
video.release()

cv2.destroyAllWindows()