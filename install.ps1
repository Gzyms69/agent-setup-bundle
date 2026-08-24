# ==============================================================================
# Installer: Multi-Platform Agent Environment & Skill Suite (Windows PowerShell)
# Supported: OpenAI Codex, Antigravity / Gemini CLI, Claude Code, Cursor IDE (.mdc)
# ==============================================================================

[CmdletBinding()]
param (
    [switch]$All,
    [switch]$Codex,
    [switch]$Gemini,
    [switch]$Claude,
    [switch]$Cursor,
    [switch]$Help
)

if ($Help) {
    Write-Host "Usage: .\install.ps1 [OPTION]"
    Write-Host "Options:"
    Write-Host "  -All       Install configuration for all platforms (default: Codex, Gemini, Claude, Cursor)"
    Write-Host "  -Codex     Install configuration for OpenAI Codex only"
    Write-Host "  -Gemini    Install configuration for Antigravity / Gemini CLI only"
    Write-Host "  -Claude    Install configuration for Claude Code only"
    Write-Host "  -Cursor    Install configuration for Cursor IDE only"
    exit 0
}

# Default to All if no specific platform switch was passed
$InstallAll = -not ($Codex -or $Gemini -or $Claude -or $Cursor)
$InstallCodex  = $All -or $Codex -or $InstallAll
$InstallGemini = $All -or $Gemini -or $InstallAll
$InstallClaude = $All -or $Claude -or $InstallAll
$InstallCursor = $All -or $Cursor -or $InstallAll

$ScriptDir = $PSScriptRoot
if (-not $ScriptDir) {
    $ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
}

$UserProfile = $env:USERPROFILE
$TargetAgentsDir = Join-Path $UserProfile ".agents"
$TargetGeminiDir = Join-Path $UserProfile ".gemini"
$TargetClaudeDir = Join-Path $UserProfile ".claude"
$TargetCursorDir = Join-Path $UserProfile ".cursor"
$TargetCodexDir  = Join-Path $UserProfile ".codex"

Write-Host "======================================================================" -ForegroundColor Cyan
Write-Host ">>> Rozpoczynam instalacje srodowiska Agenta AI (Windows PowerShell)..." -ForegroundColor Cyan
Write-Host "======================================================================" -ForegroundColor Cyan

# 0. Wspoldzielona baza: Rules, Skills, Templates w ~/.agents/
Write-Host "[+] Kopiowanie wspoldzielonych regul (16), skilli (36) i szablonow do ~/.agents/..." -ForegroundColor Green

$RulesTarget = Join-Path $TargetAgentsDir "rules"
$SkillsTarget = Join-Path $TargetAgentsDir "skills"
$TemplatesTarget = Join-Path $TargetAgentsDir "templates"

New-Item -ItemType Directory -Force -Path $RulesTarget | Out-Null
New-Item -ItemType Directory -Force -Path $SkillsTarget | Out-Null
New-Item -ItemType Directory -Force -Path $TemplatesTarget | Out-Null

Copy-Item -Path (Join-Path $ScriptDir "rules\*") -Destination $RulesTarget -Recurse -Force
Copy-Item -Path (Join-Path $ScriptDir "skills\*") -Destination $SkillsTarget -Recurse -Force
if (Test-Path (Join-Path $ScriptDir "templates")) {
    Copy-Item -Path (Join-Path $ScriptDir "templates\*") -Destination $TemplatesTarget -Recurse -Force
}
Write-Host "    -> Zainstalowano 16 regul, 36 skilli oraz szablony w ~/.agents/" -ForegroundColor Gray

# 1. Konfiguracja dla OpenAI Codex
if ($InstallCodex) {
    Write-Host "[+] Konfiguracja srodowiska OpenAI Codex (~/.codex/)..." -ForegroundColor Green
    $CodexSkillsDir = Join-Path $TargetCodexDir "skills"
    New-Item -ItemType Directory -Force -Path $CodexSkillsDir | Out-Null

    $CodexMdSource = Join-Path $ScriptDir "core\CODEX.md"
    Copy-Item -Path $CodexMdSource -Destination (Join-Path $TargetCodexDir "AGENTS.md") -Force
    Copy-Item -Path $CodexMdSource -Destination (Join-Path $TargetCodexDir "instructions.md") -Force
    Copy-Item -Path $CodexMdSource -Destination (Join-Path $TargetCodexDir "CODEX.md") -Force

    $CodexConfigTarget = Join-Path $TargetCodexDir "config.toml"
    if (-not (Test-Path $CodexConfigTarget)) {
        Copy-Item -Path (Join-Path $ScriptDir "config\codex_config.toml") -Destination $CodexConfigTarget -Force
        Write-Host "    -> Utworzono ~/.codex/config.toml (szablon z konfiguracja MCP)" -ForegroundColor Gray
    }

    # Dowiazanie skilli dla Codexa
    $CodexCustomSkills = Join-Path $CodexSkillsDir "custom"
    if (-not (Test-Path $CodexCustomSkills)) {
        try {
            New-Item -ItemType SymbolicLink -Path $CodexCustomSkills -Target $SkillsTarget -ErrorAction Stop | Out-Null
            Write-Host "    -> Utworzono dowiazanie symboliczne dla skilli ~/.codex/skills/custom" -ForegroundColor Gray
        } catch {
            # Fallback na Junction lub Directory Copy
            try {
                New-Item -ItemType Junction -Path $CodexCustomSkills -Target $SkillsTarget -ErrorAction Stop | Out-Null
                Write-Host "    -> Utworzono Directory Junction dla skilli ~/.codex/skills/custom" -ForegroundColor Gray
            } catch {
                Copy-Item -Path $SkillsTarget -Destination $CodexCustomSkills -Recurse -Force
                Write-Host "    -> Skopiowano skille do ~/.codex/skills/custom (kopia)" -ForegroundColor Gray
            }
        }
    }
    Write-Host "    -> Zainstalowano AGENTS.md, CODEX.md oraz instructions.md w ~/.codex/" -ForegroundColor Gray
}

# 2. Konfiguracja dla Antigravity / Gemini CLI
if ($InstallGemini) {
    Write-Host "[+] Konfiguracja srodowiska Antigravity / Gemini CLI (~/.gemini/)..." -ForegroundColor Green
    $GeminiPolicies = Join-Path $TargetGeminiDir "policies"
    $GeminiConfig = Join-Path $TargetGeminiDir "config"
    New-Item -ItemType Directory -Force -Path $GeminiPolicies | Out-Null
    New-Item -ItemType Directory -Force -Path $GeminiConfig | Out-Null

    Copy-Item -Path (Join-Path $ScriptDir "core\GEMINI.md") -Destination (Join-Path $TargetGeminiDir "GEMINI.md") -Force
    Copy-Item -Path (Join-Path $ScriptDir "policies\mcp-planning.toml") -Destination (Join-Path $GeminiPolicies "mcp-planning.toml") -Force

    $GeminiSettings = Join-Path $TargetGeminiDir "settings.json"
    if (-not (Test-Path $GeminiSettings)) {
        Copy-Item -Path (Join-Path $ScriptDir "config\settings.json") -Destination $GeminiSettings -Force
        Write-Host "    -> Utworzono ~/.gemini/settings.json (szablon)" -ForegroundColor Gray
    }
    $GeminiMcpConfig = Join-Path $GeminiConfig "mcp_config.json"
    if (-not (Test-Path $GeminiMcpConfig)) {
        Copy-Item -Path (Join-Path $ScriptDir "config\mcp_config.json") -Destination $GeminiMcpConfig -Force
        Write-Host "    -> Utworzono ~/.gemini/config/mcp_config.json (szablon)" -ForegroundColor Gray
    }
}

# 3. Konfiguracja dla Claude Code
if ($InstallClaude) {
    Write-Host "[+] Konfiguracja srodowiska Claude Code (~/.claude/)..." -ForegroundColor Green
    $ClaudeAgents = Join-Path $TargetClaudeDir "agents"
    New-Item -ItemType Directory -Force -Path $ClaudeAgents | Out-Null

    Copy-Item -Path (Join-Path $ScriptDir "core\CLAUDE.md") -Destination (Join-Path $TargetClaudeDir "CLAUDE.md") -Force
    Copy-Item -Path (Join-Path $ScriptDir "core\claude\agents\*") -Destination $ClaudeAgents -Recurse -Force

    # Dowiazanie skilli dla Claude Code
    $ClaudeSkills = Join-Path $TargetClaudeDir "skills"
    if (-not (Test-Path $ClaudeSkills)) {
        try {
            New-Item -ItemType SymbolicLink -Path $ClaudeSkills -Target $SkillsTarget -ErrorAction Stop | Out-Null
            Write-Host "    -> Utworzono dowiazanie symboliczne dla skilli ~/.claude/skills" -ForegroundColor Gray
        } catch {
            try {
                New-Item -ItemType Junction -Path $ClaudeSkills -Target $SkillsTarget -ErrorAction Stop | Out-Null
                Write-Host "    -> Utworzono Directory Junction dla skilli ~/.claude/skills" -ForegroundColor Gray
            } catch {
                Copy-Item -Path $SkillsTarget -Destination $ClaudeSkills -Recurse -Force
                Write-Host "    -> Skopiowano skille do ~/.claude/skills (kopia)" -ForegroundColor Gray
            }
        }
    }

    $ClaudeMcp = Join-Path $TargetClaudeDir "mcp.json"
    if (-not (Test-Path $ClaudeMcp)) {
        Copy-Item -Path (Join-Path $ScriptDir "config\mcp_config.json") -Destination $ClaudeMcp -Force
        Write-Host "    -> Utworzono ~/.claude/mcp.json (szablon MCP)" -ForegroundColor Gray
    }
    Write-Host "    -> Zainstalowano CLAUDE.md oraz subagentow w ~/.claude/agents/" -ForegroundColor Gray
}

# 4. Konfiguracja dla Cursor IDE (Modern MDC format)
if ($InstallCursor) {
    Write-Host "[+] Konfiguracja regul Modern Cursor (~/.cursor/rules/*.mdc)..." -ForegroundColor Green
    $CursorRules = Join-Path $TargetCursorDir "rules"
    New-Item -ItemType Directory -Force -Path $CursorRules | Out-Null

    Copy-Item -Path (Join-Path $ScriptDir "core\cursor\rules\*") -Destination $CursorRules -Recurse -Force
    $CursorMcp = Join-Path $TargetCursorDir "mcp.json"
    if (-not (Test-Path $CursorMcp)) {
        Copy-Item -Path (Join-Path $ScriptDir "config\cursor_mcp.json") -Destination $CursorMcp -Force
        Write-Host "    -> Utworzono ~/.cursor/mcp.json (szablon)" -ForegroundColor Gray
    }
}

Write-Host "======================================================================" -ForegroundColor Cyan
Write-Host ">>> SUKCES: Srodowisko agenta zostalo w pelni zainstalowane na Windows!" -ForegroundColor Green
Write-Host ">>> Zainstalowane komponenty:"
Write-Host "    - Shared Suite: ~/.agents/ (16 regul, 36 skilli, szablony AGENTS.md)" -ForegroundColor White
if ($InstallCodex) {
    Write-Host "    - OpenAI Codex: ~/.codex/ (AGENTS.md, instructions.md, config.toml, skills link)" -ForegroundColor White
}
if ($InstallGemini) {
    Write-Host "    - Antigravity / Gemini CLI: ~/.gemini/ (GEMINI.md, settings.json, policies)" -ForegroundColor White
}
if ($InstallClaude) {
    Write-Host "    - Claude Code: ~/.claude/ (CLAUDE.md, .claude/agents/, skills link, mcp.json)" -ForegroundColor White
}
if ($InstallCursor) {
    Write-Host "    - Cursor IDE: ~/.cursor/ (rules/*.mdc, mcp.json)" -ForegroundColor White
}
Write-Host ""
Write-Host ">>> Wskazowki konfiguracji:" -ForegroundColor Yellow
Write-Host "    1. Skopiuj templates/AGENTS.md do korzenia swoich projektow." -ForegroundColor Gray
Write-Host "    2. Uzupelnij klucze API w settings.json / config.toml / mcp.json." -ForegroundColor Gray
Write-Host "    3. W ~/.agents/rules/system-identity.md wpisz bazowe dane sprzetu." -ForegroundColor Gray
Write-Host "======================================================================" -ForegroundColor Cyan
