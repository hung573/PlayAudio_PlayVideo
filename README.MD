# Play Audio And Play Video

Đây là một ứng dụng mà bạn có thể thêm 1 hoặc nhiều các bài hát mà bạn yêu thích hoặc có thể là những video mà bạn muốn xem. Được thiết kế dựa trên thư viện Pygame và Tkinter của Python. Nó cho phép bạn có thể điều chỉnh được âm lượng khi play các audio, chuyển bài nếu bạn muốn, bạn có thể tua đoạn nhác đến lúc bạn muốn và cuối cùng là bạn có thể dừng đoạn nhạc khi cần.

## Prerequisites

Before running the application, ensure you have the following dependencies installed:

- Python 3.x
- Tkinter
- Pygame
- OS
- Mutagen
- Time
- hreading
- OpenCV

You can install the dependencies using pip:

```
pip install pytube Pillow requests
```
## How to Use

**Clone the Repository:**
```
git clone https://github.com/hung573/PlayAudio_PlayVideo
```
**Navigate to the Project Directory:** 
```
cd PlayAudio_PlayVideo
```
**Run the Application:** 
```
python main.py
```
**UI_Main:** 
```
![UI_Main](img/UI_main.png)

1. **Enter YouTube URL:**
- In the provided entry field, enter the URL of the YouTube video you want to download.
- Click on the "Search Video" button to retrieve video information.

2. **Select Resolution:**
- After searching for the video, a list of available resolutions will be displayed in the dropdown menu.
- Select the desired resolution from the dropdown menu.

3. **Download Video:**
- Once you have selected the resolution, click on the "Download Selected" button to start downloading the video.
- The downloaded video will be saved in the same directory as the application.

4. **Error Handling:**
- If there are any errors during the process, error messages will be displayed in a pop-up window.

## Notes

- This application only supports downloading videos available in progressive streams.