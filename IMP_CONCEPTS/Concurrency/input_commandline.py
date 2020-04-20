'''import subprocess

command = ['ls', '-l']
p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.IGNORE)
text = p.stdout.read()
retcode = p.wait()'''

import sys
import trace

# create a Trace object, telling it what to ignore, and whether to
# do tracing or line-counting or both.
tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=0,
    count=1)

# run the new command using the given tracer
tracer.run('main()')

# make a report, placing output in the current directory
r = tracer.results()
r.write_results(show_missing=True, coverdir=".")