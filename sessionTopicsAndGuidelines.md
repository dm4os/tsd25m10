# Steps before start working on your projects

1. Make sure you open a git bush terminal or CMD window either separately or embedded on your IDE (e.g. Visual Studio Code).

2. Activate virtual environment(s) you need for running your applications
    -> Source <location of your virtual environment>/Scripts/activate  # On Windows
    -> Source <location of your virtual environment>/Bin/activate # On Linux
3. Pull repositories you are working on.
    case 1: You have SSH-config file then only -> git pull
    case 2: You DO NOT have SSH-config file then:
        a. Initialize the ssh-agent
            -> eval "$(ssh-agent -s)"
        b. "Tell the agent" where and which an SSH PRIVATE KEY is located
            -> ssh-add ~/.ssh/<name of your PRIVATE KEY> 