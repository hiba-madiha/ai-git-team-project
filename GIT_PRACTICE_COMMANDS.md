# Git Practice Commands

## 1. New project start

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
```

## 2. GitHub remote add

```bash
git remote add origin https://github.com/YOUR_USERNAME/ai-git-team-project.git
git push -u origin main
```

## 3. New branch

```bash
git checkout -b feature/my-feature
```

## 4. Commit changes

```bash
git status
git add .
git commit -m "Add my feature"
```

## 5. Push branch

```bash
git push -u origin feature/my-feature
```

## 6. Merge branch into main

```bash
git checkout main
git pull origin main
git merge feature/my-feature
git push origin main
```

## 7. Pull colleague branch

```bash
git fetch origin
git checkout -b feature/colleague-work origin/feature/colleague-work
```

## 8. Rebase your branch with latest main

```bash
git checkout feature/my-feature
git fetch origin
git rebase origin/main
```

## 9. Abort merge if mistake

```bash
git merge --abort
```

## 10. Abort rebase if mistake

```bash
git rebase --abort
```

## 11. Delete local branch

```bash
git branch -d feature/my-feature
```

## 12. Delete remote branch

```bash
git push origin --delete feature/my-feature
```
