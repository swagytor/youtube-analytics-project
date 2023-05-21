import json
import os

from src.utils import find_value
from pprint import pprint
from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""
    service_name: str = 'youtube'
    service_version: str = 'v3'
    yt_api_key: str = os.getenv('YT_API_KEY')
    service = build(service_name, service_version, developerKey=yt_api_key)

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id: str = channel_id
        self.__channel_name = None
        self.__channel_description = None
        self.__channel_url = None
        self.__channel_subscribers_count = None
        self.__channel_video_count = None
        self.__channel_summary_views = None

        self.channel = Channel.service.channels().list(id=self.__channel_id, part='snippet,statistics').execute()

        self.set_info()

    def set_info(self):
        self.__channel_name: str = find_value(self.channel, 'title')
        self.__channel_description: str = find_value(self.channel, 'description')
        self.__channel_url: str = f"https://www.youtube.com/channel/{find_value(self.channel, 'id')}"
        self.__channel_subscribers_count: str | int = find_value(self.channel, 'subscriberCount')
        self.__channel_video_count: str | int = find_value(self.channel, 'videoCount')
        self.__channel_summary_views: str | int = find_value(self.channel, 'viewCount')

    @property
    def channel_id(self) -> str:
        return self.__channel_id

    @property
    def channel_name(self) -> str:
        return self.__channel_name

    @channel_name.setter
    def channel_name(self, channel_name: str):
        self.__channel_name = channel_name

    @property
    def channel_description(self) -> str:
        return self.__channel_description

    @channel_description.setter
    def channel_description(self, channel_description: str):
        self.__channel_description = channel_description

    @property
    def channel_url(self) -> str:
        return self.__channel_url

    @channel_url.setter
    def channel_url(self, channel_url: str):
        self.__channel_url = channel_url

    @property
    def channel_subscribers_count(self) -> str | int:
        return self.__channel_subscribers_count

    @channel_subscribers_count.setter
    def channel_subscribers_count(self, channel_subscribers_count: str | int):
        self.__channel_subscribers_count = channel_subscribers_count

    @property
    def channel_video_count(self) -> str | int:
        return self.__channel_video_count

    @channel_video_count.setter
    def channel_video_count(self, channel_video_count: str | int):
        self.channel_video_count = channel_video_count

    @property
    def channel_summary_views(self) -> str | int:
        return self.__channel_summary_views

    @channel_summary_views.setter
    def channel_summary_views(self, channel_summary_views: str | int):
        self.__channel_summary_views = channel_summary_views

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        pprint(self.channel, sort_dicts=False)

    @classmethod
    def get_service(cls):
        return cls.service

    def to_json(self, file_name: str) -> None:
        channel_data = {"channel_id": self.__channel_id,
                        "channel_name": self.__channel_name,
                        "channel_description": self.__channel_description,
                        "channel_url": self.__channel_url,
                        "subscribers_count": self.__channel_subscribers_count,
                        "video_count": self.__channel_video_count,
                        "summary_views": self.__channel_summary_views
                        }

        with open(file_name, "w", encoding="utf-8") as json_file:
            json.dump(channel_data, json_file, indent=2, ensure_ascii=False)
