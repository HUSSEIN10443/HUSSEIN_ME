from TikTokApi import TikTokApi

def download_tiktok_video(post_url, save_path):
    api = TikTokApi.get_instance()
    video_data = api.get_video_by_url(post_url)
    with open(save_path, 'wb') as f:
        f.write(video_data)
