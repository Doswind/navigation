#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import json
import threading

from ansible_collections.google.cloud.plugins.modules.gcp_iam_role import self_link


class Navi:
    """

    """

    def __init__(self):
        self.lock = threading.Lock()
        self.jsonfile = os.path.join(os.path.dirname(__file__), "link.json")

    def load(self):
        jsonstr = None
        with self.lock:
            with open(self.jsonfile, encoding='utf-8') as f:
                jsonstr = json.loads(f.read())
        linkgroup = {}
        for grp in jsonstr:
            link = []
            for name, value in grp['link'].items():
                highlight = 'no'
                twinkle = 'no'
                if name in grp['highlight']:
                    highlight = 'yes'
                if name in grp['twinkle']:
                    twinkle = 'yes'
                link.append([name, value, highlight, twinkle])
            linkgroup[grp['group']] = link
        return linkgroup

    def save(self,jsonstr):
        with self.lock:
            with open(self.jsonfile, "w", encoding='utf8') as f:
                json.dump(jsonstr, f, indent=4, ensure_ascii=False)

    def print(self, jsonstr):
        print(jsonstr)

if __name__ == '__main__':
    o = Navi()
    p = o.load()
    print(p)
