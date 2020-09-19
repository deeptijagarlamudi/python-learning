import git
import difflib
repo = git.Repo("C:\\Users\\user\\git\\spring-boot-properties-project-poc")
# repo.git.diff("development", "release")
print(repo.active_branch)
print(repo.remotes)
commit_master = repo.commit("master")
commit_release = repo.commit("origin//release")

diff_index = commit_master.diff(commit_release)
print(diff_index)
for diff_item in diff_index.iter_change_type('M'):
    for line in difflib.Differ().compare(diff_item.a_blob.data_stream.read().decode('utf-8'), diff_item.b_blob.data_stream.read().decode('utf-8')):
        print(line)
