# Play Audio And Play Video

Đây là một ứng dụng mà bạn có thể thêm 1 hoặc nhiều các bài hát mà bạn yêu thích hoặc có thể là những video mà bạn muốn xem. Ứng dụng được thiết kế dựa trên thư viện Pygame và Tkinter của Python. Nó cho phép bạn có thể điều chỉnh được âm lượng khi play các audio, chuyển bài nếu bạn muốn, bạn có thể tua đoạn nhạc đến lúc bạn muốn và cuối cùng là bạn có thể dừng đoạn nhạc khi cần.

## Prerequisites

Trước khi chạy ứng dụng, hãy đảm bảo bạn đã cài đặt các phần phụ thuộc sau:

- Python 3.x
- Tkinter
- Pygame
- OS
- Mutagen
- Time
- Threading
- OpenCV

Bạn có thể cài đặt các thư viện phụ thuộc bằng pip3 nếu như python của bạn ở Version 3.x:

```
pip3 install pygame
pip3 install mutagen
pip3 install opencv-python-headless
```
## Cách tải

**Tryt cập vào github:**
```
git clone https://github.com/hung573/PlayAudio_PlayVideo
```
**Đến thư mục và tải về:** 
```
cd PlayAudio_PlayVideo
```
**Chạy Application:** 
```
python main.py
```
![UI_Main](img/UI_main.png)
```
**Hướng dẫn sử dụng** 
1. **Thêm, xoá các bài hát vào danh sách phát và chọn video:**
- Bạn click vào nút thêm bài hát và lần lượt thêm các audio mà bạn yêu thích vào.
- Bạn chọn bài hát mà bạn không thích ở danh sách phát và bạn click vào nút "Xoá bài hát" để bạn xoá bài hát ra khỏi danh sách phát.
- Bạn click vào nút "Mở Video" và thực hiện chọn video có trên mấy mình để bắt đầu play chúng, khi bạn muốn tắt video bạn có thể ấn "q".

2. **Play, pause, stop:**
- Sau khi bạn thêm được danh sách bài hát, bạn có thể ấn nút "Play" để bắt đầu play bài đầu tiên, hoặc bạn có thể chọn bài hát mà bạn muốn "Play" có trong danh sách phát và bắt đầu play nó.
- Bạn có thể tạm ngưng bài hát bằng cách ấn vào nút "Pause" và bắt chúng play tiếp tục bằng cách ấn vào nút play.
- Bạn có thể ngưng hoàn toàn bài hát bằng cách ấn vào nút "Stop".

3. **Chuyển bài:**
- Bạn có thể chuyển bài xuống bằng cách ấn vào nút "Next".
- Bạn có thể chuyển bài xuống bằng cách ấn vào nút "Prever".

4. **Điều chỉnh âm thanh, và vị trí đoạn nhạc:**
- Bạn có thể kéo tăng âm lượng hoặc giảm âm lượng bằng cách kéo lên xuống ở nút lên xuống âm lượng. Hoặc bạn có thể để âm lượng yêm lặng bằng cách ấn vào nút "mute".
- Bạn có thể điều chỉnh vị trí đoạn nhạc bằng cách kéo qua lại ở scroll chạy thời gian của đoạn nhạc.

5. **Xử lý lỗi:**
- Nếu có bất kỳ lỗi nào xảy ra trong quá trình, các thông báo lỗi sẽ được hiển thị trong một cửa sổ pop-up.

## Notes

- Ứng dụng này chỉ hổ trợ các bản audio, video đã được tải xuống, và được add vào trong danh sách phát thì ứng dụng này mới có thể phát được.
