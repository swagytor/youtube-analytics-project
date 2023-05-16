import os

from pprint import pprint
from dotenv import load_dotenv, find_dotenv
from googleapiclient.discovery import build

load_dotenv(find_dotenv())
YT_API_KEY = os.getenv('YT_API_KEY')
youtube = build('youtube', 'v3', developerKey=YT_API_KEY)


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        channel = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        pprint(channel, sort_dicts=False)
