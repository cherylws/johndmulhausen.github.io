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
from urlparse import urlparse
from os.path import splitext
import shutil
import dashtable
#import pypandoc

directoriesToKill = ['_site','audio','blog','bugs','contact','documentation','downloads','design','develop','distribute','faqs','hardware-report','mobile','oculus-start','pc','platform','reference','rift','santacruz','support','unity','unreal','webvr']
for i in range(len(directoriesToKill)):
    shutil.rmtree(directoriesToKill[i], ignore_errors=True)

filesToKill = ['audio.md','hardware-report.md','design.md','develop.md','documentation.md','mobile.md','pc.md','platform.md','unity.md','unreal.md','webvr.md','rift.md','santacruz.md']
for i in range(len(filesToKill)):
    if os.path.isfile(filesToKill[i]):
        os.remove(filesToKill[i])

def get_ext(url):
    """Return the filename extension from url, or ''."""
    parsed = urlparse(url)
    root, ext = splitext(parsed.path)
    return ext  # or ext[1:] if you don't want the leading '.'

def fetchMe(url):
    if "http" not in url:
        print(url)
        urlToUse = 'https://developer.prod.oculus.com' + url
        r = requests.get(urlToUse)
        soup = BeautifulSoup(r.text, 'html5lib')
        if ":" not in soup.title.string:
            title = soup.title.string
        else:
            title = '"' + soup.title.string + '"'
        #description = soup.description.string

        firsth1 = soup.select_one("h1")
        if firsth1:
            soup.select_one("h1").decompose()
        imgs = soup.findAll("img")
        imageNumber = 0
        for img in imgs:
            if 'https://www.facebook.com/tr?i' not in img['src']:
                print img['src']
                extension = get_ext(img['src'])
                newFileStub = '/images/' + slugify(url.decode('utf-8')) + '-' + str(imageNumber) + extension
                newFilename = os.getcwd().replace('\\','/') + newFileStub
                print newFilename
                """
                if os.path.isfile(newFilename):
                    os.remove(newFilename)
                urllib.urlretrieve(img['src'], newFilename)
                """
                imageNumber = imageNumber + 1
                img['src'] = newFileStub
                imgMD = md(str(img))
                img.name = "p"
                img.string = imgMD
        uls = soup.findAll("ul")
        for ul in uls:
            ul.string = md(str(ul))
            ul.name = 'p'
        ols = soup.findAll("ol")
        for ol in ols:
            ol.string = md(str(ol))
            ol.name = 'p'
        brs = soup.findAll("br")
        for br in brs:
            br.replaceWith('\n')
        preS = soup.findAll("pre")
        for pre in preS:
            code = soup.new_tag('code')
            tmp = pre.string
            pre.string = ''
            code.string = tmp
            pre.append(code)
        samps = soup.findAll("samp")
        for samp in samps:
            samp.name = "code"
        tables = soup.findAll("table")
        for table in tables:
            print(table)
            tableMD = dashtable.html2md(unicode(table).encode('ascii','ignore'))
            print(tableMD)
            table.string = tableMD
            table.name = "p"
        links = soup.findAll("a")
        for link in links:
            link['href'] = link['href'].replace('https://developer.oculus.com','')
        bodyHTML = str(soup.find(class_='documentation-content'))
        output = '---\n'
        output += 'title: ' + title + '\n'
        #output += 'description: ' + description + '\n'
        output += '---\n'
        #bodyMD = md(bodyHTML, heading_style='ATX')
        bodyMD = str(tomd.convert(str(bodyHTML)))
        #bodyMD = pypandoc.convert_text(bodyHTML, 'gfm', format='html')
        #print(bodyMD)
        output += bodyMD.decode('utf-8')
        if url[-1:] == '/':
            linkToUse = url[:-1]
        else:
            linkToUse = url
        outputFileName = os.getcwd().replace('\\','/') + linkToUse + '.md'
        #print(outputFileName)
        # if file exists, delete it. otherwise, forge the path and write
        if os.path.isfile(outputFileName):
            os.remove(outputFileName)
        else:
            dirname = os.path.dirname(outputFileName)
            if not os.path.exists(dirname):
                os.makedirs(dirname)
        f = open(outputFileName, 'w')
        f.write(output.encode('utf-8'))
        f.close
        print(output.encode('utf-8'))

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
