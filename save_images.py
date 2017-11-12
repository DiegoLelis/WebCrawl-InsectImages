'''This code will save a list of images from web into a folder'''
import urllib.request
from read_site import Site
import os.path
root = 'images'


def save_images(img_lst, folder):
    for img_name in img_lst:
        print('Fetching: {}'.format(img_name)
        size_img_name = img_name[-1:0:-1].find('/')
        name = img_name[len(img_name)-size_img_name:]
        directory = '{}/{}'.format(root,folder)
        if not os.path.exists(directory):
            os.makedirs(directory)
            print('Creating Directory: {}'.format(directory))
        name_path = '{}/{}'.format(directory,name)
        if not os.path.isfile(name_path):
            with open(name_path, 'wb') as img_file:
                img_file.write(urllib.request.urlopen(img_name).read())
                print('Creating File: {}'.format(name_path))


if __name__ == '__main__':
    site = Site('https://www.insectimages.org/browse/taxthumb.cfm?order=369', 1)
    save_images(site.lst_img_path, 'cockroaches')