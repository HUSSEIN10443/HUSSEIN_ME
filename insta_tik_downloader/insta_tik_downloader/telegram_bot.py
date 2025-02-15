from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from insta_tik_downloader.instagram_downloader import download_instagram_video
from insta_tik_downloader.tiktok_downloader import download_tiktok_video

def start(update: Update, context: CallbackContext):
    update.message.reply_text('Hello, I can download videos from Instagram and TikTok.')

def download_instagram(update: Update, context: CallbackContext):
    post_url = context.args[0]
    save_path = "instagram_video.mp4"
    download_instagram_video(post_url, save_path)
    update.message.reply_text(f'Video from Instagram downloaded to {save_path}')

def download_tiktok(update: Update, context: CallbackContext):
    post_url = context.args[0]
    save_path = "tiktok_video.mp4"
    download_tiktok_video(post_url, save_path)
    update.message.reply_text(f'Video from TikTok downloaded to {save_path}')

def main():
    updater = Updater("YOUR_BOT_TOKEN", use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("download_instagram", download_instagram))
    dp.add_handler(CommandHandler("download_tiktok", download_tiktok))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
