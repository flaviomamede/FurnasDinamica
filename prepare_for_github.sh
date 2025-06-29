#!/bin/bash

# Script para preparar o projeto FurnasDinamica para publicação no GitHub
# Autor: Assistente IA
# Data: $(date)

echo "🚀 Preparando FurnasDinamica para publicação no GitHub..."

# 1. Remover o repositório Git original (se existir)
if [ -d ".git" ]; then
    echo "📁 Removendo repositório Git original..."
    rm -rf .git
fi

# 2. Inicializar novo repositório Git
echo "🔧 Inicializando novo repositório Git..."
git init

# 3. Adicionar todos os arquivos
echo "📦 Adicionando arquivos ao Git..."
git add .

# 4. Fazer commit inicial
echo "💾 Fazendo commit inicial..."
git commit -m "Initial commit: FurnasDinamica - Sistema FEM para radiers estaqueados

- Sistema automatizado de análise de elementos finitos
- Geração paramétrica de geometria com GMSH
- Solver CalculiX (CCX) para análises estáticas, modais e dinâmicas
- Visualização com CGX e ParaView
- Desenvolvido para FURNAS (TC 8000012851)

Autores: Jonathas Kennedy Alves Pereira e Walid Joseph Esper
ESPER Engenharia de Projetos"

# 5. Configurar branch principal
echo "🌿 Configurando branch principal..."
git branch -M main

echo "✅ Projeto preparado com sucesso!"
echo ""
echo "📋 Próximos passos:"
echo "1. Crie um novo repositório no GitHub: https://github.com/flaviomamede"
echo "2. Execute os comandos que aparecerão no GitHub:"
echo "   git remote add origin https://github.com/flaviomamede/FurnasDinamica.git"
echo "   git push -u origin main"
echo ""
echo "🔗 Ou use este comando direto (substitua pelo nome do seu repositório):"
echo "git remote add origin https://github.com/flaviomamede/FurnasDinamica.git"
echo "git push -u origin main" 