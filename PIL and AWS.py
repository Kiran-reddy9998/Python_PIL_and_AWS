import boto3
from PIL import Image, ImageDraw, ImageFont
import datetime as dt

d_img = Image.open('eyes_1.jpg')
w_img, h_img = d_img.size

dr_image = ImageDraw.Draw(d_img)
txt_img = "@Kiran Reddy"

font_img = ImageFont.truetype('GeraldinePersonalUseItalic-PK12m.ttf',70)
text_width, text_height = dr_image.textsize(txt_img,font_img)

font_margin = 250
x = w_img - text_height - font_margin
y = h_img - text_height - font_margin

dr_image.text((x,y), txt_img, font = font_img)
#d_img.show()

current_dt = dt.datetime.now().strftime('%d-%m-%Y %I-%M-%S')
# this line is used to the img name in the format of date and time.
file_name = current_dt + '.jpg'

d_img.save(file_name)

file_name_1 = "'"+file_name+"'"
print(file_name_1)



resource = boto3.client('s3')
resource.upload_file(
    Filename=file_name,
    Bucket='bucket-for-pt1',
    Key='pic_1.jpg'
)
print("File Uploaded to your S3 Bucket Successfully")

#os.remove(file_name)





