#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import json
import threading

class Navi:
    """

    """

    def __init__(self):
        self.lock = threading.Lock()
        self.jsonfile = os.path.join(os.path.dirname(__file__), "link.json")

    def load(self):
        with self.lock:
            with open(self.jsonfile, encoding='utf-8') as f:
                return json.loads(f.read())

    def save(self,jsonstr):
        with self.lock:
            with open(self.jsonfile, "w", encoding='utf8') as f:
                json.dump(jsonstr, f, indent=4, ensure_ascii=False)

    def tbody(self):
        link = self.load()

        html = '\t\t<tbody>'
        for group in link:
            grp_name = group['group']
            link_hl = group['highlight']
            html = html + '''
            <tr class ="success" >
                <td class ='tr-field' >&#9827;&#9827;  %s </td>
                <td> </td> <td> </td> <td> </td>
            </tr>\n'''%grp_name

            pairs = list(group['link'].items())
            idx = 0
            while idx < len(pairs):
                link_name = pairs[idx][0]
                link_addr = pairs[idx][1]
                if link_name in group['highlight']:
                    link_str = '''\t\t\t\t<td><a class='tr-notice' href="%s" target="_blank">%s</a></td>\n''' % (link_addr, link_name)
                elif link_name in group['twinkle']:
                    link_str = '''\t\t\t\t<td><a class='tr-notice' href="%s" target="_blank"><div class="blink">%s</div></a></td>\n''' %(link_addr, link_name)
                else:
                    link_str = '''\t\t\t\t<td><a href="%s" target="_blank">%s</a></td>\n''' % (link_addr, link_name)

                if idx % 4 == 0:
                    html = html + '\t\t\t<tr>\n'
                    html = html + link_str
                elif idx % 4 == 3:
                    html = html + link_str
                    html = html + '\t\t\t</tr>\n'
                else:
                    html = html + link_str

                if idx + 1 == len(pairs) and idx % 4 < 3:
                    for i in range(3 - idx%4):
                        html = html + '''\t\t\t\t<td><a href=""></a>\n'''
                    html = html + "\t\t\t</tr>\n"

                idx = idx + 1

        html = html + '\t\t</tbody>'
        return html

    def generate(self, demo, html_file):
        html = ""
        with open(demo, encoding='utf-8') as f:
            for line in f.readlines():
                #print(line.rstrip())
                if line.startswith('<CODE_BLOCK_TBODY/>'):
                    html = html + self.tbody()
                else:
                    html = html + line
        with open(html_file, 'w', encoding='utf-8') as out_f:
            out_f.write(html)
        return html

    def print(self, jsonstr):
        print(jsonstr)

if __name__ == '__main__':
    o = Navi()
    p = o.load()
    out = o.generate('demo.html', 'hao456.html')
    print(out)
