# How To Contribute To This Repository

This document will be a step-by-step guide on how to contribute your content to this repository for the first time. There is some initial setup work that we will do here that you only need do once, but it will be noted as such. If you like to read, I would at this point say to have a look at the [About collaborative models](https://help.github.com/en/articles/about-collaborative-development-models) article. We are using the _fork and pull_ model of collaborative development.

Let's say you want to contribute an episode guide:

1. **Fork this repository!** The first point to start is with GitHub's own [Fork a repo](https://help.github.com/en/articles/fork-a-repo) documentation. Click that link. Click it! GitHub has excellent documentation so make sure to use it!

  A fork is your own copy of this repository, but it is related to this copy. For you, the original repository is considered to be and is called _upstream_. Once you have forked your copy of the repository on GitHub, you will want to have a local copy  of it to work on. You can add changes to your local copy, push them to your fork on GitHub, and when ready submit them to  _upstream_ in the form of a [Pull Request](https://help.github.com/en/articles/about-pull-requests).

  But we get ahead of ourselves. For now, just click the `Fork` button at the top right of screen. This only needs to be done once.

2. Install `Git` on your local computer. This is one of those steps you only need to do once, if you have not done it already, and installation is different dependant on your operating system.

  For Windows: Vist https://gitforwindows.org/ to download. Choose to use the OpenSSH tools instead of the Windows implementation, and you should be good to go.

  For Mac - https://git-scm.com/download/mac

3. **Clone the forked repository to make a local copy:**

  You will need a copy on your computer to work with. This is called [cloning](https://help.github.com/en/articles/cloning-a-repository). Theoretically, you only need to do this once :wink:

  You can also use a GUI programme, [GitHub Desktop](https://desktop.github.com/). However, I am going to focus on the command line as it is the easiest way to learn.

  Open the GitBash terminal in Windows, or the Terminal on a Mac or Linux and run the following:

  ```
  git clone https://github.com/[your-username]/xena-warrior-princess.git
  cd xena-warror-princess
  ls
  ```

  This will download your fork, change directory into the working directory and then list the files.

  Success?

  If you have issues cloning, please go back and read the [cloning a repository](https://help.github.com/en/articles/cloning-a-repository) link from earlier in this README.

  Once `Git` is installed and you are ready to work, it needs to know the committers email address and name. You can configure this globally (for all repositories), or [per repository](https://help.github.com/en/articles/setting-your-username-in-git#setting-your-git-username-for-a-single-repository). For now, we will just set our name and email for the `xena-warrior-princess` repository only.

  Open a GitBash or Terminal window, `cd` to the `xena-warrior-princess` directory and type:

  ```
  git config user.name "Your Name"
  ```

  and for the email:

  ```
  git config user.email "[your-username]@users.noreply.github.com"
  ```

  **If you wish to keep your email private**, please see the [About commit email addresses](https://help.github.com/en/articles/setting-your-commit-email-address#about-commit-email-addresses) article for information to help you enter the correct thing for you. Do not cut and paste the above!


4. Create your episode guide:

  How are you going to create your content? The content is required to be in the form of plain text [Markdown](https://help.github.com/en/articles/basic-writing-and-formatting-syntax) files. Any text editor can be used, and there are plenty of good and popular ones out there. My recommendation is to use [Atom](https://atom.io/), which is open source and maintained by GitHub. It has `Git` and GitHub support built-in. It has good Markdown preview support, is cross-platform, and is simple to use.

  Once you have installed and opened Atom, press `CTRL+SHIFT+A` or choose File -> Add Project Folder. Select the `xena-warrior-princess` directory that was created when you cloned your fork. You should now see the project directory and file listing on the left.

  To add your content to your local repository, simply create a new file with an `.md` extension. For instance, in Atom, there are several ways you could do this, but I would say right-click on the directory you wish to create a file in, and choose New File. Type in the filename (i.e. `A-Day-In-The-Life.md`) and a new empty file will be presented to you. Type away.

  If you want to add an image to your document, please **host the image somewhere else and link to it**. GitHub is not a file server. Personally I host images to my articles at [imgur.com](www.imgur.com). It's free, you can too.

  Coming soon will be templates for episode guides, character bios, etc. but in the meantime structure the content as you see fit. You may asked to change it in the future for uniformity.

5. **Commit** your episode guide to the repository:

  Once you are ready (are you sure?) to submit your content to the _upstream_ repository, the first step is to commit the changes to your local repository. Open GitBash or a Terminal, and navigate to the working directory:

  ```
  git add "xena-warrior-princess/Episodes/Season 2/A-Day-In-The_Life.md"
  ```

  This command adds the file to the _staging area_. This is an important concept in `Git`. You can always unstage a file if you would like to make further changes. You can check the staging area with the `git status` command. If you want to now commit that file to the repository:

  ```
  git commit -m "Add episode guide A-Day-In-The-Life.md"
  ```

  The `-m` is to specify the commit message. [Commit messages are very important](https://chris.beams.io/posts/git-commit/). Basically they should be succinct, and describe what you did, i.e. "Add file.md" or, "Change 'About Us' section".

  And with that, all files and outstanding changes in the staging area are committed to the local repository. Now you should push your changes to the remote fork.

6. Pushing local changes to the remote fork:

  See the article [Pushing Commits to a remote repository](https://help.github.com/en/articles/pushing-commits-to-a-remote-repository).

  Use `git push` to push commits made on your local branch to your remote repository on GitHub.

  The git push command takes two arguments:

    - A remote name, for example, `origin` <-- this is your fork
    - A branch name, for example, `master` <-- this is the default branch

  For example:

  ```
  git push  <REMOTENAME> <BRANCHNAME>
  ```

 As an example, you usually run `git push origin master` to push your local changes to your online repository's default branch.

 If you are wondering what I mean by "branch", please see the [About branches](https://help.github.com/en/articles/about-branches) documentation for further reading. Branches provide a simple way to isolate your work-in-progress without affecting other branches in the repository.


7. Configuring a "remote" for your fork:

  Before you can sync changes from the _upstream_ repository into your local copy (and then push them to your GitHub fork, thereby syncing the repositories), you need to tell your local `Git` which repository is considered _upstream_. **This only needs to be done once**. See the [Configuring a remote for a fork](https://help.github.com/en/articles/configuring-a-remote-for-a-fork) documentation for more information.

  Open GitBash or a Terminal, and type the following in the working directory to list your currently configured remotes:

  ```
  git remote -v

  origin  https://github.com/YOUR_USERNAME/xena-warrior-princess.git (fetch)
  origin  https://github.com/YOUR_USERNAME/xena-warrior-princess.git (push)
  ```

  Now specify a new remote upstream repository that will be synced with your fork:

  ```
  git remote add upstream https://github.com/judelucien/xena-warrior-princess.git
  ```

  Now you have specified the _upstream_ repository, you can sync your fork on GitHub with your local repository _and_ fetch changes from _upstream_ to keep up-to-date.

8. Sync a fork of a repository to keep it up-to-date with the upstream repository.

  Syncing with upstream is a small process you should read about in the [Syncing a fork](https://help.github.com/en/articles/syncing-a-fork) documentation.

  I will outline the steps here but please read the doc - it's short!

- Open GitBash or a Terminal.
- Change the current working directory to your local project.

  ```
  git fetch upstream
  git checkout master
  git merge upstream/master
  ```

  Syncing your fork only updates your local copy of the repository. To update your fork on GitHub, you must push your changes:

  ```
  git push origin master
  ```

  And with that, you have up-to-date repositories, both locally and your fork on GitHub. But really. Read that doc! Read them all!!

9. Submitting a Pull Request to have your changes added to Upstream.

  When you are ready to have your content reviewed for inclusion, submit a [Pull Request](https://help.github.com/en/articles/about-pull-requests). The articles [Creating a Pull Request](https://help.github.com/en/articles/creating-a-pull-request) and [Creating a Pull Request from a fork](https://help.github.com/en/articles/creating-a-pull-request-from-a-fork) give step-by-step instructions.

  For now, PLEASE SUBMIT PULL REQUESTS AGAINST THE `draft` BRANCH, and not `master`.

There is probably a lot of stuff I have forgot in this README - if so, please file an [Issue](https://github.com/judelucien/xena-warrior-princess/issues) if you find incomplete or incorrect instructions, or something just plain wrong, or you have an idea to make something clearer.
