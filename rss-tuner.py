# Import RSS feed, search first entry for "figure" and replace that with "img" and add width and height.
# Also add style to pre tag to make it scrollable. Then write the new feed to a file.

import feedparser
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup


# get feed
feed = feedparser.parse("https://ralfzosel.de/feed/")
# get first entry
entry = feed.entries[0]
# get content
content = entry.content[0].value

# replace all figure tags with img tags that contain the URL of the figure
soup = BeautifulSoup(content, "html.parser")
for figure in soup.find_all("figure"):
    # check if there are nested figures
    if figure.find("figure") is None:
        img = soup.new_tag("img", src=figure.img["src"], width="100%", height="auto")
        # replace figure with img
        figure.replace_with(img)

# remove figure tags but keep img tags within
for figure in soup.find_all("figure"):
    figure.unwrap()

# put a href around the img tag that links to the image file
for img in soup.find_all("img"):
    a = soup.new_tag("a", href=img["src"])
    img.wrap(a)

# add to pre tag style attribute to make it scrollable
for pre in soup.find_all("pre"):
    pre["style"] = "white-space: pre-wrap;"

# replace content of first feed entry with new content
feed.entries[0].content[0].value = str(soup)


rss = ET.Element("rss")
rss.set("version", "2.0")

# Create channel element
channel = ET.SubElement(rss, "channel")

# Set channel elements
ET.SubElement(channel, "title").text = feed.feed.title
ET.SubElement(channel, "link").text = feed.feed.link
ET.SubElement(channel, "description").text = feed.feed.description
ET.SubElement(channel, "language").text = feed.feed.language

# Set item elements
for entry in feed.entries:
    item = ET.SubElement(channel, "item")
    ET.SubElement(item, "title").text = entry.title
    ET.SubElement(item, "link").text = entry.link
    ET.SubElement(item, "description").text = entry.content[0].value
    ET.SubElement(item, "pubDate").text = entry.published
    ET.SubElement(item, "guid").text = entry.id

    # add the content to item
    # ET.SubElement(item, "content").text = entry.content[0].value


# Create ElementTree and write to file
tree = ET.ElementTree(rss)
tree.write("feed.rss")
