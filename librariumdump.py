import os
import argparse
import urllib.request
import selenium.webdriver
import selenium.webdriver.support.ui 
import selenium.webdriver.support.expected_conditions

parser = argparse.ArgumentParser()
parser.add_argument('--output-directory', '-o', default = 'librariumdump')
parser.add_argument('--input-path', '-i', default = 'librariumdump.txt')
parser.add_argument('--chromedriver', default = '/usr/bin/chromedriver')
parser.add_argument('--timeout', type = float, default = 60.0)
args = parser.parse_args()

chrome_service = selenium.webdriver.chrome.service.Service(executable_path = args.chromedriver)
driver = selenium.webdriver.Chrome(service = chrome_service)
wait = selenium.webdriver.support.ui.WebDriverWait(driver, args.timeout)

magazine_urls = list(map(str.strip, filter(bool, open(args.input_path))))
first_magazine_url = magazine_urls[0]

sanitize_url = lambda url: url.replace(':', '_').replace('/', '_')

driver.get(os.path.dirname(first_magazine_url))

k = 0
while k < len(magazine_urls):
    magazine_url = magazine_urls[k]
    print(magazine_url)
    
    try:
        if magazine_url != first_magazine_url:
            driver.get(magazine_url)
        wait.until(selenium.webdriver.support.expected_conditions.url_to_be(magazine_url))

        page_urls = [link.get_attribute('href') for link in driver.find_elements('link text', '') if magazine_url in link.get_attribute('href')]

        for i, page_url in enumerate(page_urls):
            print(page_url)
            driver.get(page_url)
            wait.until(selenium.webdriver.support.expected_conditions.url_to_be(page_url))
            
            img_url, = [link.value_of_css_property('background-image').lstrip('url("').rstrip('")') for link in driver.find_elements('link text', '') if magazine_url in link.get_attribute('href')]
            print(img_url)

            dirname = os.path.join(args.output_directory, sanitize_url(magazine_url))
            basename = str(i).zfill(2) + '_' + sanitize_url(page_url) + '_' + sanitize_url(img_url)
            
            os.makedirs(dirname, exist_ok=True)
            with open(os.path.join(dirname, basename), 'wb') as f:
                f.write(urllib.request.urlopen(img_url).read())

        k += 1
    except Exception as e:
        print(e)
        k += 0

driver.quit()
