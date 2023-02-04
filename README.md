# PythonUI - For Python 3.6
#### Developed by Gabriel Margarido - Feb 4th 2022

<img src="python.png" width="60%" height="60%">

## Import Python UI
- Download Python UI at releases page and move it to your project's folder.
- Add this line of code at the top of your main source-code file: `import pythonui`

## Input Boxes
### Create Password Input Box
`"Password"` is the title of the window, `"Password is needed"` is the message of the window.
```
mypassword = pythonui.PasswordInputBox("Password","Password is needed")
```

### Create Text Input Box
`"Info"` is the title of the window, `"Some message here"` is the message of the window.
```
mymessage = pythonui.TextInputBox("Info","Some message here")
```

## Dialog Boxes
### Create Message Dialog Box
`"Dialog"` is the title of the window, `Hello world!"` is the message of the window.
```
pythonui.MessageBox("Dialog","Hello world!")
```
### Create Warning Dialog Box
`"Warning"` is the title of the window, `"Hello world!"` is the message of the window.
```
pythonui.WarningBox("Warning","Hello world!")
```
### Create Error Dialog Box
`"Some error"` is the title of the window, `"Error has been happened"` is the message of the window.
```
pythonui.ErrorBox("Some error","Error has been happened")
```

## File Input Boxes
### Select folder from local SSD/HD
```
mylocation = pythonui.FolderWindow()
```

### Create File Input Box
`".txt"` is the default supported extension of files inside the window.
```
myfile = pythonui.FileWindow(".txt")
```

### Create Files Input Box
`".txt"` is the default supported extension of files inside the window.
```
myfiles = pythonui.FileWindows(".txt")
```


## Question Boxes
### Create Question Box
`"Confirm?"` is the title of the window, `"Are you sure?"` is the message of the window.
```
myquestion = pythonui.AskQuestionBox("Confirm?","Are you sure?")
```

### Create Ok-Cancel Question Box
`"Question"` is the title of the window, `"Are you sure to do this?"` is the message of the window.
```
myquestion = pythonui.AskOkCancelBox("Question","Are you sure to do this?")
```

### Create Retry Question Box
`"Retry?"` is the title of the window, `"Do you wish to retry?"` is the message of the window.
```
myretry = pythonui.AskRetry("Retry?","Do you wish to retry?")
```


## Yes-No Boxes
### Create Retry Question Box
`"Confirmation"` is the title of the window, `"Do you wush to confirm?"` is the message of the window.

*Returns*: `True` or `False`
```
myretry = pythonui.AskYesNoBox("Confirmation","Do you wish to confirm?")
```

### Create Retry Question Box
`"Confirmation"` is the title of the window, `"Do you wish to confirm?"` is the message of the window.

*Returns*: `True`, `False` or `None`

```
myretry = pythonui.AskYesNoCancelBox("Confirmation","Do you wish to confirm?")
```



## Execute Shell Commands as Sudo (Super user)
`123` is the superuser password, `sudo apt install sct -y` is the command we wish to run.
```
ExecuteSudoCommand("123","sudo apt install sct -y")
```

## Execute Shell Commands as default user (~/)
`sudo apt install sct -y` is the command we wish to run.
```
ExecuteCommand("sudo apt install sct -y")
```



###### Developed by Gabriel Margarido - Licensed under BSD 2-clause license (FreeBSD Project)
     
    
   
    