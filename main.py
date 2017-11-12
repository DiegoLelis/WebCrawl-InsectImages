'''This will download images from the website: https://www.insectimages.org/ and save into a folder inside the images folder'''

from read_site import Site
from save_images import save_images

# This number specify what is the minimum number of images necessary, then the software will paginate the website ultil it reaches the min number.
NUM_MIN = 5

#This specifies what is the url to search for images (It will discard images from the website that are not relevant)
# URL = 'https://www.insectimages.org/browse/taxthumb.cfm?order=369' #cockroaches
URL = 'https://www.insectimages.org/browse/taxthumb.cfm?order=159' #Orthoptera

#This specifies the folder in wich the mages should be saved according to the species
# FOLDER = 'cockroaches'
FOLDER = 'orthoptera'

if __name__ == "__main__":
    site = Site(URL, NUM_MIN)
    save_images(site.lst_img_path, FOLDER)
    site.browser.quit()
