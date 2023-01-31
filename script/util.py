#!/usr/bin/python3

import glob
from pathlib2 import Path
paths = "../*"
files = glob.glob(paths)

searchdir = ('basics','chicken','garden')

def getSidebar(pre,post):
    htm = ""
    allfiles = {}
    htm = htm +"\n"+pre
    for f in files:
        if not Path(f).is_file() and Path(f).stem in searchdir:
            htm = htm + "\n"+"- "+Path(f).stem.capitalize()
            print("- "+Path(f).stem.capitalize())
            foo = glob.glob(f+'/*')
            for fim in foo:
                b = fim.split('-')
                li = ' '.join(b[3:])[0:-3]
                htm = htm +"\n" +"  - ["+li+"]("+Path(fim).stem+"/"+Path(fim).stem+")"
                print("  -["+li+"]("+Path(f).stem+"/"+Path(fim).stem+")")
                allfiles.setdefault(Path(fim).stem,Path(f).stem+"/"+Path(fim).stem)
    htm = htm +"\n" + post
    htm = htm +'\n'+"- Paper Roll"
    print("- Paper Roll")
    keys = list(allfiles.keys())
    keys.sort(reverse=True)
    for a in keys:
        htm =  htm +"\n" +"  - ["+a+"]("+allfiles[a]+")"
        print("  -["+a+"]("+allfiles[a]+")")
    return htm

pre = "&nbsp;&nbsp;![ig](https://tejasbuds.com/images/logo-small.png)\n\n* [Biochar Hub](./)"
post = "* [Back to Tejas Buds](https://tejasbuds.com/)\n* [About](https://tejasbuds.com/about.html)\n* [Contact](./contact/)"
h = getSidebar(pre,post)
with open('../_sidebar.md','w') as foo:
    foo.write(h)
foo.close()