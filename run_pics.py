import sys
import os
import json
import time
import tkinter as tk
from PIL import Image, ImageTk


classes = [('Airliner', 'n02690373'),
            ('Sorrel', 'n02389026'),
            ('Jack-o’-lantern', 'n03590841'),
            ('Panda', 'n02510455'),
            ('Anemone fish', 'n02607072')]


images_path = 'images_data/'

timestamps = []
inclass_delay = 600
outer_delay = 5000
pics_per_class = 70
num_classes = len(classes)

class App(tk.Tk):
    def __init__(self, image_files):
        tk.Tk.__init__(self)
        self.w = self.winfo_screenwidth()
        self.h = self.winfo_screenheight()
        self.overrideredirect(1)
        self.geometry("%dx%d+0+0" % (self.w, self.h))
        self.pictures = []
        self.track_img_ndex = 0
        for img in image_files:
            self.pictures.append(img)
        self.picture_display = tk.Label(self)
        self.picture_display.pack(expand=True, fill="both")

    def show_slides(self):
        if self.track_img_ndex < len(self.pictures):
            delay = inclass_delay if self.track_img_ndex % (pics_per_class / 2 + 1) else outer_delay
            x = self.pictures[self.track_img_ndex]
            self.track_img_ndex +=1
            original_image = Image.open(x)
            resized = original_image.resize((self.w, self.h),Image.ANTIALIAS)
            new_img = ImageTk.PhotoImage(resized)
            self.picture_display.config(image=new_img)
            self.picture_display.image = new_img
            self.title(os.path.basename(x))
            timestamps.append(time.time_ns())
            self.after(delay, self.show_slides)
        else:
            timestamps.append(time.time_ns())
            print("End of list!")
            self.destroy()


if len(sys.argv) != 3:
    print('Provide only output file name as arg')
    exit()

file_path = sys.argv[1] + '_timestamps' + '.json'
if os.path.exists(file_path):
    print("file already exists")
    os.exit(0)

img_paths_file = sys.argv[1] + '_img_paths' + '.json'
if os.path.exists(img_paths_file):
    print("file already exists")
    os.exit(0)

image_files = []
for cl in classes:
    image_files.append(images_path + 'black_screen.jpg')
    for num in range(part_num - 1, pics_per_class, 2):
        image_files.append(images_path + cl[0] + '/' + str(num) + '.jpg')

app = App(image_files)
app.show_slides()
app.mainloop()

print('timestamps len =', len(timestamps))
print('avg time per pic =', (timestamps[-1] - timestamps[0]) / (pics_per_class * num_classes))

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(timestamps, f, ensure_ascii=False, indent=4)

with open(img_paths_file, 'w', encoding='utf-8') as f:
    json.dump(image_files, f, ensure_ascii=False, indent=4)
