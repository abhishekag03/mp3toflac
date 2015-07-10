#!/usr/bin/python3.4
#written by Kirk Hammond 20150710. kirkdhammond@gmail.com
#this scipt was developed and executed on Fedora 22. I have not tested any version of python other than 3.4

# script will locate all .mp3 files in a directory and convert them to .flac files.
#I wrote this after purchasing a car deck that will play flac files that had some issues with mp3 files showing up as n/a, but all flac files played fine.

#usage:
# ./mp3toflac.py <target_dir>


#import modules
import os
import sys
from subprocess import call


# show variables (for troubleshooting)
def show_vars(target_dir):
    print('target_dir = ' + target_dir)
    print('target_dir (absolute) = ' + os.path.abspath(target_dir))


#get full list of mp3 files from your target directory
def get_mp3_list(target_dir):
    mp3_list = []
    for root, dirs, files in os.walk(target_dir):
        for dir in dirs:
            path = root + dir
            for file in os.listdir(path):
                if file.endswith(".mp3"):
                    return_data = path + "/" + file
                    mp3_list.append(return_data)
    return mp3_list


#convert mp3 to flac if the flac target file does not already exist
def convert_mp3(mp3_list,target_dir):
    for mp3 in mp3_list:
        flac = mp3[:-4] + ".flac"
        if os.path.isfile(flac):
            print('File ' + flac + ' already exists')
        else:
            call(["ffmpeg", "-i", mp3, flac])


#main function: controls script flow
def main():
    target_dir = sys.argv[1]
    mp3_list = get_mp3_list(target_dir)
    convert_mp3(mp3_list, target_dir)


#call main funciont
if __name__ == '__main__':
    main()

