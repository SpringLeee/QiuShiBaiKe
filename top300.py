import os
import urllib.request
from pyquery import PyQuery as Jquery
import PyHelper


cc=1
Fs=open("糗事百科TOP150.txt","w",encoding="utf-8")
for x in range(1,10):
	purl="http://www.qiushibaike.com/text/page/"+str(x)+"/?s=4958576"  
	contentlist = HttpGet(purl).find(".mb15")
	for y in contentlist.items():
		author=y.find(".author").find("h2").html()
		content=y.find(".content").find("span").html().replace("<br />","\n")
		Fs.write("\n")
		Fs.write("	"+author+"\n")
		Fs.write("\n")
		Fs.write("	"+content+"\n")

		cc+=1
		Fs.write("\n")
		Fs.write("\n")

		print("正在抓取  "+ author+"    的数据......")
print("一共抓取了"+str(cc)+"条数据")
Fs.close()



 




   	



