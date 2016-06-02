#!/usr/bin/python
#! -*- coding=utf-8 -*-
import os
import sys
import re
import json
import time
import datetime
reload(sys)
sys.setdefaultencoding('utf-8')


def try_json(file_c):
    fin_list=[]
    re_m=re.compile(r"char \d{1,10} - \d{1,10}")

    m_count=0
    while True:
        m_count+=1
        try:
            mid_data=json.loads(file_c)
            fin_list.extend(mid_data["hits"]["hits"])
            return fin_list
        except Exception,e:
            print str(e)
            char_from=re_m.search(str(e))
            if char_from is not None:
                fin_char_from=int((char_from.group().split())[1])
                front_part=file_c[0:fin_char_from]
                mid_data=json.loads(front_part)
                fin_list.extend(mid_data["hits"]["hits"])
                file_c=file_c[fin_char_from:]
                

def read_file(filepath):
    f_h=open(filepath, "r")
    f_c=f_h.read()
    f_h.close()
    
    return f_c
    


    
if __name__=="__main__":
    if len(sys.argv)==3:
        org_data_list=read_file(sys.argv[1])
        great_r=try_json(org_data_list)
        f_h=open(sys.argv[2],"w")
        print len(great_r)
        m_count=0
        for i in great_r:
            f_h.write(json.dumps(i,ensure_ascii=False)+"\n")
        f_h.close()
    
