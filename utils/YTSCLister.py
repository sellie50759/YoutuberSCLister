from utils.APIInformationExtractor import extract
from utils.SuperChat import SuperChat
import time


class YtScLister:

    def __init__(self, youtube_client) -> None:
        self._youtube_client = youtube_client

    # get all sc in 30days
    def getAllSc(self) -> list[SuperChat]:
        page_token = ''
        final_sc_list = []
        number_of_result = 1

        while number_of_result != 0:
            sc_list, page_token, number_of_result = self.getScRecord(page_token)
            print(f"fetch {number_of_result} data")
            time.sleep(0.1)

            final_sc_list.extend(sc_list)

        return final_sc_list

    # get one api record
    def getScRecord(self, page_token) -> tuple[list[SuperChat], str, int]:
        request = self._youtube_client.superChatEvents().list(
            maxResults=50,
            pageToken=page_token,
            part="snippet"
        )

        resp_json = request.execute()

        return extract(resp_json)
