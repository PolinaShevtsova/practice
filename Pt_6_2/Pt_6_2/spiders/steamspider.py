import scrapy


class SteamspiderSpider(scrapy.Spider):
    name = "steamspider"
    allowed_domains = ["store.steampowered.com"]
    url = "https://store.steampowered.com/search/?category1=998&filter=topsellers&ndl=1&page=%s"
    page = 1
    start_urls = [url % page]
    games_count = 0

    def parse(self, response, **kwargs):
        games = response.css("a.search_result_row.ds_collapse_flag")

        for game in games:
            yield response.follow(game, callback=self.parse_tags, cookies={"birthtime": 880909201})

        if self.games_count < 1000:
            self.page += 1
            yield response.follow(self.url % self.page, callback=self.parse)

    def parse_tags(self, response):
        if self.games_count < 1000:
            yield {
                'Name': response.css("div.apphub_AppName::text").get(),
                'url': response.url,
                'tags': [tag.css("a::text").get().strip() for tag in response.css("a.app_tag")]
            }
        else:
            return
        self.games_count += 1
