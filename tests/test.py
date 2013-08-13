from sitemapserpent.sitemapserpent import SMSerpent
from datetime import datetime
import json


json_data = open('data.json').read()
data = json.loads(json_data)

site = SMSerpent(image=True)

for loc in data.keys():
    site.index(
        loc=loc,
        lastmod=datetime.now(),
        changefreq='never',
        priority=0.5,
        images=data[loc]
    )

more_sites = ['www.aaronhsmith.com', 'aaronhsmith.com']

for new_loc in more_sites:
    site.index(
        loc=new_loc,
        lastmod=datetime.now()
    )


print site.output(pretty=True)
