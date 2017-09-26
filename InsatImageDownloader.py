import urllib.request
import schedule
import time
import datetime

now=datetime.datetime.now()


def downloadimage(url):
    now = datetime.datetime.now()
    tname=now.strftime("%Y-%m-%d %H%M")
    filename=str(tname) +".jpg"
    urllib.request.urlretrieve(url,filename)

downloadimage("http://satellite.imd.gov.in/img/3Dglobe_ir1.jpg")
schedule.every(30).minutes.do(downloadimage,"http://satellite.imd.gov.in/img/3Dglobe_ir1.jpg")

while(1):
    schedule.run_pending()
    time.sleep(1)


