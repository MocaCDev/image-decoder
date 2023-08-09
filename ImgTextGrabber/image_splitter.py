import backend
import cv2
import os
import numpy

class ImageWorker:

    def __init__(self, image_path, image_type = None) -> None:
        self.image_path = image_path
        self.image_format = None
        self.image_directory = None
        self.image = None
        self.image_heigth = 0
        self.image_width = 0
        self.image_type = image_type
        self.image_split = []

        if not self.image_type == None:
            is_valid = False

            for i in backend.image_types:
                if self.image_type in i:
                    is_valid = True
                    break
            
            if not is_valid:
                print(f'{self.image_type} is not a valid type.')
                sys.exit(1)
        
        for i in range(len(self.image_path)):
            if self.image_path[i] == '/':
                self.image_directory = self.image_path[:i]
            
            if self.image_path[i] == '.':
                i += 1
                self.image_format = self.image_path[i:]
        
        if self.image_format not in backend.image_formats:
            print(f'The image format {self.image_format} is not supported')
            sys.exit(1)
        
    
    #
    # split_mode - 'height' cuts the picture in half height wise
    #              'width' cuts the picture in half width wise
    #
    def split_image(self, split_mode = 'height') -> None:

        self.image = cv2.imread(self.image_path)
        self.image_heigth = self.image.shape[0]
        self.image_width = self.image.shape[1]

        height_cutoff = self.image_heigth // 2
        width_cutoff = self.image_width // 2

        if split_mode == 'height':
            self.image_split.append(self.image[:height_cutoff, :])
            self.image_split.append(self.image[height_cutoff:, :])
        else:
            self.image_slit.append(self.image[:, :width_cutoff])
            self.image_slit.append(self.image[:, width_cutoff:])
        
        os.system(f'rm -rf {self.image_path}')
    
    def write_split_image(self, to_files: list) -> None:
        if to_files == None or to_files == [] or len(to_files) != 2:
            print('File the split image is being written to cannot be specified as `None` to `write_split_image`')
            sys.exit(1)

        cv2.imwrite(to_files[0], self.image_split[0])
        cv2.imwrite(to_files[1], self.image_split[1])

    def merge_images_back_together(self) -> None:
        
        self.image = cv2.vconcat(self.image_split)
        cv2.imwrite(self.image_path, self.image)
    
    #
    #   Getters
    #
    def get_image(self) -> numpy.ndarray: return self.image
    def get_image_split(self) -> list[numpy.ndarray, numpy.ndarray]: return self.image_split
    def get_image_height(self) -> int or float: return self.image_heigth
    def get_image_width(self) -> int or float: return self.image_width
    def get_image_type(self) -> str: return self.image_type
    def get_image_format(self) -> str: return self.image_format
    def get_directory(self) -> str: return self.image_directory