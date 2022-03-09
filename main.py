filename = "imgs2.txt"  # /*输出目录及文件名*/
randimgs = open(filename, "a")
for numbers in range(1, 1846):  # /*输出序号，这里是从1输出到20*/
    numbers = "%04d" % numbers
    randimgs.write("https://raw.ldst.gq/github.com/gzhstu/picdev/blob/main/img/" + numbers + ".jpg\n")  # /*图片地址*/
randimgs.close()
# https://raw.ldst.gq/github.com/gzhstu/picdev/blob/main/img/0001.jpg