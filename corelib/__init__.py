#!/usr/bin/env python
#-*- coding: utf-8 -*-
from web.contrib.template import render_mako

render = render_mako(
        directories=['templates'],
        input_encoding='utf-8',
        output_encoding='utf-8',
        )
