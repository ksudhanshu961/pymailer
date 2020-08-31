try:
    import httplib
except:
    import http.client as httplib

def checkInternetHttplib(url="www.google.com", timeout=3):
    conn = httplib.HTTPConnection(url, timeout=timeout)
    try:
        conn.request("HEAD", "/")
        conn.close()
        return True
    except Exception as e:
        return False

r = checkInternetHttplib()
print(r)