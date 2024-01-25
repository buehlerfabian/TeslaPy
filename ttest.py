import teslapy

import logging
# set up logging to file - see previous section for more details
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s'
                    ' %(levelname)-8s %(message)s',
                    filename='ttest.log')


tesla = teslapy.Tesla('buehler.fabian@gmx.de')
if not tesla.authorized:
    print('Use browser to login. Page Not Found will be shown at success.')
    print('Open this URL: ' + tesla.authorization_url())
    tesla.fetch_token(authorization_response=input(
        'Enter URL after authentication: '))
vehicles = tesla.vehicle_list()
print(vehicles[0])
tesla.close()
