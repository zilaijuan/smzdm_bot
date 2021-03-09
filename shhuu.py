"""
手机淘论坛自动签到脚本
使用github actions 定时执行
@author : stark
"""
import requests
import os
from sys import argv

import config
from utils.serverchan_push import push_to_wechat


class SMZDM_Bot(object):
    def __init__(self):
        self.session = requests.Session()
        # 添加 headers
        self.session.headers = config.DEFAULT_HEADERS

    def __json_check(self, msg):
        """
        对请求 盖乐世社区 返回的数据进行进行检查
        1.判断是否 json 形式
        """
        try:
            result = msg.json()
            print(result)
            return True
        except Exception as e:
            print(f'Error : {e}')
            return False

    def load_cookie_str(self, cookies):
        """
        起一个什么值得买的，带cookie的session
        cookie 为浏览器复制来的字符串
        :param cookie: 登录过的社区网站 cookie
        """
        self.session.headers = {
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'Upgrade-Insecure-Requests': '1',
            'Origin': 'http://www.shhuu.com',
            'Content-Type': 'application/x-www-form-urlencoded',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36 Edg/88.0.705.81',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Referer': 'http://www.shhuu.com/dsu_paulsign-sign.html',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cookie': 'Grix_144c_saltkey=g5v52xE2; Grix_144c_lastvisit=1615276369; safedog-flow-item=D2344379D260466F59849AA5DC5AA2D9; __51cke__=; Grix_144c_ulastactivity=5661BkbTNux84f1L10WOrt%2BZFN0XBSH41NLF%2B2ymJRdpaR5bl4py; Grix_144c_auth=c50cyUTBwcP3ZezTrAypXuTjUWBn0LVzb%2B8hTWI%2FZDfD50QdJn84z9IHhdShSuh6i3iGnx%2FK7nGexhpgja7WMMQSGgk; Grix_144c_security_cookiereport=11f32RJL%2BGRj8Xfkx%2BroH%2B3IEjm8qRlpn1uPb%2F4mN%2BDLly9FQMLq; Grix_144c_connect_is_bind=1; Grix_144c_nofavfid=1; Grix_144c_noticeTitle=1; Grix_144c_atarget=1; Grix_144c_smile=1D1; Grix_144c_st_p=154104%7C1615280190%7C9e0e1a2fff73392af44018001f643e7a; Grix_144c_viewid=tid_325852; Grix_144c_sendmail=1; Grix_144c_sid=acocz5; Grix_144c_lip=124.79.22.75%2C1615280289; Grix_144c_onlineusernum=784; Grix_144c_forum_lastvisit=D_137_1615279999D_105_1615280320; Grix_144c_visitedfid=105D50D137; Grix_144c_st_t=154104%7C1615280327%7Cb806db3ffa54acb3335b68f80e36b440; Grix_144c_lastcheckfeed=154104%7C1615280354; __tins__17492567=%7B%22sid%22%3A%201615279889077%2C%20%22vd%22%3A%2027%2C%20%22expires%22%3A%201615282082179%7D; __51laig__=27; Grix_144c_lastact=1615280370%09connect.php%09check'
        }
        self.session.headers['cookie'] = cookies

    def checkin(self):
        """
        签到函数
        """
        url = "http://www.shhuu.com/plugin.php?id=dsu_paulsign:sign&operation=qiandao&infloat=1&inajax=1"

        payload='formhash=0ed27efe&qdxq=kx&qdmode=2&todaysay=&fastreply=0'
        msg = self.session.post(url=url,data=payload)

        return msg.text


def start():
    print("=================================================")
    print("||                 shhuu Sign                    ||")
    print("=================================================")
    sb = SMZDM_Bot()
    # sb.load_cookie_str(config.TEST_COOKIE)
    cookies = os.environ["SHHUU_COOKIES"]
    sb.load_cookie_str(cookies)
    res = sb.checkin()
    print(res)
    print('代码完毕')
    print('-> 任务圆满完成')


if __name__ == '__main__':
    start()
