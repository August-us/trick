from win32com import client
import re
import os
import traceback


def judge(answer):
    if answer=='Y' or answer=='对':
        return '√'
    elif answer=='N' or answer=='错':
        return '╳'
    return answer

def processJudge(question):
    # print(question[0:1],question[0].count('\n'))
    result = ''
    for index, subject in enumerate(question):
        # print(subject.split('\n'))

        if subject.count('\n') >= 1:
            line1, line2 = subject.split('\n')[0:2]

            answer = re.findall(r'答案\s*?[:：]\s*?([YN对错])', line1)[0]
            answer=judge(answer)
            analysis = ''.join(re.split(r'答案\s*?[:：]\s*?[YN对错]', line1))
            # print(re.findall(r'答案\s*?[:：]',line1))
            # print(len(re.split(r'答案\s*?[:：]',line1)))
            if re.findall(r'[(（]\s*[)）]', line2):
                result += str(index + 1) + '. ' + re.sub(r'[(（]\s*[)）]', '( %s )' % answer, line2,1)
            else:
                result += str(index + 1) + '. ' +line2.strip()+ '   ( %s )\n' % answer
            if result[-1] != '\n':
                result += '\n'
            result += '解析: 难易程度' + analysis + '\n'

    return  result

def processChoice(question):
    # print(question[0:1],question[0].count('\n'))
    result=''
    for index,subject in enumerate(question):
        # print(subject.split('\n'))

        if subject.count('\n')>1:
            # print(subject.split('\n'))
            line1,line2=subject.split('\n')[0:2]
            line3=''
            for line in subject.split('\n')[2:]:
                if line and len(line.strip())>3 and not re.findall(r'^\s*\d{5,6}',line):
                    line3+=line+'\n'
            answer=re.findall(r'答案\s*?[:：]\s*?([A-H]+)',line1)[0]
            analysis = ''.join(re.split(r'答案\s*?[:：]\s*?[A-H]+',line1))
            # print(re.findall(r'答案\s*?[:：]',line1))
            # print(len(re.split(r'答案\s*?[:：]',line1)))
            if str(index+1)==line2.strip()[:len(str(index+1))]:
                line2=line2.strip()[len(str(index+1))+1:]
            if re.findall(r'[(（]\s*[)）]',line2):
                result+=str(index+1)+'. '+re.sub(r'[(（]\s*[)）]','( %s )'%answer,line2,1)
            else:
                result += str(index + 1) + '. ' + line2.strip() + '   ( %s )\n' % answer
            if result[-1]!='\n':
                result+='\n'
            result+=line3
            if result[-1]!='\n':
                result+='\n'
            result+='解析: 难易程度'+analysis+'\n'

    return result


def processMChoice(question):
    # print(question[0:1],question[0].count('\n'))
    result=''
    for index,subject in enumerate(question):
        # print(subject.split('\n'),len(subject.split('\n')))

        if subject.count('\n')>0:
            # print(subject.split('\n'))
            line1=subject.split('\n')[0]
            line3=''
            for line in subject.split('\n')[1:]:
                if line and len(line.strip())>3 and not re.findall(r'^\s*\d{5,6}',line):
                    line3+=line+'\n'
            line1.replace('、','')
            answer=re.findall(r'答案\s*?[:：]\s*?([A-H]+)',line1)[0]
            # print(re.findall(r'答案\s*?[:：]\s*?([A-H]+)',line1))
            analysis = ''.join(re.split(r'答案\s*?[:：]\s*?[A-H]+',line1))
            # print(re.findall(r'答案\s*?[:：]',line1))
            # print(len(re.split(r'答案\s*?[:：]',line1)))
            if str(index+1)==line3.strip()[:len(str(index+1))]:
                line3=line3.strip()[len(str(index+1))+1:]
            if re.findall(r'[(（]\s*[)）]',line3):
                result +=str(index+1)+'. '+re.sub(r'[(（]\s*[)）]','( %s )'%answer,line3,count=1)

            else:
                result += str(index + 1) + '. ' + '( %s )' % answer+line3.strip()+'\n'
            if result[-1]!='\n':
                result+='\n'
        #     result+=line3
        #     if result[-1]!='\n':
        #         result+='\n'
            result+='解析: 难易程度'+analysis+'\n'
        else:
            print(subject.split('\n'), len(subject.split('\n')))

    return result

def segSubject(path):
    analysis,answer=None,None
    flag=0
    # it could process the docx and doc file
    mw=client.Dispatch("Word.Application")
    mw.Visible = True
    docToSave = mw.Documents.Add()
    r = docToSave.Range(0, 0)
    doc=mw.Documents.Open(path)
    print(path+"     processing")
    # doc.SaveAs(toPath,format)  # fromat=2 represent that txt file
    text=''
    for paragraph in doc.Paragraphs:
        line=paragraph.Range.Text
        if len(line)!=1:
            text+=str(line+'\n')
    text=text.replace('\r\n','\n')
    text = text.replace('\r', '\n').replace('\x0b','\n')
    if len(re.findall('(.*)单选(.*)',text))==1:
        index1 =re.search('(.*)单选(.*)',text).span()[1]
    else:
        doc.Close()
        docToSave.Close()
        mw.Quit()
        raise Exception('文档无法确定单选开始位置')
    if len(re.findall('(.*)多选(.*)',text))==1:
        index1_,index2=re.search('(.*)多选(.*)', text).span()
        print(index1_,index2)
        # '二、多项选择题'
    else:
        doc.Close()
        docToSave.Close()
        mw.Quit()
        raise Exception('文档无法确定多选开始位置')
    if len(re.findall('(.*)判断题(.*)',text))==1:
        index2_, index3 = re.search('(.*)判断题(.*)', text).span()
    else:
        doc.Close()
        docToSave.Close()
        mw.Quit()
        raise Exception('文档无法确定判断开始位置')
    choice=text[index1:index1_].split('难易程度')
    Mchoice = text[index2:index2_].split('难易程度')
    judge_=text[index3:].split('难易程度')
    judge_[-1]=''.join(judge_[-1].split('\n')[0:2])
    r.InsertAfter('一、单项选择题\n')
    r.InsertAfter(processChoice(choice[1:]))
    r.InsertAfter('二、多项选择题\n')
    r.InsertAfter(processMChoice(Mchoice[1:]))
    r.InsertAfter('三、判断题\n')
    r.InsertAfter(processJudge(judge_[1:]))

    doc.Close()
    docToSave.SaveAs(path.split('.')[0] + '1.doc')
    docToSave.Close()
    os.remove(path)
    os.rename(path.split('.')[0] + '1.doc', path)

    try:
        mw.Quit()
    except:
        pass

if __name__=="__main__":
    # path=r'D:\document\python\trick\wordConvert\ZNLY-1-3-02（理论题）综合布线系统（双绞线）安装与认证测试(1).doc'
    rootpath=''
    from tkinter import filedialog

    default_dir = r"C:\Users\lenovo\Desktop"  # 设置默认打开目录
    rootpath = filedialog.askdirectory(initialdir=(os.path.expanduser(default_dir)))

    for file in os.listdir(rootpath):
        path=os.path.join(rootpath,file)
        if " " in path:
            path_new=str(path).replace(' ','')
            os.rename(path, path_new)
            path=path_new
        try:
            segSubject(path)
        except Exception as e:
            print('Error! '+path)
            traceback.print_exc()
