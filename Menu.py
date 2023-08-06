import os
import platform
import socket
import time
import webbrowser
from colorama import Fore, Style

# Function to clear the screen based on the operating system
def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

# Function to print the header of the menu
def print_header(text):
    print(f"{Fore.MAGENTA}{text}{Style.RESET_ALL}")

# Function to print the options of the menu
def print_option(number, text):
    print(f"{Fore.CYAN}{number}. {text}{Style.RESET_ALL}")

# Function to consult the IP address of a website
def check_website_status(site):
    try:
        ip = socket.gethostbyname(site)
        print(f"\n{Fore.MAGENTA}=== Informações do site {site} ===")
        print(f"IP do site: {ip}")

        # Check for open ports
        print(f"\n{Fore.MAGENTA}=== Verificando portas abertas do site {site} ===")
        check_open_ports(site)

        # Check if the site is offline
        print(f"\n{Fore.MAGENTA}=== Verificando se o site {site} está offline ===")
        check_site_status(site)

    except socket.gaierror:
        print(f"{Fore.RED}Não foi possível encontrar o IP para o site {site}. O site pode estar fora do ar ou não existe.")

# Function to verify the response time of the website
def get_website_response_time(site):
    try:
        ip = socket.gethostbyname(site)
        start_time = time.time()
        socket.create_connection((ip, 80), timeout=10)
        end_time = time.time()
        response_time = end_time - start_time
        print(f"\n{Fore.MAGENTA}=== Tempo de Resposta do site {site} ===")
        print(f"Tempo de resposta: {response_time:.2f} segundos")
    except socket.gaierror:
        print(f"{Fore.RED}Não foi possível encontrar o IP para o site {site}. O site pode estar fora do ar ou não existe.")
    except socket.timeout:
        print(f"{Fore.RED}O site {site} não respondeu em um tempo razoável.")

# Function to check if the site is offline
def check_site_status(site):
    try:
        response = os.system(f"ping -c 1 {site}")
        if response == 0:
            print(f"O site {site} está online.")
        else:
            print(f"O site {site} está offline.")
    except:
        print(f"{Fore.RED}Ocorreu um erro ao verificar o status do site {site}.")

# Function to check if the site is UDP or TCP
def check_site_protocol(site):
    try:
        # Implement here the check if the site is UDP or TCP
        print(f"\n{Fore.MAGENTA}=== Protocolo do site {site} ===")
        print(f"Verificação do protocolo em andamento...")
    except:
        print(f"{Fore.RED}Ocorreu um erro ao verificar o protocolo do site {site}.")

# Function to check the open ports of the site
def check_open_ports(site):
    try:
        ip = socket.gethostbyname(site)
        print(f"\n{Fore.MAGENTA}=== Portas Abertas do site {site} ===")

        port_found = False  # Variable to control if an open port is found

        for port in range(1, 1025):  # Checks ports from 1 to 1024
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((ip, port))
            if result == 0:
                print(f"Porta {port} está aberta.")
                port_found = True  # Set to True if an open port is found
                break  # Exit the loop since an open port is found
            sock.close()

        if not port_found:
            print(f"Todas as portas estão fechadas no site {site}.")
    except socket.gaierror:
        print(f"{Fore.RED}Não foi possível encontrar o IP para o site {site}. O site pode estar fora do ar ou não existe.")

# Main menu loop
message_counter = 0  # Initialize the message counter

while True:
    clear_screen()  # Clear the screen

    print_header("=== MENU ===")
    print_option(1, "Consultar IP de um site")
    print_option(2, "Verificar se o site está fora do ar")
    print_option(3, "Verificar tempo de resposta do site")
    print_option(4, "Verificar se o site é UDP ou TCP")
    print_option(5, "Verificar portas abertas do site")
    print_option(6, "Créditos")
    print_option(7, "Salves")
    print_option(0, "Sair")

    choice = int(input(f"{Fore.CYAN}Escolha uma opção: {Style.RESET_ALL}"))

    if choice == 1:
        site = input(f"{Fore.YELLOW}Digite o nome do site: {Style.RESET_ALL}")
        check_website_status(site)
    elif choice == 2:
        site = input(f"{Fore.YELLOW}Digite o nome do site: {Style.RESET_ALL}")
        check_site_status(site)
    elif choice == 3:
        site = input(f"{Fore.YELLOW}Digite o nome do site: {Style.RESET_ALL}")
        get_website_response_time(site)
    elif choice == 4:
        site = input(f"{Fore.YELLOW}Digite o nome do site: {Style.RESET_ALL}")
        check_site_protocol(site)
    elif choice == 5:
        site = input(f"{Fore.YELLOW}Digite o nome do site: {Style.RESET_ALL}")
        check_open_ports(site)
    elif choice == 6:
        print(f"\n{Fore.GREEN}Créditos: @ZedHacking no telegram {Style.RESET_ALL}")
    elif choice == 7:
        print(f"\n{Fore.GREEN}Salves para: guibppg, nero senka e slowz7{Style.RESET_ALL}")
    elif choice == 0:
        print(f"{Fore.RED}Saindo do programa...{Style.RESET_ALL}")
        break
    else:
        print(f"{Fore.RED}Opção inválida. Tente novamente.{Style.RESET_ALL}")

    message_counter += 1  # Increment the message counter

    if message_counter == 3:
        input("\nPressione Enter para continuar...")
        message_counter = 0  # Reset the message counter after two messages
