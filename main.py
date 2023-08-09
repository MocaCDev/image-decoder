from ImgTextGrabber import image_decoder, image_splitter
import sys

if __name__ == '__main__':

    @lambda _: _()
    def main():
        IW = image_splitter.ImageWorker('BillOfSales/download.jpg', 'BOS')
        ID = image_decoder.ImageDecoder(IW = IW)
        #IW.split_image()
        #IW.write_split_image(to_files = ['BillOfSales/f2.jpg', 'BillOfSales/f3.jpg'])
        #IW.merge_images_back_together()

        return 0
    
    if main == 0: sys.exit(main)
    
    sys.exit(1)