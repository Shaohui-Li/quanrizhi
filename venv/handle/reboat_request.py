import requests
import json
class Reboat_request():
    def reboat_markdown_test(self,case_number=None,success_number=None,fail_number=None):
        data = {
            "msgtype": "markdown",
            "markdown": {
                "content": "测试执行用例总数：<font color='comment'>%s</font>例；\n"
                           "执行成功用例数：<font color='info'>%s</font>例；\n"
                           "执行失败用例数: <font color='warning'>%s</font>例。"%(case_number,success_number,fail_number)
            }
        }
        request_data = json.dumps(data)
        hearder = {
            "Content-Type": "application/json",
            "Connection": "keep-alive",

        }
        result = requests.post(
            "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=c1d60a22-b682-493e-839c-5dd8bcc30d99",
            data=request_data, headers=hearder)
        return print(result)
    def reboat_upload_file(self,filename):
        url="https://qyapi.weixin.qq.com/cgi-bin/webhook/upload_media?key=c1d60a22-b682-493e-839c-5dd8bcc30d99&type=file"
        hearder = {
            "Content-Type": "multipart/form-data",
            "Connection": "keep-alive",
            "Content-Length": "220",
        }
        files = {'file': open(filename, 'rb')}
        # data={
        #     "Content-Disposition": "form-data",
        #     "filelength": "6",
        #     "name": "media",
        #     "file_name": "D:/project/quanrizhi/venv/case/report.html",
        #     "Content - Type": "application / octet - stream",
        # }
        # request_data = json.dumps(data)
        result = requests.post(url,files=files,headers=hearder).text
        print(result)
        result=json.loads(result)
        media_id=result["media_id"]
        return media_id
    def reboat_fileadress(self,media_id):
        url="https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=c1d60a22-b682-493e-839c-5dd8bcc30d99"
        data={
            "msgtype": "file",
            "file": {
            "media_id": "%s"%(media_id)
                    },
            }
        hearder = {
            "Content-Type": "application/json",
            "Connection": "keep-alive",
        }
        request_data = json.dumps(data)
        result=requests.post(url,data=request_data,headers=hearder).text
        return result
if __name__=="__main__":
    # Reboat_request().reboat_test(10,8,2)
    media_id=Reboat_request().reboat_upload_file()
    print(Reboat_request().reboat_fileadress(media_id))
