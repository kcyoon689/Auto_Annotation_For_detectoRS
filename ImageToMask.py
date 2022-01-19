import os
from pathlib import Path

import cv2
# pip install opencv-python
import numpy as np

from tqdm import tqdm

print("Start Image2Mask")

category_names_list = ['desk', 'chair', 'drawer'] # Background > 237
threshold_list = [211, 254, 254]

for class_id, _ in enumerate(category_names_list): # class_id(step) = 0, 1, 2 (table, chair, drawer)

  imageDirPath = Path('../images/' + category_names_list[class_id]).absolute()
  # imageDirPath = "C:/Users/kcyou/Desktop/detectoRS/images/desk"
  imageNameList = os.listdir(imageDirPath)

  # print("imageDirPath: {}".format(imageDirPath))``
  # print("imageNameList: {}".format(imageNameList))
  print(imageDirPath)

  imagePathList = [os.path.join(imageDirPath,imageName) for imageName in imageNameList]
  # imagePathList = imagePathList[:10]

  for imagePath in tqdm(imagePathList):
    image = cv2.imread(imagePath, cv2.IMREAD_COLOR)
    # cv2.imshow("image", image)
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # cv2.imshow("image_gray", image_gray)
    # print(image_gray[344][252])
    # print(image_gray[252][344])

    # grayPath = imagePath.replace("images", "grays")
    # grayPath = grayPath.replace("png", "bmp")
    # cv2.imwrite(grayPath, image_gray)


    ret, mask = cv2.threshold(image_gray, threshold_list[class_id], 255, cv2.THRESH_BINARY_INV)
    # cv2.imshow("mask", mask)
    # cv2.waitKey(0)

    # mask_rgb = cv2.cvtColor(mask, cv2.COLOR_GRAY2RGB) # 255,255,255
    mask_classId = np.where(mask == 255, class_id+1, 0)

    maskPath = imagePath.replace("images", "masks")
    maskPath = maskPath.replace("png", "bmp")
    cv2.imwrite(maskPath, mask_classId)

