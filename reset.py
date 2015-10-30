#!/usr/bin/python3

import os
import subprocess
import glob
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("blog", help="The blog to deploy with this script.")
arguments = parser.parse_args()

def deploy_blog(blogname):
    subprocess.call(("rm", "-rf", blogname))
    subprocess.call(("git", "clone", blogname + ".git"))
    os.chdir(blogname)
    subprocess.call(("jekyll", "build", "--source", ".", 
                    "-d", "~/" + blogname + "-staging"))
    os.chdir(os.path.expanduser("~"))
    for path in glob.glob(blogname + "-staging/*"):
        subprocess.call(("cp", "-r", path, blogname + ".com/"))

if arguments.blog == "softholm":
    deploy_blog("softholmsyndrome")
else:
    deploy_blog(arguments.blog)
