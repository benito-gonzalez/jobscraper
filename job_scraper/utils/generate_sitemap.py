import os
from bs4 import BeautifulSoup
from job_scraper.utils import request_support
from lxml import etree

if os.path.isfile(os.path.dirname(os.path.dirname(__file__)) + '/../webapp/.is_development'):
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webapp.settings.development')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webapp.settings.production')

my_path = os.path.abspath(os.path.dirname(__file__))


def main():
    server_name = 'https://www.jobsportal.fi'
    urls = ['/locations', '/companies', '/tags']
    generated_urls = set()

    for url in urls:
        generated_urls.add(url)
        html = request_support.simple_get(server_name + url)
        soup = BeautifulSoup(html, 'lxml')

        for link in soup.find_all('a'):
            if link.get('href').startswith('/jobs-in'):
                generated_urls.add(link.get('href'))
                location_html = request_support.simple_get(server_name + link.get('href'))
                location_soup = BeautifulSoup(location_html, 'lxml')
                for location_link in location_soup.find_all('a'):
                    if location_link.get('href').startswith('/tags-in-'):
                        tag_html = request_support.simple_get(server_name + link.get('href'))
                        tag_soup = BeautifulSoup(tag_html, 'lxml')
                        container = tag_soup.find('div', class_='main-div')
                        if container:
                            for tag_link in container.find_all('a'):
                                if '-jobs-in-' in tag_link.get('href'):
                                    generated_urls.add(tag_link.get('href'))

            if link.get('href').startswith('/jobs-at'):
                generated_urls.add(link.get('href'))
            if link.get('href').endswith('-jobs'):
                generated_urls.add(link.get('href'))

    root = etree.Element("urlset", xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")

    for generated_url in generated_urls:
        url = generated_url.replace(' ', '%20')
        url_tag = etree.SubElement(root, "url")
        loc_tag = etree.SubElement(url_tag, "loc")
        loc_tag.text = server_name + url
        changefreq_tag = etree.SubElement(url_tag, "changefreq")

        priority_tag = etree.SubElement(url_tag, "priority")
        if url.startswith("jobs-in"):
            priority_tag.text = "0.80"
            changefreq_tag.text = "daily"
        elif url.endswith("-jobs"):
            priority_tag.text = "0.80"
            changefreq_tag.text = "daily"
        elif url.startswith("jobs-at"):
            priority_tag.text = "0.60"
            changefreq_tag.text = "weekly"
        elif "-jobs-in-" in url:
            priority_tag.text = "0.70"
        else:
            priority_tag.text = "0.90"
            changefreq_tag.text = "daily"

    with open('sitemap_generated.xml', 'wb') as f:
        f.write(etree.tostring(root, encoding='UTF-8', pretty_print=True))


if __name__ == "__main__":
    # execute only if run as a script
    main()
