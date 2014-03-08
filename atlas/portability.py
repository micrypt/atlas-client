try:
    from urllib import urlopen
    from urllib import urlencode
except ImportError:
    from urllib.request import urlopen
    from urllib.parse import urlencode

def get_content_type(message):
    if hasattr(message, 'get_content_type'):
        return message.get_content_type()
    return message.type

def load_response(response):
    if hasattr(response, 'readall'):
        return response.readall().decode('utf-8')
    return response
