## git


### Git init repository

- 如何在本地创建一个folder和远程的github进行交互。
  
```shell
git init
# set origin URL
git remote add origin "**.git"
# check 
git remote -v
# push
git push --set-upstream origin master
```

-  how to solve master and remote main branch: nothing to merge problem

```shell
git branch main
git checkout main

# change to main
git branch --set-upstream-to=origin/main main 
# pull remote repo
git pull --allow-unrelated-histories

git push
```