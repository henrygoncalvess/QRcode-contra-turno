<h1 align=center>🚀 Eu nunca vi um cientista 🚀<h1>

## Projeto QR Code para Controle de Presença

Criação de um sistema para Controle de presença, visando a segurança de alunos e funcionários da escola

<br>

**licença e tecnologias utilizadas**:  
<img src="https://img.shields.io/github/license/henrygoncalvess/QRcode-contra-turno?style=for-the-badge&labelColor=gray&color=97ca00"> <a href="https://docs.python.org/3/"><img src="https://img.shields.io/badge/python-3.11.9-3776AB?style=for-the-badge&logo=python&logoColor=3776AB&labelColor=gray"></a>

<br>

<details open="open">
<summary>Tabela de Conteúdos</summary>
  
- [💡 Ideia Inicial](#ideia)
  - [Utilização do `ESP32` para **IOT**](#esp32)
  - [Implementação do `ESP32`](#implementacao)
  - [Implementação de Banco de Dados (futuro)](#implementacao-db)
- [🛠 Recursos Gerais](#recursos)
- [⚙ Geração de QR code](#qrcode)
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

<a name="implementacao"></a>
### Implementação do `ESP32`

Utilização em modo `Station` (STA)

1. O `ESP32` conecta-se a um roteador Wi-Fi existente.
2. O servidor web fica acessível via IP local (ex: 192.168.1.100).

Exemplo de Funcionamento (Fluxo Básico)

1. Inicialização do Wi-Fi  
O ESP32 conecta-se a uma rede

2. Configuração do Servidor Web  
Usando bibliotecas como ESPAsyncWebServer ou WebServer, define-se rotas (ex.: /, /data).

3. Tratamento de Requisições  
`POST:` Envia JSON (ex: leitura de sensores).  
`GET:` Recebe dados de formulários (ex: acionar um relé).

4. Interface do Usuário  
Página HTML simples e intuitiva, Planilha Excel (Visualização dos dados)

#### Exemplo com imagem

![fluxo básico com imagem](images/fluxo_code.png)

<a name="implementacao-db"></a>
### Implementação de Banco de Dados (futuro)

- [x] Escolha do Banco de dados para armazenar registros (MySQL)
- [ ] Implementação e Conexão com `ESP32`

<br>

<a name="recursos"></a>
### 🛠 Recursos Gerais

- [ ] ESP32 Cam
- [ ] ESP32 Module
- [x] Arduino UNO
- [ ] **opcional:** ESP32-CAM-MB
- [ ] **opcional:** ESP8266 (ESP01)
- [x] Jumpers Elétricos
- [x] LEDs
- [x] Resistores

<br>

<a name="qrcode"></a>
### ⚙ Geração de QR code

⚫[QR Code Monkey](https://www.qrcode-monkey.com/) → Gera um por um, mas é fácil de usar.  
⚫[QR code API](https://goqr.me/api/) → API gratuita para gerar em massa.  
🟢 Usando `Python` → para gerar em massa (com logo).

#### Gerando com Python

> [!TIP]
> Documentação da biblioteca `qrcode` → [Clique aqui](https://pypi.org/project/qrcode/)

1. Instalação das bibliotecas qrcode e Pillow:
```bash
pip install qrcode[pil]
```

2. Código → Clique [AQUI](qr-code.py) para acessar

3. Exemplo de resultado

![exemplo de QR Code com logo do Batista Renzi](images/batista-code.png)

<br>

<a name="ref"></a>
### 📄 Referências
<img src="https://cdn.simpleicons.org/youtube/FF0000/FF0000" width=24>&nbsp; [WebServer: Arduino UNO com WiFi ESP01](https://youtu.be/_WPXhNV07Q8?si=PmHWCHl0Lrf5LABd) → configuração e explicação arduino + ESP8266 (ESP01)  
<img src="https://cdn.simpleicons.org/youtube/FF0000/FF0000" width=24>&nbsp; [Arduino Retornando Dados no Formato JSON no Web Server](https://youtu.be/eSMZxWEYgZs?si=KtAnpWq5ySvwE1lo) → configuração do arduino + Ethernet Shield para retorno de JSON no web server  
<img src="https://cdn.simpleicons.org/youtube/FF0000/FF0000" width=24>&nbsp; [Program ESP32-CAM using Arduino UNO](https://easyelectronicsproject.com/esp32-projects/program-esp32cam-arduino/) → configuração da ESP32 cam + arduino  
<img src="https://cdn.simpleicons.org/youtube/FF0000/FF0000" width=24>&nbsp; [Arduino IDE + ESP32 CAM | ESP32-CAM QR Code Scanner](https://www.youtube.com/watch?v=tZV7b8dGgw4) → ESP32 CAM + ESP32-CAM-MB  
<img src="https://cdn.simpleicons.org/youtube/FF0000/FF0000" width=24>&nbsp; [Criando um Web Server com ESP32](https://www.youtube.com/watch?v=ZSyqNFGAF8o) → exemplo da biblioteca `WiFi` do ESP32  
<img src="https://cdn.simpleicons.org/googledocs/FFFFFF/FFFFFF" width=24>&nbsp; [ESP32 Documentation](https://docs.espressif.com/projects/arduino-esp32/en/latest/index.html) → WiFi API, Wi-Fi STA Example  
<img src="https://cdn.simpleicons.org/youtube/FF0000/FF0000" width=24>&nbsp; [Sending Data from ESP32 or ESP8266 to Google Sheets](https://youtu.be/3V1S0Cj4mas?si=nfMsxMOIjSp5avWR) → ESP32 + google sheets  
<img src="https://cdn.simpleicons.org/youtube/FF0000/FF0000" width=24>&nbsp; [ESP8266 Enviando Dados para Planilha do Google via HTTP - Tutorial Completo com Códigos](https://youtu.be/dTB2lD6ToSk?si=Qwb1mgBSHx-CIxTv) → ESP32 + google sheets  
<img src="https://cdn.simpleicons.org/youtube/FF0000/FF0000" width=24>&nbsp; [Esp32 Data Logger con Google Drive y Hoja de Cálculo 📊](https://youtu.be/L8MWleQVpqM?si=7_VOkyH51vw-rF92) → ESP32 + google sheets  
