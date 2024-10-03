# Importando módulos necessários
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import NoSuchElementException
import csv
import time
from constants import (
    USERNAME,
    PASSWORD,
    COMMASEPARATED,
    CONNECTION_MESS,
    UPTO_PAGE,
    BCOLORS,
)


# Configuração inicial do WebDriver
def configurations():
    global driver

    # Inicializa o WebDriver Chrome
    driver = webdriver.Chrome()

    # Navega para a página de login do LinkedIn
    driver.get("https://www.linkedin.com/login")


# Classe para operações com arquivos CSV
class Csv_io:
    def __init__(self, filename, mode, newline):
        self.filename = filename
        self.mode = mode
        self.newline = newline

        self.openfile()
        self.writer_setup()

    def openfile(self):
        # Abre o arquivo CSV para escrita
        self.file_to_write = open(self.filename, mode=self.mode, newline=self.newline)

    def writer_setup(self):
        # Configura o objeto de escrita CSV
        self.csv_writer = csv.writer(self.file_to_write)

    def insert_row(self, info):
        # Insere uma nova linha no arquivo CSV
        self.csv_writer.writerow(info)


# Classe para operações na página web
class Webpage:
    def visit(self, url):
        # Navega para a URL especificada
        driver.get(url)

    def click_with_css_selector(self, css_selector):
        # Clica em um elemento usando seletor CSS
        driver.find_element(css_selector).click()

    def grab_text_with_css_selector(self, css_selector):
        # Obtém o texto de um elemento usando seletor CSS
        return driver.find_element(css_selector).text

    def get_url(self):
        # Retorna a URL atual da página
        return driver.current_url


# Classe para operações do navegador
class Browser:
    def end_session(self):
        # Finaliza a sessão do WebDriver
        driver.quit()

    def wait(self, duration):
        # Espera implícita por um tempo específico
        driver.implicitly_wait(duration)


# Função para logar mensagens no console


def log(text):
    print(text)


# Função principal
def main():
    configurations()

    # Inicializa o objeto CSV_IO para gerenciar o arquivo CSV
    csv_io = Csv_io("OutputFolder/dataset.csv", "a", "")

    webpage = Webpage()
    browser = Browser()

    # Aguarda por 2 segundos antes de prosseguir
    browser.wait(2)

    # Realiza login no LinkedIn
    userName = driver.find_element(By.ID, "username")
    userName.clear()
    userName.send_keys(USERNAME)
    userName.send_keys(Keys.RETURN)

    password = driver.find_element(By.ID, "password")
    password.clear()
    password.send_keys(PASSWORD)
    password.send_keys(Keys.RETURN)

    # Loop através das palavras-chave e páginas
    for keyword in list(COMMASEPARATED.split(";")):
        for page in range(1, int(UPTO_PAGE) + 1):
            time.sleep(5)

            link = f"https://www.linkedin.com/search/results/people/?keywords={keyword}&origin=CLUSTER_EXPANSION&network=%5B%22S%22%2C%22O%22%5D&page={page}"

            driver.get(link)

            # Espera até que os cartões de resultados estejam presentes na página
            list_of_cards = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located(
                    (By.CLASS_NAME, "reusable-search__result-container")
                )
            )

            log(f"TOTAL CARDS{len(list_of_cards)} - KEYWORD {keyword} - PAGE {page}")

            first_number = None

            # Loop através dos cartões de resultados
            for i in range(1, len(list_of_cards) + 1):
                time.sleep(2)

            try:
                button_connect = driver.find_elements(
                    By.CSS_SELECTOR, "span.artdeco-button__text"
                )

                connect_found = False
                for label in button_connect:
                    if "connect" in label.text.lower():
                        connect_found = True
                        print(f"Botão de conexão encontrado para o cartão {i}")
                        break

                if not connect_found:
                    print(f"Nenhum botão de conexão encontrado para o cartão {i}")
                else:
                    print(f"Verificação concluída para card {i}")

                time.sleep(1)

                # Clica no nome da pessoa
                person_name_link = driver.find_element(
                    By.CSS_SELECTOR,
                    f"li[class='reusable-search__result-container']:nth-child({i}) span.app-aware-link",
                )
                person_name_link.click()
                time.sleep(2)

                # Aguarda a página do perfil carregar
                WebDriverWait(driver, 10).until(lambda driver: driver.title != "")

                # Extrai informações do perfil
                name_grab = driver.find_element(By.CSS_SELECTOR, "h1").text
                description1 = driver.find_element(
                    By.CSS_SELECTOR, "div.entity-result__primary-subtitle"
                ).text
                link_to_profile = driver.current_url

                # Loga informações do perfil
                log(
                    f"{BCOLORS.WARNING}{name_grab} who is {description1} at {link_to_profile}{BCOLORS.ENDC}"
                )

                info = [name_grab, description1, link_to_profile]

                csv_io.insert_row(info)

                time.sleep(1)

                # Clica no botão Conectar para todos os cards
                connect_button = driver.find_element(
                    By.CSS_SELECTOR,
                    f"li[class='reusable-search__result-container']:nth-child({i}) button[aria-label='Connect']",
                )
                connect_button.click()
                time.sleep(0)

                # Envia solicitação de conexão
                send_now_button = driver.find_element(
                    By.XPATH, "//button[@aria-label='Send now']"
                )
                send_now_button.click()

                time.sleep(1)

            except Exception as e:
                log(f"Erro ao acessar o perfil da pessoa {i}: {e}")

                # webpage.visit(link)

                # browser.wait(10)

                # except NoSuchElementException:
                #     pass
                # except Exception as e:
                #     log(e)

        log(
            f"{BCOLORS.UNDERLINE} All New Connection's data appended to dataset.csv {BCOLORS.ENDC}"
        )

    browser.end_session()

    csv_io.insert_row(["---------", "----------", "----------", "-------------"])


if __name__ == "__main__":
    main()
