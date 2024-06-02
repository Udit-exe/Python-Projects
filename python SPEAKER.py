import os

print('''WELCOME to this TTS program
    -->If you are using macOs then you can directly continue
    -->If you are on windows then you have to install external modules''');

while True:
    inputText = input("Enter text you want system to pronounce:");
    txt = f"say{inputText}";
    if(inputText == 'n'):
        os.system("say 'Bye Bye'");
        break;
    os.system(txt);

#This project is made by "Udit Agrawal"
