# FurnasDinamica

Sistema automatizado de análise de elementos finitos (FEM) para **radiers estaqueados em tronco de cone** desenvolvido para a FURNAS.

## 📋 Descrição

O **FurnasDinamica** é uma solução computacional completa para análise estrutural de fundações especiais, implementando uma rotina automatizada que integra:

- **GMSH**: Geração paramétrica de geometria e malha
- **CalculiX (CCX)**: Solver de elementos finitos
- **CGX**: Visualização e pós-processamento
- **ParaView**: Visualização avançada de resultados

## 🏗️ Funcionalidades

### 1. Geração Paramétrica de Geometria
- **Radier em tronco de cone** com estacas circulares
- **Controle via arquivo TOML** para todos os parâmetros
- **Variação automática** de:
  - Diâmetros (base e topo)
  - Alturas (base, tronco de cone, topo)
  - Número de estacas
  - Diâmetro das estacas
  - Distância das estacas até a face externa
  - Altura das estacas

### 2. Geração de Malha
- **Elementos tetraédricos 3D** (C3D4) - 4 nós, 1 ponto de integração
- **Controle de refinamento** (tamanho mínimo/máximo)
- **Multiplicador global** de malha
- **Exportação** para formato .inp (CalculiX)

### 3. Análises Implementadas

#### Análise Estática
- Cálculo de **tensões** (normais e cisalhantes)
- Cálculo de **deslocamentos**
- Visualização no ParaView

#### Análise Modal
- **Modos de vibração** configuráveis
- **Frequências naturais**
- **Participações modais**
- Visualização dos modos no ParaView

#### Análise Dinâmica
- **Vibração forçada**
- **Time-history** de pontos específicos
- **Tensões principais** (σ₁, σ₂, σ₃)
- Visualização temporal no ParaView

### 4. Pós-processamento
- **Visualização em tempo real** no ParaView
- **Acesso aos resultados por nó**
- **Exportação para CSV**
- **Análise de tensões principais**

## 🛠️ Tecnologias Utilizadas

- **Python 3.x** - Linguagem principal
- **GMSH 4.9.4** - Geração de geometria e malha
- **CalculiX (CCX)** - Solver de elementos finitos
- **CGX** - Visualização
- **ParaView** - Pós-processamento avançado
- **NumPy** - Computação numérica
- **TOML** - Configuração de parâmetros

## 📦 Instalação

### Pré-requisitos
```bash
# Ubuntu/Debian
sudo apt update
sudo apt install -y python3 python3-pip gmsh calculix-cgx paraview
```

### Instalação do Projeto
```bash
# Clone o repositório
git clone https://github.com/xJohnKennedy/FurnasDinamica.git
cd FurnasDinamica

# Instale as dependências Python
pip install -r requirements.txt

# Configure o ambiente virtual (se necessário)
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## 🚀 Como Usar

### 1. Configuração dos Parâmetros
Edite o arquivo de configuração (formato TOML) com os parâmetros desejados:

```toml
[geometria]
h_base = 100.0      # altura da base (cm)
h_cone = 250.0      # altura do tronco de cone (cm)
diam_base = 1800.0  # diâmetro da base (cm)
diam_topo = 700.0   # diâmetro do topo (cm)
h_topo = 50.0       # altura do topo (cm)

[estacas]
num_est = 12        # número de estacas
diam_est = 60.0     # diâmetro das estacas (cm)
h_est = 1000.0      # altura das estacas (cm)
cob_est = 300.0     # cobrimento das estacas (cm)

[cargas]
num_cargas = 8      # número de pontos de carga
diam_carga = 400.0  # diâmetro do círculo de cargas (cm)

[malha]
tamanho_min = 0.1   # tamanho mínimo do elemento
tamanho_max = 2.0   # tamanho máximo do elemento
fator_malha = 1.0   # multiplicador global
```

### 2. Execução
```bash
# Execute o programa principal
python main.py

# Ou use o comando automatizado (se configurado)
furnapy
```

### 3. Visualização dos Resultados
- **ParaView**: Para visualização avançada
- **CGX**: Para visualização rápida
- **CSV**: Para análise em planilhas

## 📁 Estrutura do Projeto

```
FurnasDinamica/
├── main.py                 # Programa principal
├── requirements.txt        # Dependências Python
├── scripts/               # Scripts auxiliares
├── ccx/                   # Arquivos do CalculiX
├── cgx/                   # Arquivos do CGX
├── ccx2paraview-master/   # Conversor para ParaView
├── teste.txt              # Arquivo de teste
├── tests.py               # Testes automatizados
└── README.md              # Este arquivo
```

## 🔧 Configuração Avançada

### Ambiente Virtual Python
```bash
# Criar ambiente virtual
python -m venv venv

# Ativar ambiente
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows

# Instalar dependências
pip install -r requirements.txt
```

### Configuração do GMSH
O GMSH deve estar instalado e acessível via linha de comando:
```bash
gmsh --version
```

### Configuração do CalculiX
O CalculiX (CCX) deve estar instalado:
```bash
ccx --version
```

## 📊 Exemplos de Uso

### Análise Estática
1. Configure os parâmetros no arquivo TOML
2. Execute `python main.py`
3. Selecione "Análise Estática"
4. Visualize os resultados no ParaView

### Análise Modal
1. Configure os parâmetros
2. Execute o programa
3. Selecione "Análise Modal"
4. Defina o número de modos desejados
5. Visualize os modos de vibração

### Análise Dinâmica
1. Configure os parâmetros
2. Execute o programa
3. Selecione "Análise Dinâmica"
4. Configure o carregamento dinâmico
5. Analise o time-history

## 🧪 Testes

Execute os testes automatizados:
```bash
python tests.py
```

## 📝 Relatório Técnico

Este projeto foi desenvolvido pela **ESPER Engenharia** como parte da consultoria para FURNAS (Termo Contratual nº 8000012851). O relatório técnico completo está disponível em `TC8000012851_20032023 RT_02.txt`.

### Status do Desenvolvimento
- ✅ Geração paramétrica implementada
- ✅ Análises estáticas, modais e dinâmicas funcionando
- ✅ Processamento totalmente automatizado
- ✅ Visualização no ParaView
- ⚠️ Pendente: implementação do solo envolvente
- ⚠️ Pendente: validação de limites dimensionais

## 🤝 Contribuição

Para contribuir com o projeto:

1. Faça um fork do repositório
2. Crie uma branch para sua feature (`git checkout -b feature/nova-funcionalidade`)
3. Commit suas mudanças (`git commit -am 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/nova-funcionalidade`)
5. Abra um Pull Request

## 📄 Licença

Este projeto foi desenvolvido para a FURNAS e está disponível sob os termos do contrato TC 8000012851.

## 👥 Autores

- **Jonathas Kennedy Alves Pereira** - Eng. Civil CREA-GO 1019655690/D
- **Walid Joseph Esper** - Eng. Civil CREA-GO 7119/D

**ESPER Engenharia de Projetos**  
Av. Dep. Jamel Cecílio esq. com Av. Eng. Eurico Viana, Metropolitan Mall, Torre Tokyo, 2690, sala 1417, Jardim Goiás. Goiânia – GO – CEP: 74.815-457  
Tel.: +55 62 3286.4614

## 🔗 Links Úteis

- [Repositório Original](https://github.com/xJohnKennedy/FurnasDinamica)
- [GMSH](http://gmsh.info/)
- [CalculiX](http://www.calculix.de/)
- [ParaView](https://www.paraview.org/)
- [TOML](https://toml.io/)

---

**Desenvolvido para FURNAS - Termo Contratual nº 8000012851** 