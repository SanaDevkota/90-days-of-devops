

# What is shell scripting for devops ?
    - in my own words, Shell scripting for devops means creating a scripting which helps devops to solve a repetative tasks and make their work easier.

# What is #!/bin/bash? can we write #!/bin/sh as well?
=> The line #!/bin/bash is called a shebang. It is used to specify the interpreter for the script. In this case, the interpreter is bash, the Bourne-Again SHell


# Write a Shell Script which prints I will complete #90DaysOofDevOps challenge
=>      `
#!/bin/bash
echo "I will complete #90DaysOfDevOps challenge"
`
To run the script, save it to a file with a .sh extension (e.g., 90days.sh) and make it executable by running the chmod command:
chmod +x 90days.sh
Then run the script: ./filename.sh


# Write a Shell Script to take user input, input from arguments and print the variables.
=> To private the input from user, we can use read command.
` #!/bin/bash  (shebang)
echo "Enter a name"
read first_name
echo "Your name is $first_name"
`



