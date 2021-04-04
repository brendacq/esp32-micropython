# ESP32 com MicroPython - Primeiros Passos

## Configuração

Caso seja a primeira vez usando o ESP32 com MicroPython, é necessário atualizar o firmware da placa.

**OBS**: É necessário ter Python instalado no computador.

### 1. Baixar firmware

O 1º passo é baixar o firmware do MicroPython, diretamente no [site oficial](https://micropython.org/download/). 

[![mpython-download.gif](https://s4.gifyu.com/images/mpython-download.gif)](https://gifyu.com/image/YgNz)

Recomenda-se baixara versão estável mais recente.

### 2. Instalar esptool

Usaremos a ferramenta esptool pra atualizar a memória flash do ESP32.

```bash
# Instalar usando o gerenciador de pacotes pip
$ pip3 install esptool
```

*Em caso de erro, é possível instalar o esptool com o comando `apt`.

### 3. Apagar a memória flash

É recomendado apagar toda a memória flash antes de gravar o firmware do MicroPython. Vamos fazer isso usando o programa `esptool.py`

```bash
$ esptool.py --port /dev/ttyUSB0 erase_flash
```

### 4. Deploy do Firmware

Finalmente, vamos gravar o firmware do MicroPython na memória flash da placa.
Confira o nome do arquivo `.bin`.

```bash
$ esptool.py --chip esp32 --port /dev/ttyUSB0 --baud 460800 write_flash -z 0x1000 esp32-date-version.bin
```

*Em caso de erros, diminua a taxa baud para 115200.

### Extra: Extensão VSCode

Meu editor de texto padrão é o [Visual Studio Code](https://code.visualstudio.com/). Por conveniência, utilizo a extensão [PyMakr](https://docs.pycom.io/gettingstarted/software/vscode/) pra facilitar a comunicação, programação e compilação da placa.

## Primeiro programa: Blink

Só para organização, vamos criar uma pasta para armazenar nosso primeiro programa em MicroPython. Dentro dessa pasta, criaremos dois arquivos chamados `boot.py` e `main.py`.

```sh
# Criar diretório
$ mkdir led_embutido

# Entrar na pasta
$ cd led_embutido

# Criar arquivos boot e main
$ touch boot.py main.py
```

### Piscar led embutido

No pino (ou GPIO) 2, é possível acessar um led embutido na placa - *equivalente ao led da porta 13, no Arduino*. Neste programa, vamos aprender fazer esse led piscar com intervalo de meio segundo.

No arquivo `main.py`, escrevemos:

```py
from machine import Pin
from time import sleep

# Atribuir a uma variável o GPIO2 como pino de saída
led = Pin(2, Pin.OUT)

# Atribuir ao led o estado contrário ao seu estado atual (se ligado, desliga, e vice-versa)
led.value(not led.value())

# Criar um delay de meio segundo
sleep(0.5)
```
