import docker
import time

from datetime import datetime
from pytz import timezone, utc
import sys,getopt


allpulls = []

def get_pst_time():
    date_format='%m-%d-%Y %H:%M:%S %Z'
    date = datetime.now(tz=utc)
    date = date.astimezone(timezone('US/Pacific'))
    pstDateTime=date.strftime(date_format)
    return pstDateTime


def pull(imagename,count):
    startTime=get_pst_time()

    client = docker.from_env()


    for x in range(count):
        tic = time.perf_counter()
        image = client.images.pull(imagename)
        toc = time.perf_counter()
        client.images.remove(image.short_id)
        allpulls.append(float(f"{toc - tic:0.4f}"))
        print(f"Downloaded the Image in {x} itteration {toc - tic:0.4f} seconds")
            
    endTime=get_pst_time()

    print("Start time: "+ str(startTime))
    print("End Time: "+str(endTime))
    print("Minimum Time to Pull "+ str(min(allpulls)))
    print("Maximum Time to Pull "+ str(max(allpulls)))



def main(argv):
   imagename = ''
   count = ''
   try:
      opts, args = getopt.getopt(argv,"hi:c",["imagename=","count="])
   except getopt.GetoptError:
      print('dockerpull.py -i <imagename> -c <count>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print('dockerpull.py -i <imagename> -c <count>')
         sys.exit()
      elif opt in ("-i", "--imagename"):
         imagename = arg
      elif opt in ("-c", "--count"):
         count = int(arg)

   
   print("Pulling "+ imagename )
   print("==============================================")   
   pull(imagename=imagename,count=count)
   print("==============================================")

if __name__ == "__main__":
   main(sys.argv[1:])
