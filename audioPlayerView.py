from tkinter import *
import tkinter.messagebox
import os
from tkinter import filedialog
from audioPlayerModel import audioPlayerModel
from pygame import mixer
from mutagen.mp3 import MP3
import time
import threading
import tkinter.ttk as ttk

from tkinter import filedialog
import cv2



## THIS CLASS IS ONLY TAKE CARE OF THE GUI PART OF THIS APP
class audioPlayerView:
    def __init__(self):
        #init Tkitner
        self.total_length=0
        self.current_time=0
        self.lines = []
        self.root = Tk()
        self.root.title("PlayMusic_Nhom9")
        self.root.iconbitmap(r'play_button_JpT_icon.ico')

        menubar = Menu(self.root)  # create menubar
        self.root.config(menu=menubar)

        # create status massage
        statusbar = Label(self.root, text="Welcom to my player", relief=SUNKEN)
        statusbar.pack(side=BOTTOM, fill=X)
        self.statusbar=statusbar

        submenu = Menu(menubar)

        #left frame
        left_frame = Frame(self.root)
        left_frame.pack(side=LEFT, padx=30)

        #right frame
        right_frame = Frame(self.root)
        right_frame.pack(side=RIGHT)

        #middle frame
        middle_frame = Frame(right_frame)
        middle_frame.pack(padx=10, pady=10)


        top_frame = Frame(right_frame)
        top_frame.pack()

        middle_frame = Frame(right_frame)
        middle_frame.pack(padx=10, pady=10)

        #buttom frame
        bottomframe = Frame(right_frame)
        bottomframe.pack()


        self.lenght_lable = Label(top_frame, text="Totel length :00:00 ")
        self.lenght_lable.pack()

        self.curren_Time_lable = Label(top_frame, text="current Time  :00:00 ")
        self.curren_Time_lable.pack()  #

        # tạo ds chứa các bài hát
        list_song = Listbox(left_frame)
        list_song.pack()
        self.list_song = list_song
        
        self.model = audioPlayerModel(self)
        self.load_Playlist_From_File()

        #images
        self.play_photo = PhotoImage(file='img/play-button.png')
        self.volume_photo = PhotoImage(file='img/volume.png')
        self.mute_photo = PhotoImage(file='img/mute.png')
        self.stop_photo = PhotoImage(file='img/stop.png')
        self.pause_photo = PhotoImage(file='img/pause.png')
        self.next_photo = PhotoImage(file='img/next.png')
        self.previous_photo = PhotoImage(file='img/previous.png')


        self.add_btn = Button(left_frame, text="Thêm bài hát",command=self.browse_file)
        self.add_btn.pack(side=LEFT, padx=10)

        self.del_btn = Button(left_frame, text="Xoá bài hát",command=self.update_Delet_Song)
        self.del_btn.pack(side=LEFT)
        
        self.play_video_btn = Button(left_frame, text="Mở Video", command=self.select_media)
        self.play_video_btn.pack(side=LEFT, padx=10)


        self.btn_mute = Button(bottomframe, image=self.volume_photo, command=self.update_Mute_Music)
        self.btn_mute.grid(row=0, column=1)

        self.btn_play = Button(middle_frame, image=self.play_photo,command=self.update_Play_Music)
        self.btn_play.grid(row=0, column=1, padx=10)

        self.btn_stop = Button(middle_frame, image=self.stop_photo, command=self.update_Stop_Music)
        self.btn_stop.grid(row=0, column=2, padx=10)

        self.btn_pause = Button(middle_frame, image=self.mute_photo, command=self.update_Pause_Music)

        self.btn_next = Button(middle_frame, image=self.next_photo, command=self.update_Next_Music)
        self.btn_next.grid(row=0, column=3)

        self.btn_previous = Button(middle_frame, image=self.previous_photo, command=self.update_Previous_Music)
        self.btn_previous.grid(row=0, column=0, )
        
        #tạo thanh trượt âm thanh 
        self.scale = Scale(bottomframe, from_=0, to=100, orien=HORIZONTAL,command=self.model.set_volume)  # scale of the valum
        self.scale.set(50)  # set the initial valume to be 50
        mixer.music.set_volume(0.5)
        self.scale.grid(row=0, column=2, pady=15, padx=30)

        #tạo thanh trượt hiển và điều chỉnh thời gian
        self.my_slider=ttk.Scale(top_frame, from_=0, to_=100, orient=HORIZONTAL, value=0,
        command=self.slide_Music, length=250)
        self.my_slider.pack(side=BOTTOM)

        #Đặt hành động khi cửa sổ được đóng và chạy vòng lặp chính của ứng dụng.
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()

    # mở hộp thoại để chọn tệp
    def select_media(self):
        global selected_media_path
        filetypes = [
            ("MP4 files", "*.mp4"),
            ("AVI files", "*.avi"),
            ("MOV files", "*.mov")
        ]

        selected_media_path = filedialog.askopenfilename(filetypes=filetypes)
        if selected_media_path:
            if selected_media_path.endswith((".mp4", ".avi", ".mov")):
                self.play_video(selected_media_path)
            else:
                tkinter.messagebox.showerror("Eror", "Định dạng video không đuọc hỗ trợ...")
                
    def play_video(self, video_url):
        cap = cv2.VideoCapture(video_url)
        while True: # vòng lập vô hạn để bắt đọc từ khung hình trong video
            ret, frame = cap.read() # độc khung hình từ video và lưu trữ vào frame và boolean là ret
            if not ret: # nếu đọc khung hình không thành công thì thoát khỏi vòng lặp
                break
            cv2.imshow('Video Player', frame) # hiển thị cửa sổ khung hình
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
        cap.release() # giải phóng toàn bộ nhớ
        cv2.destroyAllWindows() # đóng toàn bộ cửa sổ openCV
        
    # chọn một tệp âm nhạc từ hộp thoại
    def browse_file(self):
        global filePath
        filePath = filedialog.askopenfilename() # mở hộp thoại chọn tệp
        if(filePath != ''):
          filename = os.path.basename(filePath) # lấy tên tệp đầy đủ từ đường dẫn
          index = self.list_song.size() 
          self.list_song.insert(index, filename)
          self.list_song.pack() # cập nhật hiển thị trong ds
          self.model.add_to_playlist(filePath) # thêm vào trong mô hình
          self.lines.insert(index, filePath) # thêm vào danh sách lines
          lastIndex = len(self.lines) # cập nhật lại chiều dài
          if lastIndex > 0:
            self.list_song.selection_clear(0)
            self.list_song.activate(0)
            self.list_song.selection_set(0)

    # tải danh sách phát âm nhạc từ tệp MP3MusicList.txt
    def load_Playlist_From_File(self):
        try:
            with open("MP3MusicList.txt", "r", encoding='UTF-8') as playlist_File:
                list = playlist_File.readlines()
                for element in list:
                    if not element.isspace(): # Kiểm tra xem dòng đó không phải là dòng trống.
                        self.lines.append(element) # nếu không phải thì được add vào ds lines
                for filePath in self.lines: # kiểm tra từng đường dẫn trong ds lines
                    index = self.list_song.size()
                    f = os.path.basename(filePath.rstrip()) # lấy tên tệp ở cuối của đường dẫn "strip()" dùng để loại bỏ những ký tự
                    self.list_song.insert(index, f) # thêm tên tệp vào danh sách phát của người dùng
                    self.list_song.pack() # cập nhật hiển thị
                    self.model.add_to_playlist(filePath.rstrip())  # Thêm đường dẫn vào danh sách phát trong mô hình người dùng.
                    lastIndex = len(self.lines) # lấy chiều dài của danh sách
                    if lastIndex > 0:
                        self.list_song.selection_clear(0)
                        self.list_song.activate(0)
                        self.list_song.selection_set(0)
        except:
            print("file not found")
            playlist_File = open("MP3MusicList.txt", "w+", encoding='UTF-8')

    # chức năng play
    def update_Play_Music(self):
        if(self.model.play): # kiểm tra xem âm nhạc có đang phát không
            self.update_Pause_Music() # gọi pause để tạm dừng
            return

        self.model.play_Music() 
        if(self.model.current_song!=None):
            self.statusbar['text'] = "playing music  " + os.path.basename(self.model.current_song) # cập nhật thanh trạng thái
        else:
            tkinter.messagebox.showerror("Eror", "Not found music to play !")
        if(self.model.play):
            self.btn_play.configure(image=self.pause_photo)

    # xoá bài hát khỏi danh sách
    def update_Delet_Song(self):
        selected_song = self.list_song.curselection()
        self.list_song.delete(selected_song)
        selected_song = int(selected_song[0]) # chuyển về dạng số nguyên
        self.lines.pop(selected_song) #delete the selected song
        self.model.del_song(selected_song)
        if (selected_song > 0): # kiểm tra không phải là bài đầu tiên
            self.list_song.activate(selected_song - 1) 
            self.list_song.selection_set(selected_song - 1) # chỉ con trỏ lên bài trên
        if (selected_song == 0 and len(self.lines) != 0): # nếu là bài đầu tiên
            self.list_song.activate(selected_song)
            self.list_song.selection_set(selected_song) # chỉ con trỏ xuống bài tiếp
        self.btn_play.configure(image=self.play_photo)
        self.my_slider.config(value=0)
        self.show_current_time(0)
        self.show_total_time(0)

    # chức năng tắt âm thanh
    def update_Mute_Music(self):
      self.model.mute_Music()
      if(self.model.muted):
       self.btn_mute.configure(image=self.mute_photo)
      else:
       self.btn_mute.configure(image=self.volume_photo)

    # chức năng stop
    def update_Stop_Music(self):
        self.model.stop_Music()
        self.statusbar['text'] = "Music Stop"
        self.btn_play.configure(image=self.play_photo)
        self.my_slider.config(value=0)
        self.show_current_time(0)


   #chi tiết bài nhạc
    def show_details(self, play_song):
        file_data = os.path.splitext(play_song)
        print(file_data)
        if file_data[1] == ".mp3": # nếu thư mục là mp3
            audio = MP3(play_song)
            self.total_length = audio.info.length # dùng MP3 để lấy độ dại của bài hát
        else: # không phải mp3
            a = mixer.Sound(play_song) 
            self.total_length = a.get_length() # dùng pygame mxier.Sound() để lấy độ dài của bài hát

        self.show_total_time(self.total_length) # gọi hàm để hiển thị tổng tg bài hát trên UI
        self.statusbar['text'] = "playing music  " + os.path.basename(play_song)
        t1 = threading.Thread(target=self.start_count, args=(self.total_length,)) # tạo biến để bắt đầu đếm thời gian bằng hàm start_count
        t1.start() # bắt đầu


    # đếm thời gian của bài hát và cập nhật giao diện người dùng tương ứng.
    def start_count(self,total_length):
      # mixer.music.get.busy=return fal se when we press stop music
      self.current_time=0
      while self.current_time<=total_length and mixer.music.get_busy(): 
         if self.model.paused:
             continue # tiếp tục

         if self.model.stop:
             return # kết thúc vòng lập

         else:
          self.show_current_time(self.current_time) # cập nhật hiển thị tg hiện tại lên UI
          if(self.my_slider.get()==int(self.total_length)): # nếu thanh trượt == với tổng thời gian  
              pass 

          if(self.model.paused): # nếu tạm dừng
              pass

          elif(self.my_slider.get()==int(self.current_time)): # nếu thanh trượt đạt đến tg hiện tại của bài hát
            slider_position=int(self.total_length)
            self.my_slider.config(to=slider_position,value=int(self.current_time)) # cập nhật vị trí của thanh trượt
            
          # ở trường hợp khác cập nhật vị trí thanh trượt và hiển thị tg lên UI
          else:
              slider_position = int(self.total_length)
              self.my_slider.config(to=slider_position, value=int(self.my_slider.get()))
              next_time=int(self.my_slider.get()+1)
              self.show_current_time(next_time)
              self.my_slider.config(value=next_time)
              
              
        # nếu không thực hiện việc này sẽ làm cho vòng lập chạy quá nhanh và chạy vô hạn
          time.sleep(1) # dừng vòng lặp trong 1s để thêm thời gian theo đúng tỹ lệ thật
          self.current_time+=1 # tăng thời gian hiện tại lên một đơn vị

    #chức năng tạm dừng
    def update_Pause_Music(self):

        self.model.pause_Music()
        self.btn_play.configure(image=self.play_photo)
        self.statusbar['text'] = "Music pause"
        
    # chức năng chuyển bài
    def update_Next_Music(self):
        if self.model.current_song != None and len(self.lines) > 0:
            self.model.next_Music()
            self.next_selection()

        else:
            tkinter.messagebox.showerror("Eror", "The List is Empty!")
    # chức năng chuyển bài
    def update_Previous_Music(self):
        if self.model.current_song != None and len(self.lines) > 0:
            self.model.previous_Music()
            self.perv_selection()
        else:
            tkinter.messagebox.showerror("Eror", "The List is Empty!")


    # điều khiển thanh trượt
    def slide_Music(self,x):
        self.model.slider_Music()

    # hiển thị thời gian bài hát chạy ở khoảng tg
    def show_current_time(self,time):
        mint, sec = divmod(time, 60)
        mint = round(mint)
        sec = round(sec)
        time_formet = '{:02d}:{:02d}'.format(mint, sec)  # make the format text
        self.curren_Time_lable['text'] = "Current time  " + ' - ' + time_formet  # show total length of song


    ## hiển thị tổng thời gian bài hát
    def show_total_time(self,time):
        mint, sec = divmod(time, 60)
        mint = round(mint)
        sec = round(sec)
        time_formet = '{:02d}:{:02d}'.format(mint, sec)  # make the format text
        self.lenght_lable['text'] = "Total length  " + ' - ' + time_formet  # show total length of song time

    # chuyển bài hát khi bài hát đang phát
    def next_selection(self):
        selection_indices = self.list_song.curselection()

        # default next selection is the beginning
        next_selection = 0

        # make sure at least one item is selected
        if len(selection_indices) > 0:
            # Get the last selection, remember they are strings for some reason
            # so convert to int
            last_selection = int(selection_indices[-1])
            next_selection = last_selection + 1
        if int(selection_indices[-1]) == self.list_song.size() - 1:
            last_selection = int(selection_indices[-1])
            next_selection = 0

        self.list_song.selection_clear(last_selection)
        self.list_song.activate(next_selection)
        self.list_song.selection_set(next_selection)
        self.btn_play.configure(image=self.pause_photo)
        

    def perv_selection(self):
        selection_indices = self.list_song.curselection()

        # default next selection is the beginning
        next_selection = 0
        
        # default last selection is the beginning
        last_selection = selection_indices[0]
        
        if last_selection == 0:
            next_selection = self.list_song.size() - 1
        
        # make sure at least one item is selected
        elif last_selection <= self.list_song.size() - 1:
            next_selection = last_selection - 1

        self.list_song.selection_clear(last_selection)
        self.list_song.activate(next_selection)
        self.list_song.selection_set(next_selection)


    def update_set_Volume(self):
       self.btn_mute.configure(image=self.volume_photo)

   # function that start when we press to exit from the audioPlayer response to write the current songs to the file.
    def on_closing(self):
        self.model.stop_Music()
        self.model.write_List_To_File(self.lines)
        self.root.destroy()
