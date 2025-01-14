import sys
from jinja2 import Environment, FileSystemLoader, select_autoescape

print("\n*********** TASK: RENDERING **************")
print("Tekton Jinja Template processing")

# assumes both of these directories have been created
# and staged in previous task "staging" step
print("template and rendered directories")
assert len(sys.argv) > 2
tmpldir = sys.argv[1]
rndrdir = sys.argv[2]

print("getting filenames from urls")
assert len(sys.argv) > 3
j = 3
assert sys.argv[j] == "--urls"
j += 1
tfnames = []
while j < len(sys.argv):
    if sys.argv[j] == "--vars":
        break
    tn = ((sys.argv[j]).split("/"))[-1]
    tfnames.append(tn)
    j += 1

print("getting template variables")
j += 1
jjvs = []
while j < len(sys.argv):
    jjvs.append(sys.argv[j])
    j += 1

# this needs to be a list of var/val pairs
assert len(jjvs) % 2 == 0
j = 0
jjv = {}
while j < len(jjvs):
    jjv[jjvs[j]] = jjvs[j+1]
    j += 2

print("using jinja variables:")
print("======================")
for k, v in jjv.items():
    print("{k} = '{v}'".format(k=k, v=v))
print("======================")

print("initializing jinja environment ...")
print("template directory: {d}".format(d=tmpldir))
env = Environment( \
        loader = FileSystemLoader(tmpldir), \
        autoescape = select_autoescape(['html', 'xml']), \
        lstrip_blocks = False, \
        keep_trailing_newline = True \
    )

print("rendering templates...")
for tname in tfnames:
    print("loading {t}...".format(t=tname))
    tmpl = env.get_template(tname)
    print("rendering {t}...".format(t=tname))
    tren = tmpl.render(jjv)
    print("rendered result:")
    print("======================")
    print(tren)
    print("======================")
    rfname = rndrdir + '/' + tname
    print("writing result to file {fname}".format(fname=rfname))
    with open(rfname, "w") as rfile:
        rfile.write(tren)
