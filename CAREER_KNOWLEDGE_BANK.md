# CAREER KNOWLEDGE BANK: agent-setup-bundle
<!-- Master Source of Truth (SSOT) dla systemu JobHunt oraz raportu Dawid_Czerwinski_Raport.md -->

---

## 1. System Overview

`agent-setup-bundle` to deterministyczny, wieloplatformowy system operacyjny inżynierii AI, ujednolicający środowiska wykonawcze wiodących asystentów kodowania (OpenAI Codex, Antigravity / Gemini CLI, Claude Code, Cursor IDE) oraz integrujący dwupoziomową architekturę orkiestracji podwykonawczej (**Two-Tier Cognitive Architecture**) na systemach Linux, macOS i Windows. Architektura projektu opiera się na 16 żelaznych regułach operacyjnych (w tym protokole PRAR, bezwzględnym zakazie spekulacji, inżynierii uwagi i maszynie stanów planowania), 36 modułowych pakietach umiejętności w standardzie `agentskills.io`, serwerze FastMCP z inteligentnym routerem darmowych modeli LLM (MiniMax M3 z 1M kontekstu, NVIDIA Nemotron 550B MoE, Zhipu GLM-5.2) oraz siatce dowiązań symbolicznych eliminującej duplikację konfiguracji. Całość zarządzana jest przez trzy natywne, idempotentne instalatory z trójstopniowym silnikiem kaskadowego fallbacku dla Windows oraz zautomatyzowany walidator jakości kodu zapobiegający degradacji promptów i dryfowi reguł.

---

## 2. Matryca Perspektyw Stanowiskowych (Role Angles)

### 2.1. Kąt DevOps / Platform & Site Reliability Engineering (SRE)
- **Kluczowe mechanizmy:** Projektowanie idempotentnych skryptów wdrożeniowych w trzech językach powłokowych (POSIX Bash z `set -euo pipefail`, Windows PowerShell z obsługą bloków `[CmdletBinding()]`, uniwersalny Python 3 z biblioteką `pathlib`).
- **Niezawodność i odporność:** Ochrona istniejących konfiguracji użytkownika (`settings.json`, `config.toml`, `mcp.json`) przed nadpisaniem podczas aktualizacji systemu, gwarantująca zerową utratę kluczy API i tokenów produkcyjnych.
- **Zarządzanie stanem systemu:** Wdrożenie siatki dowiązań symbolicznych (`~/.agents/skills` -> `~/.codex/skills/custom` oraz `~/.claude/skills`), redukującej redundancję dyskową do zera i umożliwiającej natychmiastowe propagowanie zmian we wszystkich środowiskach bez przestojów.
- **Obsługa ograniczeń OS:** Trzystopniowy fallback na systemach Windows (SymbolicLink -> NTFS Junction -> Recursive Copy), eliminujący awarie instalatora na maszynach bez włączonego trybu deweloperskiego lub uprawnień administratora.

### 2.2. Kąt AI Systems Engineering & Agentic Workflow Architecture
- **Kontrola behawioralna agentów:** Transformacja nieprzewidywalnych modeli LLM w deterministyczne narzędzia inżynieryjne poprzez 16 reguł operacyjnych i wymuszenie protokołu PRAR (Perceive, Reason, Act, Refine).
- **Zarządzanie budżetem uwagi i kontekstem:** Wdrożenie reguły twardego zrzutu danych powyżej 100 linii lub 5 KB do `./scratch/`, eliminującej zjawisko Attention U-Curve (Lost-in-the-Middle) i chroniącej model przed szumem informacyjnym.
- **Ochrona przed kaskadą błędów:** Wdrożenie bezpiecznika zatrucia kontekstu (*Context Poisoning Circuit Breaker*), nakazującego natychmiastową kwarantannę błędnych założeń flagą `[INVALIDATED]` i uniemożliwiającego modelowi nawarstwianie kolejnych prób na sfałszowanym kontekście.
- **Ekonomia roju i orkiestracja subagentów:** Twardy routing modeli według złożoności obliczeniowej (`flash_lite` dla operacji I/O, `flash` dla wyszukiwania, `pro` dla architektury), izolacja katalogów roboczych oraz protokół *Zero Context Bleed* (zakaz wylewania surowych logów narzędziowych do agenta nadrzędnego).
- **Zachowanie ciągłości procesów (Zero Context Loss):** Maszyna stanów planowania z blokadą odkrytych faktów i atomowymi wpisami `[PRUNED]`, a także protokół bezstratnego przekazania sesji (*Session Handoff*) generujący samowystarczalne prompty startowe dla kolejnych instancji agenta.

### 2.3. Kąt Software Architecture & Systems Engineering
- **Czysta architektura i separacja granic:** Egzekwowanie Clean/Hexagonal Architecture we wszystkich skryptach i regułach (`modular-architecture.md`), twardy limit długości plików do 150-200 linii oraz całkowity zakaz tworzenia plików typu "god-object" czy niekohezyjnych `utils.py`.
- **Typowane kontrakty:** Eliminacja niekontrolowanych struktur danych (`dict[str, Any]` oraz `any`) na granicach modułów na rzecz ścisłych schematów Pydantic i interfejsów TypeScript.
- **Wzorzec Single Source of Truth (SSOT / DRY):** Architektura jednego repozytorium dystrybuującego wiedzę i reguły do 4 odmiennych ekosystemów AI, uniemożliwiająca rozbieżność implementacyjną między platformami.
- **Standard AAIF (Agentic AI Foundation):** Opracowanie ujednoliconego szablonu `AGENTS.md` definiującego Prawdę Wykonywalną (konkretne polecenia CLI z flagami, topografia folderów i niezmienniki projektowe).

### 2.4. Kąt Quality Assurance & Test Automation Engineering
- **Zautomatyzowany test harness CI/CD:** Opracowanie skryptu `scripts/validate_suite.py`, sprawdzającego integralność całego repozytorium przed wdrożeniem lub commitem.
- **Walidacja syntaktyczna i semantyczna:** Regexowy parser weryfikujący poprawność nagłówków YAML frontmatter, spójność nazewnictwa katalogów ze znacznikami `name:` oraz zgodność limitu długości opisu (`len <= 1024` znaków) zapobiegająca obcinaniu promptów w modelach AI.
- **Weryfikacja wieloplatformowa:** Automatyczne testowanie poprawności syntaktycznej plików konfiguracyjnych JSON (`mcp_config.json`, `settings.json`, `cursor_mcp.json`), obecności szablonów TOML oraz zgodności manifestów bazowych (`CODEX.md`, `GEMINI.md`, `CLAUDE.md`, `.cursorrules`).
- **Egzekwowanie procedur TDD i bramki kompilacji:** Zdefiniowanie nieomijalnej bramki TypeScript Safety Gate (`npx tsc --noEmit`) oraz protokołu TDD (Red-Green-Refactor) w `rules/systemic-excellence.md` i `skills/skill-qa-engineer`.

### 2.5. Kąt Technical Support L2 & Systems Operations (Incident Triage)
- **Eliminacja obejść (Anti-Workaround Protocol):** Twardy wymóg lokalizowania i usuwania pierwotnej przyczyny awarii na najniższym możliwym poziomie stosu (`Kernel > Driver > OS Config > Runtime > Framework > Application Code`), zakazujący stosowania sztucznych nakładek, aliasów, symlinków maskujących błędy czy pustych bloków `try/catch`.
- **Weryfikacja skutków komend (Command Outcome Verification):** Wdrożenie procedury sprawdzania realnego stanu dysku/systemu po każdej komendzie mutującej stan, zamiast polegania wyłącznie na kodzie wyjścia exit code 0.
- **Rygor diagnostyczny:** Zastąpienie domysłów twardymi danymi telemetrycznymi – zakaz zgadywania specyfikacji sprzętowej i wersji bibliotek, wymuszenie uruchamiania poleceń inspekcyjnych (`uname -r`, `lspci`, `free -h`, `lsblk`).
- **Niezmiennik ochrony środowiska produkcyjnego:** Całkowity zakaz destrukcyjnych poleceń (`git clean`, masowe wyszukiwanie i zamiana) bez uprzedniej symulacji i zgody operatora.

### 2.6. Kąt AI Cost Optimization & Multi-Tier Sub-Agent Orchestration
- **Architektura dwupoziomowa (Two-Tier Cognitive Systems):** Separacja procesów planowania i nadzoru (modele flagowe Reasoning: Gemini 3.7 Pro / Flash) od masowego wykonawstwa kodu (darmowe wyspecjalizowane modele: MiniMax M3, NVIDIA Nemotron 550B, GLM-5.2).
- **Redukcja kosztów API do 0.00 USD:** Zbudowanie mostka Aider Headless + FastMCP, który przejmuje 100% pracochłonnych, tokenożernych zadań (generowanie 2000+ LOC rusztowań, masowe testy jednostkowe TDD, JSDoc, migracje typów) przy zerowym zużyciu płatnych tokenów agenta głównego.
- **Inteligentny Router Zadaniowy (Task-to-Model Router):** Dynamiczne dopasowywanie modelu do specyfiki promptu (MiniMax M3 dla rusztowań full-stack 1M kontekstu, Nemotron 550B MoE dla operacji binarnych/C/Rust, GLM-5.2 dla naprawy bugów SWE-bench i precyzyjnych diffów).
- **Piaskownica i automatyczna samonaprawa (Self-Healing Sandboxing):** Izolacja każdego zadania podwykonawcy w dedykowanym Git Worktree oraz sprzężenie wykonania z automatycznym linterem/testerem (`npx tsc --noEmit`, `pytest`, `cargo test`), eliminujące halucynacje składniowe przed scaleniem kodu do repozytorium.
- **Dynamiczne wstrzykiwanie wiedzy domenowej (Dynamic Skill Injection):** Mostkowanie 36 pakietów `agentskills.io` bezpośrednio do bezstanowych wywołań Aidera jako kontekst read-only (`--read`).

---

## 3. Pula Twardych Punktów Google XYZ

### Kategoria A: DevOps, Automatyzacja & Platform Engineering
1. **Wdrożono** zautomatyzowany, trójstopniowy silnik fallbacku linkowania w PowerShell (`install.ps1`), **zapewniając** 100% powodzenia instalacji na systemach Windows bez uprawnień administratora, **poprzez** kaskadową próbę utworzenia SymbolicLink, automatyczne przejście do NTFS Directory Junction i ostateczny fallback do bezpiecznej kopii rekurencyjnej.
2. **Skonstruowano** wieloplatformowy system instalacyjny w Bash, PowerShell i Pythonie, **skracając** czas wdrożenia kompletnego środowiska AI na nowej maszynie do poniżej 3 sekund, **poprzez** deterministyczną dystrybucję 16 reguł i 36 skilli do ujednoliconego katalogu `~/.agents/`.
3. **Wyeliminowano** redundancję danych i ryzyko dryfu konfiguracji w 4 środowiskach AI, **utrzymując** rozmiar instalacji na poziomie pojedynczego zestawu plików źródłowych, **poprzez** spięcie katalogów `~/.codex/skills/custom` oraz `~/.claude/skills` dynamicznymi dowiązaniami symbolicznymi do wspólnego zasobu.
4. **Zabezpieczono** klucze API i tokeny użytkowników przed przypadkowym zresetowaniem podczas aktualizacji, **gwarantując** zerowe nadpisania plików konfiguracyjnych, **poprzez** implementację warunków sprawdzających obecność istniejących plików `settings.json`, `config.toml` oraz `mcp.json` przed kopiowaniem szablonów.
5. **Zunifikowano** konfigurację narzędziową dla 12 serwerów Model Context Protocol (MCP), **eliminując** manualne konfigurowanie narzędzi w różnych IDE, **poprzez** centralne szablony JSON/TOML mapujące uprawnienia dla baz danych, kontenerów Docker, profili Lighthouse, sub-workerów i automatyzacji przeglądarek.

### Kategoria B: AI Systems Engineering & Architektura Agentowa
6. **Zredukowano** degradację uwagi modelu (zjawisko Attention U-Curve) w długich sesjach roboczych, **obniżając** objętość kontekstu o 60-80% przy intensywnych operacjach wejścia-wyjścia, **poprzez** wymuszenie reguły automatycznego zrzutu logów przekraczających 100 linii lub 5 KB do plików `./scratch/` z pozostawieniem w oknie kontekstowym 3-5 punktowego abstraktu.
7. **Wyeliminowano** kaskadowe błędy i pętle halucynacji w procesie wnioskowania agenta, **skracając** czas powrotu do poprawnej ścieżki wykonania po błędnym założeniu, **poprzez** zaprojektowanie bezpiecznika zatrucia kontekstu (*Context Poisoning Circuit Breaker*) natychmiast kwarantannującego fałszywe przesłanki flagą `[INVALIDATED]`.
8. **Zoptymalizowano** koszt tokenowy i czas wykonania wieloetapowych zadań roju agentów, **eliminując** niepotrzebne narzuty modeli reasoningowych na zadania wejścia-wyjścia, **poprzez** rygorystyczny routing modeli (`flash_lite` dla odczytu plików, `flash` dla wyszukiwania, `pro` wyłącznie dla refaktoryzacji architektonicznych).
9. **Zapobieżono** zanieczyszczaniu kontekstu głównego agenta przez procesy potomne, **redukując** narzut pamięciowy w zadaniach równoległych, **poprzez** wdrożenie protokołu *Zero Context Bleed* wymuszającego komunikację wyłącznie ustrukturyzowanym kontraktem (`Status`, `Findings`, `Artifacts`, `Blockers`).
10. **Zabezpieczono** spójność kodu i wyeliminowano kolizje zapisu podczas pracy współbieżnej, **zapewniając** deterministyczne scalanie zmian, **poprzez** izolację przestrzeni roboczych subagentów w niezależnych worktree i egzekwowanie barier synchronizacji przed uruchomieniem zadań zależnych.
11. **Wyeliminowano** utratę kontekstu i amnezję agenta podczas wieloturowego projektowania architektury (`/plan`), **zapewniając** 100% zachowanie odkrytych ścieżek i komend weryfikacyjnych, **poprzez** 3-stanową maszynę stanów planowania z nagłówkiem `Iteration Delta` oraz blokadą `Discovered Baseline Facts`.
12. **Zlikwidowano** problem powstawania kodu-zombie i hybrydowych implementacji w modelach LLM, **utrzymując** czystość aktywnej specyfikacji technicznej, **poprzez** procedurę bezwzględnego usuwania wycofanych fragmentów architektury z sekcji aktywnej i zastępowania ich atomowymi wpisami `[PRUNED]` w logu decyzji.
13. **Zapewniono** bezstratny transfer wiedzy między kolejnymi sesjami programowania w parach (*Zero Context Loss*), **eliminując** zjawisko zaśmiecania głównych plików reguł historią czatu, **poprzez** protokół *Session Handoff* generujący samowystarczalne prompty startowe sprzężone z plikiem `NEXT_SESSION_PLAN.md`.

### Kategoria C: AI Cost Optimization & Sub-Worker Delegation
14. **Zredukowano** koszty operacyjne API do 0.00 USD dla 100% masowych zadań programistycznych (scaffolding 2500+ LOC, pakiety testów TDD, dokumentacja JSDoc), **odciążając** płatne okna kontekstowe modeli nadrzędnych, **poprzez** architekturę dwupoziomowej orkiestracji FastMCP (`worker_mcp.py`) sprzężoną z silnikiem Aider Headless i darmowymi modelami z puli OpenRouter/Zhipu.
15. **Zaprojektowano i wdrożono** Task-Specialized Intelligent Router dla modeli open-source, **uzyskując** 92-95% skuteczności wykonania zadań w benchmarkach syntetycznych, **poprzez** dynamiczną kategoryzację promptów i kierowanie ich do wyspecjalizowanych modeli (MiniMax M3 z 1M kontekstu dla rusztowań, Nemotron 550B MoE dla kodu binarnego/niskopoziomowego, GLM-5.2 dla naprawy bugów).
16. **Wyeliminowano** problem obcinania generowanego kodu w wieloplikowych zadaniach sub-agentów, **zwiększając** maksymalny rozmiar pojedynczego zrzutu kodu z 4k do 65k tokenów wyjściowych, **poprzez** rekonfigurację metadanych `.aider.model.metadata.json` i synchronizację limitów z faktycznymi specyfikacjami API OpenRouter.
17. **Zautomatyzowano** pętlę samonaprawczą (Self-Healing Loop) w zadaniach generowania kodu przez modele chińskie, **zapobiegając** wprowadzaniu błędów składniowych i regresji typów, **poprzez** automatyczną detekcję stosu technologicznego (`npx tsc --noEmit`, `pytest`, `cargo test`) i przekazywanie flagi `--auto-test` do kontenera Git Worktree.
18. **Wdrożono** mechanizm Dynamic Skill Injection dla bezstanowych procesów roboczych, **podnosząc** zgodność generowanego kodu ze standardami architektonicznymi projektu, **poprzez** dynamiczne mapowanie i wstrzykiwanie 36 pakietów `agentskills.io` do kontekstu wykonawczego Aidera w trybie read-only (`--read`).

### Kategoria D: Software Architecture & Systems Design
19. **Zunifikowano** implementację reguł inżynieryjnych dla 4 odmiennych środowisk AI (Codex, Antigravity, Claude, Cursor), **zapewniając** 100% spójność zachowania modeli bez względu na używany edytor, **poprzez** transpilację wspólnych dyrektyw do formatów `CODEX.md`, `GEMINI.md`, `CLAUDE.md` oraz reguł `.cursor/rules/*.mdc`.
20. **Wyeliminowano** powstawanie monolitycznych plików i trudnego w utrzymaniu kodu, **ograniczając** rozmiar pojedynczych jednostek kodu do maksymalnie 150-200 linii, **poprzez** egzekwowanie Clean/Hexagonal Architecture i separację logiki domenowej od frameworków i sterowników.
21. **Zapewniono** integralność granic architektonicznych w tworzonych projektach, **eliminując** błędy typu runtime TypeError i niejawne mutacje, **poprzez** rygorystyczny zakaz używania typów `any` oraz arbitralnych struktur `dict[str, Any]` na rzecz ścisłych kontraktów Pydantic i interfejsów TypeScript.
22. **Zminimalizowano** duplikację logiki biznesowej i powstawanie konkurujących funkcji pomocniczych, **utrzymując** spójność architektury kodu (DRY / Single Source of Truth), **poprzez** procedurę obowiązkowego audytu repozytorium przed napisaniem jakiejkolwiek nowej funkcji i refaktoryzację istniejących modułów in-place.
23. **Wdrożono** standard Agentic AI Foundation (AAIF) dla konfiguracji repozytoriów, **eliminując** zgadywanie parametrów kompilacji i uruchomienia przez asystentów AI, **poprzez** szablon `templates/AGENTS.md` definiujący jawną Prawdę Wykonywalną, mapę granic katalogowych oraz niezmienniki systemowe.

### Kategoria E: Quality Assurance & Test Automation
24. **Zbudowano** zautomatyzowane narzędzie walidacji integralności środowiska w Pythonie (`scripts/validate_suite.py`), **wykrywając** 100% błędów składniowych i niespójności konfiguracyjnych przed commitem, **poprzez** wieloaspektowy audyt 36 skilli, 16 reguł, 4 manifestów, serwera sub-workerów i plików konfiguracyjnych.
25. **Zabezpieczono** modele LLM przed obcinaniem krytycznych instrukcji systemowych, **gwarantując** pełną czytelność metadanych skilli, **poprzez** automatyczną kontrolę długości opisu w blokach YAML frontmatter z twardym limitem 1024 znaków.
26. **Wprowadzono** mechanizm weryfikacji zgodności nazewnictwa w standardzie `agentskills.io`, **zapobiegając** błędom dynamicznego ładowania umiejętności, **poprzez** regexowy audyt dopasowania pola `name:` w pliku `SKILL.md` do fizycznej nazwy katalogu.
27. **Zabezpieczono** spójność semantyczną promptów bazowych dla 4 platform, **gwarantując** obecność procedury 4-fazowej bramki Pre-Flight Skill Gate we wszystkich manifestach, **poprzez** zautomatyzowaną inspekcję zawartości plików `CODEX.md`, `GEMINI.md`, `CLAUDE.md` i `.cursorrules`.
28. **Wymuszono** bezwzględne bezpieczeństwo typów w projektach TypeScript, **eliminując** regresje funkcjonalne wywołane próbami omijania kompilatora, **poprzez** twardą bramkę TypeScript Safety Gate (`npx tsc --noEmit`) zakazującą usuwania logiki biznesowej w celu naprawy błędów typowania.

### Kategoria F: Technical Support L2 & Incident Response
29. **Wyeliminowano** ryzyko wprowadzania pozornych poprawek maskujących awarie systemowe, **zapewniając** usuwanie problemów u źródła, **poprzez** protokół *Root Cause Only* wymuszający analizę w kolejności warstw: `Kernel > Driver > OS Config > Runtime > Framework > Application Code`.
30. **Zabezpieczono** systemy produkcyjne przed cichymi awariami poleceń ze skutkami ubocznymi, **eliminując** fałszywe potwierdzenia wykonania operacji, **poprzez** protokół Command Outcome Verification nakazujący wykonanie wtórnego sprawdzenia stanu (np. odczyt pliku, status usługi, stan procesu) po każdym poleceniu mutującym stan.

---

## 4. Baza Pytań Rekrutacyjnych i Historii STAR+R

### Historia 1: Kaskadowy Fallback Instalatora na Windows (Problem Uprawnień i Ograniczeń OS)
- **Kontekst (Situation):** Projekt wymagał zapewnienia identycznego środowiska narzędziowego i współdzielenia 36 modułów skilli na systemach Linux, macOS i Windows. Na systemie Windows domyślna próba utworzenia linku symbolicznego (`New-Item -ItemType SymbolicLink`) kończy się krytycznym błędem `UnauthorizedAccessException`, jeśli użytkownik nie posiada uprawnień administratora lub nie ma włączonego trybu Developer Mode (brak przywileju `SeCreateSymbolicLinkPrivilege`).
- **Zadanie (Task):** Opracować natywny skrypt PowerShell (`install.ps1`), który zainstaluje całe środowisko bez zgłaszania błędów uprawnień, bez wymuszania na użytkowniku uruchamiania powłoki z prawami administratora oraz zachowa mechanizm pojedynczego źródła prawdy (SSOT).
- **Działanie (Action):** Zaimplementowano odporny mechanizm kaskadowej obsługi wyjątków w PowerShell. Skrypt w pierwszym kroku próbuje utworzyć natywny link symboliczny. W przypadku przechwycenia błędu uprawnień, blok `catch` automatycznie deleguje operację do utworzenia Directory Junction (`New-Item -ItemType Junction`), który w systemie plików NTFS nie wymaga podwyższonych uprawnień. Jeżeli system plików nie wspiera junction, kolejny poziom kaskady wykonuje bezpieczną kopię rekurencyjną (`Copy-Item -Recurse`).
- **Wynik (Result):** Osiągnięto 100% deterministyczną instalację na dowolnej konfiguracji systemu Windows 10/11 bez potrzeby eskalacji uprawnień, eliminując zgłoszenia awarii instalatora i zachowując pełną kompatybilność ze środowiskiem OpenAI Codex.
- **Refleksja (Reflection):** Projektowanie narzędzi deweloperskich cross-platform wymaga dogłębnej znajomości niskopoziomowych mechanizmów systemów operacyjnych. Zamiast zmuszać użytkownika do obchodzenia polityk bezpieczeństwa systemu (np. wymuszanie roota/admina), właściwym podejściem inżynieryjnym jest zaprojektowanie wielowarstwowej degradacji funkcjonalności (graceful degradation).

---

### Historia 2: Eliminacja Zjawiska Attention U-Curve i Ochrona Budżetu Uwagi Modeli LLM
- **Kontekst (Situation):** W trakcie długich, wielogodzinnych sesji programowania z agentami AI, wklejanie surowych wyników poleceń testowych, logów kompilacji czy zawartości baz danych (>200-500 linii) powodowało drastyczny spadek jakości odpowiedzi modeli. Zjawisko utraty uwagi w środku okna kontekstowego (*Lost-in-the-Middle* / *Attention U-Curve*) prowadziło do ignorowania kluczowych reguł architektonicznych i halucynacji na temat kodu.
- **Zadanie (Task):** Zaprojektować i skodyfikować deterministyczny mechanizm zarządzania kontekstem, który uniemożliwi zaśmiecanie okna uwagi wielkimi zrzutami tekstu bez utraty krytycznych informacji diagnostycznych.
- **Działanie (Action):** Stworzono regułę operacyjną `context-engineering.md` oraz powiązaną umiejętność `skill-context-engineering`. Wprowadzono twardy niezmiennik inżynieryjny: każdy wynik narzędzia lub log przekraczający 100 linii lub 5 KB musi zostać natychmiast przekierowany do pliku na dysku w katalogu `./scratch/`. W oknie kontekstowym agent ma bezwzględny zakaz prezentowania pełnego zrzutu – generuje jedynie 3-5 punktów syntezy i jawną ścieżkę do pliku, a szczegóły doczytuje chirurgicznie za pomocą poleceń z zakresami linii (`view_file` StartLine/EndLine). Dodatkowo wprowadzono regułę kotwiczenia uwagi (reguły systemowe na szczycie promptu, aktualny cel i kryteria akceptacji na samym dole).
- **Wynik (Result):** Zredukowano objętość zbędnego tekstu w oknie kontekstowym o ponad 70%, eliminując przypadki łamania reguł projektowych podczas długotrwałego debugowania i skracając czas wnioskowania modeli.
- **Refleksja (Reflection):** Okno kontekstowe modeli językowych nie jest bezpłatnym śmietnikiem na logi. Zarządzanie budżetem uwagi wymaga traktowania tokenów jako zasobu o ograniczonej przepustowości i stosowania takich samych wzorców jak w inżynierii systemów rozproszonych: kompresji brzegowej, stronicowania i wskaźników referencyjnych na dysk.

---

### Historia 3: Dwupoziomowa Orkiestracja Agentów i Inteligentny Router Darmowych Modeli (Zero Cost Grunt Work)
- **Kontekst (Situation):** Wykonywanie masowych, powtarzalnych zadań programistycznych (tworzenie 2000+ linii kodu rusztowań modułów, pisanie setek asercji testów jednostkowych, wklepywanie JSDoc i refaktoryzacje typów) przez flagowe modele reasoningowe (Claude 3.7 Sonnet / Gemini 3.7 Pro) generowało wysokie koszty tokenowe i szybko zapychało okno kontekstowe szumem boilerplate'u. Z kolei wczesne próby delegowania zadań do darmowych modeli open-source kończyły się ucinaniem kodu w połowie pliku i błędami kompilacji.
- **Zadanie (Task):** Zaprojektować i wdrożyć architekturę dwupoziomowej orkiestracji (**Two-Tier Cognitive Architecture**), w której drogi agent główny pełni rolę architekta/planisty, a darmowe podwykonawcze modele LLM realizują masowe zadania w izolowanej piaskownicy z automatyczną kontrolą jakości i zerowym kosztem tokenów.
- **Działanie (Action):** 
  1. *Root Cause Fix Limitów:* Zdiagnozowano, że obcinanie plików wynikało ze sztucznego ograniczenia `max_tokens: 4096` w konfiguracji Aidera – odblokowano limity do 65k tokenów wyjściowych i 1M kontekstu zgodnie z rzeczywistą specyfikacją API OpenRouter.
  2. *FastMCP Worker Bridge & Task Router:* Zbudowano serwer FastMCP (`scripts/worker_mcp.py`) wyposażony w inteligentny router zadaniowy dopasowujący model do specyfiki kodu: `minimax-m3` (1M kontekstu) do scaffoldingów full-stack, `nemotron-550b` (550B MoE) do algorytmów binarnych/C/Rust, `glm-5.2` do naprawy bugów SWE-bench oraz `nemotron-lightning` do testów TDD.
  3. *Worktree Sandboxing & Self-Healing Loop:* Każde zadanie uruchamiane jest w odizolowanym Git Worktree (`.git/worktrees_active/<id>`) z automatycznym przekazaniem wykrytego polecenia testowego (`npx tsc --noEmit` / `pytest`) do pętli samonaprawczej Aidera (`--auto-test --test-cmd`).
  4. *Dynamic Skill Injection:* Zaimplementowano mostek przekazujący pakiety `agentskills.io` do bezstanowych subagentów w trybie read-only (`--read`).
- **Wynik (Result):** Osiągnięto **100% redukcję kosztów tokenowych** (0.00 USD) dla masowych zadań inżynieryjnych przy **92-95% skuteczności wykonania** w benchmarkach syntetycznych. Agent nadrzędny otrzymuje jedynie 3-linijkowe ustrukturyzowane podsumowanie (*Zero Context Bleed*), a kod trafia do repozytorium dopiero po pomyślnej weryfikacji bramki jakościowej.
- **Refleksja (Reflection):** Skalowalne systemy agentowe nie wymagają używania najdroższych modeli do każdego podzadania. Kluczem inżynieryjnym jest rozdzielenie odpowiedzialności poznawczej: model o najwyższym reasoning projektuje interfejsy i weryfikuje diffy, podczas gdy darmowe, wyspecjalizowane modele wykonawcze pracują w izolowanych piaskownicach z twardymi, automatycznymi testami kompilacji.

---

### Historia 4: Maszyna Stanów Planowania i Eliminacja Kodu-Zombie w Sesjach Interaktywnych
- **Kontekst (Situation):** Tradycyjne planowanie wieloetapowych zadań przez agentów AI cierpiało na tzw. "amnezję rewizyjną" – gdy użytkownik zgłaszał poprawkę w trzeciej turze dyskusji, model potrafił przepisać cały plan od nowa, tracąc wcześniej zweryfikowane ścieżki do plików, wersje bibliotek czy polecenia testowe, lub zostawiał w planie przestarzały kod, tworząc hybrydowe potworki implementacyjne.
- **Zadanie (Task):** Opracować i sformalizować protokół integralności dokumentów żyjących (`planning-and-document-integrity.md`), który zagwarantuje ciągłość wiedzy i uniemożliwi powstawanie kodu-zombie.
- **Działanie (Action):** Zdefiniowano jawną maszynę stanów planowania:
  1. *State 1 (Draft):* Odkrycie i zablokowanie faktów o repozytorium (*Discovered Baseline Facts Lock*).
  2. *State 2 (Refinement):* Obowiązkowy nagłówek `Iteration Delta` dokumentujący co dodano, co zmieniono, a co usunięto. Wprowadzono zasadę czyszczenia aktywnej specyfikacji technicznej (*Active SSOT*) – wycofane rozwiązania są bezwzględnie wycinane z sekcji aktywnej i zapisywane jako 1-linijkowy atomowy nagrobek `[PRUNED]` w logu decyzji.
  3. *State 3 (Execution):* Niezmienny plan staje się kontraktem fazy wdrożeniowej po uzyskaniu zgody "GO".
- **Wynik (Result):** Całkowicie wyeliminowano sytuacje, w których agent ponownie zadawał te same pytania lub gubił odkryte wcześniej komendy testowe. Czystość aktywnej specyfikacji zapobiegła powstawaniu błędów implementacyjnych wynikających z mieszania starych i nowych założeń.
- **Refleksja (Reflection):** Modele językowe generują tekst probabilistycznie na podstawie całego widocznego kontekstu. Pozostawienie wycofanego pomysłu w tekście specyfikacji "dla pamięci" drastycznie zwiększa prawdopodobieństwo, że model wygeneruje kod łączący sprzeczne koncepcje. Jedyną skuteczną obroną jest fizyczne wyczyszczenie aktywnego bloku kodu i zachowanie wyłącznie deklaracji w audytowalnym logu decyzji.

---

### Historia 5: Zautomatyzowany Walidator Jakości Środowiska CI/CD (`validate_suite.py`)
- **Kontekst (Situation):** Wraz z rozrostem ekosystemu do 36 umiejętności i 16 reguł systemowych, ręczne sprawdzanie czy każdy skill spełnia standardy `agentskills.io`, czy nazwa katalogu zgadza się ze znacznikiem YAML i czy opisy nie przekraczają limitów tokenowych stało się podatne na błędy ludzkie. Przekroczenie limitu opisu w pliku `SKILL.md` powodowało ciche ucinanie promptów systemowych przez asystentów AI.
- **Zadanie (Task):** Zbudować zautomatyzowane narzędzie kontroli jakości (Quality Gate), które w sposób deterministyczny zweryfikuje integralność wszystkich komponentów pakietu przed każdym commitem.
- **Działanie (Action):** Opracowano skrypt `scripts/validate_suite.py` w czystym Pythonie 3 bez zewnętrznych zależności. Skrypt implementuje:
  1. Parser regexowy frontmatter YAML weryfikujący poprawność struktury bloków `---`.
  2. Twardą asercję `desc_val <= 1024` znaków zapobiegającą degradacji promptu systemowego.
  3. Weryfikację tożsamości nazwy katalogu z wartością pola `name:`.
  4. Walidator składni JSON dla plików konfiguracyjnych MCP za pomocą modułu `json`.
  5. Semantyczny audyt obecności krytycznych dyrektyw (m.in. Pre-Flight Skill Gate) w 4 manifestach bazowych (`CODEX.md`, `GEMINI.md`, `CLAUDE.md`, `.cursorrules`).
  6. Weryfikację integralności podsystemu Sub-Workerów (`worker_mcp.py`, `worker_cli.py`, `worker_profiles.json`, szablony Aidera).
- **Wynik (Result):** Utworzono niezawodny test harness zwracający kod wyjścia 0 w przypadku sukcesu lub kod 1 z listą precyzyjnych błędów. Czas wykonania pełnej walidacji 36 skilli i 16 reguł wynosi poniżej 50 ms.
- **Refleksja (Reflection):** Dokumentacja i prompty systemowe dla agentów AI to taki sam kod jak każdy inny. Wymagają automatycznych testów jednostkowych, linterów i bramek jakościowych. Jeśli reguła nie jest testowana automatycznie, prędzej czy później ulegnie cichej degradacji.

---

## 5. Zweryfikowany Twardy Stos Technologiczny

| Kategoria | Technologie, Narzędzia i Protokoły |
|---|---|
| **Języki i Powłoki** | Python 3.8+ (`pathlib`, `shutil`, `re`, `json`, `argparse`, `subprocess`), POSIX Bash 4+ (`set -euo pipefail`), Windows PowerShell 5.1 / 7+ (`CmdletBinding`, `New-Item`, `Copy-Item`) |
| **Architektura Orkiestracji Sub-Agentów** | FastMCP (`fastmcp` Python SDK), Aider Headless Engine (`aider`), Git Worktrees (`git worktree add/remove`), Two-Tier Cognitive Architecture, Task-Specialized Intelligent Routing |
| **Pula Modeli i API** | OpenRouter Free Tier (`minimax/minimax-m3:free` 1M Context, `nvidia/nemotron-3-ultra-550b-a55b:free` 550B MoE, `z-ai/glm-5.2:free` 256k Context, `nvidia/nemotron-3.5-lightning:free`), Zhipu BigModel PAAS Direct API (`glm-4-flash`), SiliconFlow |
| **Standardy AI i Schematy** | `agentskills.io` standard (YAML frontmatter), Agentic AI Foundation (AAIF) `AGENTS.md` standard, Model Context Protocol (MCP) v1.0, Markdown, Mermaid.js |
| **Wspierane Platformy AI** | OpenAI Codex CLI / Codex API (`~/.codex/`), Antigravity / Gemini CLI (`~/.gemini/`), Anthropic Claude Code (`~/.claude/`), Cursor IDE (.mdc rules format & `.cursorrules`) |
| **Systemy Operacyjne** | Linux (Ubuntu / Debian / RHEL - ext4), macOS (Darwin - APFS / zsh), Windows 10/11 (NTFS - PowerShell Core) |
| **Serwery MCP i Narzędzia** | `chinese-worker` (Autonomous Sub-Worker Bridge), `mempalace` (Long-Term Knowledge Graph), `@danielsogl/lighthouse-mcp` (Web Audits), `chrome-devtools-mcp` (Chromium Performance Timelines), `@modelcontextprotocol/server-postgres`, `@modelcontextprotocol/server-docker`, `firecrawl-mcp` (Stealth Web Scraper), `@ast-grep/mcp` (AST Tree Search & Linting), `@modelcontextprotocol/server-puppeteer`, `@modelcontextprotocol/server-github`, `oracle.oci-api-mcp-server`, Google StitchMCP |
| **Jakość i Weryfikacja** | Deterministic Quality Harness (`scripts/validate_suite.py`), TypeScript Safety Gate (`npx tsc --noEmit`), TDD Red-Green-Refactor, Self-Healing Quality Gate, 5-Axis Code Review (Correctness, Readability, Architecture, Security OWASP Top 10, Performance) |
| **System Kontroli Wersji** | Git CLI, GitHub API (przez dedykowany GitHub MCP Server) |
