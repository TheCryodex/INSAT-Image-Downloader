import urllib.request
import schedule
import time
import datetime
import os

now=datetime.datetime.now()


def downloadimage(url):
    now = datetime.datetime.now()
    tname=now.strftime("%Y-%m-%d %H%M")
    filename=str(tname) +".jpg"
    urllib.request.urlretrieve(url,filename)
    cwd = os.getcwd()
    print("------Satellite image downloaded succesfully-----")
    print(f"Image saved at: {cwd}\{filename}")
    print("\n\nDownloading the next image after 30 minutes")

downloadimage("https://mausam.imd.gov.in/Satellite/3Dasiasec_ir1.jpg")
schedule.every(30).minutes.do(downloadimage,"http://satellite.imd.gov.in/img/3Dglobe_ir1.jpg")

while(1):
    schedule.run_pending()
    time.sleep(1)