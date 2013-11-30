SiteMapSerpent
--------------

### Installation

Sitemapserpent can be installed with pip.

`pip install sitemapserpent`

### Generate a Sitemap

#### Non-image Sitemap

If your Sitemap contains one or more images, you need to use an image Sitemap.

If not, simply pass in an array of urls.

```python
site = SiteMap()

locations = ['www.example.com', 'www.example.org', 'www.example.net']

for loc in locations:
    site.index(
        loc=loc,
        lastmod=datetime.now(),
        changefreq='never',
        priority=0.5
    )

```


#### Image Sitemap

Tell the Sitemap generator if your Sitemap will contain images:

```python
site = SiteMap(image=True)
```

Pass in a dictionary of urls that contains a list of images: 


```python
data = {
    "www.example.com": [
        {
            "loc": "www.example.com/IMAGE",
            "caption": "Image about kittens",
            "geo_location": "London, England",
            "title": "Kitten Image",
            "License": "Example License"
        },
        {
            "loc": "www.example.com/IMAGE2",
            "caption": "Second Image about kittens",
            "geo_location": "London, England",
            "title": "Kitten Image",
            "License": "Example License"
        }
    ]
}
```

Finally, iterate through the <b>keys</b> of your dictionary to generate the Sitemap

```python

for loc in data.keys():
    site.index(
        loc=loc,
        lastmod=datetime.now(),
        changefreq='never',
        priority=0.5,
        images=data[loc]
    )

```

### Output

To output your sitemap:

```python
print site.output()
```

To pretty print your Sitemap:

```python
print site.output(pretty=True)
```

Pretty printing defaults to false


### More information

Priority is automatically set to 0.5 if a priority value is not given.

Check out test.py to functioning code for the program.
