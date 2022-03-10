from pathlib import Path


# Shows what files with *.py are in the project
path = Path()
for file in path.glob("*.py"):
    print(file)

print("\n=====================================\n")

# Shows all files in the projects
for file in path.glob("*"):
    print(file)
