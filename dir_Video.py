def dir2video(folder='/home/dell/Pictures/*.png'):
    """converts all the images to Directories""" 
    import cv2
    import numpy as np
    import glob
    img_array = []
    for filename in glob.glob(folder):
        img = cv2.imread(filename)
        height, width, layers = img.shape
        size = (width,height)
        img_array.append(img)
    # print(len(img_array))
    
    out = cv2.VideoWriter('project.avi',cv2.VideoWriter_fourcc(*'DIVX'), 1, size) 
    for i in range(len(img_array)):
        out.write(img_array[i])
    out.release()
    print("Video Creation Complete!")
dir2video()