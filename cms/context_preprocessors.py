import json
import os
from BracketsCMS.settings import BASE_DIR
from cms.models import MenuItem


def config_meta(request):
    result_dictionary = {}
    with open(os.path.join(BASE_DIR, 'cms/config/config.json')) as json_data:
        data = json.load(json_data)
        result_dictionary['site_title'] = data["site_config"]["title"]
        result_dictionary['site_description'] = data["site_config"]["description"]
        result_dictionary['site_keywords'] = data["site_config"]["keywords"]

    return result_dictionary


def navigation(request):
    return {"navigation_items": MenuItem.get_all_top_level()}


