# -*- encoding: utf-8 -*-
##############################################################################
#
#    Odoo, Open Source Management Solution
#    This module copyright (C) 2010 Savoir-faire Linux
#    (<http://www.savoirfairelinux.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

import logging
import os
import simplejson
from werkzeug.wrappers import Response

from openerp import http

logger = logging.getLogger(__name__)


class GitlabCIController(http.Controller):
    CONTROLLER_PREFIX = '/gitlab_ci'

    @http.route(CONTROLLER_PREFIX, type="http", auth="public")
    def repo_view(self, ref=None):
        """Redirect to runbot page related to current repo"""
        logger.exception("Call to see repo with branch %s" % ref)

    @http.route(CONTROLLER_PREFIX + "/build", type="json", auth="public")
    def build(self, token=None):
        """Call to start build for regular push"""
        logger.info("build with token %s" % token)
        return {}

    @http.route(CONTROLLER_PREFIX + "/builds/<sha>/status.json", type="http", auth="public")
    def builds(self, sha, token=None):
        """Call on merge request open/close"""
        res = None
        try:
            logger.info("build with token %s" % token)
            logger.info("I want the status of commit %s" % sha)
            res = {
                'id': 6,
                'sha': sha,
                'status': 'pending',
            }
        finally:
            res = simplejson.dumps(res)
            return Response(res, mimetype='application/json')

    @http.route(CONTROLLER_PREFIX + "/status.png", type="http", auth="public")
    def status_badge(self, ref):
        logger.info("I want the status badge for branch %s" % ref)
        return open(os.path.join(os.path.dirname(__file__), '../status.png')).read()

    @http.route("/<namespace>/<repo>/services/gitlab_ci/edit", type="json", auth="public")
    def edit(self, namespace, repo):
        logger.exception("Edit for %s/%s" % (namespace, repo))

