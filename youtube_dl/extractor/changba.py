# coding: utf-8
from __future__ import unicode_literals

from .common import InfoExtractor


class ChangbaIE(InfoExtractor):
    _VALID_URL = r'https?://(?:www\.)?changba\.com/s/(?P<id>[0-9A-Za-z-_])'
    #_VALID_URL = r'https://changba.com/s/0GHVw6vyXv9N2FhaFi2WJg'
    _TEST = {
        'url': 'https://changba.com/s/0GHVw6vyXv9N2FhaFi2WJg',
        'md5': 'TODO: md5 sum of the first 10241 bytes of the video file (use --test)',
        'info_dict': {
            'id': '42',
            'ext': 'mp4',
            'title': 'Video title goes here',
            'thumbnail': r're:^https?://.*\.jpg$',
            # TODO more properties, either as:
            # * A value
            # * MD5 checksum; start the string with md5:
            # * A regular expression; start the string with re:
            # * Any Python type (for example int or float)
        }
    }

    def _real_extract(self, url):
        mobj = re.match(self._VALID_URL, url)
        print mobj
        video_id = self._match_id(url)
        print "video_id: " + video_id
        webpage = self._download_webpage(url, video_id)
        # print "webpage: " + webpage

        # TODO more code goes here, for example ...
        # title = self._html_search_regex(r'<h1>(.+?)</h1>', webpage, 'title')
        url = self._html_search_regex(r'<video>(.+?)</video>', webpage, 'url')
        print "url: " + url

        return {
            'id': video_id,
            'title': title,
            'description': self._og_search_description(webpage),
            'uploader': self._search_regex(r'<div[^>]+id="uploader"[^>]*>([^<]+)<', webpage, 'uploader', fatal=False),
            # TODO more properties (see youtube_dl/extractor/common.py)
        }

        return {
            'id': 'fake_id',
            'title': 'fake_title',
            'url': 'https://changba.com/s/0GHVw6vyXv9N2FhaFi2WJg',
        }
