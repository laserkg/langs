

https://guides.github.com/activities/hello-world/
* [Switching remote URLs from SSH to HTTPS](https://help.github.com/articles/changing-a-remote-s-url/)
```
$ git remote -v
origin  git@github.com:USERNAME/REPOSITORY.git (fetch)
origin  git@github.com:USERNAME/REPOSITORY.git (push)


$ git remote set-url origin https://github.com/USERNAME/REPOSITORY.git

$ git remote -v
# Verify new remote URL
origin  https://github.com/USERNAME/REPOSITORY.git (fetch)
origin  https://github.com/USERNAME/REPOSITORY.git (push)
```

The next time you `git fetch`, `git pull`, or `git push` to the remote repository, you'll be asked for your GitHub username and password.
