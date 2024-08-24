import cv2

# Загрузка исходного изображения
oriImg = cv2.imread('input_image.jpg', cv2.IMREAD_GRAYSCALE)

# Применение гауссовского сглаживания
grayImg = cv2.GaussianBlur(oriImg, (3, 3), 0)

# Применение оператора Лапласа
laplaceImg = cv2.Laplacian(grayImg, cv2.CV_16S, ksize=3)

# Конвертация в 8-битное изображение
abs_laplaceImg = cv2.convertScaleAbs(laplaceImg)

# Объединение сглаженного изображения и результата Лапласа
dstImg = cv2.add(abs_laplaceImg, grayImg)

# Отображение результата
cv2.imshow('Output Image', dstImg)
cv2.waitKey(0)
cv2.destroyAllWindows()
