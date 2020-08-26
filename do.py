f = open('questions.md', 'r')
w = open('qs.md', 'a')
l = f.readline()
while l:
    w.write("- %s" % l)
    l = f.readline()
f.close()
w.close()