import re
import glob
import subprocess

import os

class Repository :
	CONFIG = 'config'
	GIT    = '.git'

	def __init__ (self, path) :
		self.path     = re.sub(self.GIT + '$', '', path)
		self.local    = None

	# :return return wraped path ('/home/user/Documents' to '~/Documents')
	def wrap_path (self) :
		r = '^{path}'.format(path=os.path.expanduser('~'))
		return re.sub(r, '~', self.path)

	# :return return the name of the repository (directory name)
	def name (self) :
		return os.path.basename(re.sub(os.path.sep + '$', '', self.path ))

	def branches ( self ) :
		cmd_response = subprocess.check_output(['git', "-C", self.path, "branch"])
		l = cmd_response.decode('utf-8').split('\n')
		branches = []
		for branch in l :
			branch_dict = {}

			if branch == '' :
				continue

			if branch[:2] == '* ' :
				branch_dict['curent'] = True
			else :
				branch_dict['curent'] = False

			branch = branch.strip('*')
			branch = branch.strip(' ')
			branch_dict['name'] = branch
			branches.append(branch_dict)

		if len(branches) == 0 :
			branches.append({
				'name':   'master',
				'curent': True
			})

		return branches


import time

class Gitup :
	
	def __init__ (self, path='~') :
		self.path = os.path.abspath(path)
		self.list_git = []

	def scan (self) :
		for file in glob.glob(os.path.join(self.path, os.path.join('**', '.git')), recursive=True):
			if os.path.isdir(file) and os.path.isfile(os.path.join(file, 'config')) :
				repo = Repository(file)
				self.list_git.append(repo)
				yield repo

	def find ( self, searched_repo ) :
		for repo in self.scan() :
			if repo.name() == searched_repo :
				yield repo

