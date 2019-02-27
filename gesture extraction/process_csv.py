import re as re
import matplotlib.pyplot as plt
from matplotlib.pyplot import cm
from datetime import datetime
import numpy as np

p_t = re.compile('(\d):(\d+).*')
p_ges_b = re.compile('.*\(.*(beats).*\).*')
p_ges_m = re.compile('.*\(.*(metaphoric).*\).*')
p_ges_d = re.compile('.*\(.*(deictic).*\).*')
p_ges_i = re.compile('.*\(.*(iconic).*\).*')

filename="ges_ps.csv"
#output_file="ges.csv"
f_out= open("counts_"+filename,"w+")
with open(filename) as f:
    lis=[line.split() for line in f]        # create a list of lists
    out_str = "time(s),beats,metaphoric,deictic,iconic\n"
    f_out.write(out_str)
    for i,x in enumerate(lis):              #print the list items
        print("line{0} = {1}".format(i,x))
        if(len(x)==0): continue
        m_t = p_t.search(x[0])
        cur_str = ",".join(x)
        if (m_t is None):
            print("skip:%s"%(cur_str))
            continue

        b_len, m_len, d_len, i_len = 0,0,0,0
        m_b = p_ges_b.search(cur_str)
        if(m_b is not None):
            b_len = len(m_b.groups())
        m_m = p_ges_m.search(cur_str)
        if (m_m is not None):
            m_len = len(m_m.groups())
        m_d = p_ges_d.search(cur_str)
        if (m_d is not None):
            d_len = len(m_d.groups())
        m_i = p_ges_i.search(cur_str)
        if (m_i is not None):
            i_len = len(m_i.groups())

        t_min = int(m_t.group(1))
        t_sec = int(m_t.group(2))
        t = t_min*60 + t_sec

        out_str = "%d, %d, %d, %d, %d\n"%(t,b_len,m_len,d_len,i_len)
        f_out.write(out_str)
f_out.close()