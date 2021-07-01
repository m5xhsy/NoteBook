工作区 当前工作的地方

缓存区 git add 后的地方

版本库 git commit后的地方





```shell
$ git init
$ git status
$ git add manage.py
$ git add .

$ git config --global --edit
$ git config --global user.name
$ git commit -m "创建了文件"
$ git checkout x.html	# 丢弃工作区的改动

$ git log
$ git reset --hard 7e062d3291ff5f236107735166b86f1224f946be
$ git reflog
$ git reset --hard 7e062d3
$ git reset HEAD db.sqlite3 			# 清除缓冲区的内容(所有add的内容都清除,add后修改的内容不变)
$ git checkout -- templates/xsp.html	# 回到最后一次add状态,没有add状态就回到版本库状态(缓冲区(版本库)文件拉取到工作区)
$ git log -p master origin/master 		# 比较本地分支和远程分支的差异
$ git log --pretty=oneline
# 对比
$ git diff templates/index.html			# 工作区和缓存区对比
$ git diff --cached templates/index.html  # 缓存区和版本库组件对比




# 将当前开发内容放在某个地方
$ git stash 							# 保存 
$ git stash save "修改了xxx"		  	  # 保存是添加标记
$ git stash push -m "修改了xxx"	  	  # 和save一样，需要-m参数，--message的缩写,不能省略
$ git stash push -m "创建了f" f		  # 指定文件
$ git stash list						# 查看stash列表
$ git stash clear						# 清空stash列表
$ git stash pop stash@{0}				# 恢复并删除 不加参数恢复最后一次保存的
$ git stash drop stash@{0}				# 删除指定stash 不加参数删除最后一次保存的
$ git stash apply stash@{0}				# 恢复但是不删除 不加参数恢复最后一次保存的
$ git stash show stash{0}				# 显示仓库做了哪些改动 (就和diff一样)
$ git stash show stash{0} -p			# 显示仓库做了哪些具体改动
$ git stash branch kf					# 创建新的分支来保存
$ git stash create 						# 创建一个悬空提交，不会储存，返回一个字符串
$ git stash store -m "创建了xxx" -q xxx  # 保存悬空提交,-q后面参数为create返回的字符串




# 分支管理
$ git branch		# 查看分支
$ git branch dev	# 创建分支
$ git checkout dev 	# 切换分支
$ git checkout -b bug	# 将当前分支备份成bug分支
$ git merge bug		# 将bug分支合并到当前分支
```





```shell
用法：git checkout [<选项>] <分支>
  或：git checkout [<选项>] [<分支>] -- <文件>...

    -q, --quiet           不显示进度报告
    -b <分支>             创建并检出一个新的分支
    -B <分支>             创建/重置并检出一个分支
    -l                    为新的分支创建引用日志
    --detach              HEAD 从指定的提交分离
    -t, --track           为新的分支设置上游信息
    --orphan <新分支>     新的没有父提交的分支
    -2, --ours            对尚未合并的文件检出我们的版本
    -3, --theirs          对尚未合并的文件检出他们的版本
    -f, --force           强制检出（丢弃本地修改）
    -m, --merge           和新的分支执行三方合并
    --overwrite-ignore    更新忽略的文件（默认）
    --conflict <风格>     冲突输出风格（merge 或 diff3）
    -p, --patch           交互式挑选数据块
    --ignore-skip-worktree-bits
                          对路径不做稀疏检出的限制
    --ignore-other-worktrees
                          不检查指定的引用是否被其他工作区所占用
    --recurse-submodules[=<checkout>]
                          control recursive updating of submodules
    --progress            强制显示进度报告
```



```shell

通用选项
    -v, --verbose         显示哈希值和主题，若参数出现两次则显示上游分支
    -q, --quiet           不显示信息
    -t, --track           设置跟踪模式（参见 git-pull(1)）
    -u, --set-upstream-to <上游>
                          改变上游信息
    --unset-upstream      取消上游信息的设置
    --color[=<何时>]      使用彩色输出
    -r, --remotes         作用于远程跟踪分支
    --contains <提交>     只打印包含该提交的分支
    --no-contains <提交>  只打印不包含该提交的分支
    --abbrev[=<n>]        用 <n> 位数字显示 SHA-1 哈希值

具体的 git-branch 动作：
    -a, --all             列出远程跟踪及本地分支
    -d, --delete          删除完全合并的分支
    -D                    删除分支（即使没有合并）
    -m, --move            移动/重命名一个分支，以及它的引用日志
    -M                    移动/重命名一个分支，即使目标已存在
    -c, --copy            拷贝一个分支和它的引用日志
    -C                    拷贝一个分支，即使目标已存在
    --list                列出分支名
    -l, --create-reflog   创建分支的引用日志
    --edit-description    标记分支的描述
    -f, --force           强制创建、移动/重命名、删除
    --merged <提交>       只打印已经合并的分支
    --no-merged <提交>    只打印尚未合并的分支
    --column[=<风格>]     以列的方式显示分支
    --sort <key>          排序的字段名
    --points-at <对象>    只打印指向该对象的分支
    -i, --ignore-case     排序和过滤属于大小写不敏感
    --format <格式>       输出格式

```



```shell
$ git remote 												# 查看已经配置的远程仓库服务
$ git remote -v		# 显示需要读写远程仓库使用的Git保存的简写与对应的 URL。能非常方便地拉取其它用户的贡献,拥有向他们推送的权限
$ git remote add origin https://github.com/m5xhsy/test.git	# 添加一个新的远程Git仓库，可用用origin代替url
$ git remote show origin	
$ git fetch pb			# 拉取仓库有但是本地没有的信息

$ git fetch orgin master 	//将远程仓库的master分支下载到本地当前branch中
$ git merge origin/master 	//进行合并


$ git push -u origin master									# 
$ git clone https://github.com/m5xhsy/test.git				# 远程仓库克隆到本地
$ git clone https://github.com/m5xhsy/test.git mytest		# 远程仓库克隆到本地重命名
$ git push origin dev	


# 忽略文件上传
vim .gitignore
###
xxx.py
###




```





```shell
ssh-keygen -t rsa -b 4096 -C "m5xhsy@163.com"
```

