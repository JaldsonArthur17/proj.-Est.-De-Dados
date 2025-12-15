# 🏥 Sistema de Atendimento com Fila e Prioridade

## 📖 Descrição do Projeto

Este projeto consiste no desenvolvimento de um **Sistema de Atendimento**, que simula o fluxo de atendimento de clientes/pacientes em um ambiente como uma clínica, banco ou empresa. O sistema gerencia clientes comuns e prioritários, organiza a ordem de atendimento e permite desfazer ações recentes, aplicando conceitos fundamentais de **Estruturas de Dados** estudados na disciplina.

O objetivo principal é demonstrar, na prática, o uso eficiente de diferentes estruturas de dados para resolver um problema realista de organização e atendimento.

---

## 🎯 Objetivo Geral

Desenvolver uma aplicação que utilize, de forma significativa, estruturas de dados para controlar o atendimento de clientes, considerando **ordem de chegada**, **prioridade** e **histórico de ações**.

---

## 💡 Justificativa da Escolha do Tema

O sistema de atendimento foi escolhido por representar um problema real e amplamente utilizado em diversos contextos do dia a dia. Ele permite a aplicação clara e objetiva de várias estruturas de dados, facilitando o entendimento do seu funcionamento e evidenciando sua importância na organização e eficiência dos processos.

---

## 🏗️ Estruturas de Dados Utilizadas

### 🔹 Fila (Queue)

- Utilizada para armazenar clientes **sem prioridade**, respeitando a ordem de chegada (FIFO).
- Garante um atendimento justo e organizado.

### 🔹 Heap (Fila de Prioridade)

- Usada para gerenciar clientes **prioritários** (idosos, emergências, etc.).
- Clientes com maior prioridade são atendidos primeiro.
- Demonstra o uso de estrutura baseada em prioridade.

### 🔹 Pilha (Stack)

- Responsável por armazenar o **histórico de atendimentos**.
- Permite desfazer a última ação realizada (funcionalidade de _undo_).

> ✔️ O uso dessas estruturas atende ao requisito mínimo de utilização de pelo menos duas estruturas de dados distintas.

---

## ⚙️ Funcionalidades do Sistema

- Cadastro de clientes comuns e prioritários
- Atendimento automático respeitando prioridade
- Visualização da fila de espera
- Registro do histórico de atendimentos
- Opção de desfazer o último atendimento realizado
- Interface em modo texto (console)

---

## 💻 Interface do Sistema

O sistema possui uma **interface em modo texto (console)**, apresentando um menu interativo para que o usuário possa navegar pelas funcionalidades de forma simples e intuitiva.

---

## 🧠 Desafios Enfrentados

- Integração correta entre fila comum e fila de prioridade
- Garantir que o atendimento respeitasse corretamente as regras de prioridade
- Implementação do desfazer atendimento utilizando pilha
- Organização do código para facilitar manutenção e entendimento

### 🔧 Soluções Encontradas

- Separação clara das estruturas de dados por responsabilidade
- Criação de funções específicas para cada operação
- Uso de comentários e boas práticas de programação

---

## ▶️ Instruções para Execução

1. Certifique-se de ter o **Python 3.x** instalado.
2. Clone ou faça o download do repositório.
3. Acesse a pasta do projeto pelo terminal.
4. Execute o arquivo principal:

```bash
python main.py
```

5. Utilize o menu exibido no console para interagir com o sistema.
