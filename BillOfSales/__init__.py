BOS_image_data = {
    'BOS State': None,
    'Date Of Sale': None,
    'Seller Name': None,
    'Payment Ammount': 0.00,
    'Buyer Name': None,
    'Vehicle Information': {
        'Year': None,
        'Make': None,
        'Model': None,
        'VIN': None,
    },
    'Transferor Information': {
        'Full Name': None,
        'Address': None,
        'City State Zip': None,
        'Phone Number': None,
    },
    'Transferee Information': {
        'Full Name': None,
        'Address': None,
        'City State Zip': None,
        'Phone Number': None,
    },
    'Sworn Day': [None, None],
    'Sworn Month': [None, None]
}

name = 'hey'

class BOSID:
    
    def not_None(value):
        if value == None:
            print('`None` value found')
            sys.exit(1)

    def set_bos_state(state: str):
        BOS_image_data['BOS State'] = state
    
    def set_date_of_sale(DOS: str):
        BOS_image_data['Date Of Sale'] = DOS