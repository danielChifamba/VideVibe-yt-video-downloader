from django.shortcuts import render
from django.http import HttpResponse, FileResponse
from django.shortcuts import redirect
import os

from .models import YoutubeVideo

from .misc import getDetails
from .misc import truncateWords
from .misc import downloadMedia

# Create your views here.
def home(request):
    if not YoutubeVideo.objects.exists():
        print('Model Now Empty')
    else:
        YoutubeVideo.objects.all().delete()

    if request.method == 'POST':
        url = request.POST['youtube_url']
        if url:
            details = getDetails(url)
            desc = truncateWords(details['description'])
            video = YoutubeVideo(url=url, title=details['title'], description=desc, thumbnail=details['thumbnailURL'])
            if video.save() is None:
                return redirect('download')
        else:
            print('URL error')
    return render(request, 'index.html')

def download(request):
    video = YoutubeVideo.objects.first()
    return render(request, 'download.html', {'video':video})

def completeDownload(request, format_type):
    video = YoutubeVideo.objects.first()
    url = video.url
    title = video.title
    
    file = downloadMedia(url, format_type, title)

    return FileResponse(open(file, 'rb'), as_attachment=True, filename=os.path.basename(file))

def about(request):
    return render(request, 'about.html')
