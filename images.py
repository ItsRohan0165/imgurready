import asyncio
import random
import configparser
import images
from imgurpython import ImgurClient


client_id = '68a43e97332a592'
client_secret = '8f795c78fe550eea8009cdfe4e06a388e2e66365'
client = ImgurClient(client_id, client_secret)

def topCommand():
    items = client.gallery()
    max_item = None
    max_views = 0
    for item in items:
        if item.views > max_views:
            max_item = item
            max_views = item.views
    return max_item

def imgCommand(tag):
    items = client.gallery_search(tag)
    if not items:
        return False
    else:
        resultimg = random.choice(items)
        return resultimg
