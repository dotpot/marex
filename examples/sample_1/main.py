#!/usr/bin/python
# -*- coding: utf-8 -*-
import webapp2

config = {}
routes = []

app = webapp2.WSGIApplication(routes=routes, config=config, debug=False)
