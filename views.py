from flask import Blueprint 

@views.route("/"):
def home():
  return "homepage"