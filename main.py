#!/usr/bin/env python
import os
import jinja2
import webapp2
import random


template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)


class BaseHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        return self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        return self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if params is None:
            params = {}
        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))


class MainHandler(BaseHandler):
    def get(self):
        return self.render_template("vnesi.html")

class LoginHandler(BaseHandler):
    def post(self):

        skrito_stevilo = random.randint(1,100)
        #skrito_stevilo = 42

        podatki = {"vneseno_st": int(self.request.get("vneseno-st")),
                   "skrito_st": skrito_stevilo} #get ime zato ker je v htmlju name="ime"
        return self.render_template("pokazi.html", podatki)

        #return self.write("Uspesen post request " + self.request.get("ime") +
         #                 "Tvoj priimek je: " + self.request.get("priimek"))

app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/rezultat', LoginHandler)

], debug=True)
