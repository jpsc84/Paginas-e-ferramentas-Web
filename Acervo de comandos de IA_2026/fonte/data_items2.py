from data_items1 import it, P

# ---------------- 6. Planilhas e dados ----------------
it(6, "Analisar e criar Excel", ["prompt"], P,
   "Organiza dados e cálculos em uma nova versão da planilha.",
   "Anexe XLSX ou CSV; explique colunas, unidades e regras. Confirme que o ambiente executa código ou cria arquivos.",
   "Analise o XLSX anexado e crie uma nova versão com resumo mensal, fórmulas de total e gráfico de receita. Preserve a aba original e confira se os totais reconciliam.",
   "Valide fórmulas e unidades. Macros, conexões externas e recursos avançados podem não ser preservados.",
   ["C19", "A3"])
it(6, "Visualizações e painéis", ["prompt"], P,
   "Explica dados com gráficos ou uma interface simples.",
   "Peça formato, interações e fontes; confirme a ferramenta de publicação se precisar de link.",
   "Crie uma visualização interativa que compare orçamento previsto e realizado nos dados anexados, com filtro por mês e tabela de apoio.",
   "Interatividade depende do ambiente. Publicar é uma etapa separada, com hospedagem e revisão.",
   ["C18", "A4"])
it(6, "Limpar e reconciliar dados", ["prompt"], P,
   "Organiza uma base sem perder rastreabilidade.",
   "Anexe os dados e descreva colunas e unidades.",
   "Limpe o arquivo anexado em uma nova cópia. Padronize datas, liste duplicatas e dados ausentes, e confira totais antes e depois. Não remova registros sem documentar o critério.",
   "Duplicatas aparentes podem ser registros válidos. Preserve o original.",
   [])
it(6, "Fórmula com exemplo verificável", ["prompt"], P,
   "Ajuda a montar um cálculo de planilha.",
   "Descreva a regra e os nomes das colunas.",
   "Sugira uma fórmula para [regra] usando as colunas [nomes]. Considere Excel em pt-BR. Explique a lógica e teste com dois exemplos e um caso vazio.",
   "Funções e separadores variam por aplicativo e idioma (no Excel em pt-BR, ponto e vírgula). Teste no arquivo real.",
   [])
it(6, "Cenários com hipóteses", ["prompt"], P,
   "Explora mudanças em parâmetros.",
   "Liste entradas e hipóteses explicitamente.",
   "Monte cenários conservador, base e otimista com os dados abaixo. Separe entradas, hipóteses e resultados e indique qual variável mais muda a conclusão.",
   "Cenários não são previsões; não transforme estimativas em fatos.",
   [])
it(6, "Excel com Copilot no Microsoft 365", ["ui", "prompt"], ["copilot"],
   "Analisa e edita a pasta de trabalho dentro do Excel.",
   "Abra o painel do Copilot no Excel (licença Microsoft 365 Copilot). As notas de setembro de 2026 citam links que destacam as alterações e o painel Show Changes.",
   "Crie uma aba de resumo por categoria com totais mensais e um gráfico de colunas. Destaque as células que você alterou.",
   "Recursos dependem de licença e implantação. Confira cada alteração antes de salvar.",
   ["M4"], origin="v4")
it(6, "Orçamento doméstico", ["prompt"], P,
   "Organiza gastos e identifica onde ajustar.",
   "Anexe o extrato em CSV ou cole as despesas.",
   "Classifique as despesas abaixo em categorias, some por mês e mostre as três categorias que mais cresceram. Não invente valores; marque lançamentos sem descrição clara.",
   "Confira a classificação; descrições de extrato são ambíguas. Não envie dados bancários sensíveis sem necessidade.",
   [], origin="v4")

# ---------------- 7. Estudo, voz e reuniões ----------------
it(7, "Aprender com exercícios", ["prompt"], P,
   "Organiza uma sessão de estudo ativa.",
   "Indique nível, objetivo e tempo disponível.",
   "Ensine porcentagem para um iniciante em 15 minutos. Use um exemplo de desconto, faça três perguntas uma de cada vez e explique os erros sem dar a resposta antes da tentativa.",
   "É um roteiro pedido por prompt; não depende de comando /study. Confira as soluções.",
   [])
it(7, "Voz e ditado no ChatGPT", ["ui", "prompt"], ["chatgpt"],
   "Voz permite conversa falada; ditado converte fala em texto antes de enviar.",
   "No desktop, selecione Start voice chat ou Start new voice chat; o atalho é configurável em Settings > Voice > Voice chat hotkey.",
   "Vamos ensaiar uma apresentação de dois minutos. Faça o papel do público e depois dê feedback sobre clareza e organização.",
   "Voice exige plano Plus, Pro, Business, Edu ou Enterprise. Só uma conversa de voz ativa por vez no desktop. Transcrição pode errar nomes e números.",
   ["C12"])
it(7, "Ata de reunião", ["prompt"], P,
   "Transforma notas ou transcrição em decisões.",
   "Cole uma transcrição autorizada ou notas; identifique participantes.",
   "Organize esta transcrição em decisões, ações, responsáveis, prazos e dúvidas. Não atribua uma decisão a alguém se isso não estiver claro no texto.",
   "Notas não contêm tudo; áudio pode ter falhas de transcrição. Não invente responsáveis.",
   [])
it(7, "Flashcards e revisão espaçada", ["prompt"], ["portatil", "notebook"],
   "Prepara estudo ativo a partir de uma fonte.",
   "Anexe o material e informe seu nível.",
   "Crie 15 flashcards do material anexado, com pergunta, resposta curta e trecho de apoio. Prepare um roteiro de revisão de sete dias e um quiz sem mostrar o gabarito antes da tentativa.",
   "O roteiro não cria lembretes sozinho. Verifique as respostas contra a fonte.",
   ["N2"])
it(7, "Audio Overview para estudar ouvindo", ["ui"], ["notebook", "gemini"],
   "Converte documentos em resumo em áudio.",
   "No Gemini Notebook, carregue as fontes e gere o Audio Overview. No Gemini, Canvas e Deep Research também oferecem Audio Overview.",
   "Foque o resumo em áudio nas diferenças entre os capítulos 3 e 4 e nos termos que costumam cair em prova.",
   "O áudio pode simplificar ou errar; confira com o texto.",
   ["N2", "G2", "G3"], origin="v4")
it(7, "Modos de estudo: Copilot e Perplexity", ["ui", "prompt"], ["copilot", "perplexity"],
   "Modos pensados para explicação passo a passo e perguntas de acompanhamento.",
   "Copilot: selecione Study and Learn. Perplexity: Learn Mode.",
   "Explique juros compostos como se eu estivesse começando. Pare depois de cada conceito e me faça uma pergunta para checar se entendi.",
   "O modo muda o estilo da resposta; não garante exatidão.",
   ["M1", "P1"], origin="v4")
it(7, "Simulado comentado", ["prompt"], P,
   "Gera questões no estilo de uma prova e corrige com explicação.",
   "Informe banca, conteúdo e nível; anexe o edital ou material.",
   "Crie 10 questões de múltipla escolha sobre [tema], no estilo da banca [nome]. Mostre uma por vez, espere minha resposta e só então explique o gabarito com a fonte.",
   "Questões geradas podem conter erros ou ambiguidades; valide com material oficial.",
   [], origin="v4")

# ---------------- 8. Memória e projetos ----------------
it(8, "Memória no ChatGPT", ["ui", "prompt"], ["chatgpt"],
   "Reutiliza contexto útil entre conversas.",
   "Revise as opções de personalização e memória da conta. No desktop, /memories define se a conversa usa ou gera memórias.",
   "Considere minha preferência por respostas curtas em português do Brasil. Diga se é possível salvar essa preferência como memória neste ambiente.",
   "Não suponha que uma preferência foi salva só porque foi mencionada. Confira a lista de memórias.",
   ["C13", "C2"])
it(8, "Projetos e instruções", ["ui", "prompt"], P,
   "Mantém arquivos, chats e instruções de um trabalho juntos.",
   "Crie ou abra um projeto; acrescente fontes e instruções. No ChatGPT desktop, projetos locais podem apontar para pastas do computador.",
   "Neste projeto, use pt-BR, valores em reais e datas no formato dia/mês/ano. Ao analisar os arquivos, cite o nome da fonte e destaque dados ausentes.",
   "Projetos não dão acesso a todos os arquivos da conta. No Claude, o contexto não passa entre chats do projeto se não estiver na base de conhecimento.",
   ["C15", "A5"])
it(8, "Projects do Claude, Gems e skills do Gemini", ["ui", "prompt"], ["claude", "gemini"],
   "Reutiliza contexto ou instruções em assistentes próprios.",
   "Claude: claude.ai/projects > + New Project; adicione conhecimento e instruções (Free cria até 5 projetos). Gemini: Gems seguem funcionando, mas em novembro de 2026 viram skills nas contas pessoais; crie skills em Settings > Skills.",
   "Crie instruções para um assistente de revisão: use pt-BR, preserve fatos, sinalize lacunas e entregue versão final mais notas de mudanças.",
   "Project, Gem e skill não são recursos idênticos. Skills do Gemini: só contas pessoais, 18 anos ou mais, nome em minúsculas com hífen.",
   ["A5", "G4", "G5"])
it(8, "Memória do Claude", ["ui"], ["claude"],
   "Lembra papel, projetos e preferências entre conversas.",
   "Settings > Memory: ligue Generate memory from chats e Search and reference chats (busca em planos pagos). Cada projeto tem memória separada. Chats anônimos não entram na memória.",
   "O que discutimos sobre o orçamento da reforma na semana passada?",
   "Temas sensíveis exigem opção separada. Revise e edite as memórias salvas.",
   ["A6"], origin="v4")
it(8, "Memória do Copilot", ["ui", "prompt"], ["copilot"],
   "Guarda preferências pessoais sob seu controle.",
   "Peça para lembrar, atualizar ou esquecer uma informação.",
   "Lembre que prefiro receitas sem lactose e respostas em tópicos curtos.",
   "Confira o que foi salvo nas configurações de memória.",
   ["M2"], origin="v4")
it(8, "Instruções personalizadas portáteis", ["prompt"], P,
   "Texto-base para colar em qualquer plataforma que aceite instruções.",
   "Cole no campo de instruções da plataforma ou no início da conversa.",
   "Sobre mim: [profissão, objetivo]. Como responder: português do Brasil, direto, comece pela conclusão, sem repetir minha pergunta. Sempre separe fatos de suposições e diga quando não souber.",
   "Cada plataforma limita o tamanho e a aplicação das instruções.",
   [], origin="v4")

# ---------------- 9. Planejamento e decisões ----------------
def pp(title, what, ex, lim, origin="v3"):
    it(9, title, ["prompt"], P, what, "Informe tarefas, restrições, datas e o que precisa decidir.", ex, lim, [], origin)
pp("Planejar o dia", "Organiza prioridades e tempo.",
   "Com estas tarefas e reuniões, organize meu dia em blocos realistas. Separe urgente, importante e adiável; preserve os compromissos fixos e deixe intervalos.",
   "A IA não conhece sua agenda sem contexto ou conexão autorizada.")
pp("Comparar opções", "Explicita critérios e concessões.",
   "Compare as opções abaixo por custo, prazo, esforço e adequação. Use somente os dados fornecidos; destaque informações faltantes e não dê notas sem explicar o critério.",
   "Se preços ou regras atuais importarem, pesquise e confira as fontes.")
pp("Plano de projeto", "Converte um objetivo em entregas.",
   "Transforme este objetivo em etapas, entregáveis, dependências e critérios de conclusão. Indique riscos, perguntas essenciais e uma primeira ação executável hoje.",
   "O plano depende de recursos e prazos reais; não assume que a execução já aconteceu.")
pp("Revisão semanal pessoal", "Fecha a semana e prepara a próxima.",
   "Com base nas anotações abaixo, liste o que concluí, o que ficou pendente e por quê, e proponha as três prioridades da próxima semana.",
   "Depende da qualidade das anotações.", origin="v4")
pp("Decisão com pré-mortem", "Testa uma decisão imaginando que ela deu errado.",
   "Vou decidir [decisão]. Imagine que daqui a seis meses deu errado. Liste as cinco causas mais prováveis, os sinais de alerta de cada uma e o que posso fazer agora para reduzir o risco.",
   "Exercício de reflexão, não previsão.", origin="v4")
pp("Roteiro de viagem", "Organiza dias, deslocamentos e reservas.",
   "Monte um roteiro de 7 dias em [destino] para um casal com uma criança pequena, com no máximo duas atividades por dia, tempo de deslocamento e alternativas para chuva. Marque o que exige reserva.",
   "Horários e preços mudam; confira nos sites oficiais.", origin="v4")

# ---------------- 10. Programação e automações ----------------
it(10, "Explicar e depurar código", ["prompt"], P,
   "Encontra hipóteses para um problema reproduzível.",
   "Forneça código, objetivo, ambiente e mensagem de erro.",
   "Analise o código e o erro abaixo. Explique a causa provável, proponha a menor correção e diga como verificar. Não afirme que executou testes se não tiver executado.",
   "Sem execução, a correção é uma proposta; dependências e ambiente mudam o comportamento.",
   [])
it(10, "Criar uma ferramenta pequena", ["prompt"], P,
   "Define uma implementação revisável.",
   "Descreva funções, dispositivos e onde os dados ficam.",
   "Crie uma página HTML responsiva para organizar minhas tarefas, com busca, filtros e armazenamento local. Verifique teclado, celular e persistência; entregue o arquivo final.",
   "Armazenamento local não sincroniza dispositivos. Publicar requer etapa e permissão próprias.",
   ["A4"])
it(10, "Revisar uma mudança", ["prompt"], P,
   "Avalia riscos concretos de uma alteração.",
   "Cole o diff ou descreva a mudança.",
   "Revise esta alteração buscando erros de comportamento, acessibilidade e dados. Dê prioridade a problemas reproduzíveis, com localização e impacto. Se não achar problema, diga o que foi verificado.",
   "Revisão não substitui teste completo.",
   [])
it(10, "Ambientes de código: Codex, Claude Code, Vibe Code", ["ui"], ["chatgpt", "claude", "mistral"],
   "Ambientes com acesso a repositório, terminal e execução.",
   "Codex no app ChatGPT, CLI e extensão de IDE; Claude Code no terminal e em apps; Vibe Code em CLI, VS Code e web.",
   "Leia o repositório, explique a arquitetura em dez linhas e proponha a menor mudança para [objetivo]. Rode os testes antes e depois.",
   "Comandos de cada agente não são universais. Revise permissões antes de permitir escrita.",
   ["C10", "A10", "V1"], origin="v4")
it(10, "Script de automação local", ["prompt"], P,
   "Gera um script pequeno para tarefa repetitiva no computador.",
   "Informe sistema operacional, pastas e regra.",
   "Escreva um script em Python que renomeie os PDFs desta pasta para AAAA-MM-DD_assunto.pdf usando a data do arquivo. Primeiro mostre o que faria (modo simulação), sem renomear nada.",
   "Teste em uma cópia da pasta. Scripts podem apagar ou sobrescrever arquivos.",
   [], origin="v4")
it(10, "Fórmula de expressão regular", ["prompt"], P,
   "Cria e explica um padrão de busca.",
   "Dê exemplos que devem e não devem casar.",
   "Crie uma expressão regular que encontre CPFs no formato 000.000.000-00. Explique cada parte e teste com três exemplos válidos e dois inválidos.",
   "Formato válido não significa número válido; confira dígitos verificadores à parte.",
   [], origin="v4")

# ---------------- 11. Imagens ----------------
it(11, "Criar uma imagem no ChatGPT", ["ui", "prompt"], ["chatgpt"],
   "Produz um visual a partir de uma descrição.",
   "Descreva assunto, estilo, composição e proporção em uma a três frases. Para invocar a skill de forma explícita, inclua $imagegen (modelo gpt-image-2).",
   "Crie uma ilustração editorial de um escritório brasileiro com plantas, luz de manhã e cores azul e areia. Composição horizontal 16:9, sem texto nem logotipos.",
   "Pode não obedecer exatamente detalhes ou contagem de objetos. Gerações contam no limite de uso.",
   ["C4"])
it(11, "Remover fundo e trocar objetos", ["prompt"], ["chatgpt", "portatil"],
   "Solicita uma alteração localizada.",
   "Anexe a imagem; nomeie o objeto e a área. No ChatGPT, é possível selecionar áreas e comentar imagens específicas.",
   "Remova apenas o fundo da foto anexada e entregue um PNG com transparência. Preserve produto, rótulo, cores e contornos.",
   "Preservação não é garantida pixel a pixel; confira bordas e se a transparência é real.",
   ["C4"])
it(11, "Preservar rosto, mudar estilo e proporção", ["prompt"], ["chatgpt", "portatil"],
   "Orienta variações com elementos fixos.",
   "Identifique a referência e altere uma variável por vez.",
   "Edite esta foto para uma composição vertical 9:16, expandindo o cenário. Preserve a identidade facial, expressão e roupa; não corte a cabeça nem estique a pessoa.",
   "Pode haver deriva de identidade. Use imagens de pessoas com autorização.",
   ["C4"])
it(11, "Texto e nitidez em imagens", ["prompt"], ["chatgpt", "portatil"],
   "Pede texto curto ou versão visualmente mais nítida.",
   "Forneça o texto exato entre aspas; confira a arte no tamanho final.",
   "Crie uma versão mais nítida desta arte, preservando a composição. Use somente o título \"CAFÉ DA MANHÃ\" no topo. Não acrescente letras ou números.",
   "Não é recuperação garantida de detalhes nem aumento técnico de resolução.",
   ["C4"])
it(11, "Interpretar uma imagem", ["prompt"], P,
   "Lê captura de tela, gráfico ou diagrama.",
   "Anexe imagem legível e diga qual região importa.",
   "Analise o gráfico anexado. Separe observações visíveis de inferências e sinalize qualquer número ilegível.",
   "Texto pequeno e baixa resolução causam erros; forneça os dados originais quando possível.",
   ["C5"])
it(11, "Referências no Midjourney", ["ui", "prompt"], ["midjourney"],
   "Orienta composição e estilo de uma nova imagem.",
   "Na web, adicione a imagem como Image Prompt na barra Imagine. --iw ajusta o peso da imagem; --sref usa referência de estilo.",
   "Foto editorial de uma mesa com caderno e café, luz natural pela esquerda, paleta azul e areia. Use a referência para a composição, sem texto e sem logotipos.",
   "Referência é inspiração, não cópia. Parâmetros com -- são do Midjourney.",
   ["J1", "J4"])
it(11, "Descrever uma imagem para virar prompt", ["cmd"], ["midjourney"],
   "Gera quatro sugestões de prompt a partir de uma imagem enviada.",
   "No Discord, use /describe e envie a imagem.",
   "/describe",
   "As sugestões são ponto de partida; edite antes de usar.",
   ["J2"], origin="v4")
it(11, "Gemini: imagens com Nano Banana", ["ui", "prompt"], ["gemini"],
   "Cria e edita imagens no app Gemini.",
   "Descreva a imagem ou anexe uma foto e diga o que alterar.",
   "Crie um ícone simples de cofrinho em estilo flat, fundo branco, cores verde e dourado, sem texto.",
   "Regras para rostos reais e marcas variam. Confira direitos antes de publicar.",
   ["G1"], origin="v4")
it(11, "Copilot: Imagine", ["ui", "prompt"], ["copilot"],
   "Cria imagens novas ou edita imagens existentes por texto.",
   "Peça a imagem no Copilot ou anexe uma imagem para editar.",
   "Transforme esta foto do meu escritório em ilustração no estilo aquarela, mantendo a disposição dos móveis.",
   "Confira se elementos importantes foram mantidos.",
   ["M2"], origin="v4")
it(11, "Grok: Imagine", ["ui", "api", "prompt"], ["grok"],
   "Gera imagens a partir de texto no app; na API, o modelo de imagem é o Grok Imagine Image 2.0.",
   "No app, abra Imagine e descreva a imagem.",
   "Pôster minimalista de uma corrida de rua ao amanhecer, sem texto, cores laranja e azul.",
   "Revise regras de uso de pessoas reais e marcas antes de publicar.",
   ["X2", "X3"], origin="v4")
it(11, "Variações de paleta", ["prompt"], P,
   "Explora cores mantendo a composição.",
   "Anexe a arte e defina o que não muda.",
   "Crie três versões desta arte mudando apenas a paleta. Preserve texto, composição e objetos.",
   "Texto pode ser redesenhado com erros; confira letra por letra.",
   [])
