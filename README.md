# Gilliat Finance — Ecossistema Quantitativo de Conteúdo & Infoprodutos

Este repositório contém a infraestrutura completa para:
1. **Geração e Publicação de Conteúdo no LinkedIn** focado em atrair a audiência qualificada (Quants, Data Scientists, Economistas, Analistas de Mercado);
2. **Produtos Digitais Prontos para Monetização** (Playbook de Transição Quant, Newsletter Automatizada de Fatores e Toolkit de Econometria Financeira);
3. **Automação de Publicação** (suporte a API oficial do LinkedIn, Buffer API e exportação em lote).

---

## 📁 Estrutura do Projeto

```
gilliat-finance/
├── content_generator/          # Motor de inteligência de conteúdo
│   ├── prompts.py              # Definição de persona, tom de voz e pilares
│   └── generate_batch.py       # Gerador de lotes semanais de postagens
├── publisher/                  # Conectores de publicação
│   ├── linkedin_api.py         # Conector direto com a API Oficial do LinkedIn
│   └── buffer_publisher.py     # Conector para agendamento seguro via Buffer/Publer
├── posts/                      # Posts gerados e prontos para publicação
│   └── batch_01/               # Lote 1 com posts técnicos e CTAs de conversão
└── products/                   # Infoprodutos estruturados para venda
    ├── quant_transition_playbook/   # Produto 1: E-book + Códigos de Portfólio
    ├── factor_newsletter/           # Produto 2: Pipeline da Newsletter de Fatores
    └── econometrics_toolkit/        # Produto 3: Templates de Modelos em Python
```

---

## 🚀 Como Usar

### 1. Gerar Novos Posts para o LinkedIn
Para gerar um novo lote de postagens com ganchos de alta conversão:
```bash
python content_generator/generate_batch.py
```

### 2. Publicar ou Agendar
* Para revisar os posts gerados: abra os arquivos em `posts/batch_01/`.
* Para enviar automaticamente via Buffer ou LinkedIn API, configure as credenciais no arquivo `config.py`.

### 3. Venda dos Produtos
* Os arquivos dos produtos em `products/` já vêm formatados para upload imediato em plataformas de entrega automática como **Gumroad** ou **Hotmart**.
