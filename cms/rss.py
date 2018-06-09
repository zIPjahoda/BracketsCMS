from django.contrib.syndication.views import Feed
from .models import Article

class LatestPosts(Feed):
    title = "Random web"
    link = "/sitenews/"
    description = "Random  description"

    def items(self):
        return Article.objects.all()

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.description

    def item_link(self, item):
        return item.url


