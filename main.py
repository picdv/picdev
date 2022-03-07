filename = "imgs.txt"  # /*输出目录及文件名*/
randimgs = open(filename, "a")
for numbers in range(1, 1846):  # /*输出序号，这里是从1输出到20*/
    numbers = "%04d" % numbers
    randimgs.write("https://cdn.jsdelivr.net/gh/gzhstu/picdev/img/" + numbers + ".jpg\n")  # /*图片地址*/
randimgs.close()
