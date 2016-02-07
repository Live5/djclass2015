import urllib.request
import threading
from time import ctime
from bs4 import BeautifulSoup
def getPM25(cityname):
    site = 'http://www.pm25.com/' + cityname + '.html'
    html = urllib.request.urlopen(site)
    soup = BeautifulSoup(html)
    city = soup.find(class_ = 'bi_loaction_city')   # ��������
    aqi = soup.find("a",{"class","bi_aqiarea_num"})  # AQIָ��
    quality = soup.select(".bi_aqiarea_right span")  # ���������ȼ�
    result = soup.find("div",class_ ='bi_aqiarea_bottom')   # ������������
    print (city.text + u'AQIָ����' + aqi.text + u'\n����������' + quality[0].text + result.text)
    print ('*'*20 + ctime() + '*'*20)
def one_thread():   # ���߳�
    print ('One_thread Start: ' + ctime() + '\n')
    getPM25('hefei')
    getPM25('shanghai')
def two_thread():   # ���߳�
    print ('Two_thread Start: ' + ctime() + '\n')
    threads = []
    t1 = threading.Thread(target=getPM25,args=('hefei',))
    threads.append(t1)
    t2 = threading.Thread(target=getPM25,args=('shanghai',))
    threads.append(t2)
    for t in threads:
        # t.setDaemon(True)
        t.start()
if __name__ == '__main__':
    one_thread
    print ('\n' * 2)
    two_thread