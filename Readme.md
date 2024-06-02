Guassap2.0 és un projecte en el qual realitzem els diferents patrons en els sistemes distribuits, en el qual utilitzem implementacions com RabbitMq, Redis i Docker. 

A continuació mostrem els passos a realitzar per al correcte funcionament del programa:
(Si ja teniu Ubuntu instalat, passeu al pas 3)
  1. Instalar Ubuntu amb wsl. Powershell amb permisos d’administrador → wsl --install -d Ubuntu.
  2. Reiniciar pc
  3. Conectar-se a Ubuntu (amb la comanda Ubuntu a powershell) i executar les següents comandes:
      3.1. sudo apt update
      3.2. sudo apt-get install redis-server
      3.3. sudo apt-get install redis-cli
  4. Descarregar Docker Desktop des de https://www.docker.com/products/docker-desktop/
  5. Preparar un venv de python 3.11 a VSC
  6. Executar la comanda "py Main.py" des del terminal del venv.
