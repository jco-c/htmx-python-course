from typing import Optional

from models.video_model import Video
from viewmodels.shared.viewmodelbase import ViewModelBase


class AddVideoViewModel(ViewModelBase):
    def __init__(self, cat_name: str):
        super().__init__()
        self.cat_name = cat_name
        self.id: str | None = None
        self.title: str | None = None
        self.author: str | None = None
        self.view_count: int | None = None

    def restore_from_form(self):
        d = self.request_dict
        self.id = d.get("id")
        self.title = d.get("title")
        self.author = d.get("author")
        self.view_count = int(d.get("view_count", 0))
