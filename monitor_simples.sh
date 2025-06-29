#!/bin/bash

echo "🔍 Monitorando CalculiX..."
echo "=========================="

while true; do
    clear
    
    # Verificar se o CalculiX está rodando
    CCX_PID=$(pgrep ccx)
    
    if [ -n "$CCX_PID" ]; then
        echo "✅ CalculiX rodando - PID: $CCX_PID"
        
        # Informações do processo
        CPU=$(ps -p $CCX_PID -o %cpu --no-headers)
        MEM=$(ps -p $CCX_PID -o %mem --no-headers)
        TIME=$(ps -p $CCX_PID -o etime --no-headers)
        
        echo "🖥️  CPU: ${CPU}%"
        echo "💾 Memória: ${MEM}%"
        echo "⏱️  Tempo: ${TIME}"
        
        echo ""
        echo "📁 Arquivos de saída:"
        echo "---------------------"
        
        # Verificar arquivos de saída
        for file in teste/teste_estatico_solve.{cvg,dat,frd,sta}; do
            if [ -f "$file" ]; then
                size=$(du -h "$file" | cut -f1)
                echo "🟢 $(basename $file): $size"
            else
                echo "⚪ $(basename $file): 0 B"
            fi
        done
        
        echo ""
        echo "⏰ $(date '+%H:%M:%S')"
        echo "Pressione Ctrl+C para parar..."
        
    else
        echo "❌ CalculiX não está rodando"
        break
    fi
    
    sleep 3
done 