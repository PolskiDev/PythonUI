import pythonui

a = pythonui.AskYesNoCancelBox("d","Hello world")
print(a)

senha = pythonui.PasswordInputBox("Senha","Digite a senha")
pythonui.MessageBox("Aviso",senha)

folder = pythonui.FolderWindow()
pythonui.MessageBox("Aviso",folder)

