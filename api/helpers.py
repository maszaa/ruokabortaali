def checkUrl(url):
    urlPrefix = url
    urlSuffix = ""
    if "?format=json" in url:
        urlPrefix = self.split("?")[0]
        urlSuffix = "?format=json"
    return urlPrefix, urlSuffix
