import feedparser
import facebook


def get_api(cfg):
    graph = facebook.GraphAPI(cfg['access_token'])
    resp = graph.get_object('me/accounts')
    page_access_token = None
    for page in resp['data']:
        if page['id'] == cfg['page_id']:
            page_access_token = page['access_token']
            graph = facebook.GraphAPI(page_access_token)
    return graph


def posts(graph, name, link):
    attachment = {
        'name': name,
        'link': link
    }

    status = graph.put_wall_post(name, attachment)

if __name__ == '__main__':
    cfg = {
        'page_id': "1928743740690198",
        'access_token': "EAACplwjxa28BABqCi1j4CRPxxsSAJBqruPXRoaEFzMhrkaDC0j9r8v44F4uBwun5f8hYaH2WF6lgepCFFmtfPhmn7q4ZAqnFgujqLJdpuLDIRFFQZCz7aJgnCEHnZC7kuPN4hD62jyEwZCFF4TSJz4OpZBgXXyJsZD"
    }

    graph = get_api(cfg)

    posts(graph, "This is Google", "http://google.com/")
