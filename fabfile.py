from __future__ import print_function
from fabric.api import local, lcd
import os


def session(direc=os.path.dirname(__file__), bin_path='../webdev/bin'):
    with lcd(direc):
        local("tmux neww 'exec vim -i .viminfo'")
        local(r"""tmux split-window -v -l 8 \
                'ipython profile create {0}
                exec ipython3 --profile={0}'""".format('ProjectEuler'))
        local('tmux select-pane -t 0')

