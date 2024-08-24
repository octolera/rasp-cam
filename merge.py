import cv2
import numpy as np

def stack_images(image_paths, output_path):
    """
    Объединяет несколько снимков в один для улучшения качества.
    
    Args:
        image_paths (list): Список путей к исходным изображениям.
        output_path (str): Путь для сохранения результирующего изображения.
    """
    # Загрузка и преобразование изображений в numpy-массивы
    images = [cv2.imread(path, cv2.IMREAD_GRAYSCALE) for path in image_paths]
    
    # Вычисление среднего значения пикселей
    avg_image = np.mean(images, axis=0).astype(np.uint8)
    
    # Сохранение результирующего изображения
    cv2.imwrite(output_path, avg_image)

# Пример использования
image_paths = ['image1.jpg', 'image2.jpg', 'image3.jpg']
output_path = 'stacked_image.jpg'
stack_images(image_paths, output_path)
