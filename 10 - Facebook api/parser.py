import pprint
import feedparser
from facebookapi import posts, get_api

pp = pprint.PrettyPrinter(indent=4)

url = "https://www.google.co.in/alerts/feeds/00744545946518415237/6843756865603829686"

parser = feedparser.parse(url)

# print(type(parser))

# print(parser)

cfg = {
    'page_id': "1928743740690198",
    'access_token': "EAACplwjxa28BABqCi1j4CRPxxsSAJBqruPXRoaEFzMhrkaDC0j9r8v44F4uBwun5f8hYaH2WF6lgepCFFmtfPhmn7q4ZAqnFgujqLJdpuLDIRFFQZCz7aJgnCEHnZC7kuPN4hD62jyEwZCFF4TSJz4OpZBgXXyJsZD"
}

graph = get_api(cfg)

for post in parser.entries:
    posts(graph, post.title, post.link.split('url=')[1])
    break
