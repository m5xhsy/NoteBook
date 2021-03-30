# Vim打造成Python IDE

## 1.安装vim

```shell
sudo add-apt-repository ppa:jonathonf/vim
sudo apt-get update
sudo apt install vim
```

## 2.**安装vundle**

```shell
git clone https://github.com/gmarik/vundle.git /etc/vim/bundle/vundle
```

## 3.添加vundle支持

```shell
filetype off
set rtp+=/etc/vim/bundle/vundle/
call vundle#rc()

if filereadable(expand("/etc/.vimrc.bundles"))
  source /etc/.vimrc.bundles
endif
```

## 4.通过/etc/.vimrc.bundles管理我们安装的插件

```shell
if &compatible
    set nocompatible
end

filetype off
set rtp+=/etc/vim/bundle/vundle/
call vundle#rc()

" Let Vundle manage Vundle
Bundle 'gmarik/vundle'

" Define bundles via Github repos
" 标签导航
Bundle 'majutsushi/tagbar'
Bundle 'vim-scripts/ctags.vim'
" 静态代码分析
Bundle 'vim-syntastic/syntastic'
" 文件搜索
Bundle 'kien/ctrlp.vim'
" 目录树导航
Bundle "scrooloose/nerdtree"
" 美化状态栏
Bundle "Lokaltog/vim-powerline"
" 主题风格
Bundle "altercation/vim-colors-solarized"
" python自动补全
Bundle 'davidhalter/jedi-vim'
Bundle "klen/python-mode"
" 括号匹配高亮
Bundle 'kien/rainbow_parentheses.vim'
" 可视化缩进
Bundle 'nathanaelkane/vim-indent-guides'
if filereadable(expand("/etc/vim/.vimrc.bundles.local"))
    source /etc/vim/.vimrc.bundles.local
endif

filetype on
```





![img](https://gitee.com/m5xhsy/picture-bed/raw/master/images/C%5D5OUOX_G~ZP7JQEN%60QX7T7.png)