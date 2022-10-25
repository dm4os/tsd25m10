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


# Ex 3
## py lib/resources
    * https://www.w3schools.com/python/module_random.asp

### TODO from 13:08 to 14:08
Based on the function we have created you need to:
1. Create a function which only returns SPEEDS LIMITS not intervals
2. Create a 2nd function which takes that generated SPEED LIMIT and returns it.
    example-> def myfunc(theGenSpeedLimit):
                    return (theGenSpeedLimit)
3. print the returned value of the executed function on step 2
4. git add ****, git commit ***, git push your changes