import git
import difflib
import re
repo = git.Repo("C:\\Users\\user\\git\\spring-boot-properties-project-poc")
# repo.git.diff("development", "release")
commit_master = repo.commit("master")
commit_release = repo.commit("origin//release")

diff_index = commit_master.diff(commit_release)
difftextAdded = ''
difftextRemoved= ''
for diff_item in diff_index.iter_change_type('M'):
    if "application-env.yml" in str(diff_item):
        for line in difflib.Differ().compare(diff_item.a_blob.data_stream.read().decode('utf-8'), diff_item.b_blob.data_stream.read().decode('utf-8')):
            if "+" in line:
                difftextAdded = difftextAdded + line
            elif "-" in line:
                difftextRemoved = difftextRemoved + line
finalText = (str(difftextAdded).replace('+', '').replace(' ', ''))
searchObj = re.findall(r'\{{([^}]+)\}}', finalText)

print("Properties need to be configured in dictionaries"+str(searchObj))
