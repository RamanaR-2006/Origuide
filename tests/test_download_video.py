import unittest

from download_video import is_youtube_url


class IsYoutubeUrlTests(unittest.TestCase):
    def test_accepts_supported_youtube_hosts(self):
        urls = (
            "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
            "https://youtu.be/dQw4w9WgXcQ",
            "https://m.youtube.com/shorts/dQw4w9WgXcQ",
            "https://www.youtube-nocookie.com/embed/dQw4w9WgXcQ",
        )
        for url in urls:
            with self.subTest(url=url):
                self.assertTrue(is_youtube_url(url))

    def test_rejects_invalid_or_deceptive_urls(self):
        urls = (
            "not a url",
            "ftp://youtube.com/video",
            "https://youtube.com.example.com/watch?v=123",
            "https://example.com/?url=https://youtube.com/watch?v=123",
        )
        for url in urls:
            with self.subTest(url=url):
                self.assertFalse(is_youtube_url(url))


if __name__ == "__main__":
    unittest.main()
