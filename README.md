# 🚀 Eu nunca vi um cientista 🚀

## Projeto QR Code para Controle de Presença

Criação de um sistema para Controle de presença, visando a segurança de alunos e funcionários da escola

<br>

**licença e tecnologias utilizadas**:  
<img src="https://img.shields.io/github/license/henrygoncalvess/QRcode-contra-turno?style=for-the-badge&labelColor=gray&color=97ca00"> <a href="https://docs.python.org/3/"><img src="https://img.shields.io/badge/python-3.11.9-3776AB?style=for-the-badge&logo=python&logoColor=3776AB&labelColor=gray"></a> <a href="https://docs.npmjs.com"><img src="https://img.shields.io/badge/npm-11.0.0-CB3837?style=for-the-badge&logo=npm&logoColor=CB3837&labelColor=gray"></a> <a href="https://nodejs.org/pt"><img src="https://img.shields.io/badge/node-22.12.0-5FA04E?style=for-the-badge&logo=node.js&logoColor=5FA04E&labelColor=gray"></a> <a href="https://fastify.dev/docs/latest/Guides/Getting-Started/"><img src="https://img.shields.io/badge/fastify-5.3.2-000000?style=for-the-badge&logo=fastify&logoColor=000000&labelColor=gray"></a>

<br>

<details open="open">
<summary>Tabela de Conteúdos</summary>
  
- [💡 Ideia Inicial](#ideia)
  - [Utilização do `ESP32` para **IOT**](#esp32)
  - [Exemplo de uso com Fluxo básico](#fluxo)
- [🛠 Recursos Gerais](#recursos)
- [⚙ Geração de QR code com Python](#qrcode)
- [⚙ Configuração da API Google Sheets](#configSheetsApi)
- [⚙ Instalação do Node.js e NPM](#install)
  - [Configuração do Servidor](#npm)
  - [Execução do Servidor](#nodeServer)
- [📄 Referências](#ref)
  
</details>

<br>

<a name="ideia"></a>

## 💡 Ideia Inicial
<a name="esp32"></a>
### Utilização do `ESP32` para **IOT** (rede de dispositivos físicos que são conectados à internet e podem coletar e compartilhar dados)

![exemplo com ESP32](images/ESP32_iot.png)

### Utilização do `ESP32 Cam` para escaneamento de QR Code

![exemplo com ESP32](images/ESP32CAM_code.png)

O microcontrolador `ESP32` é amplamente utilizado para a criação de Web Servers embarcados (servidor web que está integrado em um dispositivo, como um microcontrolador, permitindo que ele ofereça serviços web, como páginas HTML, sem a necessidade de um servidor web separado), graças ao seu poder de processamento, conectividade Wi-Fi e suporte a protocolos modernos. Abaixo estão as principais características, benefícios e funcionamento nesse contexto:

- Baixo Custo e Alto Desempenho  
Comparado a soluções como Raspberry Pi, o ESP32 é mais barato e consome menos energia, sendo ideal para **IoT** (rede de dispositivos físicos que são conectados à internet e podem coletar e compartilhar dados).

- Suporte a Protocolos Web Modernos  
HTTP/HTTPS, WebSocket, MQTT (para comunicação em tempo real).

- Multitarefa  
Pode rodar um servidor web enquanto executa outras tarefas em paralelo (Leitura a partir de sensores, por exemplo).

- Fácil Integração com Sensores e Atuadores  
Pode ler sensores (DHT11, LM35, etc.) e controlar dispositivos (relés, LEDs, motores) via interface web.

<a name="fluxo"></a>
#### Exemplo de uso com Fluxo básico

![fluxo básico com imagem](images/fluxo_code.png)

Implementação de Banco de Dados (futuro)

<br>

<a name="recursos"></a>
### 🛠 Recursos Gerais

- [ ] 2x - ESP32 Cam
- [ ] 2x - ESP32 Module
- [x] Arduino UNO
- [ ] **opcional:** ESP32-CAM-MB
- [x] Jumpers Elétricos
- [x] LEDs
- [x] Resistores

<br>

<a name="qrcode"></a>
### ⚙ Geração de QR code com Python

> [!NOTE]
> Documentação da biblioteca `qrcode` → [Clique aqui](https://pypi.org/project/qrcode/)

Instalação das bibliotecas qrcode e Pillow:
```bash
pip install qrcode[pil]
```

Código → [CLIQUE AQUI](qr-code.py) para acessar

`Exemplo de resultado`

![exemplo de QR Code com logo do Batista Renzi](images/batista-code.png)

<br>

<a name="configSheetsApi"></a>
### ⚙ Configuração da API Google Sheets

- Escolher um Modelo de Planilha, copiar o `Sheet Id` da url e enviar um email para a conta de serviço autorizando acesso a planilha

- Criar uma conta de serviço em [Google Cloud](https://console.cloud.google.com/welcome) e configurar a API → ver [Referências](#ref)

<img src="https://cdn.simpleicons.org/googlesheets/34A853/34A853" width=24>&nbsp; [Exemplo de Lista de Presença](docs/modelo-lista-presenca.xlsx) (arquivo excel)

<br>

<a name="install"></a>
### ⚙ Instalação do Node.js e NPM

Página oficial de Download do [Node.js](https://nodejs.org/pt)  
_NPM é o gerenciador de pacotes padrão do Node.js. É instalado automaticamente junto com o Node_

<a name="npm"></a>
#### Configuração do Servidor

1. Inicialize o projeto Node.js

`node/server`
``` bash
npm init
```

2. Adicione o seguinte código ao package.json:

`node/server/package.json`
``` json
"scripts": {
  "dev": "node --watch --env-file=.env server.js",
  "start": "node --env-file=.env server.js"
},
"dependencies": {
  "@fastify/cors": "^11.0.1",
  "bcryptjs": "^3.0.2",
  "fastify": "^5.3.2",
  "googleapis": "^148.0.0",
  "jimp": "^1.6.0",
  "qrcode-reader": "^1.0.4"
}
```

3. Com as dependências listadas em `package.json`, inicie a instalação

`node/server`
``` bash
npm install
```

4. Crie o arquivo `.env` e preencha as informações de acordo com seus dados

```.env
SHEET_ID = sheet-id da url da planilha
PORT = 1234
AUTH_ADDR = IP do dispositivo (ESP32)
WORKSHEET = nome da página da planilha
```

<a name="nodeServer"></a>
#### Execução do Servidor

1. Faça o Download dos arquivos [`server.js`](src/server.js), [`routes.js`](src/routes.js) e [`sheetService.js`](src/sheetService.js)

2. Inclua os arquivos na mesma pasta que contém `package.json`

3. Inicie o servidor

`node/server`
```bash
npm run start
```

<br>

<a name="ref"></a>
### 📄 Referências

<img src="https://cdn.simpleicons.org/youtube/FF0000/FF0000" width=24>&nbsp; [WebServer: Arduino UNO com WiFi ESP01](https://youtu.be/_WPXhNV07Q8?si=PmHWCHl0Lrf5LABd) → configuração e explicação arduino + ESP8266 (ESP01)  
<img src="https://cdn.simpleicons.org/youtube/FF0000/FF0000" width=24>&nbsp; [Arduino Retornando Dados no Formato JSON no Web Server](https://youtu.be/eSMZxWEYgZs?si=KtAnpWq5ySvwE1lo) → configuração do arduino + Ethernet Shield para retorno de JSON no web server  
<img src="https://cdn.simpleicons.org/youtube/FF0000/FF0000" width=24>&nbsp; [Program ESP32-CAM using Arduino UNO](https://easyelectronicsproject.com/esp32-projects/program-esp32cam-arduino/) → configuração da ESP32 cam + arduino  
<img src="https://cdn.simpleicons.org/youtube/FF0000/FF0000" width=24>&nbsp; [Arduino IDE + ESP32 CAM | ESP32-CAM QR Code Scanner](https://www.youtube.com/watch?v=tZV7b8dGgw4) → ESP32 CAM + ESP32-CAM-MB  
<img src="https://cdn.simpleicons.org/youtube/FF0000/FF0000" width=24>&nbsp; [Criando um Web Server com ESP32](https://www.youtube.com/watch?v=ZSyqNFGAF8o) → exemplo da biblioteca `WiFi` do ESP32  
<img src="https://cdn.simpleicons.org/youtube/FF0000/FF0000" width=24>&nbsp; [Sending Data from ESP32 or ESP8266 to Google Sheets](https://youtu.be/3V1S0Cj4mas?si=nfMsxMOIjSp5avWR) → ESP32 + google sheets  
<img src="https://cdn.simpleicons.org/youtube/FF0000/FF0000" width=24>&nbsp; [ESP8266 Enviando Dados para Planilha do Google via HTTP](https://youtu.be/dTB2lD6ToSk?si=Qwb1mgBSHx-CIxTv) → ESP32 + google sheets  
<img src="https://cdn.simpleicons.org/youtube/FF0000/FF0000" width=24>&nbsp; [Esp32 Data Logger con Google Drive y Hoja de Cálculo 📊](https://youtu.be/L8MWleQVpqM?si=7_VOkyH51vw-rF92) → ESP32 + google sheets  
<img src="https://cdn.simpleicons.org/youtube/FF0000/FF0000" width=24>&nbsp; [Google Sheets with Node.js](https://youtu.be/QQNArEqBCHQ?si=OHBbPL9E-j2tyAcC&t=45) → Service Account, Google Sheet API  
<img src="https://cdn.simpleicons.org/googledocs/FFFFFF/FFFFFF" width=24>&nbsp; [ESP32 Documentation](https://docs.espressif.com/projects/arduino-esp32/en/latest/index.html) → WiFi API, Wi-Fi STA Example  
<img src="https://cdn.simpleicons.org/googlecloud/4285F4/4285F4" width=24>&nbsp; [Google Cloud](https://console.cloud.google.com/welcome)  
<img src="https://cdn.simpleicons.org/google/4285F4/4285F4" width=24>&nbsp; [Google Sheets API](https://developers.google.com/workspace/sheets/api/reference/rest?hl=en)  
