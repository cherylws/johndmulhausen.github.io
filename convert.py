import tomd
from markdownify import markdownify as md
from bs4 import BeautifulSoup
import requests
import re
import yaml
import os
import urllib
import urllib2
from slugify import slugify

def fetchMe(url):
    if "http" not in url:
        urlToUse = 'https://developer.prod.oculus.com' + url
        if urlToUse=='https://developer.prod.oculus.com/documentation/pcsdk/latest/concepts/pcsdk-intro/':
            r = requests.get(urlToUse)
            asciidata=r.text.encode("ascii","ignore")
            soup = BeautifulSoup(asciidata, 'html5lib')
            title = soup.title.string
            #description = soup.description.string

            soup.select_one("h1").decompose()
            imgs = soup.findAll("img")
            imageNumber = 0
            for img in imgs:
                if 'https://www.facebook.com/tr?i' not in img['src']:
                    print img['src']
                    newFilename = '/images/' + slugify(url) + '-' + str(imageNumber)
                    print newFilename
                    #urllib.urlretrieve(img['src'], os.path.basename(newFilename))
                    imageNumber = imageNumber + 1
            bodyHTML = str(soup.find(class_='documentation-content'))
            output = '---\n'
            output += 'title: ' + title + '\n'
            #output += 'description: ' + description + '\n'
            output += '---\n'
            bodyMD = md(bodyHTML, heading_style='ATX')
            bodyMDFixedImages = re.sub(r'(?:!\[(.*?)\]\((.*?)\))',r'\1\n',bodyMD)
            output += bodyMD
            outputFileName = os.getcwd() + url[:-1].replace('/','\\') + '.md'
            print(outputFileName)
            try:
                f = open(outputFileName, 'r')
            except IOError:
                f = open(outputFileName, 'w')
            f.write(output)
            f.close
            print(output)

def parseTree(tree):
    global paths
    #print('tree is a ' + str(type(tree)))
    if str(type(tree)) == "<type 'dict'>":
        for key, value in tree.iteritems():
            #print('Dict! key is ' + str(type(key)) + ' and value is ' + str(type(value)))
            if str(type(key)) == "<type 'dict'>":
                parseTree(key)
            if str(type(key)) == "<type 'str'>":
                if str(type(value)) == "<type 'str'>":
                    # there are no further values here
                    #print('String! key is ' + str(key) + ' and value is ' + str(value))
                    if str(key) == 'path':
                        paths = paths + 1
                        fetchMe(str(value))
                elif str(type(value)) == "<type 'list'>":
                    # there are more values here
                    parseTree(value)
    else:
        for key in tree:
            #print(type(key))
            if str(type(key)) == "<type 'dict'>":
                parseTree(key)
            if str(type(key)) == "<type 'str'>":
                print('***STRING IN A LIST****! Key is: ' + str(type(key)))
paths = 0
with open("_data/nav.yaml", 'r') as stream:
    try:
        nav = yaml.load(stream)
        print('leftnav is a ' + str(type(nav['leftnav'])))
        parseTree(nav['leftnav'])
    except yaml.YAMLError as exc:
        print(exc)

print('All done! Paths found: ' + str(paths))

"""
r = requests.get('https://developer.oculus.com/documentation/pcsdk/latest/concepts/pcsdk-intro/')
asciidata=r.text.encode("ascii","ignore")
soup = BeautifulSoup(asciidata, 'html5lib')
title = soup.title.string
#description = soup.description.string
bodyHTML = str(soup.find(class_='documentation-content'))
output = '---\n'
output += 'title: ' + title + '\n'
#output += 'description: ' + description + '\n'
output += '---\n'
bodyMD = md(bodyHTML, heading_style='ATX')
bodyMDFixedImages = re.sub(r'(?:!\[(.*?)\]\((.*?)\))',r'\1\n',bodyMD)
output += bodyMD
print(output)
"""
