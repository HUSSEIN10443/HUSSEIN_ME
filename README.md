#HUSSEIN_ME

This is a Python library for downloading videos and images from Instagram and TikTok without watermarks. It also includes a Telegram bot to download and send media.

## Installation

To install the library, use the following:
```bash
pip install insta_tik_downloader

from insta_tik_downloader.instagram_downloader import download_instagram_video

download_instagram_video("https://www.instagram.com/p/XYZ", "path_to_save_video")
from insta_tik_downloader.tiktok_downloader import download_tiktok_video

download_tiktok_video("https://www.tiktok.com/@user/video/1234567890", "path_to_save_video")
/run your telegram bot and use the commands
### 4. **ملف `insta_tik_downloader/instagram_downloader.py`:**
```python
import instaloader

def download_instagram_video(post_url, save_path):
    L = instaloader.Instaloader()
    post = instaloader.Post.from_shortcode(L.context, post_url.split("/")[-2])
    L.download_post(post, target=save_path)
