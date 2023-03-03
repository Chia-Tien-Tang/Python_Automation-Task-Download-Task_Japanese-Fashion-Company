import requests
import os
import csv

"""Storage Path"""
imgfolder="/users/erictang/desktop"
fn = "/users/erictang/desktop/台湾商品画像インポート.csv"

"""Official Format"""
size = ["O","L","S1","S2"]
cd = ["C","D"]
category = ["商品番号", "画像種類", "画像番号", "メイン画像", "カラーコード", "ファイル名", "並び順", "画像補足文", "状態", "台湾画像フラグ"]

"""import list"""
print("~~~ Input data must be in csv file ~~~")
filelist = input("""Please type in the file name
< Notice > Don't type (.csv) in the name : """)
filelist = "/users/erictang/desktop/" + filelist + ".csv"

with open(filelist, newline='') as f:
    reader = csv.reader(f)
    list_num = list(reader)

product_num_tw = []
product_num_jp = []

for i in list_num:
    if i[1] == "tw":
        product_num_tw.append(i[0])
    elif i[1] == "jp":
        product_num_jp.append(i[0])
        
        
"""Download and Create csv"""
csv_data = []
total = {}
    
"""Download TW / JP"""
for n in product_num_tw:
    for j in size:
        for l in cd:
            if l == "C":
                for i in range(10):
                    url = f"https://cdn.beams.co.jp/img/goods/{n}/{j}/{n}_{l}_{i+1}.jpg"
                    if requests.get(url).status_code == 200:
                        response = requests.get(url).content
                        file_name = f"{n}_{l}_{i+1}.jpg"
                        os.makedirs(os.path.dirname("%s/%s.jpg" % (imgfolder, f"/{n}/{j}/{n}_{l}_{i+1}")), exist_ok=True)
                        with open("%s/%s.jpg" % (imgfolder, f"/{n}/{j}/{n}_{l}_{i+1}") , 'wb') as f:
                            f.write(response)                            
                        if j == "O" and i == 0:
                            file_csv = [n, l, 1001, 1, "", file_name, "", "", 0, 1]
                            csv_data.append(file_csv)
                        elif j == "O":
                            file_csv = [n, l, 1001+i, 0, "", file_name, "", "", 0, 1]
                            csv_data.append(file_csv)
                        
                    else:
                        pass
                    
            elif l == "D":
                for i in range(30):
                    url = f"https://cdn.beams.co.jp/img/goods/{n}/{j}/{n}_{l}_{i+1}.jpg"
                    if requests.get(url).status_code == 200:
                        response = requests.get(url).content
                        file_name = f"{n}_{l}_{i+1}.jpg"
                        os.makedirs(os.path.dirname("%s/%s.jpg" % (imgfolder, f"/{n}/{j}/{n}_{l}_{i+1}")), exist_ok=True)
                        with open("%s/%s.jpg" % (imgfolder, f"/{n}/{j}/{n}_{l}_{i+1}") , 'wb') as f:
                            f.write(response)
                        if j == "O" and i == 0:
                            file_csv = [n, l, 1001, 0, "", file_name, "", "", 0, 1]
                            csv_data.append(file_csv)
                        elif j == "O":
                            file_csv = [n, l, 1001+i, 0, "", file_name, "", "", 0, 1]
                            csv_data.append(file_csv)
                    else:
                        pass                 

for n in product_num_jp:
    for j in size:
        for l in cd:
            if l == "C":
                for i in range(10):
                    url = f"https://cdn.beams.co.jp/img/goods/{n}/{j}/{n}_{l}_{i+1}.jpg"
                    if requests.get(url).status_code == 200:
                        #response = requests.get(url).content
                        file_name = f"{n}_{l}_{i+1}.jpg"
                        #os.makedirs(os.path.dirname("%s/%s.jpg" % (imgfolder, f"/{n}/{j}/{n}_{l}_{i+1}")), exist_ok=True)
                        #with open("%s/%s.jpg" % (imgfolder, f"/{n}/{j}/{n}_{l}_{i+1}") , 'wb') as f:
                            #f.write(response)                            
                        if j == "O" and i == 0:
                            file_csv = [n, l, 1, 1, "", file_name, "", "", 0, 0]
                            csv_data.append(file_csv)
                        elif j == "O":
                            file_csv = [n, l, 1+i, 0, "", file_name, "", "", 0, 0]
                            csv_data.append(file_csv)
                        
                    else:
                        pass
                    
            elif l == "D":
                for i in range(30):
                    url = f"https://cdn.beams.co.jp/img/goods/{n}/{j}/{n}_{l}_{i+1}.jpg"
                    if requests.get(url).status_code == 200:
                        #response = requests.get(url).content
                        file_name = f"{n}_{l}_{i+1}.jpg"
                        #os.makedirs(os.path.dirname("%s/%s.jpg" % (imgfolder, f"/{n}/{j}/{n}_{l}_{i+1}")), exist_ok=True)
                        #with open("%s/%s.jpg" % (imgfolder, f"/{n}/{j}/{n}_{l}_{i+1}") , 'wb') as f:
                            #f.write(response)
                        if j == "O" and i == 0:
                            file_csv = [n, l, 1, 0, "", file_name, "", "", 0, 0]
                            csv_data.append(file_csv)
                        elif j == "O":
                            file_csv = [n, l, 1+i, 0, "", file_name, "", "", 0, 0]
                            csv_data.append(file_csv)
                    else:
                        pass

"""Create csv"""
with open(fn, "w", newline="") as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow(category)
    for x in csv_data:
        writer.writerow(x)

print("------------", end = "\n")
print("Download Completed!!!")
print("------------", end = "\n")