# -*- coding: utf-8 -*-

# Sample Python code for youtube.superChatEvents.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/code-samples#python
import os
import openpyxl

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

from utils.YTSCLister import YtScLister


if __name__ == '__main__':
    scopes = ["https://www.googleapis.com/auth/youtube.readonly"]

    def main():
        # Disable OAuthlib's HTTPS verification when running locally.
        # *DO NOT* leave this option enabled in production.
        os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

        api_service_name = "youtube"
        api_version = "v3"
        client_secrets_file = "secret.json"

        # Get credentials and create an API client
        flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
            client_secrets_file, scopes)

        credentials = flow.run_console()

        youtube_client = googleapiclient.discovery.build(
            api_service_name, api_version, credentials=credentials)

        lister = YtScLister(youtube_client)
        sc_list = lister.getAllSc()

        # sort by createdTime
        sc_list.sort(key=lambda x: x.getTuple()[1])

        wb = openpyxl.Workbook()
        ws = wb.active

        for sc in sc_list:
            ws.append(sc.getTuple())

        wb.save('sc.xlsx')
    print("start")
    main()
    print("generate complete")




