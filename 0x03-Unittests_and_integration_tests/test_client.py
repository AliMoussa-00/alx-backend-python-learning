#!/usr/bin/env python3
'''Parameterize and patch as decorators'''


import unittest
from unittest.mock import Mock, PropertyMock, patch
from more_itertools import side_effect
from parameterized import parameterized, parameterized_class
import requests

from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


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

        mock_get_json.return_value = TEST_PAYLOAD[0][1]

        with patch.object(
            GithubOrgClient,
            '_public_repos_url',
            new_callable=PropertyMock,
        ) as mock_repo_url:

            mock_repo_url.return_value = TEST_PAYLOAD[0][0]['repos_url']

            git = GithubOrgClient('google')

            self.assertEqual(git.public_repos(), TEST_PAYLOAD[0][2])

            mock_repo_url.assert_called_once()
        mock_get_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        '''testing "GithubOrgClient.has_license"'''
        self.assertEqual(GithubOrgClient.has_license(
            repo, license_key), expected)


@parameterized_class([{
    'org_payload': TEST_PAYLOAD[0][0],
    'repos_payload': TEST_PAYLOAD[0][1],
    'expected_repos': TEST_PAYLOAD[0][2],
    'apache2_repos': TEST_PAYLOAD[0][3]
}])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    '''Integration test to test the interaction between multiple functions'''

    @classmethod
    def setUpClass(cls):
        '''setting up fixtures for testing'''
        routs_payload = {
            'https://api.github.com/orgs/google': cls.org_payload,
            'https://api.github.com/orgs/google/repos': cls.repos_payload
        }

        def mock_requests_get(url: str):
            if url in routs_payload:
                return Mock(**{'json.return_value': routs_payload[url]})
            return requests.HTTPError

        cls.get_patcher = patch('requests.get', side_effect=mock_requests_get)
        cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        '''stop the patcher'''
        cls.get_patcher.stop()

    def test_public_repos(self):
        '''integration test for GithubOrgClient.public_repos'''
        self.assertEqual(
            GithubOrgClient('google').public_repos(),
            self.expected_repos
        )

    def test_public_repos_with_license(self):
        '''
        integration test for GithubOrgClient.public_repos
        public_repos with the argument license="apache-2.0"
        '''
        self.assertEqual(
            GithubOrgClient('google').public_repos("apache-2.0"),
            self.apache2_repos
        )


if __name__ == '__main__':
    unittest.main()
