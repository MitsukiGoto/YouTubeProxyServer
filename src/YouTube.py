import json

class YouTube:

    def __init__(self, response:str):
        self.jsonObj = json.loads(response)
        results = self.jsonObj["items"]
        for item in results[:]:
            if "channelId" in item["id"]:
                results.remove(item)
            if "playlistId" in item["id"]:
                results.remove(item)


    def get_id_and_thumbnail(self):
        list = []
        for item in self.jsonObj["items"]:
            list.append({"id":item["id"]["videoId"],"thumb":item["snippet"]["thumbnails"]["default"]["url"],"title":item["snippet"]["title"]})
        return list

    def get_Thumbnail(self):
        thumbnail_urls = []
        for item in self.jsonObj["items"]:
            thumbnail_urls.append(item["snippet"]["thumbnails"]["high"]["url"])
        return thumbnail_urls

    def get_ids(self):
        video_ids = []
        for item in self.jsonObj["items"]:
            video_ids.append(item["id"]["videoId"])
        return video_ids

