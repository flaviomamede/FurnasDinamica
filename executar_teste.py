#!/usr/bin/env python3
"""
Script para executar teste do FurnasDinamica de forma organizada
Autor: Assistente IA
Data: 2024
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path

def limpar_arquivos_anteriores():
    """Remove arquivos de execuções anteriores"""
    print("🧹 Limpando arquivos de execuções anteriores...")
    
    # Padrões de arquivos a remover
    padroes = [
        "*.geo", "*.msh", "*.inp", "*.fbd", "*.frd", "*.dat", 
        "*.sta", "*.cvg", "*.eig", "*.lst", "*.pvd", "*.vtu"
    ]
    
    for padrao in padroes:
        for arquivo in Path(".").glob(padrao):
            try:
                arquivo.unlink()
                print(f"   Removido: {arquivo}")
            except:
                pass

def verificar_dependencias():
    """Verifica se as dependências estão instaladas"""
    print("🔍 Verificando dependências...")
    
    dependencias = ['gmsh', 'ccx', 'cgx']
    faltando = []
    
    for dep in dependencias:
        if shutil.which(dep) is None:
            faltando.append(dep)
    
    if faltando:
        print(f"❌ Dependências faltando: {', '.join(faltando)}")
        print("💡 Instale com: sudo apt install calculix-cgx gmsh")
        return False
    
    print("✅ Todas as dependências encontradas!")
    return True

def executar_teste():
    """Executa o teste principal"""
    print("\n🚀 Iniciando teste do FurnasDinamica...")
    print("=" * 50)
    
    # Mudar para pasta teste
    if not os.path.exists("teste"):
        print("❌ Pasta 'teste' não encontrada!")
        return False
    
    os.chdir("teste")
    print(f"📁 Trabalhando em: {os.getcwd()}")
    
    # Verificar se teste.txt existe
    if not os.path.exists("teste.txt"):
        print("❌ Arquivo 'teste.txt' não encontrado!")
        return False
    
    # Limpar arquivos anteriores
    limpar_arquivos_anteriores()
    
    # Executar o programa principal
    print("\n🎯 Executando FurnasDinamica...")
    try:
        # Importar e executar main_func
        sys.path.append('..')
        from main import main_func
        
        # Simular entrada do usuário para teste automático
        import builtins
        original_input = builtins.input
        
        def mock_input(prompt=""):
            if "Nome do arquivo" in prompt:
                return "teste.txt"
            elif "tipo de calculo" in prompt or "Digite opcao" in prompt:
                return "1"  # Análise estática
            elif "solo envolvente" in prompt:
                return "0"  # Sem solo
            elif "copia_msh" in prompt or "Deseja copiar" in prompt:
                return "0"  # Não copiar malha
            elif "apagar a pasta" in prompt:
                return "S"  # Sim, apagar pasta
            else:
                return original_input(prompt)
        
        builtins.input = mock_input
        
        # Executar
        main_func()
        
        # Restaurar input original
        builtins.input = original_input
        
        print("\n✅ Teste executado com sucesso!")
        return True
        
    except Exception as e:
        print(f"❌ Erro durante execução: {e}")
        return False

def mostrar_resultados():
    """Mostra os arquivos gerados"""
    print("\n📊 Arquivos gerados:")
    print("=" * 30)
    
    arquivos = list(Path(".").glob("*"))
    arquivos.sort()
    
    for arquivo in arquivos:
        if arquivo.is_file():
            tamanho = arquivo.stat().st_size
            print(f"📄 {arquivo.name} ({tamanho} bytes)")
    
    # Verificar pastas de resultados
    pastas_resultado = list(Path(".").glob("resultados_*"))
    if pastas_resultado:
        print(f"\n📁 Pastas de resultados:")
        for pasta in pastas_resultado:
            if pasta.is_dir():
                num_arquivos = len(list(pasta.glob("*")))
                print(f"   📂 {pasta.name} ({num_arquivos} arquivos)")

def instrucoes_visualizacao():
    """Mostra instruções para visualização"""
    print("\n🔍 Para visualizar os resultados:")
    print("=" * 40)
    print("1. Visualizar geometria:")
    print("   cgx teste_estatico.fbd")
    print("\n2. Visualizar resultados (após análise):")
    print("   cgx teste_estatico.fbd")
    print("   # No CGX, digite: read teste_estatico.frd")
    print("   # Depois: plot d all")
    print("\n3. Abrir no ParaView:")
    print("   paraview teste_estatico.pvd")

def main():
    """Função principal"""
    print("🏗️  FurnasDinamica - Teste Automatizado")
    print("=" * 50)
    
    # Verificar dependências
    if not verificar_dependencias():
        return
    
    # Executar teste
    if executar_teste():
        mostrar_resultados()
        instrucoes_visualizacao()
    else:
        print("❌ Teste falhou!")

if __name__ == "__main__":
    main() 