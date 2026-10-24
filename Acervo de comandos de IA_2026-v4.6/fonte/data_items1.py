from data_core import VERIFIED

ITEMS = []
def it(mod, title, kinds, plats, what, how, ex, lim, src, origin="v3"):
    ITEMS.append(dict(module=mod, title=title, kinds=kinds, platforms=plats, what=what,
                      how=how, example=ex, limits=lim, sources=src, origin=origin))

P = ["portatil"]

# ---------------- 1. Primeiros passos ----------------
it(1, "Comando, recurso ou prompt?", ["prompt"], P,
   "Ajuda a escolher a forma correta de pedir uma tarefa antes de começar.",
   "Comando: escolha no menu que aparece ao digitar / no ambiente documentado. Recurso: selecione o botão, modo ou plugin. Prompt: descreva o resultado. No ChatGPT, @ conecta plugins e ferramentas e $ invoca skills, conforme a documentação.",
   "Crie um resumo de uma página do arquivo anexado, com três conclusões e dúvidas pendentes.",
   "Escrever o nome de uma função não instala ferramenta nem concede acesso. Se o menu / não mostrar o comando, ele não existe naquele ambiente.",
   ["C1", "C2"])
it(1, "Modelo, aplicativo e API", ["prompt"], P,
   "Distingue o motor de IA (modelo) do aplicativo que oferece menus, anexos, pesquisa, execução de código e arquivos.",
   "Confira qual aplicativo você usa, qual modelo está selecionado e quais ferramentas estão ligadas. Uma capacidade documentada só na API não vale automaticamente para o app.",
   "Antes de começar, diga quais materiais consegue acessar e quais ferramentas estão disponíveis nesta conversa. Se não conseguir pesquisar ou gerar arquivos, informe isso e proponha uma alternativa.",
   "A resposta do modelo não prova que uma ferramenta existe. Confirme menus, anexos lidos e arquivos efetivamente entregues.",
   ["C1", "X1", "X4"])
it(1, "Teste justo entre modelos", ["prompt"], P,
   "Compara a utilidade de duas ou mais IAs no seu caso, com o mesmo pedido e as mesmas fontes.",
   "Use as mesmas fontes, restrições e critérios. Registre modelo, aplicativo, modo e data de cada teste.",
   "Resolva a tarefa abaixo usando somente os anexos. Entregue conclusão, evidências e lacunas. Ao final, confira exatidão, completude, clareza e atendimento ao formato solicitado.",
   "Vale para o seu caso, não como ranking universal. Acesso a pesquisa e ferramentas precisa ser equivalente entre os testes.",
   [])
it(1, "Escolher a ferramenta pela tarefa", ["prompt"], P,
   "Orienta a escolha entre plataformas sem declarar um \"melhor modelo\".",
   "Liste o que a tarefa exige: pesquisa atual, arquivos de saída, mídia, integração com e-mail ou documentos, privacidade. Compare com o Mapa das plataformas (módulo 2) e com o seletor da sua conta.",
   "Tenho esta tarefa: [descrição]. Liste os requisitos técnicos dela (pesquisa web, leitura de arquivos, criação de DOCX/XLSX/PPTX, imagem, vídeo, integrações). Diga quais desses requisitos você consegue cumprir neste ambiente e quais não.",
   "A resposta reflete o ambiente da conversa. Planos, regiões e versões mudam a disponibilidade.",
   [], origin="v4")
it(1, "O caso /speedshot e similares", ["unverified"], ["portatil", "chatgpt", "flow"],
   "Evita tratar nomes como /speedshot, /orbit 360, /drone fly e /focus pull como comandos universais.",
   "Não há documentação oficial desses nomes no ChatGPT (24 slash commands documentados no desktop, nenhum de vídeo), no Google Flow (documentação de modelos e de imagem para vídeo sem presets de câmera nomeados) nem na lista de comandos do Midjourney. Eles circulam em blogs como \"códigos secretos\" do Flow, sem citar fonte. O Higgsfield tem presets parecidos (360 Orbit, FPV Drone, Focus Change, Crash Zoom), mas escolhidos na interface, sem barra e sem nenhum chamado Speedshot. Descreva o movimento por extenso (módulo 12).",
   "Quero um vídeo curto em que a câmera avança rapidamente até o produto e desacelera no final (efeito de rampa de velocidade). Antes de gerar, identifique a ferramenta disponível e explique os parâmetros aceitos.",
   "Um nome com barra pode ser preset de outra ferramenta, apelido ou invenção. Digitar a barra não comprova comando registrado. Se a ferramenta parecer obedecer, é porque interpretou o texto como descrição.",
   ["C2", "F1", "F2", "J2", "H1", "U1"])

# ---------------- 2. Mapa das plataformas ----------------
it(2, "ChatGPT (OpenAI): Chat, Work e Codex", ["ui", "prompt"], ["chatgpt"],
   "Aplicativo com três modos: Chat para conversa, Work para tarefas longas com entregáveis (documentos, planilhas, apresentações) e Codex para programação. Modelos em 06/10/2026: no Chat, GPT-5.6 Sol nos planos pagos e GPT-5.6 Luna no Free e no Go, com níveis de raciocínio e opção Pro (GPT-5.6 Sol Pro e, em planos elegíveis, GPT-6 Pro). No Work e no Codex, GPT-6 Astra, GPT-6.1 Sol, GPT-6 Sol e GPT-6 Luna.",
   "Escolha o modo no aplicativo e o modelo no seletor. Work existe na web, no celular e no desktop; o desktop dá acesso a arquivos locais no Work e no Codex.",
   "Compare os anexos e crie um relatório com fontes, números conferidos e próximos passos. Entregue um arquivo se houver ferramenta de criação.",
   "O GPT-5.5 deixa o ChatGPT em 14/10/2026 (segue na API). O GPT-6 Astra tem janelas de uso de 5 horas e semanais. Slash commands do desktop não valem para web e celular.",
   ["C1", "C10", "C20", "C21", "C22", "C23"])
it(2, "Claude (Anthropic)", ["ui", "prompt"], ["claude"],
   "Modelos em 06/10/2026: Claude Fable 5.1 (raciocínio exigente e trabalho agêntico longo), Claude Opus 5.5 (escolha padrão recomendada), Claude Sonnet 5.5 (velocidade e inteligência) e Claude Haiku 4.5 (mais rápido). O aplicativo oferece Research, criação de arquivos, Artifacts, Projects, memória, skills, tarefas agendadas e Claude in Chrome.",
   "Ative Research pelo botão + e confira Settings > Capabilities > Code execution and file creation para arquivos. Cowork e chat estão sendo unificados em uma só conversa, começando pelos planos Pro e Max.",
   "No Claude, crie um relatório dos anexos e um XLSX com os dados consolidados. Preserve fontes e verifique totais antes de entregar.",
   "Research exige plano pago e pesquisa web ligada. Recursos variam por plano e por implantação gradual. Claude Code é um ambiente de programação distinto do chat.",
   ["A1", "A2", "A3", "A7", "A11"])
it(2, "Gemini (Google)", ["ui", "prompt"], ["gemini"],
   "Aplicativo com opções Fast, Thinking e Pro, modelo 3.6 Flash (lançado em 21/07/2026), 3.1 Pro e Deep Think. Recursos: Deep Research, Canvas, Gems (em transição para skills), skills, ações agendadas, Nano Banana para imagens e Gemini Spark (agente para assinantes Ultra em países selecionados).",
   "Escolha o modelo no seletor e o recurso abaixo da caixa de texto (Deep Research, Canvas). Skills ficam em Settings > Skills.",
   "No Gemini, use Deep Research para investigar o tema abaixo. Revise o plano, compare fontes e exporte o relatório para o Google Docs.",
   "Gemini, Flow e Gemini Notebook são ambientes distintos. Skills e Spark exigem 18 anos ou mais; skills só em contas pessoais.",
   ["G1", "G2", "G3", "G4", "G5"])
it(2, "Microsoft Copilot e Microsoft 365 Copilot", ["ui", "prompt"], ["copilot"],
   "O Copilot pessoal oferece os modos Quick Response, Think Deeper, Study and Learn, Smart e Search, além de Deep Research, Pages, Vision, Imagine, Voice, Memory, Podcasts e Groups. O Microsoft 365 Copilot trabalha com e-mails, reuniões e arquivos da organização e permite referenciar conteúdo com /.",
   "No Copilot pessoal, escolha o modo antes de enviar. No Microsoft 365 Copilot, digite / para referenciar arquivos, pessoas, reuniões e e-mails.",
   "Compare estes relatórios e gere uma lista de decisões com trechos de apoio. Se houver integração com Word, prepare o documento nela.",
   "Copilot pessoal, Microsoft 365 Copilot e GitHub Copilot são produtos distintos. Sem licença do Microsoft 365 Copilot, a referência com / alcança só arquivos.",
   ["M1", "M2", "M3", "M4"])
it(2, "Perplexity", ["ui", "prompt"], ["perplexity"],
   "Busca com respostas citadas. Em 04/09/2026, o plano Pro listava Sonar 2, GPT-5.6 Terra, Gemini 3.7 Flash, Claude Sonnet 5, Kimi K3, GLM 5.3, Grok 4.6 e Nemotron 3 Ultra; o Max acrescentava GPT-5.6 Sol e Claude Opus 5. Recursos: Deep Research, Model Council (Max), Comet (navegador), Computer (agente com créditos) e Learn Mode.",
   "Selecione o modo e, nos planos pagos, o modelo. O plano Free usa seleção automática.",
   "Pesquise este tema com fontes primárias. Separe fatos de opiniões e entregue uma síntese com links, datas e questões não resolvidas.",
   "A própria Perplexity informa que os modelos mudam; confira o seletor. Os nomes de modelos de terceiros seguem a página da Perplexity. Computer consome créditos.",
   ["P1", "P3", "P4"])
it(2, "Grok (xAI)", ["ui", "api", "prompt"], ["grok"],
   "O app oferece chat, multiagente, busca na web e no X, Imagine (imagem e vídeo) e voz; o plano SuperGrok amplia limites. Na API, Grok 4.7 é o modelo principal (contexto de 500 mil tokens), com Grok Imagine Image 2.0 e Grok Imagine Video 1.5 para mídia.",
   "No X ou em grok.com, faça o pedido; o Grok decide se pesquisa posts e web. Na API, Web Search e X Search precisam ser ativados.",
   "Pesquise a notícia abaixo. Distinga publicação oficial, reportagem e postagem no X. Cite os links e não trate popularidade como comprovação.",
   "Nomes de modos do app não constam da documentação consultada. Ferramentas da API não provam acesso equivalente na interface. Posts podem conter boatos.",
   ["X1", "X2", "X3", "X4"])
it(2, "DeepSeek", ["api", "prompt"], ["deepseek"],
   "Família de modelos para conversa e raciocínio. Em 10/09/2026 a API lançou o DeepSeek-V4.1-Flash (identificador deepseek-flash), com suporte visual nativo. Pedidos ao V4-Pro passaram a ser atendidos pelo V4.1-Flash a partir de 14/09/2026.",
   "No aplicativo, envie o contexto em texto. Na API, o modo de raciocínio vem ligado por padrão (esforço high) e é ajustável.",
   "Resolva este problema com as informações abaixo. Apresente a conclusão, uma justificativa verificável e uma checagem independente; sinalize dados insuficientes.",
   "As fontes consultadas são da API. Busca, upload e exportação no app não foram confirmados nesta revisão.",
   ["D1", "D2"])
it(2, "Mistral Vibe (antigo Le Chat)", ["ui", "prompt"], ["mistral"],
   "Em 12/08/2026 o Le Chat virou Vibe, com três modos: Vibe Chat (conversa), Vibe Work (tarefas de várias etapas entre apps) e Vibe Code (CLI, extensão do VS Code e web). Contas, planos e histórico foram mantidos em chat.mistral.ai.",
   "Escolha o modo antes de iniciar e confira as ferramentas conectadas.",
   "Organize estas notas em plano de ação, responsáveis e pendências. Se o modo Work tiver acesso às fontes indicadas, use-as e cite o que consultou.",
   "Tutoriais antigos usam o nome Le Chat e menus que podem ter mudado.",
   ["V1"])
it(2, "Gemini Notebook (antigo NotebookLM)", ["ui", "prompt"], ["notebook"],
   "Consulta orientada pelas fontes que você carrega, com citações, Audio Overviews e mapas mentais. Aceita Google Docs e Slides, PDFs, texto, markdown, URLs, vídeos do YouTube, áudio e texto colado.",
   "Crie um notebook, adicione as fontes e faça perguntas. Cada fonte aceita até 500 mil palavras ou 200 MB.",
   "Com base somente nas fontes deste notebook, explique o tema, cite os trechos de apoio e informe quando a resposta não estiver nos materiais.",
   "PDFs protegidos contra cópia não são importados. Não substitui a leitura completa nem corrige fontes desatualizadas.",
   ["N1", "N2"])
it(2, "Midjourney", ["ui", "cmd", "prompt"], ["midjourney"],
   "Criação de imagens e vídeos curtos. V8.2 é a versão padrão desde 24/07/2026; também há V8.1, V7, V6.1, V6 e Niji 7. Parâmetros documentados incluem --v, --sref, --iw, --hd e --sd.",
   "Na web, use a barra Imagine; no Discord, use /imagine. Parâmetros entram ao final do prompt.",
   "Ilustração editorial de uma mesa de trabalho com caderno, café e plantas, luz lateral suave, paleta azul e areia, sem texto. Use a imagem anexada como referência de composição.",
   "Parâmetros do Midjourney não funcionam em outras IAs. Image Prompts orientam a criação; não produzem cópia exata.",
   ["J1", "J2", "J4"])
it(2, "Google Flow", ["ui", "prompt"], ["flow"],
   "Ferramenta de vídeo do Google. Modelos de vídeo: Veo 3.1 Lite, Fast e Quality, Gemini Omni Flash 1.1 e Gemini Omni. Modelos de imagem: Nano Banana Pro, Nano Banana 2 e Nano Banana 2 Lite. Recursos: texto para vídeo, Frames (inicial e final), Ingredients, edição e extensão.",
   "Abra um projeto, escolha o modelo e a resolução na caixa do prompt e confira o custo em créditos antes de gerar.",
   "Use a imagem anexada como frame inicial. A pessoa permanece parada, respirando suavemente, enquanto a câmera se aproxima devagar. Preserve rosto, roupa, luz e cenário. Sem cortes.",
   "Duração de 4 a 10 segundos conforme o modelo; extensão só no Lite, segundo a documentação. Presets de câmera nomeados não aparecem na documentação.",
   ["F1", "F2"], origin="v4")

# ---------------- 3. Escrita e comunicação ----------------
def wp(title, what, ex, lim, origin="v3", how="Cole o texto ou as notas e informe público, tom, extensão e fatos que não podem mudar."):
    it(3, title, ["prompt"], P, what, how, ex, lim, [], origin)
wp("Escrever e revisar", "Cria e melhora rascunhos.",
   "Reescreva o texto abaixo em português do Brasil, com tom profissional e acolhedor. Preserve nomes, números e compromissos. Limite a 180 palavras e liste dúvidas separadamente.",
   "Revise fatos e nuances; o modelo pode acrescentar interpretações. Revisão de redação não é validação jurídica.")
wp("E-mail com pedido claro", "Transforma notas em comunicação utilizável.",
   "Escreva um e-mail cordial com assunto, contexto breve, pedido objetivo e próximo passo. Use só os fatos abaixo; marque prazo ausente como a definir.",
   "Não invente destinatários, compromissos ou fatos; revise antes de enviar. Escrever o e-mail não o envia.")
wp("Tradução com glossário", "Traduz preservando termos definidos.",
   "Traduza o texto abaixo para inglês profissional. Preserve nomes, números e os termos do glossário. Liste expressões ambíguas separadamente.",
   "Terminologia técnica exige revisão; tradução não valida o conteúdo.")
wp("Resumo em três camadas", "Adapta o mesmo material a tempos de leitura diferentes.",
   "Resuma este material em uma frase, cinco pontos e uma síntese de 250 palavras. Preserve ressalvas, datas e números; indique trechos não compreendidos.",
   "Resumo pode omitir exceções relevantes; compare com o original.")
wp("Revisão sem alterar compromissos", "Melhora clareza e tom sem mudar o que foi prometido.",
   "Revise a mensagem abaixo para clareza e concisão. Preserve todos os compromissos e datas. Mostre a versão final e explique apenas as mudanças que afetam o sentido.",
   "Revisão de redação não confirma exatidão factual.")
wp("Post para redes sociais", "Adapta uma ideia a formato curto, com gancho e chamada.",
   "Transforme o texto abaixo em três versões de post para Instagram: até 150 palavras, primeira frase de impacto, um dado concreto e uma pergunta final. Não use números que não estejam no texto.",
   "Confira dados, direitos de imagem e regras da plataforma. A IA não conhece o desempenho do seu perfil sem dados.", origin="v4")
wp("Ajustar tom para o público", "Reescreve a mesma mensagem para leitores diferentes.",
   "Reescreva a explicação abaixo em duas versões: uma para um cliente leigo (sem jargão, até 120 palavras) e outra para um colega técnico (com termos precisos). Mantenha os mesmos fatos.",
   "Simplificar pode apagar ressalvas importantes; confira se nada essencial sumiu.", origin="v4")
wp("Mensagem difícil", "Prepara uma comunicação delicada com firmeza e respeito.",
   "Ajude-me a escrever uma mensagem recusando o pedido abaixo. Tom respeitoso e direto, sem justificativas longas, oferecendo uma alternativa concreta. Entregue duas versões, curta e média.",
   "Releia antes de enviar; a IA não conhece o histórico da relação.", origin="v4")

# ---------------- 4. Pesquisa e checagem ----------------
it(4, "Pesquisa web", ["ui", "prompt"], P,
   "Busca informações atuais com fontes.",
   "Confirme que a pesquisa está ligada no aplicativo. Informe tema, período e preferência por fontes primárias.",
   "Pesquise as novidades de IA publicadas nos últimos sete dias. Traga cinco itens com data de publicação, data do evento e link para a fonte original.",
   "Fontes podem estar erradas, desatualizadas ou inacessíveis. Sem ferramenta de busca, o modelo responde só com o que aprendeu no treinamento.",
   ["C8"])
it(4, "Deep research no ChatGPT", ["ui", "prompt"], ["chatgpt"],
   "Investiga uma questão em várias fontes e entrega relatório.",
   "Segundo a documentação atual: abra o modo Work, entre em Plugins, habilite Deep research, descreva a pergunta e o escopo, depois revise relatório e fontes.",
   "Pesquise três formas de reduzir desperdício em uma cafeteria no Brasil. Compare evidência, custos e esforço; cite fontes, lacunas e data da pesquisa em um relatório.",
   "Não há /deepresearch documentado. Disponibilidade depende da conta e do workspace. Não garante acesso a conteúdo pago.",
   ["C8", "C10"])
it(4, "Pesquisa aprofundada em outras plataformas", ["ui", "prompt"], ["claude", "gemini", "perplexity", "copilot"],
   "Adapta a mesma investigação ao recurso disponível em cada plataforma.",
   "Claude: botão + > Research, com pesquisa web ligada (planos pagos). Gemini: botão Deep Research; o plano é editável e o relatório leva de 5 a 10 minutos. Perplexity: Deep Research. Copilot: Deep Research.",
   "Investigue [tema] até a data de hoje. Compare fontes primárias, explique divergências e entregue conclusão, evidências, limitações e links por afirmação principal.",
   "Limites diários e fontes diferem entre plataformas. Não peça pesquisa se o ambiente não tiver busca.",
   ["A2", "G2", "P4", "M2"])
it(4, "Checar uma afirmação", ["prompt"], P,
   "Testa uma notícia ou conclusão específica.",
   "Forneça a afirmação, o contexto e o link original.",
   "Verifique esta afirmação com fontes primárias. Classifique como sustentada, contradita ou inconclusiva e explique a evidência. Separe data de publicação da data do evento.",
   "Ausência de evidência não prova falsidade; resultados de busca podem ser incompletos.",
   ["C8", "X1"])
it(4, "Deep Research do Gemini com fontes próprias", ["ui", "prompt"], ["gemini"],
   "Combina busca web com Gmail, Drive, arquivos enviados ou notebooks.",
   "Clique em Deep Research, adicione as fontes (Workspace exige conectar a conta) e edite o plano antes de gerar. Exporte para Google Docs, Canvas ou Audio Overview.",
   "Pesquise o histórico de reajustes do meu condomínio usando os PDFs enviados e fontes públicas sobre índices de reajuste. Separe o que veio dos meus arquivos e o que veio da web.",
   "Exige 18 anos ou mais. Gráficos e simuladores interativos são do plano Ultra e não valem com fontes do Workspace.",
   ["G2"], origin="v4")
it(4, "Pesquisa com citações na Perplexity", ["ui", "prompt"], ["perplexity"],
   "Responde com fontes numeradas, útil para conferência rápida.",
   "Escolha Search ou Deep Research; nos planos pagos, selecione o modelo.",
   "Quais mudanças nas regras do [tema] foram publicadas em 2026? Use apenas fontes oficiais e jornalísticas, com data de cada uma.",
   "Abra os links; a citação pode não sustentar exatamente a frase.",
   ["P1", "P4"], origin="v4")
it(4, "Separar fato, opinião e boato", ["prompt"], P,
   "Organiza informações conflitantes de redes sociais e notícias.",
   "Cole os textos ou links e peça a classificação.",
   "Classifique cada afirmação abaixo como fato verificável, opinião ou boato. Para cada fato, indique a fonte primária que o confirmaria e se você a encontrou.",
   "Sem busca ativa, a classificação é apenas textual.",
   [], origin="v4")

# ---------------- 5. PDF, Word e PowerPoint ----------------
it(5, "Ler e comparar PDFs", ["prompt"], P,
   "Extrai ideias e compara materiais.",
   "Anexe os PDFs, identifique cada um e peça referências de página.",
   "Compare os dois PDFs anexados. Liste diferenças de prazo, preço e responsabilidades com página e trecho de apoio. Se uma página estiver ilegível, sinalize.",
   "PDF digitalizado pode exigir OCR; tabelas, gráficos e texto em imagem podem não ser recuperados. Confira as páginas citadas.",
   [])
it(5, "Criar ou revisar Word", ["prompt"], P,
   "Organiza conteúdo em documento editável.",
   "Peça explicitamente DOCX e descreva estrutura e padrão visual. Confirme que o ambiente cria arquivos.",
   "Crie um DOCX de proposta comercial usando as notas anexadas. Inclua resumo, escopo, entregáveis e cronograma. Marque valores ausentes como \"a definir\" e confira a paginação.",
   "Layout complexo, comentários e controle de alterações exigem ferramenta compatível. Texto formatado no chat não é DOCX.",
   ["C9", "A3"])
it(5, "Produzir PowerPoint", ["prompt"], P,
   "Transforma conteúdo em apresentação.",
   "Peça PPTX com público, número de slides e objetivo.",
   "Crie um PPTX de oito slides com base no relatório anexado. Uma mensagem central por slide, fontes nas notas e conclusão com três ações. Verifique textos cortados e gráficos.",
   "Gerar tópicos não é entregar PPTX. Fontes, animações e aparência podem variar no PowerPoint.",
   ["C9", "A3"])
it(5, "Criar PDF e HTML", ["prompt"], P,
   "Entrega o mesmo conteúdo em formatos de distribuição.",
   "Defina conteúdo equivalente, legibilidade e revisão.",
   "Crie um PDF A4 e um HTML responsivo do conteúdo anexado. Inclua índice, referências e exemplos copiáveis. Verifique ambos e entregue os arquivos finais.",
   "HTML interativo depende do navegador. PDF tem paginação fixa e não reproduz botões ou filtros.",
   ["C9"])
it(5, "Arquivos no Claude", ["ui", "prompt"], ["claude"],
   "Produz e edita Word, Excel, PowerPoint e PDF.",
   "Ative Settings > Capabilities > Code execution and file creation (em Team e Enterprise, nas configurações da organização). Anexe as fontes.",
   "Crie DOCX, XLSX e PPTX a partir destas notas. Use o mesmo conjunto de números, cite fontes e confira consistência entre os três arquivos.",
   "Limite de 30 MB por arquivo. A criação consome mais da cota do plano.",
   ["A3"])
it(5, "Copilot e Canvas do Gemini", ["ui", "prompt"], ["copilot", "gemini"],
   "Usa material anexado em interfaces de trabalho.",
   "No Microsoft 365 Copilot, digite / para referenciar o arquivo. No Gemini, clique em Canvas para documento ou slides; exporte para Docs ou Slides (slides também em PDF).",
   "Use o anexo para criar um documento executivo com resumo, decisões e próximos passos. Informe qual opção de exportação está disponível.",
   "Suporte de entrada não garante saída em todo formato. No Microsoft 365 Copilot, até 10 arquivos ou páginas de um mesmo site do SharePoint por referência.",
   ["G3", "M3", "M5"])
it(5, "Extrair tabela de PDF", ["prompt"], P,
   "Converte uma tabela de documento em dados reutilizáveis.",
   "Indique página e tabela; peça CSV ou XLSX.",
   "Extraia a tabela da página que eu indicar para CSV; preserve unidades e marque células ilegíveis.",
   "Células mescladas e números em imagem geram erros; confira totais.",
   [])
it(5, "Revisar contrato em linguagem simples", ["prompt"], P,
   "Explica cláusulas e destaca pontos de atenção.",
   "Anexe o contrato e diga o seu papel (contratante, contratado).",
   "Explique este contrato em linguagem simples. Liste prazos, multas, renovação automática e obrigações de cada parte, com a cláusula de origem. Indique o que eu deveria perguntar antes de assinar.",
   "Não substitui orientação jurídica. Confira cada cláusula citada no original.",
   [], origin="v4")
