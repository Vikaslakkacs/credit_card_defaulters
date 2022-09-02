#with open("requirements.txt","r") as requirement:
#    print(requirement.readlines().remove("-e ."))

with open("requirements.txt") as requirements_file:
    x= requirements_file.readlines()
    print(x)
    print("-e ."  in x)