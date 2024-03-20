import time
import ChromeDriverManager as ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import pickle
import os
import pyautogui

driver = webdriver.Chrome(ChromeDriverManager().install())

def bot(num_coment, post_url):
    pessoas = ["loy_jeck", "agro_3divisa.brasil", "lucasxipaia", "araujo.cleisiane", "xavier.kamylla",
               "mardholy_kelete_", "erick_leandroo", "yx.maby_", "os_boiadeiros_da_230", "souza.denisesantosde",
               "vini__caxiado", "murilo.moschen", "grazielehelinch", "gabxxt", "frutuosonalia", "lrluiz",
               "renata.damasco", "bruno.saviofc", "priv.e5454", "iasmim_nasci", "mariane_medeiros_455", "dixx_isis__",
               "alaidy_silva__", "danty_tkd", "rogerioselvaticodos", "thai_mello24", "wendelmcosta", "any_andrade8",
               "geysi_souza_krause", "eaeleo25", "rammys_teixeira", "andremartins88", "elaine_silva_influencer",
               "jardel_m4rques", "maia_gracieny", "flavio_aguiar888", "idila_silv4", "dixx_pipoh", "yasmin_oliiveiraaa",
               "nutri.personal_sirleirezende", "dixx_annyx5", "cristinajoaquinadasilva", "arthur_mardegan",
               "emillylopesdeassis", "depilpele", "dixx_rechin", "franchagas_78", "raquellopes_ben",
               "mariaheloisacruztomaela01", "lorrane_caetanoo", "_rech", "vaqueirinho_gaucho244", "barreto_v021",
               "eu.thiago_alves", "andressaalves532", "rebeka_faryas", "dr.leomoreira_pabn", "tamiresarcanjo_",
               "kelvisson_edite", "kelry_mayyy", "assesoria_kamylinha_ofc", "marloncarpanedo", "pk_rech01",
               "comercio_com_lisa80", "cavalo_forte_bn", "paulla6613", "fazendarf_grf", "nagilafrutuoso191",
               "earaujo14", "r.barbosa_01", "whwbkwkw", "eugabrielarocha27", "neres.eulandya", "c_gabriel_s2",
               "luxuoso_bn", "jrinacio43", "allciany._.martiins", "hamburguergourmet52", "thamyresdixx",
               "salao.brilho.demulher", "dixx_lavanholis2", "jumara_figueiredo", "fagner__067", "rafaelfehlber",
               "eduarda_srosario", "ines_fnd2012", "biancardi_bruna", "josycunhaoficial", "kai0_santos", "mmilene262",
               "petric591", "danii_022_", "marcela_lopesw", "mariliafelberg", "eli.sayury17", "jhonatagomeskrause_24",
               "joel.jhonata.18", "rhitinha_oliveirra", "kailany_55", "kariny__080", "wuanderson55", "sammya_cardoso",
               "griffith_story", "raimundaamorim623", "rosilanefernandes85", "britto.thainara19", "oliveirakloss",
               "tauanny_b_de_almeida407", "eduardo.lagares_16", "nicolly_willemann", "_eusthefny",
               "bruna_fernandes.olv", "poly_oliveira8", "lilianegarcia93", "rafael_martins679", "angelasouza__16",
               "moschenclaudio", "aninha_silvahhhhh", "leandro0liveira_", "filipp_sperotto", "eu_yara_8", "privv_ylg",
               "buttowisk2022", "laura.milly2", "leo___5___", "spelamarys", "najllasabrinny", "lindelainejp",
               "05.netinho", "pereira__gislaine", "capschool_english", "sofia_pinheiro111", "mirnamoschenbarros",
               "yara_lorranee", "luanaandrade2122", "leticiia_boa", "suelley31", "keury__araujo", "fabio.krause.167",
               "nutrimais_pecuaria", "marcelo_do_pix071_", "jociane2005", "emiliagarciamoschen", "ilianaolliveira",
               "johnny_valleoficial", "mayarabreger_16", "priihshantos", "sarterzinha_oficial", "alinedecristo5",
               "andersomrony", "jinacio8", "dayane_luysa", "monicacarvalho618", "rafaeljong19", "carolinaricarti",
               "marcelrech", "alinemelo_093", "brayanp.desouza", "danilo_costa_23", "paulocesarmartinss_",
               "luizsantos7492", "ezequiel2019brasilgmail.com1", "deivid_rigoni18", "amaro.thamires",
               "valdilene.lara18", "fazendacantagaloo", "privaterocha_", "armandowandersondasilva", "evell.ynandrade",
               "jameson_alves_18", "allineportoh", "nelore_tocantins", "jhennysilva.a", "carolina45281", "carol_mayy_",
               "nikeury__menezes", "mxrix_yxyx", "marlon_vitor_kelete", "adrianorodrigues4455", "lihanny_hanauer",
               "heitor.carneiro.9655", "regigomeskrause", "alves_aguiuria", "vilsofehlberg", "andre_fernandes_bn244",
               "celine__cardoso", "m.heloisa_gomes", "geovana_vitalino", "ricardo_fehlberg", "made.in2009_",
               "celia_flogueira_oficial", "karyn.ferreira381", "kevely_sarter", "rana.andrade.737", "dixx_iay",
               "enzo_andrade51", "ana_dinniz344", "rayanne.fernandes.16144", "nanaamaralatelie", "evelyn12ns",
               "marcosvenicios007", "rm_mello07", "joselene510", "cia.derodeiormbulls", "gorete4140", "espanta_ranch",
               "pauloxingu13", "stephanny_silva_17", "sennaramon5", "gulhevy_", "raisarter", "suzana_costa.17",
               "esteffanyferreira2", "menezes.leticiadecarvalho", "yasmin_sarter", "taty_annalivya", "willianaferberk",
               "otavio_n.martins", "grazy.grazy.d", "valdeilap", "valdicleia_paiva", "caykmay", "pinhoeloah",
               "willians.carvalho_", "kellysilva065", "sofiarammoos", "maysm.priv", "bn_vet_", "coming_sooncoming",
               "inmetricsoficial_br", "natalia_loewecke", "higorsousa41", "felipe_martins5412",
               "adaylson_pelxoto_da_silva_160", "grupomaturu", "meullycoss", "agnicia.alves", "pamella_beatrizf",
               "layane.frutuoso.9", "filemom_dheficy", "bladimir.peralta.507", "terceirao2023bn", "mello_eloysa",
               "janiele_oliveiraaa", "fran_neerys", "duas_rodas_moto_pecas", "_ssamilly", "wilkesantos__",
               "david_krauze563", "jessicaferreirasoaresf", "brito_da_pecuaria", "allana.sl_", "bruno_brandao91",
               "tomazinimarcela", "fazenda_santa.ines", "filipe_caetano22", "vitor_kelete", "silva_anne05",
               "cyannasilva774", "ana_luiiza015", "jefersonferreira763", "vinicius_kbn", "clevebaiano",
               "everson_carvalho_45", "weldonsouza9", "aderlanypereira", "alinne_albuquerque03", "graziellyarajo373",
               "enfjhenifferrodrigues", "josycuhaoficial", "any_kristinaa", "jamily.s_", "katiely.santos",
               "2.0.0.3__lara", "estefanysouza63", "geovana.biancardi", "katiely_rs", "bruno_silver__trader332",
               "rodrigues_keven_", "douglasquiezi", "gabriel_.santo_s", "carla_valurim", "lucielly_balbino_",
               "romario.candido.315", "daniele.lima.1023611", "mainara_figueiredo", "juliasilva20953",
               "gleicy_albuquerque01", "_kamylla_santos21", "ws_linny", "silva_amandaa_5", "michelly.r_20",
               "adv.carolineoliveiraa", "lileiagomes", "sarterrichelmy", "teofilocleusa", "sabrina_arruda_mecca",
               "madeinroca2022", "geovanesilva7503", "aiceb.pinheiro", "2526cristiano", "felipemartins136",
               "inaciojose23", "_.marcosaguiar", "bs_bruna__", "maycon_rzt01", "nykoly_figueiredo", "_hr_ranch_",
               "camila_rech22", "kedimanails", "petric417", "kescamilo", "elajoycce_silva26", "marcelo_pix_fortunato",
               "mirian_keila18", "flaviogardem", "efraim_farias14", "jhonata_barbeiro10", "pr.moschen",
               "rodrigues22cawboy", "estheroliveira52021", "danilo09226", "alcianymartins654", "aline._rochaa",
               "karolinasouza27337", "edrienesilvagomes", "gdhclili", "sophia_antonelli_", "guilherme_peixoto_17",
               "izaadrade", "vaqueraotestado", "hera_kons.tantina.94", "alexa_ndre7600", "brombis_", "murillo_niraj",
               "werisson_01", "lucivania3087", "lucas_precheca17", "monicafeller2020", "edenilso_1oliveira", "guzxr",
               "mirele__9", "m.vet.cowboy.loeblein", "beatrizmarques6865", "tropa_do_agro_pr", "mayarabreger",
               "liviia_caetano", "lucas_joaquim_krause_", "darlanysousaof", "lucassvoigt", "sidneyy.10", "b_girardello",
               "ricardo_santos212", "macielsperotto", "samiriasantoss", "_rech__sx", "_nathy_mrr_", "jesus_motivacao",
               "olheiro97196", "miriaalves.ofc", "loosil_", "yasminfehlberg1263", "pedrohenrriquesantosaraujo",
               "paulo.coxta7", "jhonathanmendesr", "voigtlarisse", "wenicio_araujo", "rezendebergamin", "ar.jhenifer",
               "daniel_sousa_barbosa_", "kaianoliveira_", "denisgoncalvesdg", "wenderson_bitencourt", "6577_celia",
               "carvalho_reis_06", "ramosvenicios", "sartersilva", "equiexplosion_sp", "may.anacarolina2006",
               "eu_leh_fehlberg_", "kelsonrd_oficial", "hozeysilva45", "caeduardo2073", "erdesign_de_sobrancelha",
               "felbergkrodrigo", "kessialara.o2018", "sabrii_namello", "lorrany_4567", "nmarcosgo", "raio__11__",
               "bruno_rafaelsales", "janekellybatistaaraujo", "lucivaniaalmieda60", "page_country_western",
               "lubatistask", "paulocesar.martins.5876", "evillyncristina2021", "xavierrhaykelly", "fra.n31",
               "mikael.menezesf4000", "samuelgomeskrause", "pathvargens", "_gileade_mota_", "mariakarolinadesouza",
               "raquelsilva3941", "dayne_1830", "layenne_nogueira", "williamlopes.ferreira", "paixaoyanna",
               "camxlla__karen", "marcel__rech", "simonepereiradac", "calvimiguelaraujo", "iklusl", "david.krauze.7",
               "maycon_costa_da_silva", "wendemcesar", "luisfilipe016", "claudiomarviana_", "amanda_ponciana",
               "iarima_taina", "reginaldoaguiarsilva", "luam.chagas.soares", "dinoshomeestradeiros",
               "derlianycandido.77", "pk_rech04", "def4ult_its_a_magic", "karoldejesus0844", "jerlienev15",
               "kayani_kock_dos_santos_", "mariasousabn", "gabrielevital_designer", "andersonferreira9047",
               "dheyson_do_agro", "sabrinaa_andradx", "mariaheloisacruztomaela", "thaisbrito128", "iasmim152020",
               "gabryellfonseca26", "melolilia84", "josecarlo_s1", "hozeys", "lucasjoaquimkrause", "rubens_santos1999",
               "duorty_paola", "evellyn_andrade1513", "nicollywillimann_", "canela_vaqueiro_", "galvao911",
               "anaclaramoreira20", "leandro87reis", "horse_training_pro", "gehmendes_07", "geovani3131",
               "mariasabrinasoaresde", "fehlbergricardo", "sabrinamelllo123", "nathallia_santtos22",
               "robson_santos2001", "oelcimo_souza", "_maria_gaabs", "morais_livya", "felberg_kaua12", "wenicio_xavier",
               "valerialima127", "kevyllencosta195", "ricardorodrigues_rick", "xorrena_ynda_", "carolmesquitah",
               "brunosilva1230101", "karinee_paiva_", "terere_dos_cria", "casa_e_pao", "emylle_krause",
               "vivianefcsilva", "afrancilenelima", "beatriz_barros_07", "tallyta_sarah", "robwardetex", "lopesiklus",
               "legalpremium_", "maria_gabrieli_pontes", "alice_sbiancardi", "gabriella_sampaio13m",
               "krausecalvi_kevily", "souza_de_oliveira_1747", "kerginaldokf", "dye_go_04", "kayky.dantas69",
               "vinicius.3003", "thamires_biancard", "_queren_hapuquee_", "josean_azevedo", "letyciakrause_",
               "letticya_lucenna", "welvis_silva09", "sousadeoliveirakrause", "semnomedeusuariopfv", "cost.apaulo",
               "luisfilipefeudesouza"]
    comentario = ''
    for i in range(num_coment):
        try:
            url = random.choice(post_url)
            driver.get(url)
            time.sleep(10)
            pessoas_escolhida = random.sample(pessoas, 1 if url == 'https://www.instagram.com/p/Csl0l5hutaR/' else 2)

            # Remove chosen users from the list
            for user in pessoas_escolhida:
                pessoas.remove(user)
                comentario += ' @' + user

            # Localiza o campo de comentário pelo XPath
            comment_field = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//textarea[@placeholder='Adicione um comentário...']"))
            )
            comment_field.click()

            # Select all text in the input field
            #   pyautogui.hotkey('ctrl', 'a')

            # Press backspace to delete all selected text
            #   pyautogui.press('backspace')

            comment_field = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//textarea[@placeholder='Adicione um comentário...']"))
            )
            comment_field.send_keys(comentario)  # Insira o texto do comentário desejado

            botao_publicar = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//div[contains(text(), "Publicar")]'))
            )
            botao_publicar.click()
        except StaleElementReferenceException:
            pass
        # Aguarda um tempo antes de executar novamente
        time.sleep(random.randint(90, 120))


def login(driver):
    # Abre o Instagram
    driver.get("https://www.instagram.com/")
    time.sleep(5)

    # Path to the cookies file
    cookies_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cookies.pkl")

    # If cookies file exists, load the cookies
    if os.path.exists(cookies_file):
        with open(cookies_file, "rb") as file:
            cookies = pickle.load(file)
        for cookie in cookies:
            driver.add_cookie(cookie)
        driver.refresh()
    else:
        try:
            # Localiza e preenche o campo de usuário pelo XPath
            username_field = driver.find_element(By.XPATH, "//input[@name='username']")
            username_field.send_keys("Murilo.moschen")

            # Localiza e preenche o campo de senha pelo XPath
            password_field = driver.find_element(By.XPATH, "//input[@name='password']")
            password_field.send_keys("adedonha98765")

            # Localiza e clica no botão de login pelo XPath
            login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
            login_button.click()

            # Aguarda o login ser concluído
            time.sleep(5)
            # Dump cookies
            with open(cookies_file, "wb") as file:
                pickle.dump(driver.get_cookies(), file)
        except Exception as e:
            print(f"um erro ocorreu durante o login: {e}")


# Insira o link do post do Instagram
post_url = ['https://www.instagram.com/p/CszmiXExcpI/',
            'https://www.instagram.com/p/Cs9gsFrJjeK/',
            'https://www.instagram.com/p/Csl0l5hutaR/']

# Inicializa o driver do Chrome
driver = webdriver.Chrome()

login(driver)

# Executa o bot
bot(160, post_url)

# Fecha o navegador
driver.quit()
