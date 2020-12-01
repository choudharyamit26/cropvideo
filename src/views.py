from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from django.utils import timezone
import os


class CropVideo(APIView):

    def post(self, request, *args, **kwargs):
        # start_time = self.request.POST.get('start_time')
        # end_time = self.request.POST.get('end_time')
        # input_video = self.request.POST.get('input_video')
        start_time = self.request.POST['start_time']
        end_time = self.request.POST['end_time']
        input_video = self.request.POST['input_video']

        output_video = str(timezone.now()) + ".mp4"
        print(output_video)
        ffmpeg_extract_subclip(input_video, int(start_time), int(end_time), targetname=output_video)
        # x = os.listdir()
        # for y in x:
        #     print(y)
        #     if y.endswith(".mp4"):
        #         print(y)
        #         print('>>>>>>>>>>', os.path.dirname(os.path.realpath(__file__)))
        print('_______________________', os.path.abspath(output_video))
        return Response({"message": "Video cropped successfully", "output_video_path": os.path.abspath(output_video),
                         "output_video_name": output_video, "status": HTTP_200_OK})
