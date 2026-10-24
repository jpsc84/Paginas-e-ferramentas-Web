"""Módulo 11 ampliado (v4.3): construção de cena, estilos visuais, técnicas e parâmetros."""
from data_items1 import it, P, ITEMS
_START = len(ITEMS)

IMG = ["portatil", "chatgpt", "gemini", "copilot", "grok", "midjourney", "firefly"]
HOW_STYLE = ("Copie, troque os campos entre colchetes e mantenha a ordem: assunto, cena, composição, luz, cor, estilo, formato. "
             "No Midjourney, acrescente parâmetros como --ar no final; nos demais, escreva a proporção por extenso.")
LIM_STYLE = ("Descreva características do estilo em vez de citar artistas vivos, marcas ou personagens protegidos. "
             "Confira mãos, texto, proporções e detalhes pequenos no tamanho final.")
SRC_GEN = ["C4", "J1", "M2"]

def scene(title, what, how, ex, lim, src=SRC_GEN):
    it(11, "Cena: " + title, ["prompt"], IMG, what, how, ex, lim, src, origin="v4")

def style(title, what, ex, lim=LIM_STYLE):
    it(11, "Estilo: " + title, ["prompt"], IMG, what, HOW_STYLE, ex, lim, SRC_GEN, origin="v4")

def tech(title, kinds, plats, what, how, ex, lim, src):
    it(11, "Técnica: " + title, kinds, plats, what, how, ex, lim, src, origin="v4")

# ---------- Construção de cena ----------
scene("ficha completa de cena",
      "Modelo-mestre para descrever uma imagem com todos os elementos que mais influenciam o resultado.",
      "Preencha só os campos que importam; campos vazios deixam a IA decidir. Use frases concretas (de onde vem a luz, que objeto fica em primeiro plano) em vez de adjetivos vagos.",
      "Assunto: [quem ou o quê, com idade, roupa, expressão]. Ação: [o que está fazendo]. Ambiente: [lugar, época, clima, hora do dia]. Primeiro plano: [objeto]. Fundo: [elementos]. Enquadramento: [plano e ângulo]. Lente: [focal e profundidade de campo]. Luz: [fonte, direção, dureza, cor]. Paleta: [3 a 5 cores]. Estilo: [fotografia, ilustração, pintura, 3D]. Textura e acabamento: [grão, pincelada, brilho]. Atmosfera: [sensação]. Formato: [proporção e uso]. Evite: [elementos indesejados].",
      "Prompts muito longos podem gerar conflitos entre instruções; se o resultado sair confuso, corte para os 5 campos mais importantes.")
scene("enquadramento e ângulo",
      "Define o quanto do assunto aparece e de onde a câmera olha.",
      "Escolha um plano (geral, conjunto, médio, americano, close, detalhe) e um ângulo (altura dos olhos, plongée de cima para baixo, contra-plongée de baixo para cima, vista aérea zenital, ponto de vista subjetivo, ângulo holandês inclinado).",
      "Plano médio de uma cozinheira sorrindo ao provar um molho, câmera levemente em contra-plongée, altura do peito, cozinha profissional ao fundo desfocada, luz lateral quente, formato 4:5.",
      "Ângulos extremos podem distorcer rosto e mãos. Peça um só ângulo por imagem.")
scene("lente e profundidade de campo",
      "Usa vocabulário fotográfico para controlar perspectiva e desfoque.",
      "Grande angular (16 a 24 mm) amplia o espaço e distorce bordas; 35 mm é natural e documental; 50 mm próximo do olho humano; 85 a 135 mm comprime o fundo e favorece retratos; macro mostra detalhes. Abertura grande (f/1.4 a f/2.8) desfoca o fundo; pequena (f/8 a f/16) deixa tudo nítido.",
      "Retrato de um senhor pescador na beira do rio, lente de 85 mm, f/1.8, fundo com bokeh suave de reflexos na água, foco nos olhos, luz de fim de tarde, formato 3:4.",
      "A IA simula o efeito; números de lente não garantem óptica exata. Tilt-shift e olho de peixe podem exagerar.")
scene("iluminação",
      "Controla clima, volume e realismo pela descrição da luz.",
      "Diga a fonte (sol, janela, luminária, neon), a direção (frontal, lateral, contraluz, de cima), a qualidade (dura com sombras marcadas ou suave difusa) e a temperatura (quente, neutra, fria). Esquemas úteis: hora dourada, hora azul, luz de janela, Rembrandt (triângulo de luz na bochecha), três pontos de estúdio, recorte de contraluz, luz de vela, neon noturno.",
      "Mulher lendo junto à janela, luz natural suave vindo da esquerda, sombras longas no chão de madeira, poeira visível no feixe de luz, tons quentes de fim de tarde, atmosfera tranquila, formato 16:9.",
      "Fontes de luz conflitantes geram sombras incoerentes; mantenha uma luz principal.")
scene("paleta e gradação de cor",
      "Fixa as cores dominantes e o tratamento de cor da imagem.",
      "Liste de 3 a 5 cores com nomes claros (azul-petróleo, terracota, creme) e diga o tratamento: alto contraste, tons pastel, monocromático, dessaturado, cores complementares, grade cinematográfica laranja e azul-esverdeado.",
      "Cena de café de bairro ao amanhecer, paleta restrita a verde-oliva, creme e cobre, baixa saturação, contraste suave, sem cores vibrantes.",
      "Códigos hexadecimais nem sempre são respeitados; prefira nomes de cores e confira na imagem final.")
scene("composição",
      "Organiza os elementos para guiar o olhar e reservar espaço útil.",
      "Indique regra dos terços, centralização simétrica, linhas guia, moldura natural, diagonal, primeiro plano com profundidade ou espaço negativo para texto (diga em que lado).",
      "Ciclista solitário em estrada de terra, posicionado no terço inferior direito, estrada formando linha guia até o horizonte, céu amplo ocupando dois terços superiores como espaço livre para título, formato 16:9.",
      "Se o espaço para texto for essencial, confira se ficou realmente vazio; a IA às vezes preenche.")
scene("atmosfera, clima e época",
      "Acrescenta condições do ambiente que mudam a sensação da cena.",
      "Combine estação do ano, tempo (neblina, chuva fina, neve, poeira, calor), hora e época histórica ou futura. Elementos atmosféricos ajudam a dar profundidade.",
      "Rua de paralelepípedos de uma cidade colonial brasileira em manhã de neblina, década de 1950, lampiões ainda acesos, chão molhado refletindo a luz, poucas pessoas com roupas da época.",
      "Detalhes históricos podem sair anacrônicos; confira roupas, carros e placas.")
scene("materiais e texturas",
      "Descreve superfícies para dar realismo ou acabamento artístico.",
      "Nomeie materiais (madeira crua, mármore polido, linho, couro gasto, vidro fosco, metal escovado) e o acabamento (fosco, acetinado, brilhante, oxidado). Em ilustração, cite a técnica (aquarela granulada, guache opaco, lápis de cor).",
      "Mesa de madeira de demolição com xícara de cerâmica artesanal esmaltada em azul, guardanapo de linho amassado, colher de latão envelhecido, luz suave lateral realçando as texturas, foto em close.",
      "Texturas finas podem ser suavizadas na geração; peça close quando o material for o foco.")
scene("personagem detalhado",
      "Descreve uma pessoa ou personagem original de forma consistente e respeitosa.",
      "Informe faixa etária, traços gerais, cabelo, roupa, acessórios, postura e expressão. Evite pedir semelhança com pessoas reais sem autorização.",
      "Personagem original: mulher de cerca de 35 anos, cabelo cacheado preso em coque, óculos redondos, camisa de linho verde-oliva, relógio de couro, sorriso discreto, segurando uma prancheta, postura confiante.",
      "Não use para imitar pessoas reais identificáveis. Detalhes como acessórios podem mudar entre gerações.")
scene("cena com várias pessoas ou objetos",
      "Organiza múltiplos elementos sem que se misturem.",
      "Descreva cada elemento com posição (à esquerda, ao centro, ao fundo) e uma característica própria. Limite a três ou quatro elementos principais.",
      "Mesa de reunião vista de lado: à esquerda, homem de camisa azul apontando um gráfico no notebook; ao centro, mulher de blazer cinza tomando notas; à direita, jovem de moletom amarelo sorrindo; janela ao fundo com cidade desfocada.",
      "Contagem e posição de pessoas falham com frequência; confira e regere a partir da melhor versão.")

# ---------- Estilos ----------
style("fotografia editorial", "Visual de revista, com narrativa e luz cuidada.",
      "Fotografia editorial de uma empreendedora em sua oficina de cerâmica, retrato ambiental em plano médio, luz natural de janela lateral, paleta terrosa, profundidade de campo rasa, textura de filme sutil, formato 4:5.")
style("fotojornalismo documental", "Aparência espontânea e real, sem pose.",
      "Foto documental em preto e branco de uma feira livre no Nordeste ao amanhecer, momento espontâneo de um feirante entregando frutas, lente 35 mm, grão visível, contraste alto, sem pose.",
      "Não use para criar imagens que possam ser confundidas com registros de fatos reais. " + LIM_STYLE)
style("retrato corporativo", "Foto profissional para perfil ou site.",
      "Retrato corporativo de um homem de 40 anos, camisa social clara, fundo cinza neutro com leve gradiente, luz de estúdio suave em três pontos, expressão confiante e acessível, enquadramento de busto, formato 1:1.")
style("fotografia de produto (packshot)", "Produto isolado e nítido para catálogo ou loja.",
      "Foto de produto de um frasco de perfume de vidro âmbar, fundo infinito branco, luz de estúdio difusa com reflexo controlado, sombra suave no chão, foco total, ângulo frontal levemente elevado, formato 1:1, sem texto.")
style("produto em ambiente (lifestyle)", "Mostra o produto em uso, em contexto real.",
      "Caneca térmica verde sobre a mesa de um escritório em casa, notebook aberto ao fundo desfocado, manhã com luz de janela, planta ao lado, sensação de rotina organizada, formato 4:5.")
style("fotografia gastronômica", "Comida apetitosa com estilo de revista.",
      "Prato de moqueca baiana em panela de barro, vista de cima em 45 graus, vapor visível, folhas de coentro frescas, toalha de linho e talheres antigos ao lado, luz natural lateral, fundo escuro de madeira, formato 4:5.")
style("arquitetura e interiores", "Ambientes com linhas retas e luz equilibrada.",
      "Sala de estar minimalista com pé-direito duplo, janelas do chão ao teto, sofá de linho cru, piso de cimento queimado, plantas grandes, luz do meio da manhã, lente grande angular com linhas verticais corrigidas, formato 16:9.")
style("paisagem e natureza", "Cenas abertas com profundidade e clima.",
      "Paisagem dos Lençóis Maranhenses ao nascer do sol, lagoas de água azul-turquesa entre dunas brancas, céu com nuvens rosadas, primeiro plano com ondulações de areia, vista ampla, formato 16:9.")
style("cinematográfico (still de filme)", "Quadro com cara de cena de cinema.",
      "Still cinematográfico de um homem esperando em uma estação de trem vazia à noite, formato anamórfico 2.39:1, luz fria de lâmpadas fluorescentes e reflexos no piso molhado, grade de cor azul-esverdeada e laranja, grão de filme, clima de suspense.")
style("fotografia analógica", "Estética de filme fotográfico, com grão e cores de época.",
      "Foto de família em um quintal no verão, aparência de filme 35 mm colorido dos anos 1990, cores levemente desbotadas, grão visível, luz dura de meio-dia, enquadramento casual, formato 3:2.")
style("ilustração vetorial flat", "Formas simples e cores chapadas para web e apresentações.",
      "Ilustração vetorial flat de uma pessoa organizando finanças em um notebook, gráficos de barras e moedas ao redor, paleta azul-petróleo, mostarda e branco, sem sombras, formas geométricas simples, fundo liso, formato 16:9, sem texto.")
style("aquarela", "Pintura com transparências e bordas suaves.",
      "Ilustração em aquarela de um casario colorido de cidade histórica, manchas de cor transparentes, bordas que se espalham no papel, granulação do papel visível, áreas em branco preservadas, paleta suave de ocre, azul e rosa.")
style("pintura a óleo clássica", "Aparência de tela com pinceladas e luz dramática.",
      "Pintura a óleo em estilo clássico de natureza-morta com frutas tropicais, jarro de cerâmica e pano dobrado, fundo escuro, luz lateral dramática, pinceladas visíveis, verniz levemente amarelado.")
style("ilustração de livro infantil", "Traço acolhedor e cores alegres para histórias.",
      "Ilustração de livro infantil de uma menina e um cachorro explorando um jardim mágico com cogumelos gigantes, traço arredondado, texturas de lápis de cor e guache, cores alegres e suaves, expressões gentis, formato 4:3.")
style("3D estilizado (clay/isométrico)", "Objetos com aparência de massinha ou maquete.",
      "Cena isométrica em 3D estilizado de um pequeno escritório com mesa, computador, estante e planta, aparência de massinha fosca, cores pastel, iluminação suave de estúdio, fundo liso, sem texto.")
style("low poly e pixel art", "Visual de jogo retrô ou geométrico.",
      "Pixel art em 32 bits de uma vila costeira ao pôr do sol, barcos de pesca, coqueiros e casinhas, paleta limitada a 16 cores, contornos nítidos, formato 16:9.")
style("anime e mangá (original)", "Estética de animação japonesa com personagem original.",
      "Ilustração em estilo anime de uma estudante original andando de bicicleta por uma rua arborizada no verão, céu azul com nuvens volumosas, cores vivas, contornos limpos, luz do sol filtrada pelas folhas, formato 16:9.",
      "Use personagens originais; personagens existentes são protegidos. " + LIM_STYLE)
style("traço, nanquim e esboço", "Desenho de linha para estudo, livro ou tatuagem.",
      "Desenho em nanquim de uma árvore antiga com raízes expostas, traço fino com hachuras para sombras, fundo branco, sem cor, estilo de caderno de esboços.")
style("infográfico e diagrama", "Explica um processo ou dado de forma visual.",
      "Infográfico vertical explicando as 4 etapas para montar uma reserva de emergência, ícones simples para cada etapa, setas conectando os blocos, paleta verde e azul, muito espaço em branco. Títulos curtos: \"Gastos\", \"Meta\", \"Aporte\", \"Guarde\".",
      "Texto e números em imagem costumam sair com erros; para dados exatos, gere a arte sem texto e diagrame depois. " + LIM_STYLE)
style("pôster tipográfico e capa", "Peça com título forte e hierarquia visual.",
      "Pôster vertical para um festival de jazz, título \"NOITE DE JAZZ\" em letras grandes no topo, silhueta de saxofonista em contraluz, paleta azul-noite e dourado, textura de papel envelhecido, espaço inferior livre para informações.")
style("logotipo e ícone (rascunho)", "Gera conceitos visuais para orientar um designer.",
      "Três conceitos de ícone para um app de finanças pessoais chamado \"Ponta do Lápis\": formas simples, combinação de lápis e gráfico de barras, duas cores (verde-petróleo e dourado), fundo branco, sem texto.",
      "Resultados servem como rascunho; vetorize e verifique originalidade e registro de marca antes de usar. " + LIM_STYLE)
style("mockup de embalagem", "Visualiza um produto antes de produzir.",
      "Mockup de embalagem de café especial: pacote kraft com válvula, rótulo minimalista em creme e terracota, apoiado em bancada de madeira com grãos espalhados, luz natural lateral, foto realista, formato 4:5, rótulo sem texto.")
style("thumbnail e capa para redes", "Imagem de alto contraste para chamar atenção no feed.",
      "Capa para vídeo sobre organizar o orçamento: pessoa surpresa olhando um extrato, fundo amarelo saturado, alto contraste, iluminação frontal forte, espaço livre à direita para título, formato 16:9.")
style("surreal e conceitual", "Metáforas visuais para ideias abstratas.",
      "Imagem conceitual surreal: uma escada de livros abertos subindo até as nuvens, pessoa pequena no primeiro degrau, céu ao entardecer, luz suave, estilo de fotografia manipulada realista, formato 4:5.")
style("fantasia e concept art", "Ambientes imaginários para histórias e jogos.",
      "Concept art de uma cidade construída nas copas de árvores gigantes da Amazônia, pontes suspensas de cipó, casas iluminadas por lanternas, névoa entre as árvores, vista ampla ao entardecer, pintura digital detalhada.")
style("ficção científica e cyberpunk", "Futuro urbano com tecnologia e neon.",
      "Rua de uma metrópole futurista em noite de chuva, letreiros de neon magenta e ciano refletidos no asfalto, pessoas com capas translúcidas, vapor saindo de bueiros, vista em nível da rua, estilo cinematográfico.")
style("retrô anos 70 e 80", "Cores, tipografia e texturas de época.",
      "Ilustração em estilo de anúncio de revista dos anos 1970: família na praia com carro conversível, cores quentes desbotadas, retícula de impressão visível, bordas arredondadas, sensação nostálgica.")
style("minimalista e flat lay", "Composição limpa vista de cima.",
      "Flat lay minimalista de itens de viagem organizados em grade sobre fundo bege: passaporte, óculos de sol, caderno, câmera analógica e mapa dobrado, sombras suaves, muito espaço livre, vista de cima, formato 1:1.")

# ---------- Técnicas ----------
tech("matriz de estilos", ["prompt"], IMG,
     "Gera a mesma cena em vários estilos para comparar antes de escolher.",
     "Mantenha cena e composição fixas e varie só o estilo; gere uma imagem por estilo se a ferramenta não aceitar várias de uma vez.",
     "Mesma cena em quatro versões, uma por imagem: casal tomando café em uma varanda com vista para o mar ao amanhecer. Versão 1: fotografia editorial. Versão 2: aquarela. Versão 3: ilustração vetorial flat. Versão 4: 3D estilizado em massinha. Mantenha composição e cores principais.",
     "Algumas ferramentas mudam também a composição ao trocar o estilo; compare lado a lado.",
     SRC_GEN)
tech("variação controlada", ["prompt"], IMG,
     "Ajusta uma imagem mudando uma única variável por vez.",
     "Anexe ou cite a imagem escolhida e diga exatamente o que muda e o que deve permanecer.",
     "Mantenha tudo igual nesta imagem e mude apenas a hora do dia para noite, com as luzes da casa acesas e céu estrelado.",
     "Mesmo pedindo uma só mudança, outros detalhes podem variar; compare antes e depois.",
     ["C4"])
tech("exclusões e prompt negativo", ["prompt", "cmd"], ["portatil", "midjourney"],
     "Evita elementos indesejados.",
     "Na maioria das ferramentas, escreva \"sem...\" no fim do texto. No Midjourney, use o parâmetro --no seguido dos termos.",
     "Mesa de trabalho organizada com notebook e caderno, luz natural, foto realista --no texto, logotipos, pessoas",
     "Excluir com frases negativas nem sempre funciona; o Runway, por exemplo, recomenda descrever apenas o que deve aparecer. Se o elemento persistir, reescreva a cena sem mencioná-lo.",
     ["J5", "R1"])
tech("texto dentro da imagem", ["prompt"], IMG,
     "Aumenta a chance de o texto sair correto.",
     "Coloque o texto exato entre aspas, curto (até 5 palavras), diga posição, tamanho e estilo de letra. Gere a arte sem texto quando a precisão for essencial.",
     "Cartaz de padaria artesanal com o título \"PÃO DE FERMENTAÇÃO NATURAL\" em letras serifadas grandes no topo, ilustração de pão rústico ao centro, fundo creme, sem outros textos.",
     "Acentos e palavras longas em português costumam errar; confira letra por letra.",
     ["C4"])
tech("edição localizada", ["ui", "prompt"], ["chatgpt", "gemini", "firefly", "midjourney", "portatil"],
     "Altera uma área da imagem preservando o restante.",
     "No ChatGPT, selecione a área ou comente na imagem. No Midjourney, use Vary Region ou o modelo de edição (--edit). Descreva o que muda e o que fica igual.",
     "Na área selecionada, troque o vaso de plantas por uma luminária de chão de metal preto. Preserve parede, luz, sombras e todos os outros objetos.",
     "Bordas da área editada podem ficar visíveis; amplie e confira.",
     ["C4", "J5"])
tech("expandir a imagem (outpainting)", ["prompt"], IMG,
     "Aumenta o quadro mantendo o conteúdo original.",
     "Anexe a imagem, diga a nova proporção e o que deve aparecer nas áreas novas.",
     "Expanda esta foto de 1:1 para 16:9, completando as laterais com a continuação da praia e do céu. Não altere a pessoa nem o centro da imagem.",
     "As áreas novas são inventadas; confira emendas e repetições.",
     ["C4"])
tech("personagem consistente", ["prompt"], IMG,
     "Mantém o mesmo personagem em várias imagens.",
     "Crie primeiro uma folha de personagem e use-a como referência nas imagens seguintes, repetindo a mesma descrição física palavra por palavra.",
     "Folha de personagem original: menino de 8 anos, cabelo crespo curto, camiseta laranja com listra azul, bermuda jeans, tênis verde. Mostre de frente, de perfil, de costas e três expressões (alegre, curioso, assustado), fundo branco, mesmo estilo de ilustração.",
     "A consistência não é garantida; detalhes de roupa e rosto podem variar. No Midjourney V8, a referência de pessoa ou objeto passou para o modelo de edição.",
     ["C4", "J5"])
tech("estilo a partir de referência", ["ui", "prompt"], ["midjourney", "firefly", "chatgpt", "gemini"],
     "Usa uma imagem sua para guiar a aparência de novas criações.",
     "Midjourney: --sref com a imagem ou código de estilo e --sw para a força. Firefly: Styles > Reference para estilo e Composition > Reference para estrutura, com controle de força. ChatGPT e Gemini: anexe a imagem e descreva o que copiar (paleta, traço, luz) e o que mudar.",
     "Use a imagem anexada apenas como referência de estilo (paleta, textura e traço). Crie uma nova cena: farol no alto de um penhasco em dia de vento, gaivotas, mar agitado.",
     "Use referências próprias ou com direito de uso. A referência guia; não copia.",
     ["J5", "AD2", "AD3", "C4"])
tech("esboço para arte final", ["prompt"], IMG,
     "Transforma um rascunho em imagem acabada mantendo a composição.",
     "Anexe a foto do esboço e diga o estilo final; peça para preservar posições e proporções.",
     "Transforme este esboço a lápis em uma ilustração digital colorida e finalizada. Mantenha posição dos personagens, perspectiva e enquadramento. Paleta quente de fim de tarde.",
     "Esboços pouco legíveis geram interpretações livres; reforce no texto o que cada traço representa.",
     ["C4", "AD3"])
tech("descobrir o prompt de uma imagem", ["prompt", "cmd"], ["portatil", "midjourney"],
     "Descreve uma imagem de referência em formato de prompt para recriar algo parecido.",
     "Em assistentes com visão, anexe a imagem e peça a descrição estruturada. No Midjourney (Discord), /describe sugere prompts.",
     "Descreva esta imagem como um prompt de geração, separando assunto, ambiente, enquadramento, lente, luz, paleta, estilo e proporção. Não identifique pessoas reais.",
     "A descrição aproxima o resultado; não reproduz a imagem original.",
     ["C5", "J2"])
tech("Midjourney: parâmetros essenciais", ["cmd"], ["midjourney"],
     "Ajusta formato e comportamento da geração no fim do prompt.",
     "--ar define a proporção; --stylize ou --s controla o toque artístico (0 a 1000, padrão 100); --chaos ou --c dá variedade (0 a 100, padrão 0); --weird ou --w torna o resultado incomum (até 3000, padrão 0); --raw dá mais controle; --seed ajuda a repetir testes; --tile cria padrões contínuos; --q ajusta qualidade; --hd gera em 2048 px no V8.1.",
     "retrato editorial de uma ceramista em sua oficina, luz de janela, paleta terrosa --ar 4:5 --s 250 --c 10 --raw",
     "Deixe um espaço antes de cada parâmetro e não use pontuação dentro dele. Faixas e suporte variam por versão; confira a documentação.",
     ["J5", "J6", "J7", "J8"])
tech("Midjourney: estilo pessoal e moodboards", ["cmd", "ui"], ["midjourney"],
     "Aplica preferências de estilo salvas na conta.",
     "--profile ou --p aplica o perfil de personalização e moodboards; --sref e --sw usam referência de estilo; --iw ajusta o peso de imagens no prompt.",
     "jardim de inverno com plantas tropicais e cadeira de vime, luz difusa --ar 3:2 --p",
     "O perfil reflete suas escolhas anteriores no site; resultados mudam conforme você treina o perfil.",
     ["J5"])

for _x in ITEMS[_START:]:
    _x["verified_at"] = "10/10/2026"
