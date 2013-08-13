from lxml import etree


PRIORITIES = ['always', 'hourly', 'daily', 'weekly', 'monthly', 'yearly', 'never']

class SMSerpent(object):
    def __init__(self, root=None, image=False):
        if root is not None:
            self.root = root
        else:
            if image is True:
                self.root = etree.Element('urlset', xmlns='http://www.sitemaps.org/schemas/sitemap/0.9', nsmap={'image': 'http://www.google.com/schemas/sitemap-image/1.1'})
                self.image = True
            else:
                self.root = etree.Element('urlset', xmlns='http://www.sitemaps.org/schemas/sitemap/0.9')

    def index(self, loc, lastmod=None, changefreq=None, priority=None, images=None):
        if len(loc) >= 2048:
            print "This link contains too many characters:\n" + loc
            return
        url_branch = etree.SubElement(self.root, 'url')
        etree.SubElement(url_branch, 'loc').text = loc

        if lastmod is not None:
            iso_date = lastmod.replace(microsecond=0).isoformat('T')
            etree.SubElement(url_branch, 'lastmod').text = iso_date

        if changefreq in PRIORITIES:
            etree.SubElement(url_branch, 'changefreq').text = changefreq

        if 0.0 <= priority and priority <= 1.0:
            etree.SubElement(url_branch, 'priority').text = str(priority)
        elif priority is None:
            etree.SubElement(url_branch, 'priority').text = '0.5'
        else:
            print "Priority is out of range"

        if images is None:
            return self.root

        for image in images:
            self.index_image(url_branch, image)

        return self.root        

    def index_image(self, url_branch, images):
        loc = images['loc']  # required
        caption = images.get('caption')  # optional
        geo_location = images.get('geo_location')  # optional
        title = images.get('title')  # optional
        license = images.get('license')  # optional

        prefix = '{http://www.google.com/schemas/sitemap-image/1.1}'

        image_branch = etree.SubElement(url_branch, prefix + 'image')
        etree.SubElement(image_branch, prefix + 'loc').text = loc
        
        if caption is not None:
            etree.SubElement(image_branch, prefix + 'caption').text = caption

        if geo_location is not None:
            etree.SubElement(image_branch, prefix + 'geo_location').text = geo_location

        if title is not None:
            etree.SubElement(image_branch, prefix + 'title').text = title

        if license is not None:
            etree.SubElement(image_branch, prefix + 'license').text = license

    def output(self, pretty=False):
        return etree.tostring(self.root, pretty_print=pretty, xml_declaration=True, encoding='UTF-8')
