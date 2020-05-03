import os
import sh
'''
def getFolderSize(folder):
        total_size = os.path.getsize(folder)
        for item in os.listdir(folder):
            itempath = os.path.join(folder, item)
            if os.path.isfile(itempath):
                total_size += os.path.getsize(itempath)
            elif os.path.isdir(itempath):
                total_size += getFolderSize(itempath)
        return total_size

def getFolderSize(path):
    total = 0
    for entry in os.scandir(path):
        if entry.is_file():
            total += entry.stat().st_size
        elif entry.is_dir():
            total += getFolderSize(entry.path)
    return total
'''
def getFolderSize(path):
    return int(sh.du("-s",path).split("\t")[0])

class File:
    '''
    Only Works with os.scandir objects
    '''
    def __init__(self,fileobject,path=False):
        if path==True:
            #scandir object assignment
            path_address, file_name = os.path.split(fileobject)
            for _  in os.scandir(path_address):
                if _.name == file_name:
                    self.fileobject= _ 
                    break
        else:
            self.fileobject=fileobject

    def path(self):
        return self.fileobject.path

    

    def size(self):
        '''
        returns size in MBs and GBs
        2 decimal
        '''
        size_unit =" KB" #basic unit
        if self.fileobject.is_file():
            size_kb = os.path.getsize(self.fileobject.path)/(1024) #bytes
        else:
            size_kb=0
            #size_kb = getFolderSize(self.fileobject.path)/(1024)
            
        if size_kb >1000:
            size_kb = size_kb/1024
            size_unit = " MB"

        if size_kb>1000:
            size_kb = size_kb/1024
            size_unit = " GB"

        return "{:.2f}".format(size_kb)+size_unit
        
            
    def is_file(self):
        return self.fileobject.is_file()
        
    def name(self):
        return self.fileobject.name[0:20]
    def name_full(self):
        return self.fileobject.name
    def ext(self): #for icons
        if "." not in self.fileobject.name:
            return "file"
        else:
            with open('/root/filemanager/filemanager/fm/ext.txt') as file:
                extens = file.read()
            extension = self.fileobject.name.split(".")[-1].lower()
            if extension not in extens:
                return "file"
            return extension
    '''
    def scanner(self):
        files,folders=[],[]
        for i in os.scandir(self.fileobject.path):
        if i.is_file():
            files.append(i)
        else:
            folders.append(i)
        return {'foldersfiles':folders+files}
    '''

