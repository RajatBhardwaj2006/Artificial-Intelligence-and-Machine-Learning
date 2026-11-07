# Git & GitHub Command Guide and Reference

A practical, field-tested handbook and reference for mastering **Git version control** and **GitHub collaboration workflows**. This directory contains quick-reference cheat sheets, common troubleshooting scenarios, and step-by-step terminal instructions.

---

## 📌 Overview

Whether starting a brand-new project, pushing commits from VS Code, collaborating with branches, or resolving merge conflicts, this directory provides immediate reference material for everyday version-control workflows.

---

## 📁 Files in This Directory

| File | Type | Description |
|---|---|---|
| [`Commands_sheet.txt`](Commands_sheet.txt) | Plaintext Guide | Quick copy-paste snippet cheat sheet for initial repo setup and standard daily push workflows. |
| [`GitCommands.txt`](GitCommands.txt) | In-depth Guide | Comprehensive walkthrough covering terminal navigation in VS Code, git initialization, remote linkage, branching, and troubleshooting frequent beginner errors. |
| [`git-cheat-sheet-education.pdf`](git-cheat-sheet-education.pdf) | Official Cheatsheet | GitHub Education's official two-page visual Git cheat sheet covering commands, options, and terminology. |

---

## 🚀 Everyday Git Workflow

```text
Working Directory  ──(git add)──>  Staging Area  ──(git commit)──>  Local Repo  ──(git push)──>  Remote (GitHub)
```

Run these commands inside your project root:

```bash
# 1. Check current status
git status

# 2. Stage changes (all files or specific file)
git add .
# or: git add <file-name>

# 3. Create a descriptive commit
git commit -m "feat: Add new module or feature"

# 4. Push changes to GitHub
git push origin main
```

To fetch and integrate remote changes made by teammates or via GitHub's web editor:
```bash
git pull origin main
```

---

## 🛠️ Complete Command Reference

### Repository Setup & Identity Configuration
```bash
# Configure global author identity
git config --global user.name "Your Name"
git config --global user.email "you@example.com"

# Check active configuration
git config --list

# Initialize a new repository
git init

# Clone an existing remote repository
git clone https://github.com/username/repository.git
```

### Staging, Inspecting & Committing
| Command | Action |
|---|---|
| `git status` | Displays staged, modified, and untracked files |
| `git diff` | Shows unstaged line-by-line differences |
| `git diff --staged` | Shows differences between staged files and the last commit |
| `git add <file>` | Stages a specific file |
| `git add .` | Stages all modified and new files in the current folder |
| `git commit -m "msg"` | Records staged snapshot with a descriptive message |
| `git commit --amend` | Modifies the most recent commit (e.g. typo fix) |
| `git log --oneline` | Displays compact, one-line commit history |

### Branching & Merging
```bash
# List local branches
git branch

# Create and switch to a new feature branch
git switch -c feature/new-pipeline
# (Alternatively: git checkout -b feature/new-pipeline)

# Switch back to main branch
git switch main

# Merge feature branch into current branch
git merge feature/new-pipeline

# Delete feature branch after merge
git branch -d feature/new-pipeline
```

### Remote Repository Management
```bash
# Verify remote repository URLs
git remote -v

# Link local repository to GitHub remote
git remote add origin https://github.com/username/repository.git

# Set upstream tracking and push main branch
git branch -M main
git push -u origin main

# Update remote URL if repository renamed or relocated
git remote set-url origin https://github.com/username/new-repo.git
```

---

## ⚠️ Common Issues & Troubleshooting

| Issue / Error | Cause | Resolution |
|---|---|---|
| `fatal: not a git repository` | Ran command outside a initialized git directory | Run `git init` or `cd` into the directory containing `.git`. |
| `Updates were rejected because remote contains work` | Remote has commits not present locally | Run `git pull origin <branch>` to merge remote changes first, resolve conflicts if any, then push. |
| `fatal: remote origin already exists` | Remote named `origin` already defined | Verify with `git remote -v`, or update using `git remote set-url origin <url>`. |
| Merge Conflict markers (`<<<<<<< HEAD`) | Overlapping edits in the same file lines | Open the file, keep the desired code block, remove conflict markers, then `git add <file>` and `git commit`. |
| Accidentally staged unwanted files | Staged sensitive or large files | Run `git restore --staged <file>` to unstage without losing your local modifications. |
