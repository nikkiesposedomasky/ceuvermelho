define n = Character("(...)", color="#B0B0B0")
define y = Character("Yamato")
define c = Character("Chiriro", color="#FFFFFF")
define a = Character("Ayato", color="#A020F0")
define z = Character("Zen", color="#FFD60A")


image a bravo = Transform("ayato_bravo.png", zoom=0.43)
image a bravofalando = Transform("ayato_bravofalando.png", zoom=0.43)
image a feliz = Transform("ayato_feliz.png", zoom=0.43)
image a felizfalando = Transform("ayato_felizfalando.png", zoom=0.43)
image a normal = Transform("ayato_normal.png", zoom=0.43)
image a normalfalando = Transform("ayato_normalfalando.png", zoom=0.43)
image a triste = Transform("ayato_triste.png", zoom=0.43)
image a tristefalando = Transform("ayato_tristefalando.png", zoom=0.43)


image c brava = Transform("chiriro_brava.png", zoom=0.50)
image c bravafalando = Transform("chiriro_bravafalando.png", zoom=0.50)
image c feliz = Transform("chiriro_feliz.png", zoom=0.50)
image c felizfalando = Transform("chiriro_felizfalando.png", zoom=0.50)
image c normal = Transform("chiriro_normal.png", zoom=0.50)
image c normalfalando = Transform("chiriro_normalfalando.png", zoom=0.50)
image c triste = Transform("chiriro_triste.png", zoom=0.50)
image c tristefalando = Transform("chiriro_tristefalando.png", zoom=0.50)


image y bravo = Transform("yamato_bravo.png", zoom=0.57)
image y bravofalando = Transform("yamato_bravofalando.png", zoom=0.57)
image y falandonormal = Transform("yamato_normalfalando.png", zoom=0.57)
image y feliz = Transform("yamato_feliz.png", zoom=0.57)
image y felizfalando = Transform("yamato_felizfalando.png", zoom=0.57)
image y normal = Transform("yamato_normal.png", zoom=0.57)
image y triste = Transform("yamato_triste.png", zoom=0.57)
image y tristefalando = Transform("yamato_tristefalando.png", zoom=0.57)

image z bravo = Transform("zen_bravo.png", zoom=0.45)
image z bravofalando = Transform("zen_bravofalando.png", zoom=0.45)
image z feliz = Transform("zen_feliz.png", zoom=0.45)
image z felizfalando = Transform("zen_felizfalando.png", zoom=0.45)
image z normal = Transform("zen_normal.png", zoom=0.45)
image z normalfalando = Transform("zen_normalfalando.png", zoom=0.45)
image z triste = Transform("zen_triste.png", zoom=0.45)
image z tristefalando = Transform("zen_tristefalando.png", zoom=0.45)

image bg escola2 = Transform(
    "escola2.png",
    xsize=config.screen_width,
    ysize=config.screen_height
)
image bg escola1 = Transform(
    "escola1.png",
    xsize=config.screen_width,
    ysize=config.screen_height
)

image bg rua1 = Transform(
    "rua1.png",
    xsize=config.screen_width,
    ysize=config.screen_height
)
image bg rua2 = Transform(
    "rua2.png",
    xsize=config.screen_width,
    ysize=config.screen_height
)
image bg rua3 = Transform(
    "rua3.png",
    xsize=config.screen_width,
    ysize=config.screen_height
)
image bg rua4 = Transform(
    "rua4.png",
    xsize=config.screen_width,
    ysize=config.screen_height
)
image bg shrine = Transform(
    "shrine.png",
    xsize=config.screen_width,
    ysize=config.screen_height
)
image bg shrine2 = Transform(
    "shrine2.png",
    xsize=config.screen_width,
    ysize=config.screen_height
)
image bg corredor = Transform(
    "corredor.png",
    xsize=config.screen_width,
    ysize=config.screen_height
)
image bg corredorvermelho = Transform(
    "corredor_vermelho.png",
    xsize=config.screen_width,
    ysize=config.screen_height
)
image bg corredor2 = Transform(
    "corredor2.png",
    xsize=config.screen_width,
    ysize=config.screen_height
)
image bg saladosprof = Transform(
    "saladosprof.png",
    xsize=config.screen_width,
    ysize=config.screen_height
)
image bg salavermelha = Transform(
    "sala_vermelha.png",
    xsize=config.screen_width,
    ysize=config.screen_height
)
image bg carrointerior = Transform(
    "interior_carro.png",
    xsize=config.screen_width,
    ysize=config.screen_height
)
image cadernocapa = "caderno_capa.png"
image cadernop1 = "caderno_pg1.png"
image cadernop2 = "caderno_pg2.png"
image chavecarro = "chave_carro.png"
image icone_caderno = Transform("caderno_capa.png", zoom=0.18)
default chave_carro = False
default mapa_carro = False
default pegou_caderno = False
default anotacoes = ""

label start:

    scene bg escola1 with fade
    n "Mais dez minutos."
    n "Só mais dez minutos."
    n "Ou pelo menos era o que eu achava."
    n "O relógio da sala parecia não se mover."
    n "Talvez estivesse quebrado."
    n "Talvez eu estivesse morrendo de tédio."
    show z normalfalando at left
    z "Puta que pariu."
    z "Eu não aguento mais."
    n "Zen jogou a cabeça na mesa."
    z "Quem inventou aula até esse horário devia ser preso."
    show c normalfalando at right
    c "Você fala isso em todas as aulas."
    z "Porque TODAS as aulas são longas."
    c "Você só não gosta de estudar."
    z "Exatamente."
    c "Pelo menos é honesto."
    z "Eu sou um homem de princípios."
    hide c normalfalando at right
    show a normalfalando at right
    a "Seus princípios são faltar aula e reclamar."
    hide z normalfalando at left
    show z felizfalando at left
    z "Tá vendo? Me entendem perfeitamente."
    hide z felizfalando at left
    hide a normalfalando at right
    n "A sala inteira parecia já ter desistido da aula."
    n "Algumas pessoas conversavam."
    n "Outras fingiam prestar atenção."
    n "O professor fingia que ninguém estava conversando."
    n "Era uma relação saudável."
    show z normalfalando at left
    z "Yamato."
    show y normal at right
    y "Hm."
    z "Me empresta a atividade."
    hide y normal at right
    show y falandonormal at right
    y "Não."
    z "Mas você nem fez ainda."
    y "Exatamente."
    z "Caramba, você é inútil."
    hide y falandonormal at right
    show c bravafalando at right
    c "Olha quem tá falando."
    z "Eu pelo menos admito."
    hide c bravafalando at right
    show a normalfalando at right
    a "Isso não melhora sua situação."
    z "Melhora sim."
    a "Como?"
    z "Porque eu sou sincero."
    hide a normalfalandol at right
    show a bravo at right
    n "Ayato apenas suspirou."
    n "Ele sempre tinha a mesma reação."
    n "Como se já esperasse aquilo."
    hide a bravo at right
    show c felizfalando at right
    c "Vocês viram que vai ter eclipse hoje?"
    hide z normalfalando at left
    show z felizfalando at left
    z "Ah é!"
    z "Tinha esquecido."
    hide c felizfalando at right
    show c normalfalando at right
    c "Como você esquece uma coisa dessas?"
    z "Eu esqueço meu aniversário às vezes."
    c "Isso é preocupante."
    z "É liberdade."
    hide c normalfalando at right
    show a normalfalando at right
    a "Não acho que seja."
    hide a normalfalando at right
    show c normalfalando at right
    c "Vai ser visível daqui da escola."
    z "Aposto que os professores vão tentar impedir a gente de ver."
    c "Claro que não."
    z "Eles sempre estragam a diversão."
    hide c normalfalando at right
    show a normalfalando at right
    a "Você considera olhar para o céu diversão?"
    z "Melhor do que matemática."
    n "Difícil discordar."
    hide a normalfalando at right
    show c normalfalando at right
    c "Você também, Yamato?"
    y "Não fui eu quem falou."
    c "Mas concordou."
    hide z felizfalando at left
    show y falandonormal at left
    y "Talvez."
    c "Traidor."
    n "Ela apontou para mim dramaticamente."
    hide y falandonormal
    show z felizfalando at left
    z "Finalmente alguém percebeu."
    c "Vocês dois são impossíveis."
    z "E você adora a gente."
    c "Infelizmente."
    hide c normalfalando at right
    show a normalfalando at right
    a "Ela tem razão."
    z "Vocês são muito cruéis comigo."
    n "Zen colocou a mão no peito."
    n "Como se tivesse acabado de sofrer a maior traição da história."
    hide z felizfalando at left
    show z tristefalando at left
    z "Meu próprio grupo me abandonou."
    hide a normalfalando at right
    show c normalfalando at right
    c "Milagre."
    hide z tristefalando at left
    hide c normalfalando at right
    n "Algumas pessoas começaram a guardar o material."
    n "O sinal estava próximo."
    n "Dava para sentir."
    n "A energia da sala mudava."
    n "Todo mundo parecia mais vivo."
    n "Como prisioneiros ouvindo os portões se abrirem."
    show z felizfalando at left
    z "Se o professor falar 'só mais uma coisa', eu vou embora."
    show c normalfalando at right
    c "Você não vai."
    z "Vou sim."
    hide c normalfalando at right
    show a normalfalando at right
    a "Não vai."
    z "Por que ninguém acredita em mim?"
    a "Histórico."
    z "..."
    z "Tá, justo."
    hide z felizfalando at left
    hide a falandonormal at right
    n "Acabei olhando pela janela."
    n "Sem motivo."
    n "Só olhei."
    n "O céu parecia estranho."
    n "Não vermelho."
    n "Não ainda."
    n "Mas havia algo errado."
    n "Como se a luz estivesse fraca demais."
    n "Como se estivesse ficando tarde muito rápido."
    n "Eu não sabia explicar."
    n "Mas aquilo me deixou inquieto."
    show c normalfalando at right
    c "Yamato?"
    show y falandonormal at left
    y "Hm?"
    c "Você tá encarando a janela faz um tempão."
    y "Tô pensando."
    c "Ih."
    hide y falandonormal at left
    show a normalfalando at left
    a "Perigoso."
    c "Muito perigoso."
    hide a normalfalando at left
    show y falandonormal at left
    y "Engraçadinhos."
    hide y felizfalando at left
    hide c normalfalando at right
    n "Eles riram."
    n "Eu também."
    n "Mas quando olhei para a janela novamente..."
    n "A sensação continuava lá."
    n "Como se alguma coisa estivesse esperando."
    n "E eu não fazia ideia do quê."
    n "Então o sinal tocou."
    show z felizfalando at left
    show c normalfalando at right
    z "ALELUIA!"
    c "Você não precisava gritar."
    z "Precisava sim."
    hide c normalfalando at right
    show a normalfalando at right
    a "A escola inteira ouviu."
    z "Ótimo."
    z "Que saibam que estou livre."
    n "E pela primeira vez naquele dia..."
    n "Acho que todos nós concordamos com ele."
    n "As cadeiras começaram a arrastar pelo chão no mesmo instante em que o sinal tocou."
    n "Todo mundo parecia estar esperando por aquilo há horas."
    show z felizfalando at left
    z "LIBERDADE!"
    hide z felizfalando
    show z feliz at left
    hide a normalfalando at right
    show c felizfalando at right
    c "Você vai acabar sendo expulso um dia."
    hide c felizfalando
    show c feliz at right
    show z felizfalando at left
    z "Vale a pena."
    hide z felizfalando
    show z feliz at left
    n "Zen praticamente se jogou para fora da sala."
    n "Nenhuma novidade."
    n "A gente seguiu atrás dele junto com o resto da turma."
    scene bg corredor with fade
    n "O corredor estava lotado."
    n "Alunos conversando, professores tentando organizar a saída e gente correndo sem motivo."
    show z normalfalando at left
    z "Ei, vocês vão fazer alguma coisa hoje?"
    hide z normalfalando
    show z normal at left
    show c normalfalando at right
    c "Eu vou sair com umas amigas."
    c "Se elas não cancelarem de novo."
    hide c normalfalando
    show c normal at right
    show z felizfalando at left
    z "Elas vão cancelar."
    hide z felizfalando
    show z feliz at left
    show c felizfalando at right
    c "Obrigada pelo apoio."
    hide c felizfalando
    show c feliz at right
    hide c feliz
    show a normal at right
    show a normalfalando at right
    a "Eu vou para casa."
    a "Tenho algumas coisas para resolver."
    hide a normalfalando
    show a normal at right
    show z felizfalando at left
    z "Você sempre tem alguma coisa pra resolver."
    z "Isso é suspeito."
    hide z felizfalando
    show z feliz at left
    show a felizfalando at right
    a "Talvez eu seja uma pessoa ocupada."
    hide a felizfalando
    show a feliz at right
    show z normalfalando at left
    z "Ou talvez você seja um agente secreto."
    hide z normalfalando
    show z normal at left
    show a felizfalando at right
    a "Você descobriu."
    hide a felizfalando
    show a feliz at right
    show z felizfalando at left
    z "EU SABIA!"
    hide z felizfalando
    show z feliz at left
    n "Chegamos aos armários."
    n "Pela primeira vez desde o sinal, estava relativamente silencioso."
    n "Relativamente."
    hide a feliz
    show y normal at right
    show z normalfalando at left
    z "Yamato."
    hide z normalfalando
    show z normal at left
    show y falandonormal at right
    y "Hm."
    hide y falandonormal
    show y normal at right
    show z felizfalando at left
    z "Você esqueceu alguma coisa, né?"
    hide z felizfalando
    show z feliz at left
    show y falandonormal at right
    y "Talvez."
    hide y falandonormal
    show y normal at right
    hide y normal
    show c normal at right
    show c normalfalando at right
    c "Ele esqueceu."
    hide c normalfalando
    show c normal at right
    show z felizfalando at left
    z "Eu sabia."
    hide z felizfalando
    show z feliz at left
    n "Abri meu armário."
    n "..."
    hide c normal
    show y normal at right
    show y falandonormal at right
    y "Achei."
    hide y falandonormal
    show y normal at right
    show z normalfalando at left
    z "O quê?"
    hide z normalfalando
    show z normal at left
    show y falandonormal at right
    y "Meu celular."
    hide y falandonormal
    show y normal at right
    hide y normal
    show c normal at right
    show c normalfalando at right
    c "Você esqueceu o celular no armário?"
    hide c normalfalando
    show c normal at right
    show z felizfalando at left
    z "Como alguém esquece o celular?"
    hide z felizfalando
    show z feliz at left
    hide c normal
    show y normal at right
    show y falandonormal at right
    y "Não faço ideia."
    hide y falandonormal
    show y normal at right
    n "Guardei as últimas coisas na mochila."
    n "Por algum motivo, meus olhos foram até a janela do corredor."
    n "A luz parecia estranha."
    n "Escura demais para aquele horário."
    n "Talvez fosse só impressão."
    hide y normal
    show c normal at right
    show c normalfalando at right
    c "Yamato?"
    hide c normalfalando
    show c normal at right
    hide c normal
    show y normal at right
    show y falandonormal at right
    y "Hm?"
    hide y falandonormal
    show y normal at right
    hide y normal
    show c feliz at right
    show c felizfalando at right
    c "Você tá encarando a janela de novo."
    hide c felizfalando
    show c feliz at right
    show z normalfalando at left
    z "Ele tá estranho desde a aula."
    hide z normalfalando
    show z normal at left
    hide c feliz
    show y normal at right
    show y falandonormal at right
    y "Tô normal."
    hide y falandonormal
    show y normal at right
    hide y normal
    show c feliz at right
    show c felizfalando at right
    c "Foi exatamente o que uma pessoa estranha diria."
    hide c felizfalando
    show c feliz at right
    hide c feliz
    show a feliz at right
    show a felizfalando at right
    a "Concordo."
    hide a felizfalando
    show a feliz at right
    hide a feliz
    show y normal at right
    show y falandonormal at right
    y "Obrigado pelo apoio."
    hide y falandonormal
    show y normal at right
    n "Os três riram."
    n "Terminamos de trocar os sapatos e pegar nossas coisas."
    n "Juntos, seguimos pelo corredor em direção à saída da escola."
    n "A luz lá fora parecia mais fraca do que deveria."
    n "Mas ninguém comentou nada."
    n "Ainda."
    scene bg escola2 with fade
    n "..."
    n "Assim que atravessamos o portão..."
    n "Meu corpo inteiro congelou."
    n "O céu."
    n "..."
    n "Estava vermelho."
    show y triste at left
    show c triste at right
    show c tristefalando at right
    c "...Gente?"
    hide c tristefalando
    show c triste at right
    show y tristefalando at left
    y "..."
    y "Vocês..."
    y "Estão vendo isso também?"
    hide y tristefalando
    show y triste at left
    hide c triste
    show z triste at right
    show z tristefalando at right
    z "Que porra..."
    hide z tristefalando
    show z triste at right
    n "Nenhum de nós ria."
    n "Nenhum de nós se mexia."
    n "A rua..."
    n "Estava completamente vazia."
    n "Sem carros."
    n "Sem pessoas."
    n "Sem o barulho da cidade."
    n "Só o vento."
    hide z triste
    show a triste at right
    show a tristefalando at right
    a "...Cadê todo mundo?"
    hide a tristefalando
    show a triste at right
    show y tristefalando at left
    y "..."
    y "Isso não faz sentido."
    hide y tristefalando
    show y triste at left
    n "Era horário de saída."
    n "As ruas deveriam estar cheias."
    n "Pais esperando os filhos."
    n "Ônibus."
    n "Bicicletas."
    n "Gente indo embora."
    n "Mas não havia..."
    n "Nada."
    hide a triste
    show c triste at right
    show c tristefalando at right
    c "Isso é alguma brincadeira?"
    c "Cadê o pessoal da escola?"
    hide c tristefalando
    show c triste at right
    show y tristefalando at left
    y "Olha pra trás."
    hide y tristefalando
    show y triste at left
    n "Todos viramos ao mesmo tempo."
    n "..."
    n "O pátio."
    n "Também estava vazio."
    n "As portas estavam abertas."
    n "As mochilas tinham sumido."
    n "As vozes."
    n "Tinham desaparecido."
    hide c triste
    show z triste at right
    show z tristefalando at right
    z "NÃO..."
    z "NÃO, NÃO, NÃO..."
    z "Isso não tem graça!"
    z "EI!"
    z "TEM ALGUÉM AÍ?!"
    hide z tristefalando
    show z triste at right
    n "A voz dele ecoou pela rua."
    n "..."
    n "Ninguém respondeu."
    hide z triste
    show c triste at right
    show c tristefalando at right
    c "P-Para..."
    c "Para de gritar..."
    c "Tá me assustando..."
    hide c tristefalando
    show c triste at right
    n "A voz dela tremia."
    n "Ela tentava parecer calma."
    n "Mas não conseguia."
    hide c triste
    show a triste at right
    show a tristefalando at right
    a "Meu celular..."
    a "Sem sinal."
    hide a tristefalando
    show a triste at right
    show y tristefalando at left
    y "O meu também."
    hide y tristefalando
    show y triste at left
    hide a triste
    show z triste at right
    show z tristefalando at right
    z "Liga pra polícia!"
    hide z tristefalando
    show z triste at right
    show y tristefalando at left
    y "Sem sinal."
    hide y tristefalando
    show y triste at left
    show z tristefalando at right
    z "Pros bombeiros então!"
    hide z tristefalando
    show z triste at right
    show y tristefalando at left
    y "Sem sinal."
    hide y tristefalando
    show y triste at left
    show z tristefalando at right
    z "Qualquer pessoa!"
    z "LIGA PRA QUALQUER PESSOA!"
    hide z tristefalando
    show z triste at right
    hide z triste
    show c triste at right
    show c tristefalando at right
    c "Minha mãe..."
    c "Ela não atende..."
    c "..."
    c "Ela sempre atende..."
    hide c tristefalando
    show c triste at right
    n "Ela apertava o celular com tanta força..."
    n "Que os dedos começaram a tremer."
    hide c triste
    show y triste at right
    show y tristefalando at right
    y "Respira."
    y "Todo mundo respira."
    hide y tristefalando
    show y triste at right
    n "Nem eu acreditava nas minhas próprias palavras."
    n "Mas se alguém entrasse em pânico..."
    n "Eu tinha a sensação de que..."
    n "Tudo ia piorar."
    n "E eu não fazia ideia do porquê."
    menu:

        "Explorar a cidade":
            jump explorar_cidade

        "Voltar para a escola":
            jump voltar_escola

        "Esperar um pouco":
            jump esperar

    label voltar_escola:

    show z triste at left
    show y triste at right
    show z tristefalando at left
    z "..."
    z "Não."
    z "Eu não vou sair andando por aí."
    hide z tristefalando
    show z triste at left
    show y falandonormal at right
    y "..."
    hide y falandonormal
    show y normal at right
    show z tristefalando at left
    z "Se isso for alguma pegadinha..."
    z "Tem que ter alguém lá dentro."
    hide z tristefalando
    show z triste at left
    hide y normal
    show c triste at right
    show c tristefalando at right
    c "Eu também acho..."
    c "Talvez os professores saibam o que tá acontecendo."
    hide c tristefalando
    show c triste at right
    hide c triste
    show a triste at right
    show a tristefalando at right
    a "Se eles estiverem aqui."
    hide a tristefalando
    show a triste at right
    show z tristefalando at left
    z "Eles têm que estar."
    z "Eles simplesmente têm."
    hide z tristefalando
    show z triste at left
    hide a triste
    show y triste at right
    show y tristefalando at right
    y "..."
    y "Vamos conferir."
    hide y tristefalando
    show y triste at right
    n "Voltamos pelo portão."
    n "O prédio continuava exatamente como alguns minutos atrás."
    n "As portas ainda estavam abertas."
    n "As luzes continuavam acesas."
    n "Os ventiladores ainda giravam lentamente."
    n "Mas..."
    n "Não existia um único som."
    scene bg corredorvermelho with dissolve
    show c triste at left
    show y triste at right
    show c tristefalando at left
    c "..."
    c "Cadê todo mundo?"
    hide c tristefalando
    show c triste at left
    show y tristefalando at right
    y "..."
    hide y tristefalando
    show y triste at right
    n "Olhei para as salas."
    n "Todas vazias."
    n "Nenhum professor."
    n "Nenhum aluno."
    n "Nenhum funcionário."
    n "Só carteiras perfeitamente alinhadas."
    hide y triste
    show z triste at right
    show z tristefalando at right
    z "EI!"
    z "TEM ALGUÉM AQUI?!"
    hide z tristefalando
    show z triste at right
    n "A voz do Zen ecoou pelo corredor."
    n "..."
    n "Ninguém respondeu."
    hide c triste
    show a triste at left
    show a tristefalando at left
    a "Até o eco parece estranho..."
    hide a tristefalando
    show a triste at left
    show z tristefalando at right
    z "Isso tá me irritando."
    z "Esse silêncio..."
    hide z tristefalando
    show z triste at right
    hide z triste
    show y triste at right
    show y tristefalando at right
    y "Não é só o silêncio."
    y "Olhem em volta."
    hide y tristefalando
    show y triste at right
    n "Foi só então que percebemos."
    n "Os armários."
    n "As mochilas."
    n "Os cadernos."
    n "Tudo tinha desaparecido."
    n "Como se nunca tivesse existido."
    hide a triste
    show c triste at left
    show c tristefalando at left
    c "M-Minha mochila..."
    c "...sumiu."
    hide c tristefalando
    show c triste at left
    show y tristefalando at right
    y "A minha também..."
    hide y tristefalando
    show y triste at right
    hide y triste
    show z triste at right
    show z tristefalando at right
    z "Tá legal..."
    z "Isso já deixou de ter graça faz tempo."
    hide z tristefalando
    show z triste at right
    hide c triste
    show a triste at left
    show a tristefalando at left
    a "Primeiro a cidade..."
    a "Agora isso..."
    hide a tristefalando
    show a triste at left
    show z tristefalando at right
    z "Vamos procurar a sala dos professores."
    z "Se tiver alguém nesse lugar..."
    z "Vai estar lá."
    hide z tristefalando
    show z triste at right
    show a tristefalando at left
    a "...É nossa melhor chance."
    hide a tristefalando
    show a triste at left
    scene bg corredor2 with dissolve
    n "Corremos até a sala dos professores."
    n "..."
    n "A porta não abriu."
    n "Ao lado da maçaneta havia um pequeno teclado numérico."
    show y triste at left
    show c triste at right
    show c tristefalando at right
    c "Ela... tá trancada?"
    hide c tristefalando
    show c triste at right
    show y tristefalando at left
    y "Parece que precisa de uma senha."
    hide y tristefalando
    show y triste at left
    hide c triste
    show z triste at right
    show z tristefalando at right
    z "Ótimo."
    z "Porque o dia claramente ainda podia piorar."
    hide z tristefalando
    show z triste at right
    n "Talvez exista alguma pista pela escola."
    jump puzzle_escola

    default viu_exercicios = False
    default viu_placa = False

    label puzzle_escola:

    menu:

        "Ir para a sala de aula":
            jump sala_aula_puzzle

        "Ir para a entrada":
            jump entrada_puzzle

        "Ir para a sala dos professores":
            jump professores_puzzle

    label sala_aula_puzzle:
    scene bg salavermelha with dissolve
    show y triste at left
    show z triste at right
    n "Nossa sala continuava exatamente como antes."
    n "As cadeiras ainda estavam enfileiradas."
    n "O quadro continuava cheio de anotações."
    n "Como se a aula nunca tivesse terminado."
    show z tristefalando at right
    z "Isso tá me dando um negócio ruim..."
    hide z tristefalando
    show z triste at right
    hide z triste
    show c triste at right
    show c tristefalando at right
    c "Espera..."
    c "Tem alguma coisa escrita ali."
    hide c tristefalando
    show c triste at right
    n "No canto do quadro havia apenas uma palavra."
    n "\"Exercícios\""
    n ""
    n "5"
    n "8"
    n "3"
    n "4"
    show y falandonormal at left
    y "5834..."
    hide y falandonormal
    show y normal at left
    show c tristefalando at right
    c "Você acha que é a senha?"
    hide c tristefalando
    show c triste at right
    show y falandonormal at left
    y "Vale a tentativa."
    hide y falandonormal
    show y normal at left
    scene bg corredor2 with dissolve
    show y normal at left
    show z triste at right
    n "Voltamos correndo até a sala dos professores."
    n "Teclado ainda aguardava senha."
    $ senha = renpy.input("Digite a senha.", length=4)
    $ senha = senha.strip()
    if senha == "5834":
        n "*BEEP*"
        n "Senha incorreta."
        show z tristefalando at right
        z "Sério?"
        z "Nem essa..."
        show y falandonormal at left
        n "Então esse número não era a resposta."
        hide z tristefalando
        show z triste at right
        show c tristefalando at right
        n "Ou talvez a gente tenha interpretado errado..."
        hide c tristefalando
        jump puzzle_escola

    elif senha == "1998":

        jump saladosprof

    else:

        n "*BEEP*"
        n "Senha incorreta."
        show z tristefalando at right
        z "Droga..."
        hide z tristefalando
        show z triste at right
        jump puzzle_escola

    label entrada_puzzle:

    scene bg escola2 with dissolve
    show y normal at left
    show a triste at right
    n "Voltamos até a entrada."
    n "O silêncio continuava absoluto."
    n "Ao lado das portas havia uma placa metálica."
    show a tristefalando at right
    a "..."
    a "Essa placa sempre esteve aqui?"
    hide a tristefalando
    show a triste at right
    n ""
    n "Hoshizora High School"
    n "Fundada em"
    n "1998"
    show y falandonormal at left
    y "1998..."
    hide y falandonormal
    show y normal at left
    show a tristefalando at right
    a "Não deve significar nada..."
    hide a tristefalando
    show a triste at right
    hide a triste at right
    hide y normal at left
    scene bg corredor2 with dissolve
    $ viu_placa = True
    n "Voltamos correndo até a sala dos professores."
    n "Teclado ainda aguardava senha."
    $ senha = renpy.input("Digite a senha.", length=4)
    $ senha = senha.strip()
    if senha == "5834":
        n "*BEEP*"
        n "Senha incorreta."
        show z tristefalando at right
        z "Sério?"
        z "Nem essa..."
        show y falandonormal at left
        n "Então esse número não era a resposta."
        hide z tristefalando
        show c tristefalando at right
        n "Ou talvez a gente tenha interpretado errado..."
        hide c tristefalando
        jump puzzle_escola
    elif senha == "1998":

        jump saladosprof

    else:

        n "*BEEP*"
        n "Senha incorreta."
        show z tristefalando at right
        z "Droga..."
        hide z tristefalando
        show z triste at right
        jump puzzle_escola

    label professores_puzzle:

    show y normal at left
    show z triste at right

    n "A porta permanecia trancada."

    n "O teclado aguardava uma senha."

    $ senha = renpy.input("Digite a senha.", length=4)
    $ senha = senha.strip()
    if senha == "5834":
        n "*BEEP*"
        n "Senha incorreta."
        show z tristefalando at right
        z "Sério?"
        z "Nem essa..."
        show y falandonormal at left
        n "Então esse número não era a resposta."
        hide z tristefalando
        show z triste at right
        show c tristefalando at right
        n "Ou talvez a gente tenha interpretado errado..."
        hide c tristefalando
        jump puzzle_escola
    elif senha == "1998":

        jump saladosprof

    else:

        n "*BEEP*"
        n "Senha incorreta."
        show z tristefalando at right
        z "Droga..."
        hide z tristefalando
        show z triste at right
        jump puzzle_escola

    label saladosprof:

    scene bg saladosprof with dissolve

    show y normal at left
    show z triste at right
    n "A porta se abriu com um estalo baixo."
    n "..."
    n "A sala dos professores estava completamente vazia."
    n "Nenhuma cadeira fora do lugar."
    n "Nenhuma caneca de café."
    n "Nenhum computador ligado."
    n "Como se todos tivessem simplesmente... desaparecido."
    show z tristefalando at right
    z "..."
    z "Eu odeio isso."
    hide z tristefalando
    show z triste at right
    hide z triste
    show a triste at right
    show a tristefalando at right
    a "Olhem."
    hide a tristefalando
    show a triste at right
    n "Em cima de uma das mesas havia um molho de chaves."
    show y falandonormal at left
    y "Acho que são das salas."
    hide y falandonormal
    show y normal at left
    n "Peguei o molho de chaves."
    $ pegou_chave = True
    scene bg salavermelha with dissolve
    show y normal at left
    show c triste at right
    n "Voltamos para nossa sala."
    n "A chave girou facilmente."
    n "A porta se abriu."
    n "..."
    n "As carteiras continuavam onde sempre estiveram."
    n "As mochilas dos outros alunos haviam desaparecido."
    n "Os estojos."
    n "Os livros."
    n "Tudo."
    n "Só havia uma coisa diferente."
    show c tristefalando at right
    c "...Yamato."
    hide c tristefalando
    show c triste at right
    show y falandonormal at left
    y "Hm?"
    hide y falandonormal
    show y normal at left
    show c tristefalando at right
    c "Olha a sua mesa."
    hide c tristefalando
    show c triste at right
    n "No centro da minha carteira..."
    n "Havia um caderno preto."
    hide c triste
    show z triste at right
    show z tristefalando at right
    z "Esse caderno era seu?"
    hide z tristefalando
    show z triste at right
    show y falandonormal at left
    y "..."
    y "Eu..."
    y "Não lembro."
    hide y falandonormal
    show y normal at left
    n "No centro da minha carteira..."
    n "Havia um caderno preto."

call screen caderno_mesa

screen caderno_mesa():

     imagebutton:
        idle Transform("caderno_capa.png", zoom=1.5, rotate=-12)
        hover Transform("caderno_capa.png", zoom=1.5, rotate=-15)

        xpos 150
        ypos -220


        action Jump("abrir_caderno")

label abrir_caderno:

    scene black

    show cadernocapa

    ""

    menu:
        "Abrir o caderno":
            jump pagina1

label pagina1:

    show cadernop1

    ""

    menu:
        "Próxima página":
            jump pagina2

label pagina2:

    show cadernop2

    ""

    menu:
        "Fechar o caderno":
            jump depois_caderno

label depois_caderno:

    scene bg salavermelha with fade

    show y triste at left
    show c triste at right

    show c tristefalando at right
    c "..."
    c "Essa é a sua letra?"
    hide c tristefalando
    show c triste at right

    show y tristefalando at left
    y "Acho que sim..."
    y "Mas eu não lembro de ter escrito isso."
    hide y tristefalando
    show y triste at left

    hide c triste
    show a triste at right

    show a tristefalando at right
    a "...Isso não tem graça."
    hide a tristefalando
    show a triste at right

    show y tristefalando at left
    y "..."
    hide y tristefalando
    show y triste at left

    show a tristefalando at right
    a "Você fez isso?"
    hide a tristefalando
    show a triste at right

    show y tristefalando at left
    y "Não."
    y "E mesmo se tivesse feito..."
    y "Por que eu esqueceria?"
    hide y tristefalando
    show y triste at left

    hide a triste
    show z triste at right

    show z tristefalando at right
    z "Quer saber?"
    z "Leva esse negócio."
    z "Se alguém deixou isso pra você..."
    z "Pode acabar sendo importante."
    hide z tristefalando
    show z triste at right

    n "Guardei o caderno na mochila."

    $ pegou_caderno = True
    $ anotacoes = "• O céu ficou vermelho.\n• A cidade desapareceu.\n• Encontramos um caderno estranho."
    n "Obtido: Caderno de Anotações."

    jump convergencia

    label convergencia:

    scene bg salavermelha
    show screen botao_caderno

    show y triste at left
    show z triste at right

    n "Ninguém dizia nada."

    n "O silêncio da escola era pior do que qualquer grito."

    n "Os ventiladores ainda giravam lentamente no teto."

    n "As luzes continuavam acesas."

    n "Era como se o mundo inteiro tivesse parado..."

    n "Menos nós."

    show z tristefalando at right
    z "..."
    z "Tá."
    z "Eu já cansei de esperar."
    hide z tristefalando
    show z triste at right

    show y tristefalando at left
    y "..."
    hide y tristefalando
    show y triste at left

    hide z triste
    show c triste at right

    show c tristefalando at right
    c "Você quer fazer o quê?"
    hide c tristefalando
    show c triste at right

    hide c triste
    show z triste at right

    show z tristefalando at right
    z "Procurar alguém."

    z "Qualquer pessoa."

    z "Professor."

    z "Polícia."

    z "Sei lá."

    z "Ficar parado não tá adiantando."

    hide z tristefalando
    show z triste at right

    hide z triste
    show a triste at right

    show a tristefalando at right
    a "Concordo."

    a "Quanto mais tempo ficarmos sem entender o que aconteceu..."

    a "Pior."

    hide a tristefalando
    show a triste at right

    show y tristefalando at left
    y "..."

    y "Antes."

    y "Tem uma coisa."

    hide y tristefalando
    show y triste at left

    hide a triste
    show c triste at right

    show c tristefalando at right
    c "Hm?"

    hide c tristefalando
    show c triste at right

    show y tristefalando at left
    y "Esse caderno."

    y "Ele dizia para escrever tudo."

    y "Se nossa memória falhar..."

    y "Talvez isso seja a única forma de lembrar."

    hide y tristefalando
    show y triste at left

    hide c triste
    show a triste at right

    show a tristefalando at right
    a "Então faça."

    a "Escreva tudo."

    hide a tristefalando
    show a triste at right

    n "Abri o caderno novamente."

    n "As páginas em branco pareciam esperar por alguma coisa."

    n "Peguei uma caneta."

    n "Respirei fundo."

    n "Escrevi a primeira anotação."

    $ primeira_anotacao = True
    $ anotacoes += "\n• Meus amigos são: Zen, Ayato e Chiriro."
    n "Nova anotação adicionada ao Caderno."

    hide a triste
    show z triste at right

    show z tristefalando at right
    z "Então..."

    z "Pra onde agora?"

    hide z tristefalando
    show z triste at right

    n "Antes que alguém respondesse..."

    n "UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU..."

    n "..."

    n "Uma sirene."

    n "Muito distante."

    n "Durou apenas alguns segundos."

    n "Depois..."

    n "Silêncio."

    hide z triste
    show c triste at right

    show c tristefalando at right
    c "..."

    c "Vocês ouviram isso...?"

    hide c tristefalando
    show c triste at right

    hide c triste
    show a triste at right

    show a tristefalando at right
    a "Sim."

    a "Veio da cidade."

    hide a tristefalando
    show a triste at right

    hide a triste
    show z triste at right

    show z tristefalando at right
    z "Isso significa que tem alguém."

    z "Ou..."

    z "Alguma coisa."

    hide z tristefalando
    show z triste at right

    show y tristefalando at left
    y "..."

    y "Só existe um jeito de descobrir."

    hide y tristefalando
    show y normal at left

    hide z triste
    show z normal at right

    show z felizfalando at right
    z "Finalmente."

    z "Vamos sair daqui."

    hide z felizfalando
    show z normal at right

    n "Pela primeira vez desde que o céu ficou vermelho..."

    n "Tínhamos uma direção."

    label explorar_cidade:

    scene bg rua4
    show screen botao_caderno

    show y triste at left
    show z triste at right

    n "Assim que atravessamos o portão da escola..."

    n "O silêncio ficou ainda pior."

    n "Não era só porque não havia pessoas."

    n "Era como se a cidade inteira tivesse perdido o direito de fazer barulho."

    n "Nenhum vento."

    n "Nenhum pássaro."

    n "Nenhum cachorro."

    n "Nada."

    show z tristefalando at right
    z "..."

    z "Eu odeio isso."

    z "Prefiro quando as coisas fazem sentido."

    hide z tristefalando
    show z triste at right

    hide z triste
    show c triste at right

    show c tristefalando at right
    c "Zen..."

    c "Você nunca prefere quando as coisas fazem sentido."

    hide c tristefalando
    show c triste at right

    hide c triste
    show z triste at right

    show z tristefalando at right
    z "É..."

    z "Mas isso aqui já passou dos limites."

    hide z tristefalando
    show z triste at right

    n "Continuamos andando."
    hide z triste at right

    scene bg rua2 with fade

    n "O primeiro cruzamento da cidade continuava funcionando."

    n "O semáforo alternava normalmente entre vermelho e verde."

    n "Mesmo sem um único carro."

    show a triste at right

    show a tristefalando at right
    a "A energia ainda está ligada..."

    a "Então por que..."
    hide a tristefalando
    show a triste at right

    show y tristefalando at left
    y "..."

    y "Não sei."

    hide y tristefalando

    scene bg rua3 with fade
    show screen botao_caderno

    n "Passei por uma loja de conveniência."

    n "As luzes ainda estavam acesas."

    n "As prateleiras continuavam cheias."

    n "A porta permanecia aberta."

    show c tristefalando at right

    c "Será que..."

    c "Tem alguém aí?"

    hide c tristefalando

    n "..."

    n "Nenhuma resposta."

    n "Nem mesmo o som da geladeira."

    n "Tudo parecia congelado."

    n "Mais à frente..."

    n "Uma bicicleta estava caída no meio da rua."

    show z tristefalando at right

    z "Ela caiu faz pouco tempo."

    z "Olha a corrente."

    hide z tristefalando
    show z triste at right

    show y tristefalando at left

    y "Como você sabe?"

    hide y tristefalando
    show y triste at left

    show z tristefalando at right

    z "..."

    z "Não sei."

    z "Só sinto isso."

    hide z tristefalando


    n "Foi então que vimos."

    n "Um carro parado no meio da avenida."

    jump puzzle_carro

    label puzzle_carro:
        scene bg carrointerior with fade

        n "A porta do motorista estava aberta."

        n "Como se alguém tivesse saído às pressas."

        screen carro_screen():

            add "bg carrointerior"

            use botao_caderno

            if not chave_carro:

                imagebutton:

                    idle Transform("chave.png", zoom=0.10)
                    hover Transform("chave.png", zoom=0.12)

                    xpos 1075
                    ypos 640

                    action Jump("achou_chave")

            else:

                imagebutton:

                    idle Transform("portaluvas.png", zoom=1.0)
                    hover Transform("portaluvas_hover.png", zoom=1.0)

                    xpos 1140
                    ypos 240

                    action Jump("abrir_portaluvas")               

    label achou_chave:

        scene bg carrointerior

        show screen botao_caderno

        show y triste at left

        n "..."

        show y tristefalando at left
        y "Tem alguma coisa aqui."
        hide y tristefalando
        show y triste at left

        n "Me abaixei entre os bancos."

        n "Era uma chave."

        $ chave_carro = True

        $ anotacoes += "\n• Encontramos uma chave dentro de um carro."

        n "Obtido: Chave do carro."

        jump puzzle_carro

    label abrir_portaluvas:

        scene bg carrointerior_aberto

        show screen botao_caderno

        n "*Clique.*"

        n "O porta-luvas abriu."

        n "Lá dentro havia um mapa dobrado."

        menu:

            "Pegar o mapa":

                pass

        $ pegou_mapa = True

        n "Obtido: Mapa da Cidade."

        jump convergencia
