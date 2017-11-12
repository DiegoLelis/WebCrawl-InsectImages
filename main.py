'''This will download images from the website: https://www.insectimages.org/ and save into a folder inside the images folder'''

from read_site import Site
from save_images import save_images
from specie import Specie

# This number specify what is the minimum number of images necessary, then the software will paginate the website ultil it reaches the min number.
NUM_MIN = 140

cockroaches = Specie('https://www.insectimages.org/browse/taxthumb.cfm?order=369', 'cockroaches')
orthoptera = Specie('https://www.insectimages.org/browse/taxthumb.cfm?order=159', 'orthoptera')
neuroptera = Specie('https://www.insectimages.org/browse/taxthumb.cfm?order=152', 'neuroptera')
mantodea = Specie('https://www.insectimages.org/browse/taxthumb.cfm?order=139', 'mantodea')
isoptera = Specie('https://www.insectimages.org/browse/taxthumb.cfm?order=121', 'isoptera')
odonata = Specie('https://www.insectimages.org/browse/taxthumb.cfm?order=155', 'odonata')

lst_specie = [cockroaches,orthoptera,neuroptera,mantodea,isoptera,odonata]

def down_lst_img(specie, num_min = NUM_MIN):
    site = Site(specie.url, num_min)
    site.browser.quit()
    save_images(site.lst_img_path, specie.folder)

if __name__ == "__main__":
    for specie in lst_specie:
        down_lst_img(specie)


