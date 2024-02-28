## HAL8001

Repository del progetto HAL8001, elaborato finale del corso di Artificial Intelligence, Università degli Studi di Milano - 2023/2024

---

### Breve how-to:

#### 1. ESECUZIONE PYTHON 3.7.0
Non è possibile eseguire ChatterBot con una versione superiore a Python 3.7.0. Per rispettare questa limitazione, su Windows,
è possibile ricorrere a *pyenc-win* (https://github.com/pyenv-win/pyenv-win):

1. Eseguire *PowerShell* e installare:
```
Invoke-WebRequest -UseBasicParsing -Uri "https://raw.githubusercontent.com/pyenv-win/pyenv-win/master/pyenv-win/install-pyenv-win.ps1" -OutFile "./install-pyenv-win.ps1"; &"./install-pyenv-win.ps1"
```
2. Chiudere e riaprire *PowerShell*
3. Copiare e incollare (questo passaggio installerà la versione 3.7.0 di python):
```
pyenv install 3.7.0
```
4. Copiare e incollare (questo passaggio setterà la versione 3.7.0 di python come versione globale di python):
```
pyenv global 3.7.0
```
Per ulteriori informazioni su pyenv-win si rimanda al repository ufficiale.

__

#### 2. AVVIO AMBIENTE VIRTUALE CHAT_ENV
Per eseguire il bot è necessario avviare l’ambiente virtuale CHAT_ENV che contiente preinstallate dipendenze e librerie.
1. Aprire la cartella contente la cartella CHAT_ENV nel prompt

- In caso di avvio tramite prompt copia e incollare:
```
CHAT_ENV\Scripts\activate.bat
```
- In caso di avvio tramite PowerShell copia e incollare:
```
CHAT_ENV\Scripts\Activate.ps1
```
2. Per disattivare e chiudere terminare l’ambiente virtuale copia e incollare:
deactivate
