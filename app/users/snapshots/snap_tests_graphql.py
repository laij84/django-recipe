# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['SnapshotTests::test_snapshot_users 1'] = {
    'data': {
        'users': [
            {
                'email': '111@test.com'
            }
        ]
    }
}