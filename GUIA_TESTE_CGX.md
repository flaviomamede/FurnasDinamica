# 🔬 Guia de Teste com CGX

## 📋 Pré-requisitos

### 1. Instalar Software Necessário
```bash
# Ubuntu/Debian
sudo apt update
sudo apt install -y calculix-cgx gmsh paraview python3 python3-pip

# Verificar instalação
cgx --version
gmsh --version
paraview --version
```

### 2. Instalar Dependências Python
```bash
cd /home/flavio/Documentos/FEM/FURNASDINAMICA/FurnasDinamica
pip install -r requirements.txt
```

## 🚀 Teste 1: Execução do Programa Principal

### Passo 1: Executar o Sistema
```bash
python main.py
```

**O que esperar:**
- Menu interativo aparecerá
- Opções disponíveis:
  1. Análise Estática
  2. Análise Modal
  3. Análise Dinâmica

### Passo 2: Testar Análise Estática
1. Digite `1` para análise estática
2. Digite `1` para incluir solo (ou `0` para não incluir)
3. Digite `0` para não copiar malha existente

**Arquivos gerados:**
- `teste.geo` - Arquivo de geometria GMSH
- `teste_mesh.inp` - Arquivo de malha CalculiX
- `teste.fbd` - Arquivo de visualização CGX
- `teste.inp` - Arquivo de entrada CalculiX

## 🔬 Teste 2: Visualização com CGX

### Passo 1: Abrir Arquivo FBD
```bash
cgx teste.fbd
```

**O que esperar:**
- Interface gráfica do CGX abrirá
- Geometria do radier estaqueado será exibida
- Estrutura em tronco de cone com estacas circulares

### Passo 2: Comandos CGX Úteis
```
# Visualização básica
q - sair
h - ajuda
r - resetar visualização
z - zoom
p - pan
t - rotação

# Visualizar malha
mesh all
plot mesh all

# Visualizar geometria
plot geometry all

# Visualizar resultados (após análise)
plot d all
plot s all
```

## 🔬 Teste 3: Análise Completa

### Passo 1: Executar CalculiX
```bash
ccx teste
```

**O que esperar:**
- Processamento da análise
- Arquivos de resultado gerados:
  - `teste.frd` - Resultados CalculiX
  - `teste.dat` - Dados numéricos

### Passo 2: Visualizar Resultados no CGX
```bash
cgx teste.fbd
```

**Comandos para visualizar resultados:**
```
# Carregar resultados
read teste.frd

# Visualizar deslocamentos
plot d all

# Visualizar tensões
plot s all

# Visualizar tensões principais
plot sp all

# Animações
anim d all
anim s all
```

## 🔬 Teste 4: Análise Modal

### Passo 1: Executar Análise Modal
```bash
python main.py
# Digite 2 para análise modal
# Digite 1 para incluir solo
# Digite 0 para não copiar malha
```

### Passo 2: Visualizar Modos de Vibração
```bash
cgx teste.fbd
```

**Comandos para modos:**
```
# Carregar resultados modais
read teste.frd

# Visualizar modo específico
plot d all 1  # modo 1
plot d all 2  # modo 2
plot d all 3  # modo 3

# Animar modos
anim d all 1
anim d all 2
```

## 🔬 Teste 5: Análise Dinâmica

### Passo 1: Executar Análise Dinâmica
```bash
python main.py
# Digite 3 para análise dinâmica
# Digite 1 para incluir solo
# Digite 0 para não copiar malha
```

### Passo 2: Visualizar Time-History
```bash
cgx teste.fbd
```

**Comandos para análise dinâmica:**
```
# Carregar resultados dinâmicos
read teste.frd

# Visualizar deformação em tempo específico
plot d all 1  # passo de tempo 1
plot d all 5  # passo de tempo 5

# Animar evolução temporal
anim d all
```

## 📊 Verificação dos Resultados

### 1. Verificar Arquivos Gerados
```bash
ls -la *.geo *.inp *.frd *.dat *.fbd
```

### 2. Verificar Logs
```bash
# Verificar se não há erros
grep -i error *.log
grep -i warning *.log
```

### 3. Verificar Valores Numéricos
```bash
# Verificar frequências naturais (análise modal)
grep "FREQUENCY" teste.dat

# Verificar deslocamentos máximos
grep "DISPLACEMENT" teste.dat
```

## 🐛 Solução de Problemas

### Problema 1: CGX não abre
```bash
# Verificar se está instalado
which cgx

# Verificar dependências
ldd $(which cgx)

# Instalar dependências faltantes
sudo apt install -y libgl1-mesa-glx libglu1-mesa
```

### Problema 2: Arquivo FBD não carrega
```bash
# Verificar se arquivo existe
ls -la *.fbd

# Verificar conteúdo
head -20 teste.fbd

# Regenerar arquivo
python main.py
```

### Problema 3: CalculiX falha
```bash
# Verificar arquivo de entrada
head -50 teste.inp

# Verificar malha
grep -c "NODE" teste_mesh.inp
grep -c "ELEMENT" teste_mesh.inp
```

## 📈 Métricas de Sucesso

### ✅ Teste Bem-sucedido Se:
- [ ] CGX abre sem erros
- [ ] Geometria é exibida corretamente
- [ ] Malha é gerada sem problemas
- [ ] Análise CalculiX completa sem erros
- [ ] Resultados são visualizados no CGX
- [ ] Animações funcionam
- [ ] Valores numéricos são razoáveis

### 📊 Valores Esperados (aproximados):
- **Frequências naturais**: 1-100 Hz
- **Deslocamentos máximos**: < 1 cm
- **Tensões máximas**: < 50 MPa
- **Número de elementos**: 1000-10000
- **Número de nós**: 2000-20000

---

**🎯 Objetivo**: Verificar se todo o pipeline GMSH → CalculiX → CGX está funcionando corretamente!

**📞 Se encontrar problemas, consulte o README.md ou entre em contato.** 