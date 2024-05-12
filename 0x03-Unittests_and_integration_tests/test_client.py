#!/usr/bin/env python3
'''Parameterize and patch as decorators'''


import unittest
from unittest.mock import Mock, PropertyMock, patch
from parameterized import parameterized

from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    '''unittest class for client file'''

    @parameterized.expand([('google',), ('abc',)])
    @patch("client.get_json")
    def test_org(self, org_name, mock_get_json):
        '''testing the "GithubOrgClient.org"'''

        github_client = GithubOrgClient(org_name)
        expected_argument = github_client.ORG_URL.format(org=org_name)

        github_client.org()

        mock_get_json.assert_called_once_with(expected_argument)

    def test_public_repos_url(self):
        '''testing "GithubOrgClient._public_repos_url"'''

        expected_url = "https://api.github.com/orgs/google/repos"

        with patch.object(
            GithubOrgClient,
            'org',
            new_callable=PropertyMock
        ) as mock_org:

            mock_org.return_value = {"repos_url": expected_url}

            git = GithubOrgClient('google')

            self.assertEqual(git._public_repos_url, expected_url)

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        '''testing "GithubOrgClient.public_repos"'''
        test_payload = {
            "repos_url": "https://api.github.com/orgs/google/repos",
            'repos': [
                {
                    "id": 7697149,
                    "node_id": "MDEwOlJlcG9zaXRvcnk3Njk3MTQ5",
                    "name": "episodes.dart",
                    "full_name": "google/episodes.dart",
                    "private": False, },
                {
                    "id": 7776515,
                    "node_id": "MDEwOlJlcG9zaXRvcnk3Nzc2NTE1",
                    "name": "cpp-netlib",
                    "full_name": "google/cpp-netlib",
                    "private": False, },
                {
                    "id": 7968417,
                    "node_id": "MDEwOlJlcG9zaXRvcnk3OTY4NDE3",
                    "name": "dagger",
                    "full_name": "google/dagger",
                    "private": False,
                }
            ]
        }
        mock_get_json.return_value = test_payload['repos']

        with patch.object(
            GithubOrgClient,
            '_public_repos_url',
            new_callable=PropertyMock,
        ) as mock_public_repos_url:

            mock_public_repos_url.return_value = test_payload['repos_url']

            git = GithubOrgClient('google')

            self.assertEqual(git.public_repos(), [
                             "episodes.dart", "cpp-netlib", "dagger",])

            mock_public_repos_url.assert_called_once()
        mock_get_json.assert_called_once()


if __name__ == '__main__':
    unittest.main()
