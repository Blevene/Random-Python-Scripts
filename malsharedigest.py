# Open and catalog list of samples observed for a given date
# on Malshare.com, location: http://www.malshare.com/daily/malshare.current.txt
# To Do:
# [x] Add 'search' argument that searches result file for provided hash
import urllib2
import argparse
from sys import argv
from datetime import date

parser = argparse.ArgumentParser()
parser.add_argument("-s", "--search",
	help="Search the consolidated results file for a hash")
parser.add_argument("-p", "--pull", action="store_true",
	help="Pull the most recent Malshare digest")
args = parser.parse_args()
pull_time = str(date.today())
if (args.pull):
	mal_digest = urllib2.urlopen(url='http://www.malshare.com/daily/malshare.current.txt')
	mal_digest = mal_digest.read()
	mal_digest_all = open("results.txt", 'a')
	mal_digest_all.write(pull_time + mal_digest + '\n')
	mal_digest_all.close()
elif (args.search):
	mal_digest_all = open("results.txt", 'r')
	lines = mal_digest_all.read()
	answer = lines.find(args.search)
	if answer != -1:
		print "The hash you searched for, %s, has been found" % args.search
	else:
		print "Sorry, we don't have that hash."


	# with open("results.txt", "r") as f:
	# 	searchlines = f.readlines()
	# for line in enumerate(searchlines):
	# 	if args.search in line:
	# 		print args.search
	# 		print "The hash you searched for, %s, has been found" % args.search
