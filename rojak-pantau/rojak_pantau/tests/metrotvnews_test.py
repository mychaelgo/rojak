from unittest.case import TestCase
from rojak_pantau.spiders.metrotvnews import MetrotvnewsSpider
from util.mock_response import mock_response

class MetrotvnewsTest(TestCase):
    def setUp(self):
        self.spider = MetrotvnewsSpider()

    def _test_item_results(self, results, expected_length):
        count = 0
        for item in results:
            self.assertIsNotNone(item['title'])
            count += 1
        self.assertEqual(count, expected_length)

    def test_parse(self):
        results = self.spider.parse(mock_response('../data/metrotvnews_sample1.html',
            'http://www.metrotvnews.com/more/topic/8602/0'))
        self._test_item_results(results, 20)
