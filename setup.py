from setuptools import setup, find_packages

setup(
    name='insta_tik_downloader',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'instaloader',
        'TikTokApi',
        'python-telegram-bot',
    ],
    description='Library to download Instagram and TikTok videos without watermark.',
    author='Your Name',
    author_email='your_email@example.com',
    url='https://github.com/yourusername/insta_tik_downloader',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
