from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from fake_useragent import UserAgent
import random
import time
import pickle
import os
import pyautogui

def arrayUsers():
    return ["celestino4433", "pari19653", "dylan.lanzkhie", "dheiciane_", "neidedacruzmorais", 
            "santosfehlberg", "dixx_bianquinha777", "guibson.krause", "geysi_souza_krause", 
            "adrielmodelo", "dixx_annyx5", "financasmh.investimentos_", "__earn_with_emily_crypto___", 
            "iasmim_nasci", "anaclaramoreira20", "rafaelpereirajr06", "markooliver16", "sousaluana79", 
            "flavio_aguiar888", "wendelmcosta", "priv.e5454", "marloncarpanedo", "lilianesilvamota",
            "yasmin.dpw", "cris_da_pecuaria", "larissarroberta", "larah_santana27", "andremartins88", 
            "023_paula", "samara._.maiaa", "_privisantos", "vitoriarocon3", "talleskrause", 
            "souza_de_oliveira_1747", "kaikrochaborges7", "rute_araujo_dos_santos_", "qvs__antony", 
            "rpzwzz_", "erick_leandroo", "pedrokaua721", "eduardo_du_244", "rodrig0500", 
            "vitorianovaisluiza", "luana_santos_2008_", "jok_brsv", "gessicadasilvamoreira", 
            "lais.santos73", "bruno.saviofc", "meick_d", "edilenesilvaneto", "valquiriabarrosbn", 
            "lycia_ollyver", "rikelmygbn", "maicucharde", "thau.annyconceicao", "nicolas_gatto23", 
            "vhannly.nina.067", "conectatualmagrandemente2022", "itzanaaaaaa_", "jose_frois_mel", 
            "_lucassoouza_", "alvesolivino", "joyce_lash_dsigner", "danilo_costa_23", "ea_vivi_ts", 
            "daniel_santos_m4y", "dr.leomoreira_pabn", "xydavinz", "doutores_da_fisio_", 
            "simplexmente_eu", "duda_antonioli", "parque_dois_irmao_", "chay_felix123", 
            "kamyla.oliv", "phatriciagomes", "ligia_hubner", "katiely_rs", "t.martins22", 
            "julianaaparecida6730", "pk_rech01", "rana.andrade.737", "rhillaryadele", 
            "future_architect9", "erikzannon", "soudiney", "kleyselima", "adriele_alvesroldao", 
            "dheysedossantosoliveira", "thacy__souzanb", "gustavo10i", "vanessesouza", 
            "_samara.maia", "cristianesantos4832", "ildinho_lopes", "keury__araujo", "_dxx.brenda", 
            "carlinhos_dofuti", "yasmin_oliiveiraaa", "melissa_cristinef", "kayky_felicio", 
            "dixxkariny2", "filipe_caetano22", "_gileade_mota_", "marvinsymon", "c_gabriel_s2", 
            "e_samaramenezes", "0_seshomaru_0", "neres.eulandya", "loreee_limaaa45", "pk_rech04", 
            "kelry_mayyy", "yx.maby_", "felbergkrodrigo", "lileiagomes", "eulandya.neres", 
            "larialbuquerque25", "pr.moschen", "viniciuss_moreir", "tpertel", "karolina_oliveirra", 
            "priscila.dionisio_", "leonardosousa9276", "nelma_nunes_voigt", "pamllisboa", 
            "suelley31", "silvestregonzalez55", "manassesbomfim", "inara.mourao", "neiflorencio", 
            "mailonfrota", "vieiraronaldoluz", "isllafreitascorrea", "kayani_kock_dos_santos_", 
            "camilinha_gameplay", "esther.neres", "investor_anna_melissa_", "brenda_sousaara", 
            "pardalzin_xs", "izaelma_lima", "apunhalar", "donadom0neyoficial", "asher_variedades_", 
            "eveli_kaline", "eduardo.lagares_16", "alinecosta010", "joelmada_conceicao51", 
            "perfect.pisos", "almeiddri", "irene.claver", "edna23mar", "valdeudsonsousa", 
            "gislaine_gla", "karolaine_maijore", "andreany_vesper", "mirian_santtosx", "simone14hs", 
            "danyllo.vital", "mr_apple_mania", "amanda_menezes_", "daianesarter", 
            "frases_e_textos_romsnticos", "juliacaldeira585", "raimundaamorim623", "ped.trem0", 
            "mariliafelberg", "lucas_joaquim_krause_", "podiodamarcha", "srta_loose", "nadiaa.silv", 
            "jhonatagomeskrause_24", "davw_willian_", "kailany_55", "eugabrielarocha27", 
            "karyn.ferreira381", "patricia_suellen_s", "gabriell.custodio_", "lobatovanessa1210", 
            "djennys1", "claudineybritto2022", "menezes_maria_eduarda_", "roger_io44", 
            "fabriciopatrick7", "iasmim152020", "oliveirakloss", "kariny_corradi", "joatham_souza", 
            "britto.thainara19", "preto_barber", "priscilacarvalhobn", "_ronaldok_", "lp783209", 
            "wyslaney_karkara", "jhonata_de_moura", "rafaelfehlber", "alencaster.a.l.i.c", 
            "cyntia_rodrigs", "auisllan_medeiros", "mayarabreger_16", "jv_vaqueiro_afamado17", 
            "_comeceinvestiir", "siderleidicheti", "raquellopes_ben", "hectorrcervantesmindset", 
            "jorgemiriampires", "lavbolhas", "jig.kg", "katriel_agro", "silva_anne05", 
            "nathy_cs55", "_biancardi", "dixx_guto5", "paulo.cleiton.128", "ederdiassegantini", 
            "drykaasselvatico", "b_girardello", "polikempner", "paulopaivabueno", 
            "gabriellucas76543", "maizamoraiss", "lindelainejp", "ilianaolliveira", 
            "salve_salve_erika_lima_", "eduarda_freitas3105", "kleber4492", "jeansousa233", 
            "rubiacearural", "ninguem._.689", "mattapauloandreida", "reigilasarter", 
            "cherrynezambon", "alexiafillvock", "gabriel_.santo_s", "lara_kryscia_paiva", 
            "krauselourdes", "fabio.krause.167", "kailanypulcena3", "leticiia_boa", "taynaradsc", 
            "luciajoaquimkrause", "savio.pagung", "david_krauze563", "carol_mayy_", 
            "ricardo_fehlberg", "use.novaera", "mikaffreitas", "gabrielevital_designer", 
            "taty_annalivya", "anapancierii", "gabriel.usbert", "luciopandini", "marieduboisladdy", 
            "itsjessica.bas", "paivasalomao559", "olavo_1", "18mk2002", "lumiar_eco_lodge", 
            "oxente_cuscuzaria1", "willes.carlos.33", "vanessa_selvatico", "10edsonfarias", 
            "trade_mark_fx_", "noe.dividendos", "victorlopesduartee", "ivy_the_lion", "hosanadesing", 
            "polianazanon", "soueudeborah", "samuel.tessaro", "_taty_fr", "higor_bubu", 
            "_nathielly_silvaa", "flavio.lovatti", "moschenfc123", "mxrix_yxyx", "cafezar", 
            "beakrenak", "edna.valandro", "jadson_krause", "felipe_martins5412", "danielamello224", 
            "wri_vitor", "gislainegla", "kristianobreno", "carlosbleck", "carla_segrini", 
            "ianlucas7798", "raielyalvesferreira", "chiessilmb", "otavio_n.martins", 
            "angelicalagares1", "peterramaldes", "raul.belmont", "nutri_wrihelvitor", 
            "charonerocha_oficial", "lucassilveirar", "faustinopagode", "hadamoegito", "doug_s_leal", 
            "mc_pedrinho_oficial_4m_45", "kelvinludwig", "eduarda_thomaz", "marlon_willian_215", 
            "sarabatistahonorato", "janykelly_almeida", "wirecuco", "valquiriapenido", 
            "angellica_krause", "josycunhaoficial", "duas_rodas_moto_pecas", "byul_byu", 
            "bruna_boti21", "fr_tawane", "gui.klesse", "mainnyofc", "fran_luizaribeiro0", 
            "werisson_01", "bianka_franca_", "deivisoncasagrande", "coming_sooncoming", "rgvbatera", 
            "leo___5___", "sofia.baptista1", "americajeans23", "nayaneantoniogervasio", 
            "laysacostalonga", "jbbenfatti", "marlon_vitor_kelete", "jb_benfat", 
            "juliapassosoficial", "wanderson.p.silva.1609", "isis.bruneti", "nildarodrigues75", 
            "marcioberetagt", "ludmila_vif", "george.dasilva3", "gabryellfonseca26", 
            "keziaa.sousa", "elidianenoronha", "ana_paula_olivee", "r_aiamorim", "thaylon_thyago", 
            "kariny__080", "ribasmakciele", "alencar_bocaiuva", "miriaalves.ofc", "eduardacaetano15", 
            "almeidasa21", "luanabnovo", "efraim_farias14", "kretlisousa14", "arliene.nsc_", 
            "debora_maclicya", "juli4passos", "dasilva_george", "arlindo_ns", "vanessasantos3922", 
            "wellington_23gomes", "andressaalves532", "leticiadelazari27", "_ph.araujo", 
            "shoptudoparatodos", "alimola99003", "renan_fornaciari", "babixavierr", 
            "dayannivaladares", "claramorais1402", "gilhenriquehb", "pamelafracalossi", 
            "kamilaaguiarnunes", "camillatres", "rafaelmodeneseprado", "joaopgod", "henriqueruiqi", 
            "flavio_ld", "rayssalimah95", "mayralealdesigner", "liviany.oliveira", "ronnysrocha80", 
            "drums_jao", "joapaulo3731", "na.bi9801", "cleberlinsl", "jaogustavo_", 
            "marcio.jose.liberato", "lucelia.bn_", "jacqueline.braun2", "mayarabreger", 
            "sarterzinha_oficial", "keci_jhones", "mirele__9", "cristinagomesjoaquim", 
            "cleversonbarrere", "mariajosenascimento272", "brenovalle2022", "caike.oliveira.gtr", 
            "ailtokrause", "dirceujalmesdelazzari", "luiz.venturote", "dra_ludianykrause", 
            "esflixteleconsultor", "gazoli5", "lauvresanilda", "vilsofehlberg", "marloni_bazon", 
            "lucas_artigo_244_", "francisca_das_gracas_12", "sirleyjoaquimkrause", "josycuhaoficial", 
            "theus_msouza", "rosylima9217", "maysa_lyma22", "goldshop.br", "marcoantoniocalletti", 
            "lucasjoaquimkrause", "samuelgomeskrause", "carollainypaiva", "dhabicoin", 
            "tron_o_futuro_comecou", "ganhe.dinheiro.tron", "wendemcesar", "krisluthier", 
            "ledsonoliveiraaraujo", "anaeudasantos", "regigomeskrause", "rayssa.lima_gomes.14", 
            "vivianemoreiraclinic", "mais_arquitet10", "francidalva_silva12", "edilenejesusdias", 
            "bruch_rosy007", "akila_assis_zanetti", "mailsombraga", "franciscomartins1975", 
            "dinoshomeestradeiros", "elianepratessilva", "jean.lopesp", "utilidade_esaude", 
            "margaramessiasb", "almirfrancielledaviddaniel", "_patrickcoelho", "felberg_kaua12", 
            "eu_luborges", "dayane9795", "stiflerperfumaria", "adriano.bragatto", "deboraassism", 
            "jayane.99", "vinicius.3003", "krausecalvi_kevily", "helianipinho", "nycholas_valle", 
            "thiellystrelow", "was.menezes", "caian.meireles", "zago_bia", 
            "concreta.corretoradeseguros", "cacauway.med", "krausetharlys", "gleicianykrause", 
            "tayna_albu", "danielelimavital", "komakicolatina", "sousadeoliveirakrause", 
            "assembleiadedeuscolatina", "valeria_porto56", "edineuza1709", "tamara_cts51", 
            "danielbatista5896", "brandaoplaster", "norton.victor", "_cassia.ataide_", "cris_rnails", 
            "gabriele_krause7", "isabela_krause_an", "darliane.lima.509", "alicecoutoimportados", 
            "eduardocoutto", "talitasouzabn", "davi_osantos", "keilacostaoliv", "colatinagram", 
            "naracristina_oliveira", "tarikmorais2018", "papercyclecompany", "desativadosamira", 
            "margaramessias", "lava_jatovipcar", "monkgameplay", "fernandesluisbarbosa", 
            "gabriel.r.ribeiro", "vicentinill", "brunamello87", "duceucosta", "scarlath_horrara", 
            "andressa.sannttos", "beth_grama_", "fe_zanonidias", "felipecherque", "alzianetjacob", 
            "renatolp_"]

# Function to login to Instagram
def login_instagram(username, password, driver):
    # Maximize the browser window
    driver.maximize_window()
    # Path to the cookies file
    cookies_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cookies.pkl")
    # Access the Instagram website
    driver.get("https://www.instagram.com/")
    # If cookies file exists, load the cookies
    if os.path.exists(cookies_file):
        with open(cookies_file, "rb") as file:
            cookies = pickle.load(file)
        for cookie in cookies:
            driver.add_cookie(cookie)
        driver.refresh()
    time.sleep(5)
    # Try to handle notifications popup
    try:
        not_now_notifications_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[text()="Agora não"]')))
        not_now_notifications_btn.click()
    except TimeoutException:
        pass
    # Try to login
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'username')))
        driver.find_element(By.NAME, 'username').send_keys(username)
        driver.find_element(By.NAME, 'password').send_keys(password)
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        # Try to handle save login info popup
        try:
            time.sleep(5)
            not_now_btn = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//div[contains(text(),"Agora não")]')))
            not_now_btn.click()
        except TimeoutException:
            pass
        # Try to handle notifications popup
        try:
            time.sleep(5)
            not_now_notifications_btn = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//button[text()="Agora não"]')))
            not_now_notifications_btn.click()
        except TimeoutException:
            pass
        # Dump cookies
        with open(cookies_file, "wb") as file:
            pickle.dump(driver.get_cookies(), file)
    except Exception as e:
        print(f"An error occurred while logging in: {e}")

# Function to comment on a post
def comment_on_post(post_url, base_comment, driver, num_comments):
    pessoas = arrayUsers()
    
    for i in range(num_comments):
        url = random.choice(post_url)
        driver.get(url)
        time.sleep(10)

        if len(pessoas) < 2:
            print("Não há usuários suficientes para continuar postando comentários.")
            break

        base_comment = base_comment.lower() if random.random() < 0.5 else base_comment.upper()

        # Choose three random, non-repeating users
        chosen_users = random.sample(pessoas, 1 if url == 'https://www.instagram.com/p/Csl0l5hutaR/' else 2)

        # Remove chosen users from the list
        for user in chosen_users:
            pessoas.remove(user)

        comment = base_comment
        for user in chosen_users:
            comment += " @" + user

        comment_box = driver.find_element(By.XPATH, '//textarea[@aria-label="Adicione um comentário..."]')
        comment_box.click()
        time.sleep(1)

        # Select all text in the input field
        #pyautogui.hotkey('ctrl', 'a')

        # Press backspace to delete all selected text
        #pyautogui.press('backspace')

        comment_box = driver.find_element(By.XPATH, '//textarea[@aria-label="Adicione um comentário..."]')
        # Send the keys one by one
        for letter in comment:
            comment_box.send_keys(letter)
            time.sleep(random.uniform(0.1, 0.3))
        time.sleep(1)

        post_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//div[contains(text(), "Publicar")]')))
        post_button.click()

        print(f"Comentário #{i + 1}: {comment} às {time.strftime('%H:%M:%S')}")
        # Pause for a random time between 50 and 70 seconds
        time.sleep(random.randint(90, 120))

# Main function
def main():
    # Instagram username and password
    username = 'guibson.krause'
    password = 'jRtLjm6556600'
    # URL of the post to comment on
    post_url = ['https://www.instagram.com/p/CszmiXExcpI/',
                'https://www.instagram.com/p/Cs9gsFrJjeK/',
                'https://www.instagram.com/p/Csl0l5hutaR/']
    # Base comment
    comment = 'Me deseje boa sorte'
    # Path to the webdriver
    webdriver_service = Service(ChromeDriverManager().install())
    # Create webdriver
    driver = webdriver.Chrome(service=webdriver_service)

    try:
        # Login to Instagram
        login_instagram(username, password, driver)
        time.sleep(2)
        # Comment on post
        comment_on_post(post_url, comment, driver, 60)
        time.sleep(2)
    finally:
        # Quit driver
        driver.quit()

if __name__ == "__main__":
    main()
