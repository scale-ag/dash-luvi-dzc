# -*- coding: utf-8 -*-
"""
Configuração do cliente — TEMPLATE.

Este é o ÚNICO arquivo que precisa ser editado para colocar o funil de um
cliente novo no ar. Troque TODOS os marcadores de preenchimento (o build
se recusa a rodar enquanto algum marcador de texto continuar aqui).
Ordem completa: "CHECKLIST DE NOVO CLIENTE" no topo do CLAUDE.md.

Depois de editar, teste localmente:

    python build/build.py --meta-file meta.csv --sales-file sales.csv --out dist/index.html

`build/config.example.py` é a cópia intacta deste modelo — mantenha-o
sem preencher, para restaurar o config.py se precisar começar do zero.
"""
from __future__ import annotations

# ==========================================================================
# 1) PLANILHA(S) DO CLIENTE (Google Sheets)
# ==========================================================================
# SPREADSHEET_ID: o trecho entre /d/ e /edit na URL da planilha
#   (https://docs.google.com/spreadsheets/d/<SPREADSHEET_ID>/edit#gid=...)
# GID_META / GID_SALES: o número depois de "gid=" na URL de cada aba.
# A planilha precisa estar com o link público em modo "Qualquer pessoa com
# o link pode visualizar" (o build lê via export CSV, SOMENTE LEITURA).
SPREADSHEET_ID = "1AJC2FZNqc-KL5TiUy5scEFHt6FS_3mJdQplVBagPhiI"  # "Dados gerenciador - DZC"
# Opcional: se a lista de Compradores estiver em OUTRA planilha, coloque o ID
# dela aqui. Vazio = Compradores na mesma planilha do Meta Ads (padrão).
# Bruno Corano: Vendas fica em planilha separada ("Vendas BF2026 – Do Zero ao Contrato").
SPREADSHEET_ID_SALES = "1fVmJpiS1ubQIc2-wezzB9PkJnjs3agmeeC-0dlpcaVY"
GID_META = "0"  # aba "Página1"
GID_SALES = "1010133128"  # aba "Vendas"

# ==========================================================================
# 2) REGRAS DE NEGÓCIO
# ==========================================================================
# Fator de imposto aplicado sobre o gasto do Meta Ads quando o toggle
# "Imposto Meta" estiver ligado. Use 1.0 se o cliente não tiver imposto.
# Imposto Meta: +13,806%
TAX_FACTOR = 1.13806

# Produto principal do funil (base de Vendas/CAC/ConvCHK/Ticket). Casamento
# por PREFIXO sobre o nome NORMALIZADO (sem acento, minúsculas) da coluna
# Produto da planilha de Compradores — escreva sem acento e em minúsculas.
# Planilha: "Executa Licitação — Do Zero ao Contrato"
MAIN_PRODUCT_PREFIX = "executa licitacao — do zero ao contrato"

# Qual coluna UTM da planilha de Compradores carrega o Ad Name do Meta:
# "utm_content", "utm_term" ou "utm_medium". Depende do parametrizador de URL
# dos anúncios do cliente — CONFIRA nos dados antes de assumir: a coluna que
# não carrega o anúncio costuma trazer o posicionamento (Instagram_Feed/Stories),
# e casar pela coluna errada zera as atribuições.
# Verificado em 19/11/2026: utm_content traz o Ad Name (BF_DZC_*); utm_term traz o ID numérico do anúncio.
AD_UTM_COLUMN = "utm_content"

# A planilha de Compradores tem uma coluna de status de pagamento confiável?
# SIM -> False (o build filtra por is_paid()). NÃO (toda linha já é uma compra
# concretizada) -> True (conta todas as linhas como venda paga).
# Planilha tem a coluna "Status do pagamento" (ex.: "pago").
COUNT_ALL_AS_PAID = False

# Opcional: ignora vendas ANTERIORES a esta data (AAAA-MM-DD), ex.: compras de
# teste antes do funil ir ao ar. Bruno Corano: as compras de 17/11/2026 foram testes.
SALES_START_DATE = "2026-11-18"

# ==========================================================================
# 3) RÓTULOS EXIBIDOS NA INTERFACE
# ==========================================================================
CLIENT_NAME = "Bruno Corano"
CLIENT_SUB = "Renda em Dólar · Funil VSL"
TAX_LABEL = "Imposto Meta ×1,13806"
MAIN_PRODUCT = "Do Zero ao Contrato"

# ==========================================================================
# 4) METAS (aba Relatórios) — código de cor de CAC/ROAS
# ==========================================================================
#   • ROAS: quanto MAIOR, melhor  -> desempenho = roas / ROAS_TARGET
#   • CAC : quanto MENOR, melhor  -> desempenho = CAC_TARGET / cac
# Faixas (sobre o desempenho): <REPORT_BAND_LOW vermelho · até 0,99 amarelo ·
#   até REPORT_BAND_HIGH verde · acima disso azul-ciano.
# CAC alvo: R$ 45 por venda
CAC_TARGET = 45.0
# ROAS alvo: 2
ROAS_TARGET = 2.0
REPORT_BAND_LOW = 0.70
REPORT_BAND_HIGH = 1.30

# ==========================================================================
# 5) IA INSIGHTS (Cloudflare Worker) — ver SETUP-IA.md
# ==========================================================================
# URL pública do Worker (não é secreta). Vazio = aba IA Insights indisponível.
# Preencher depois de publicar o Worker (checklist do CLAUDE.md).
# Worker "bruno-corano-dzc-ia-insights" ainda não publicado (SETUP-IA.md) — preencher a URL depois.
IA_WORKER_URL = ""
