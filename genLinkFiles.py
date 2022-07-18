import os

os.chdir("/home/runner/work/picdev/picdev")


def genLink(path, linkFilePath):
    imgNames = os.listdir(path)
    linkFile = open(linkFilePath, "w")
    for name in imgNames:  # /*输出序号，这里是从1输出到20*/
        linkFile.write(f"https://raw.ldst.gq/picdv/picdev/main/{path}/{name}\n")
        linkFile.close()


Path1 = "imgs/web-www"
filename1 = "www.txt"  # /*输出目录及文件名*/
Path2 = "imgs/web-ani"
filename2 = "ani.txt"  # /*输出目录及文件名*/

genLink(Path1, filename1)
genLink(Path2, filename2)


# https://raw.ldst.gq/picdv/picdev/main/imgs/web-ani/001.jpg
# https://raw.ldst.gq/picdv/picdev/main/imgs/web-www/0006.jpg
