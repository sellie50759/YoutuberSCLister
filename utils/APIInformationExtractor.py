from utils.SuperChat import SuperChat


def extract(resp_json) -> tuple[list[SuperChat], str, int]:
    superchat_list = []

    '''
    resp_json format 
    source: https://developers.google.com/youtube/v3/live/docs/superChatEvents/list?hl=zh-tw
    {
      "kind": "youtube#superChatEventListResponse",
      "etag": etag,
      "nextPageToken": string,
      "pageInfo": {
        "totalResults": integer,
        "resultsPerPage": integer
      },
      "items": [
        superChatEvent resource
      ]
    }
    '''
    '''
    superChatEvent format
    source: https://developers.google.com/youtube/v3/live/docs/superChatEvents?hl=zh-tw#resource-representation
    {
      "kind": "youtube#superChatEvent",
      "etag": etag,
      "id": string,
      "snippet": {
        "channelId": string,
        "supporterDetails": {
          "channelId": string,
          "channelUrl": string,
          "displayName": string,
          "profileImageUrl": string
        },
        "commentText": string,
        "createdAt": datetime,
        "amountMicros": unsigned long,
        "currency": string,
        "displayString": string,
        "messageType": unsigned integer,
        "isSuperStickerEvent": boolean,
        "superStickerMetadata": {
          "stickerId": string,
          "altText": string,
          "language": string
        }
      }
    }
    '''
    for super_chat in resp_json['items']:
        display_name = super_chat['snippet']['supporterDetails']['displayName']
        created_at = super_chat['snippet']['createdAt']
        currency = super_chat['snippet']['currency']
        amount_micros = super_chat['snippet']['amountMicros']
        # prevent funder didn't write any msg
        comment_text = super_chat['snippet'].get('commentText')

        sc = SuperChat(display_name, created_at, currency, amount_micros, comment_text)

        superchat_list.append(sc)

    next_page_token = resp_json['nextPageToken']
    number_of_result = resp_json['pageInfo']['resultsPerPage']
    return superchat_list, next_page_token, number_of_result

