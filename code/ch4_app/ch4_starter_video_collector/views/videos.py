import flask

from infrastructure.view_modifiers import response
from viewmodels.videos.category_viewmodel import CategoryViewModel
from viewmodels.videos.play_viewmodel import PlayViewModel
from viewmodels.videos.add_video_viemodel import AddVideoViewModel
from viewmodels.videos.search_viemodel import SearchViewModel
from services.video_service import add_video

blueprint = flask.Blueprint("videos", __name__, template_folder="templates")


@blueprint.get("/videos/category/<cat_name>")
@response(template_file="videos/category.html")
def category(cat_name: str):
    vm = CategoryViewModel(cat_name)
    return vm.to_dict()


@blueprint.get("/videos/play/<video_id>")
@response(template_file="videos/play.html")
def play(video_id: str):
    vm = PlayViewModel(video_id)
    return vm.to_dict()


@blueprint.get("/videos/add/<cat_name>")
@response(template_file="/videos/partials/add_video_form.html")
def add_get(cat_name: str):
    vm = AddVideoViewModel(cat_name)
    return vm.to_dict()


@blueprint.get("/videos/add_button/<cat_name>")
@response(template_file="/videos/partials/add_video_button.html")
def add_button_get(cat_name: str):
    vm = CategoryViewModel(cat_name)
    return vm.to_dict()


@blueprint.post("/videos/add/<cat_name>")
def add_post(cat_name: str):
    vm = AddVideoViewModel(cat_name)
    vm.restore_from_form()

    add_video(
        youtube_id=vm.id,
        title=vm.title,
        author=vm.author,
        view_count=vm.view_count,
        cat_name=cat_name,
    )

    return flask.redirect(f"/videos/category/{cat_name}")


@blueprint.get("/videos/search/")
@response(template_file="/videos/search.html")
def search():
    vm = SearchViewModel()
    if vm.is_htmx_request:
        return flask.make_response(f"There are {len(vm.videos)} videos.")
    return vm.to_dict()
