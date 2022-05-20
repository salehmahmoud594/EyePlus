from django.shortcuts import render
import os
from pathlib import Path


# Create your views here.

def index(request):
    # print(os.getcwd())
    # recorings_path = Path("project/static/recordings")
    recorings_path = Path("project/static/recordings")
    output_directory = recorings_path / 'videos'
    videos = os.listdir(output_directory)
    # 3{video_name: video_path}
    records = [{videoname: str(output_directory.joinpath(videoname))}
               for videoname in videos]
    context = {"files": records, "last": last_3_videos(output_directory)}
    print(context)
    return render(request, 'pages/index.html', context=context)


def last_3_videos(path):
    files = os.listdir(path)
    return [os.path.join(path, basename) for basename in files][:3]
