import os
from scrapy.http import TextResponse, Request

def mock_response(file_name, url):
    """
    Create scrapy fake HTTP response from HTML file_name
    @param file_name: relative filename from resp.py directory
    @param url: URL for the response
    @return scrapy HTTP response that can be used for unittesting
    """
    request = Request(url=url)
    if not file_name[0] == '/':
        responses_dir = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(responses_dir, file_name)
    else:
        file_path = file_name

    file_content = open(file_path, 'r').read()

    response = TextResponse(url=url,
        request=request,
        body=file_content,
        encoding='utf-8')
    return response
