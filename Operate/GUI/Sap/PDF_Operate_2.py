from io import StringIO
import os
import re
import pdfplumber
# from arc4 import ARC4

def readPdf(inputFile):
    text = []
    with pdfplumber.open(inputFile) as pdf:
        for page in pdf.pages:
            text += page.extract_text().split("\n")  # 提取文本
            print(text)
    return text

def saveAs(inputFile,outputFile):
    with open(inputFile, 'rb') as fp1:
        b1 = fp1.read()
    with open(outputFile, 'wb') as fp2:
        fp2.write(b1)

if __name__ == '__main__':
    # files = [
    #     "C:\\Users\\chen-fr\\Desktop\\DG invoice\\SPOOL_804654.pdf",
    #     "C:\\Users\\chen-fr\\Desktop\\DG invoice\\SPOOL_804665.pdf",
    #     "C:\\Users\\chen-fr\\Desktop\\DG invoice\\SPOOL_804671.pdf",
    #     "C:\\Users\\chen-fr\\Desktop\\DG invoice\\66.441.22.5510.01.pdf",
    #     "C:\\Users\\chen-fr\\Desktop\\DG invoice\\486318964-Sun Lik Shoes & Metal Co., Ltd..pdf",
    #     "C:\\Users\\chen-fr\\Desktop\\DG invoice\\66.441.22.6366.01.pdf",
    #     "C:\\Users\\chen-fr\\Desktop\\DG invoice\\66.441.22.6521.01.pdf",
    #     "C:\\Users\\chen-fr\\Desktop\\DG invoice\\486319620-TGL (HK) LIMITED.pdf",
    #     "C:\\Users\\chen-fr\\Desktop\\DG invoice\\486319792-Sugi International Limited.pdf",
    #     "C:\\Users\\chen-fr\\Desktop\\DG invoice\\486319783-Slip Enterprises Pty Ltd.pdf",
    #     "C:\\Users\\chen-fr\\Desktop\\DG invoice\\486319782-Skys Creative Co. Limited.pdf"
    #
    # ]


    dirUrl = "C:\\Users\\chen-fr\\Desktop\\New folder"  # 文件夹目录
    files = os.listdir(dirUrl)  # 得到文件夹下的所有文件名称
    n = 1
    invoiceNoStar = 4
    orderNoStar = 7
    msg = {}
    for each in files:
        print(each)
        fileUrl = '%s\\%s' % (dirUrl, each)
        if os.path.isfile(fileUrl):
            with open(fileUrl, 'rb') as my_pdf:
                print(n)
                fileCon = readPdf(my_pdf)
                print(fileCon)
                fileNum = 0
                for fileCon[fileNum] in fileCon:
                    # if re.match('.*P. R. China', fileCon[fileNum]):
                    #     if fileCon[fileNum+2] == 'Invoice ':
                    #         print(fileCon[fileNum], fileCon[fileNum + 4], 11)
                    #         msg['Company Name'] = fileCon[fileNum + 4]
                    #     else:
                    #         print(fileCon[fileNum],fileCon[fileNum+2],11)
                    #         msg['Company Name'] = fileCon[fileNum + 2]
                    if re.match('.*Invoice No.', fileCon[fileNum]):
                        msg['Company Name'] = fileCon[fileNum].replace('Invoice No.', '')
                    elif re.match('%s\d{8}'%invoiceNoStar, fileCon[fileNum]):
                        print(fileCon[fileNum], 22)
                        msg['Invoice No'] = fileCon[fileNum]
                    elif re.match('%s\d{8}'%orderNoStar, fileCon[fileNum]):
                        print(fileCon[fileNum], 33)
                        msg['Order No'] = fileCon[fileNum]
                    elif re.match('\d{2}.\d{3}.\d{2}.\d{4,5}', fileCon[fileNum]):
                        print(fileCon[fileNum], 44)
                        msg['Project No'] = fileCon[fileNum]
                    fileNum += 1
                n += 1
                # outputFlie = msg['Project No'] + '.pdf'
                outputFlie = msg['Invoice No'] + '-' + msg['Company Name'] + '.pdf'
                saveAs(fileUrl,'%s\\test\\%s' % (dirUrl, outputFlie))

        else:
            print('无')





