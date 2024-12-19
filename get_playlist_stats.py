import os, sys, datetime

from googleapiclient.discovery import build

API_KEY = os.environ['GOOGLE_API_KEY']
PLAYLIST_ID = sys.argv[1]

youtube = build('youtube', 'v3', developerKey=API_KEY)

def get_playlist_items(playlist_id):
    """
    Fetch all video IDs from the playlist.
    """
    videos = {}
    next_page_token = None

    while True:
        request = youtube.playlistItems().list(
            part="snippet,contentDetails",
            playlistId=playlist_id,
            maxResults=50,
            pageToken=next_page_token
        )
        response = request.execute()
        
        # Extract video IDs
        for item in response['items']:
            #videos.append(item['contentDetails']['videoId'],item['snippet']['title'])
            videos[item['contentDetails']['videoId']] = item['snippet']['title']
            #print(item['contentDetails']['videoId'])
        
        next_page_token = response.get('nextPageToken')
        if not next_page_token:
            break

    return videos

def get_video_statistics(video_dict):
    """
    Fetch statistics for a list of video IDs.

    video_dict = dict{id,title}
    """
    video_ids = list(video_dict.keys())
    stats = []

    for i in range(0, len(video_ids), 50):  # API allows up to 50 IDs per request
        request = youtube.videos().list(
            part="statistics",
            id=",".join(video_ids[i:i+50])
        )
        response = request.execute()

        for item in response['items']:
            #print(item)
            stats.append({
                "videoId": item['id'],"title": video_dict[item['id']],
                "views": int(item['statistics'].get('viewCount', 0)),
                "likes": int(item['statistics'].get('likeCount', 0)),
                "comments": int(item['statistics'].get('commentCount', 0)),
            })
    return stats

def get_views_last_month(video_dict):
    """
    Fetch views for the last month for each video in the playlist.
    """
    last_month_start = (datetime.datetime.now() - datetime.timedelta(days=30)).strftime("%Y-%m-%d")
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    video_ids = list(video_dict.keys())
    stats = []

    for video_id in video_ids:
        request = youtube_analytics.reports().query(
            ids="channel=={}".format(CHANNEL_ID),
            startDate=last_month_start,
            endDate=today,
            metrics="views,likes,comments",
            dimensions="video",
            filters="video=={}".format(video_id)
        )
        response = request.execute()
        
        for row in response.get("rows", []):
            stats.append({
                "videoId": row[0], "title": video_dict[item['id']],
                "views_last_month": row[1],
                "likes_last_month": row[2],
                "comments_last_month": row[3],
            })
    
    return stats

def filter_last_month(stats, video_ids):
    """
    Filter statistics for the last month based on date.
    """
    last_month_date = datetime.datetime.now() - datetime.timedelta(days=30)
    filtered_stats = []

    for video_id in video_ids:
        request = youtube.videos().list(
            part="snippet",
            id=video_id
        )
        response = request.execute()
        for item in response['items']:
            publish_date = datetime.datetime.strptime(item['snippet']['publishedAt'], "%Y-%m-%dT%H:%M:%SZ")
            if publish_date > last_month_date:
                filtered_stats.append(item)
                #print(item)

    return filtered_stats

def save_to_csv(data, filename="playlist_statistics.csv"):
    """
    Save statistics to a CSV file.
    """
    import csv

    keys = data[0].keys()  # Extract headers from the first dictionary
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)

playlist_dict = get_playlist_items(PLAYLIST_ID)

#stats = get_video_statistics(playlist_dict)
#print(stats)
stats = get_views_last_month(playlist_dict)

#filtered_data_by_month = filter_last_month(stats, playlist_items)

save_to_csv(stats)
