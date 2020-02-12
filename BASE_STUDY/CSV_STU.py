import csv

file = open('movies.csv', 'w', newline='')
csvwriter = csv.writer(file)

# 写入标题行
csvwriter.writerow(['名称', '年份'])
# 写入数据
csvwriter.writerow(['A', '1992'])
csvwriter.writerow(['B', '1998'])
csvwriter.writerow(['C', '2010'])
file.close()