# 🧪 Pasta de Testes - FurnasDinamica

Esta pasta contém os arquivos de teste e configuração para o sistema FurnasDinamica.

## 📁 Conteúdo

- `teste.txt` - Arquivo de configuração TOML para teste
- `resultados_*` - Pastas com resultados das análises (geradas automaticamente)

## 🚀 Como Executar

### Opção 1: Script Automatizado (Recomendado)
```bash
# Na pasta raiz do projeto
python executar_teste.py
```

### Opção 2: Execução Manual
```bash
# Na pasta raiz do projeto
python main.py
# Digite: teste/teste.txt
# Escolha as opções desejadas
```

### Opção 3: Execução Direta na Pasta
```bash
cd teste
python ../main.py
# Digite: teste.txt
# Escolha as opções desejadas
```

## 📊 Arquivos Gerados

Após a execução, serão criados:

### Arquivos de Geometria e Malha
- `teste_estatico.geo` - Arquivo de geometria GMSH
- `teste_estatico_mesh.inp` - Arquivo de malha CalculiX

### Arquivos de Análise
- `teste_estatico.inp` - Arquivo de entrada CalculiX
- `teste_estatico.fbd` - Arquivo de visualização CGX

### Arquivos de Resultado
- `teste_estatico.frd` - Resultados CalculiX
- `teste_estatico.dat` - Dados numéricos
- `teste_estatico.pvd` - Arquivo ParaView

### Pasta de Resultados
- `resultados_teste_estatico/` - Todos os arquivos organizados

## 🔍 Visualização

### Com CGX
```bash
cgx teste_estatico.fbd
```

**Comandos úteis no CGX:**
```
# Visualizar geometria
plot geometry all

# Visualizar malha
plot mesh all

# Carregar resultados
read teste_estatico.frd

# Visualizar deslocamentos
plot d all

# Visualizar tensões
plot s all

# Animações
anim d all
```

### Com ParaView
```bash
paraview teste_estatico.pvd
```

## ⚙️ Configuração

O arquivo `teste.txt` contém todos os parâmetros:

```toml
[geometria]
diam_base = 2220    # diâmetro da base (cm)
diam_topo = 900     # diâmetro do topo (cm)
h_base = 50         # altura da base (cm)
h_cone = 350        # altura do tronco de cone (cm)
h_topo = 25         # altura do topo (cm)

[estacas]
num_est = 15        # número de estacas
diam_est = 60       # diâmetro das estacas (cm)
h_est = 712         # altura das estacas (cm)
cob_est = 200       # cobrimento das estacas (cm)

[cargas]
num_cargas = 12     # número de pontos de carga
diam_carga = 300    # diâmetro do círculo de cargas (cm)
```

## 🧹 Limpeza

Para limpar arquivos de execuções anteriores:
```bash
# Remover arquivos temporários
rm -f *.geo *.msh *.inp *.fbd *.frd *.dat *.sta *.cvg *.eig *.lst *.pvd *.vtu

# Remover pastas de resultados
rm -rf resultados_*
```

## 📈 Resultados Esperados

### Valores Típicos
- **Frequências naturais**: 1-100 Hz
- **Deslocamentos máximos**: < 1 cm
- **Tensões máximas**: < 50 MPa
- **Número de elementos**: 1000-10000

### Verificação
```bash
# Verificar frequências (análise modal)
grep "FREQUENCY" teste_estatico.dat

# Verificar deslocamentos
grep "DISPLACEMENT" teste_estatico.dat

# Verificar número de elementos
grep -c "ELEMENT" teste_estatico_mesh.inp
```

---

**🎯 Objetivo**: Testar o sistema completo de análise de elementos finitos para radiers estaqueados. 