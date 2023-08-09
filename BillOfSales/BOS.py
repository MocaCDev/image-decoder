import cv2
from pytesseract import pytesseract
from PIL import Image
import sys

class BOS_decoder:

    def __init__(self, IW = None, BOSID = None) -> None:
        
        self.IW = IW
        self.BOS = BOSID

    def decode_BOS(self) -> None:
        
        self.IW.split_image()
        self.IW.write_split_image(to_files = [f'{self.IW.get_directory()}/img1.{self.IW.get_image_format()}', f'{self.IW.get_directory()}/img2.{self.IW.get_image_format()}'])
        self.IW.merge_images_back_together()
