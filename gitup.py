#!/usr/bin/env python3
"""
  Usage:
		gitup.py scan [--directory=<dir> | -d <dir>] [no-color]
		gitup.py branch <repo> [--directory=<dir> | -d <dir>] [no-color]
		gitup.py branch [--directory=<dir> | -d <dir>] [no-color]
		gitup.py find <repo> [--directory=<dir> | -d <dir>] [no-color]
		gitup.py -h | --help | --version

	Arguments:
		<repo>                          d
		<dir>                           d

  Options:
		scan                            d
		branch [<repo>]                 d
		find <repo>                     d
		--directory=<dir>               d
		-d <dir>                        d

  Examples:
  	gitup.py scan
  	gitup.py branch "python/gitup"
  	gitup.py find gitup
"""

from gitup  import Gitup
from docopt import docopt
from color  import COLOR
import sys

if __name__ == '__main__':
	path = ''
	arguments = docopt(__doc__, version='0.1')
	color = True

	if arguments['--directory'] is not None :
		path = arguments['--directory']
	elif arguments['-d'] is not None :
		path = arguments['<dir>']

	if arguments['no-color'] :
		color = False

	try:
		g = Gitup(path)

		if arguments['scan'] :
			print('repositories:')
			for repo in g.scan() :
				print(' - {color}{name:16}{reset} ({path})'.format(
					color = COLOR['light cyan'] + COLOR['bold'] if color else '',
					reset = COLOR['reset'] if color else '',
					name  = repo.name(),
					path  = repo.wrap_path()
				))

		elif arguments['find'] :

			print('repositories for "{color}{repo}{reset}":'.format(
				repo=arguments['<repo>'],
					color = COLOR['dark gray'] + COLOR['bold'] if color else '',
					reset = COLOR['reset'] if color else '',
			))

			i = 0
			for repo in g.find(arguments['<repo>']) :
				print(' - {color}{path}{reset}'.format(
					color = COLOR['light cyan'] if color else '',
					reset = COLOR['default'] if color else '',
					name  = repo.name(),
					path  = repo.wrap_path()
				))
				i += 1

			if i == 0 :
				print('No repository found ...')


		elif arguments['branch'] :

			print('branches for "{color}{repo}{reset}":'.format(
				repo=arguments['<repo>'],
					color = COLOR['dark gray'] + COLOR['bold'] if color else '',
					reset = COLOR['reset'] if color else '',
			))

			i = 0
			for repo in (g.find(arguments['<repo>']) if arguments['<repo>'] is not None else g.scan() ) :
				print(' - {color}{path}{reset}'.format(
					color = COLOR['light cyan'] if color else '',
					reset = COLOR['default'] if color else '',
					name  = repo.name(),
					path  = repo.wrap_path()
				))

				for branch in repo.branches() :
					print('   |{cur_color}{curent}{cur_reset} {color}{branch_name}{reset}'.format(
						cur_color = COLOR['green']+COLOR['bold'] if color else '',
						cur_reset = COLOR['reset'] if color else '',
						curent = '>' if branch['curent'] else ' ',
						color = COLOR['cyan'] if color else '',
						reset = COLOR['default'] if color else '',	
						branch_name=branch['name']
					))
				i += 1

			if i == 0 :
				print('No branch found ...')


	except :
		print('\r\rexit command ... (you\'re very rude)')
