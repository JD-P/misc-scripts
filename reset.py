#!/usr/bin/python3

import sys
import os
import subprocess
import glob
import bs4
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("blog", help="The blog to deploy with this script.")
parser.add_argument("-g", "--git-only", type=bool, default=False, 
                    dest='gitonly',
                    help="Don't run Jekyll over the cloned git repo.")
arguments = parser.parse_args()

def deploy(name, arguments):
    """Wrapper function that interprets arguments and calls a deploy_ 
    function."""
    if arguments.gitonly:
        deploy_git(name)
    else:
        deploy_blog(name)

def deploy_blog(blogname):
    """Deploy a jekyll blog stored in a git repository."""
    subprocess.call(("rm", "-rf", blogname))
    subprocess.call(("git", "clone", blogname + ".git"))
    sys.path.append(os.path.abspath(blogname + "/"))
    os.chdir(blogname)
    try:
        import prerender
        prerender.main()
    except ImportError:
        pass
    subprocess.call(("jekyll", "build", "--source", ".", 
                    "-d", "~/" + blogname + "-staging"))
    os.chdir(os.path.expanduser("~"))
    for path in glob.glob(blogname + "-staging/*"):
        subprocess.call(("cp", "-r", path, blogname + ".com/"))

def deploy_git(gitname):
    """Deploy a site directly from a git repository."""
    subprocess.call(("rm", "-rf", blogname))
    subprocess.call(("git", "clone", blogname + ".git", blogname + "staging"))
    os.chdir(blogname)
    subprocess.call("rm", "-rf", ".git")
    os.chdir(os.path.expanduser("~"))
    for path in glob.glob(blogname + "-staging/*"):
        subprocess.call(("cp", "-r", path, blogname + ".com/"))



if arguments.blog == "softholm":
    deploy("softholmsyndrome", arguments)
else:
    deploy(arguments.blog, arguments)
