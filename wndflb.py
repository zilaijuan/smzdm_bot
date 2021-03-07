"""
福利吧论坛自动签到脚本
使用github actions 定时执行
@author : stark
"""
import requests,os
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
            'authority': 'www.wnflb2020.com',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36 Edg/88.0.705.81',
            'x-requested-with': 'XMLHttpRequest',
            'accept': '*/*',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://www.wnflb2020.com/forum.php',
            'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            'cookie': 'S5r8_2132_nofavfid=1; S5r8_2132_smile=1D1; X_CACHE_KEY=6795d2a73d4e8e2cba4d53882e70414a; S5r8_2132_saltkey=j25d722Z; S5r8_2132_lastvisit=1612608786; S5r8_2132_auth=19e4RbUFdJCOuuWRoyTLz23gOOpk2CwgS%2Fkt9LzReyMoMm25cEalaFGMLusaKJcxEKiMahcEcPiRxamlsfMJtEuyzA; S5r8_2132_lastcheckfeed=12334%7C1612612407; S5r8_2132_atarget=1; S5r8_2132_visitedfid=2D37; S5r8_2132_forum_lastvisit=D_2_1614818989; S5r8_2132_sid=ljzC88; S5r8_2132_lip=116.227.74.154%2C1614818989; S5r8_2132_ulastactivity=f16eituVnOT4UDvyfg7wpAH820J3PLmYoEGNteR%2Fc2w1ira3E3iT; S5r8_2132_sendmail=1; S5r8_2132_lastact=1615036064%09home.php%09spacecp',
        }
        self.session.headers['cookie'] = cookies    

    def checkin(self):
        """
        签到函数
        """
        
        
        url = 'http://www.wnflb2020.com/plugin.php?id=fx_checkin:checkin&formhash=c36b4937&c36b4937&infloat=yes&handlekey=fx_checkin&inajax=1&ajaxtarget=fwin_content_fx_checkin'
        msg = self.session.get(url)
        if self.__json_check(msg):
            return msg.json()
        return msg.content


def start():
    sb = SMZDM_Bot()
    # sb.load_cookie_str(config.TEST_COOKIE)
    cookies = os.environ["FLB_COOKIES"]
    sb.load_cookie_str(cookies)
    res = sb.checkin()
    print(res)
    print('代码完毕')

if __name__ == '__main__':
    start()