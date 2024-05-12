#!/usr/bin/env python3
'''a main file'''


from client import GithubOrgClient


github = GithubOrgClient('google')

print(type(github.repos_payload))
