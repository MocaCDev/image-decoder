#import backend
from BillOfSales import BOSID, BOS

class ImageDecoder:

    #
    #   IW - ImageWorker
    #
    def __init__(self, IW = None):
        
        self.IW = IW

        # BOSID - Found in `BillOfSales/__init__.py`
        self.BOS = BOSID

        if self.IW == None:
            print('ImageWorker can not be `None`')
            sys.exit(1)
        
        self.BOS_decoder = BOS.BOS_decoder(self.IW, self.BOS)
        self.BOS_decoder.decode_BOS()