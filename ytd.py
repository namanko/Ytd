#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pytube import YouTube  


# In[2]:


SAVE_PATH = input("Enter file path where the videos are to be saved(for eg C:/Users/Folder/To/Save): ")


# In[8]:


def yt_down():
    link=input("enter link " )
    yt = YouTube(link)
    stream = yt.streams.first()
    stream.download(SAVE_PATH)


# In[ ]:


yt_down()
n = int(input("how many links do you want to download: "))
for i in range(n):
    yt_down()
        

