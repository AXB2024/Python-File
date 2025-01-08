# Git Cheat Sheet

## Tip 1: Clone a Remote Repository
git clone https://github.com/AXB2024/Python-File.git

touch ReadMe.md
git add .
git commit -m "Commited Message"
git status
git push 

## Tip 2: create a new repository on the command line
echo "# DemoApp" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/AXB2024/DemoApp.git
git push -u origin main