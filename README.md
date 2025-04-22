<h1 align=center>🚀 Eu nunca vi um cientista 🚀<h1>

## Projeto QR Code para Controle de Presença

Criação de um sistema para Controle de presença, visando a segurança de alunos e funcionários da escola

<br>

<details open="open">
<summary>Tabela de Conteúdos</summary>
  
- [💡 Ideia Inicial](#ideia)
  - [Utilização do `ESP32` para **IOT**](#esp32)
  - [Implementação do `ESP32`](#implementacao)
  - [Implementação de Banco de Dados (futuro)](#implementacao-db)
- [📄 Referências](#ref)
  
</details>

<br>

<a name="ideia"></a>

## 💡 Ideia Inicial
<a name="esp32"></a>
### Utilização do `ESP32` para **IOT**

![image](https://github.com/user-attachments/assets/7a1aac7a-9dac-44dd-80ef-18ae68d61414)

O microcontrolador `ESP32` é amplamente utilizado para a criação de Web Servers embarcados, graças ao seu poder de processamento, conectividade Wi-Fi e suporte a protocolos modernos. Abaixo estão as principais características, benefícios e funcionamento nesse contexto:

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

Exemplo de Funcionamento

1. Inicialização do Wi-Fi  
O ESP32 conecta-se a uma rede

2. Configuração do Servidor Web  
Usando bibliotecas como ESPAsyncWebServer ou WebServer, define-se rotas (ex.: /, /data).

3. Tratamento de Requisições  
`GET:` Envia JSON (ex: leitura de sensores).  
`POST:` Recebe dados de formulários (ex: acionar um relé).

4. Interface do Usuário  
Página HTML simples e intuitiva (Visualização dos dados)

<a name="implementacao-db"></a>
### Implementação de Banco de Dados (futuro)

- [ ] Escolha do Banco de dados para armazenar registros
- [ ] Implementação e Conexão com `ESP32`

<br>

<a name="ref"></a>
### 📄 Referências
- <img src="https://cdn.simpleicons.org/youtube/FF0000/FF0000" width=24>&nbsp; [Send data from Arduino to webserver | ESP8266+Arduino+database](https://www.youtube.com/watch?v=DTk3yQow5bM&list=PLg4zINck8MBqisx_ZW1l_xWla1KbbXyNV)
- <img src="https://cdn.simpleicons.org/youtube/FF0000/FF0000" width=24>&nbsp; [WebServer: Arduino UNO com WiFi ESP01](https://youtu.be/_WPXhNV07Q8?si=PmHWCHl0Lrf5LABd)
- <img src="https://cdn.simpleicons.org/youtube/FF0000/FF0000" width=24>&nbsp; [Arduino Retornando Dados no Formato JSON no Web Server](https://youtu.be/eSMZxWEYgZs?si=KtAnpWq5ySvwE1lo)
