#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import markdown2 as md
html = md.markdown_path('./test_markdown.md')

print(html)
