from models.video_model import Video
from viewmodels.shared.viewmodelbase import ViewModelBase
from services.video_service import search_videos


class SearchViewModel(ViewModelBase):
    def __init__(self):
        super().__init__()
        self.search_text: str = self.request_dict.get("search_text")
        self.videos: list[Video] = []

        if self.search_text and self.search_text.strip():
            self.videos = search_videos(self.search_text)
