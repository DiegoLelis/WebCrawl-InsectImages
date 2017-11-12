'''This code will read pages from the site:
https://www.insectimages.org/ and try to provide an array of images addresses.
Obs: It willpaginate the site in order to read all images'''

#For test: https://www.insectimages.org/browse/taxthumb.cfm?order=369

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

class Page(object):
    def __init__(self, url):
        self.url = url

class Site(object):
    def __init__(self, url, numb_min):
        self.url = url
        self.num_min = numb_min
        self.browser = webdriver.Chrome()
        self.browser.get(self.url)
        self.images_path = []
        self.get_necessary_images(self.num_min)

    def get_next_page(self):
        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)

    def get_images_path(self):
        self.images_path = []
        images = self.browser.find_elements_by_tag_name('img')
        for image in images:
            aux_path = str(image.get_attribute('src'))
            if aux_path.find('/images/') != -1:
                self.images_path.append(aux_path)

    def count_images(self):
        return len(self.images_path)

    def get_necessary_images(self, num_min):
        while self.count_images() < num_min:
            self.get_next_page()
            self.get_images_path()
        return self.images_path






if __name__ == '__main__':
    site = Site('https://www.insectimages.org/browse/taxthumb.cfm?order=369', 140)
    i = 0
    for image_url in site.images_path:
        print('{}-{}'.format(i, image_url))
        i += 1

    site.browser.quit()

