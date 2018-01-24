import webbrowser
class Got():
    def __init__(self,title,pic,video):
        self.title=title
        self.poster_image_url=pic
        self.trailer_youtube_url=video
    def show_vid(self):
        webbrowser.open(self.trailer_youtube_url)
        
