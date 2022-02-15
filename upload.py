import datetime
from Google import Create_Service
from googleapiclient.http import MediaFileUpload


def api_upload(video, category=24, title="Internet is Awesome | Best Meme Compilation #1", description=""):
    CLIENT_SECRET_FILE = 'client_secret.json'
    API_NAME = 'youtube'
    API_VERSION = 'v3'
    SCOPES = ['https://www.googleapis.com/auth/youtube.upload']

    service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

    nt = datetime.datetime.now()
    upload_date_time = datetime.datetime(
        nt.year, nt.month, nt.day, nt.hour, nt.minute, nt.second).isoformat() + '.000Z'

    request_body = {
        'snippet': {
            'categoryI': category,
            'title': title,
            'description': description,
            'tags': ['compilation', 'memes', 'trynottolaugh', ]
        },
        'status': {
            'privacyStatus': 'private',
            'publishAt': upload_date_time,
            'selfDeclaredMadeForKids': False,
        },
        'notifySubscribers': False
    }

    mediaFile = MediaFileUpload(video)

    response_upload = service.videos().insert(
        part='snippet,status',
        body=request_body,
        media_body=mediaFile
    ).execute()

    # service.thumbnails().set(
    #     videoId=response_upload.get('id'),
    #     media_body=MediaFileUpload('thumbnail.jpg')
    # ).execute()


if __name__ == "__main__":
    api_upload('intro.mp4', title='Sample Video')
