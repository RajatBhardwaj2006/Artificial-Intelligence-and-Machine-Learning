# GitHub Command Reference

A concise reference for commonly used Git and GitHub commands, workflows, and troubleshooting tips. This folder contains text-based command sheets and a PDF cheat sheet for quick revision while working on projects.

## Files in This Folder

- **`Commands_sheet.txt`** — Git command reference sheet.
- **`GitCommands.txt`** — Additional Git commands and examples.
- **`git-cheat-sheet-education.pdf`** — PDF cheat sheet for reviewing Git commands.

## Getting Started

### 1. Check Git Installation

```bash
git --version
```

### 2. Configure Your Identity

Set the name and email that Git records in your commits:

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

Check your configuration:

```bash
git config --global --list
```

## Everyday Git Workflow

Run these commands from inside your project directory:

```bash
git status
git add .
git commit -m "Describe your changes"
git push
```

- `git status` shows changed and untracked files.
- `git add .` stages changes in the current directory.
- `git commit` saves a snapshot in your local repository.
- `git push` uploads local commits to the configured remote repository.

To download and integrate remote changes, use:

```bash
git pull
```

## Useful Commands

| Command | Purpose |
|---|---|
| `git init` | Initialize a Git repository |
| `git clone <repository-url>` | Copy a remote repository locally |
| `git status` | Show repository status |
| `git add <file>` | Stage a specific file |
| `git add .` | Stage changes in the current directory |
| `git commit -m "message"` | Create a commit |
| `git log --oneline` | View compact commit history |
| `git diff` | Inspect unstaged changes |
| `git branch` | List local branches |
| `git switch <branch>` | Switch branches |
| `git switch -c <branch>` | Create and switch to a branch |
| `git merge <branch>` | Merge a branch into the current branch |
| `git remote -v` | List configured remotes |
| `git fetch` | Download remote updates without integrating them |
| `git pull` | Fetch and integrate remote changes |
| `git push` | Upload commits to a remote |
| `git stash` | Temporarily store uncommitted changes |
| `git restore <file>` | Discard unstaged changes to a file |
| `git rm <file>` | Remove a tracked file |
| `git rm --cached <file>` | Stop tracking a file while keeping it locally |

## Connect a Local Project to GitHub

If your project is not already connected to a remote repository:

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin <repository-url>
git push -u origin main
```

Replace `<repository-url>` with your GitHub repository URL. If the repository already has a remote configured, check it with `git remote -v` before adding another.

## Branching Workflow

Use a separate branch to work on a feature:

```bash
git switch -c feature/my-feature
# Make changes, then:
git add .
git commit -m "Add my feature"
git push -u origin feature/my-feature
```

Create a pull request on GitHub when you are ready to propose merging the branch.

## Undoing Changes Carefully

- **Unstage a file:** `git restore --staged <file>`
- **Discard unstaged edits:** `git restore <file>` — this permanently discards those edits.
- **Amend the latest commit:** `git commit --amend`
- **Revert a commit safely:** `git revert <commit-hash>` — creates a new commit that reverses the selected commit.

Be careful with `git reset --hard` and force-push commands: they can permanently discard work or rewrite shared history.

## Troubleshooting

- **Authentication or permission errors:** Confirm that you are signed in to the correct GitHub account and have repository access.
- **Push rejected:** Run `git status` and `git pull` first. Resolve any merge conflicts before pushing again.
- **Wrong remote:** Check `git remote -v`; update it with `git remote set-url origin <repository-url>` if needed.
- **Merge conflicts:** Open the conflicted files, resolve the conflict markers, then stage and commit the resolved files.

## Notes

- Git is the version-control tool; GitHub hosts Git repositories and provides collaboration features.
- Commands should be run in a terminal opened at the relevant repository directory.
- Replace placeholders such as `<file>`, `<branch>`, `<commit-hash>`, and `<repository-url>` with your actual values.

---

**Purpose:** Keep essential Git commands and common workflows in one place for quick reference and revision.
