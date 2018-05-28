import os

def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """
    with open("function/views/home.html") as f:
        return f.read().replace("URL", os.getenv("assets_url", "/function/assets"))

