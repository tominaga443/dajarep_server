import os
import subprocess
from bottle import route, request, run

@route("/")
def hellow_world():
#  return "Hellow World!"
  cmd = "echo 'hellow'"
  _, stdout, _ = __exec_command(cmd)
  return stdout

@route("/", method="POST")
def echo():
  text = __get_text(request)
  return text

@route("/dajarep", method="POST")
def run_dajarep():
  text = __get_text(request)
  cmd = "echo " + text + " | ./bin/dajarep/dajarep"
  _, stdout, _ = __exec_command(cmd)
  return stdout

def __get_text(request):
  text = request.forms.text
  return text

def __exec_command(cmd):
  p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
  stdout, stderr = p.communicate()
  return p.returncode, stdout, stderr

run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
