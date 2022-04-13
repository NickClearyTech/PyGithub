############################ Copyrights and license ############################
#                                                                              #
# Copyright 2022 Alson van der Meulen <alson.vandermeulen@dearhealth.com>      #
#                                                                              #
# This file is part of PyGithub.                                               #
# http://pygithub.readthedocs.io/                                              #
#                                                                              #
# PyGithub is free software: you can redistribute it and/or modify it under    #
# the terms of the GNU Lesser General Public License as published by the Free  #
# Software Foundation, either version 3 of the License, or (at your option)    #
# any later version.                                                           #
#                                                                              #
# PyGithub is distributed in the hope that it will be useful, but WITHOUT ANY  #
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS    #
# FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more #
# details.                                                                     #
#                                                                              #
# You should have received a copy of the GNU Lesser General Public License     #
# along with PyGithub. If not, see <http://www.gnu.org/licenses/>.             #
#                                                                              #
################################################################################

import datetime

import github.NamedUser
import github.Team

from . import Framework


class Environment(Framework.TestCase):
    def setUp(self):
        self.tokenAuthMode = True
        super().setUp()
        self.repo = self.g.get_user().get_repo("PyGithub")
        self.environment = self.repo.get_environment("dev")

    def testAttributes(self):
        self.assertEqual(self.environment.name, "dev")
        self.assertEqual(self.environment.id, 464814513)
        self.assertEqual(self.environment.node_id, "EN_kwDOHKhL9c4btIGx")
        self.assertEqual(
            self.environment.url,
            "https://api.github.com/repos/alson/PyGithub/environments/dev",
        )
        self.assertEqual(
            self.environment.html_url,
            "https://github.com/alson/PyGithub/deployments/activity_log?environments_filter=dev",
        )
        self.assertEqual(
            self.environment.created_at, datetime.datetime(2022, 4, 13, 15, 6, 32)
        )
        self.assertEqual(
            self.environment.updated_at, datetime.datetime(2022, 4, 13, 15, 6, 32)
        )

    def testProtectionRules(self):
        protection_rules = self.environment.protection_rules
        self.assertEqual(len(protection_rules), 3)
        self.assertEqual(protection_rules[0].id, 216323)
        self.assertEqual(protection_rules[0].node_id, "GA_kwDOHKhL9c4AA00D")
        self.assertEqual(protection_rules[0].type, "branch_policy")
        self.assertEqual(protection_rules[1].id, 216324)
        self.assertEqual(protection_rules[1].node_id, "GA_kwDOHKhL9c4AA00E")
        self.assertEqual(protection_rules[1].type, "required_reviewers")
        self.assertEqual(protection_rules[2].id, 216325)
        self.assertEqual(protection_rules[2].node_id, "GA_kwDOHKhL9c4AA00F")
        self.assertEqual(protection_rules[2].type, "wait_timer")
        self.assertEqual(protection_rules[2].wait_timer, 15)

    def testReviewers(self):
        reviewers = self.repo.get_environment("dev").protection_rules[1].reviewers
        self.assertEqual(len(reviewers), 2)
        self.assertEqual(reviewers[0].type, "User")
        self.assertIsInstance(reviewers[0].reviewer, github.NamedUser.NamedUser)
        assert isinstance(
            reviewers[0].reviewer, github.NamedUser.NamedUser
        )  # Make type checker happy
        self.assertEqual(reviewers[0].reviewer.id, 19245)
        self.assertEqual(reviewers[0].reviewer.login, "alson")
        self.assertEqual(reviewers[0].reviewer.type, "User")
        self.assertEqual(reviewers[1].type, "Team")
        self.assertIsInstance(reviewers[1].reviewer, github.Team.Team)
        assert isinstance(
            reviewers[1].reviewer, github.Team.Team
        )  # Make type checker happy
        self.assertEqual(reviewers[1].reviewer.id, 1)
        self.assertEqual(reviewers[1].reviewer.slug, "justice-league")
        self.assertEqual(reviewers[1].reviewer.url, "https://api.github.com/teams/1")

    def testGetEnvironments(self):
        environments = self.repo.get_environments()
        self.assertEqual(environments.totalCount, 1)
        self.assertEqual(
            environments[0].url,
            "https://api.github.com/repos/alson/PyGithub/environments/dev",
        )
        self.assertEqual(environments[0].name, "dev")
