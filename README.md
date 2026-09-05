# Open Workflow Skills

> **100 reusable AI workflow skills — bilingual, auditable, installable.**  
> **100 个可复用、可审计、可安装的 AI 工作流 Skills。**

[![Agent Skills](https://img.shields.io/badge/format-Agent%20Skills-111111)](https://agentskills.io/specification)
[![Skills](https://img.shields.io/badge/skills-100-blue)](#skill-catalog)
[![Production](https://img.shields.io/badge/production-47-brightgreen)](#reliability-model)
[![Integration](https://img.shields.io/badge/integration-33-blue)](#reliability-model)
[![Experimental](https://img.shields.io/badge/experimental-20-yellow)](#reliability-model)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

**Stop collecting prompts. Install workflows.**  
**别再收藏 Prompt 了，把可复用的工作流装进 Agent。**

---

## What this repository is / 这是什么

Open Workflow Skills is a bilingual library of **100 reusable AI workflows** covering content, office productivity, data, development, design, business, communication, personal productivity, DevOps, and learning.

它不是“100 个神奇 Prompt”，也不声称安装一个 Markdown 文件就会凭空获得邮箱、数据库、浏览器、服务器或付费 API 权限。

每个 Skill 都明确说明：

- **Purpose / 用途**
- **Chinese + English description / 中英文说明**
- **Production / Integration / Experimental 状态**
- **Automation level / 自动化等级**
- **Core stack / 核心工具**
- **Permissions / 所需权限**
- **Dependencies / 运行依赖**
- **Install command / 安装方式**
- **Workflow / 执行流程**
- **Validation / 验证方法**
- **Safety / 安全边界**
- **Evaluation cases / Eval 案例**

The repository follows the open **Agent Skills** directory format: every skill is a directory containing at minimum a `SKILL.md`; optional resources may live in `scripts/`, `references/`, and `assets/`.

Official/open references:

- Agent Skills specification: https://agentskills.io/specification
- OpenAI — Skills in ChatGPT: https://help.openai.com/en/articles/20001066
- OpenAI Academy — Using skills: https://openai.com/academy/skills/
- Community `skills` CLI: https://github.com/vercel-labs/skills

> `npx skills` is a **community ecosystem CLI**, not an OpenAI-official installer. Treat third-party skills as executable dependencies: inspect instructions and scripts before granting shell, filesystem, network, or credential access.

---

## Discover by task / 按你想完成的任务搜索

This repository is designed to be searchable by **real user intent**, not only by internal skill names. Common searches include:

- **AI agent skills / Agent Skills / AI automation / AI workflow / workflow automation / agent automation**
- **ChatGPT skills / Codex skills / Claude Code skills / Cursor skills / coding agent workflows**
- **video automation / AI subtitles / bilingual subtitles / long video to shorts / podcast summarizer / PPT to video**
- **office automation / email assistant / meeting minutes / calendar automation / weekly report / SOP generator**
- **Excel automation / spreadsheet analysis / data cleaning / web scraping / dashboard / anomaly detection**
- **AI coding / code review / debugging agent / unit tests / API generator / Docker / CI/CD / DevOps automation**
- **AI design / background remover / image upscale / landing page builder / Figma to code / SVG icons**
- **competitor monitoring / pricing analysis / CRM automation / financial report analysis / knowledge base / RAG**
- **resume builder / trip planner / paper summarizer / Anki flashcards / study plan / pronunciation coach**
- **AI 自动化 / AI 工作流 / AI 智能体 / Agent Skills / 自动化脚本 / AI 办公 / AI 编程**
- **视频自动字幕 / 双语字幕 / 长视频切片 / 小红书图文 / AI 配音 / PPT 转视频**
- **Excel 自动化 / 数据清洗 / 网页爬虫 / 竞品监控 / 自动周报 / 邮件自动分类**
- **AI 简历 / 论文总结 / 思维导图 / 学习计划 / 英语发音 / AI 课程生成**

For the complete bilingual alias index, see **[`docs/search-index.md`](docs/search-index.md)**. Each individual `SKILL.md` also contains task-specific English and Chinese search aliases.

> Searchability is treated as navigation, not keyword stuffing: every alias maps to a real skill in this repository.

---

## Why this exists / 为什么做这个

A useful AI workflow is rarely just:

```text
Prompt → model → answer
```

A reliable workflow usually looks more like:

```text
Intent
  ↓
Skill discovery
  ↓
SKILL.md
  ↓
Dependency & permission check
  ↓
Deterministic tool / API / model
  ↓
Validation
  ↓
Human approval when needed
  ↓
Output + audit trail
```

**Skill 负责“怎么做”，工具负责“真的执行”，验证负责“证明做对了”。**

---

## Quick start / 快速开始

### 1. Browse before installing / 先查看

```bash
npx skills add BryceYuuu/open-workflow-skills --list
```

### 2. Install one skill into the current project / 安装单个 Skill

```bash
npx skills add BryceYuuu/open-workflow-skills \
  --skill video-bilingual-subtitles
```

### 3. Install for a specific agent / 指定 Agent

```bash
npx skills add BryceYuuu/open-workflow-skills \
  --skill spreadsheet-merge \
  --agent codex
```

The community CLI supports multiple Agent Skills-compatible clients; exact support can change over time, so use `npx skills --help` or the CLI repository as the current source of truth.

### 4. Local repository preview / 本地预览

```bash
git clone https://github.com/BryceYuuu/open-workflow-skills.git
cd open-workflow-skills

./install.sh list
./install.sh video-bilingual-subtitles
```

### 5. Check environment / 环境检查

```bash
./scripts/doctor.sh
```

### 6. Validate repository / 验证仓库

```bash
python3 scripts/validate_registry.py
./scripts/test.sh
```

---

## Reliability model / 真实性与质量分级

The 100 skills were intentionally **not** given the same reliability label.

| Status | Count | Meaning |
|---|---:|---|
| 🟢 **Production Ready / 成熟可落地** | **47** | Underlying tooling is mature and the workflow can be repeatable when declared dependencies are present. |
| 🔵 **Integration Required / 需要外部集成** | **33** | Real capability, but requires an API, App, OAuth, browser session, database, external data, or infrastructure. |
| 🟡 **Experimental / Assisted / 实验性** | **20** | Technically feasible, but quality, subjectivity, real-time requirements, or end-to-end reliability require human review. |

**“Experimental” does not mean fake. “Production” does not mean risk-free.**

---

## Automation levels / 自动化等级

| Level | Definition |
|---|---|
| `L1` | AI-native reasoning or generation; little/no external execution. |
| `L2` | Local deterministic tools/scripts, such as Python, FFmpeg, Pandas, Git, ImageMagick. |
| `L3` | External APIs/models or specialized services. |
| `L4` | Connected Agent: OAuth, Apps, browser, database, webhooks, schedulers, external accounts. |
| `L5` | Human approval is required for consequential writes/actions. |

A skill may span levels, e.g. `L3-L4`.

---

## Security model / 安全模型

Installing a skill **does not grant permissions**.

A skill may *request* capabilities such as:

- filesystem read/write
- shell commands
- network access
- browser automation
- API keys
- Gmail / Calendar / CRM access
- infrastructure credentials
- privileged server access

Before running third-party skills:

1. Read `SKILL.md`.
2. Inspect `scripts/` if present.
3. Check requested permissions.
4. Prefer project-level installation for unfamiliar skills.
5. Avoid `-y` on first install of untrusted code.
6. Never paste secrets into a repository or `SKILL.md`.
7. Approval-gate production deploys, sends, payments, signing, destructive writes, and other high-impact actions.

See [SECURITY.md](SECURITY.md) and [docs/safety.md](docs/safety.md).

---

## Skill catalog

| # | Skill / 中文 | Category | Status | Quality | Level |
|---:|---|---|---|---:|---|
| 01 | [Image Watermark](skills/image-watermark/) / 批量图片水印 | Content & Media | 🟢 Production Ready | 5.0/5 | `L2` |
| 02 | [Video Bilingual Subtitles](skills/video-bilingual-subtitles/) / 视频双语字幕 | Content & Media | 🟢 Production Ready | 4.5/5 | `L2-L3` |
| 03 | [URL to Short Video](skills/url-to-short-video/) / 网页转短视频 | Content & Media | 🟡 Experimental / Assisted | 3.0/5 | `L3` |
| 04 | [Social Image Batch](skills/social-image-batch/) / 社媒配图批量生成 | Content & Media | 🔵 Integration Required | 4.0/5 | `L3` |
| 05 | [Long Video to Clip Candidates](skills/long-video-to-clips/) / 长视频高光候选 | Content & Media | 🟡 Experimental / Assisted | 3.5/5 | `L2-L3` |
| 06 | [Podcast Digest](skills/podcast-digest/) / 播客摘要与文字稿 | Content & Media | 🟢 Production Ready | 4.5/5 | `L2-L3` |
| 07 | [Social Carousel](skills/social-carousel/) / 社交媒体轮播图 | Content & Media | 🔵 Integration Required | 4.0/5 | `L3` |
| 08 | [Thumbnail Generator](skills/thumbnail-generator/) / 视频封面候选生成 | Content & Media | 🟡 Experimental / Assisted | 3.5/5 | `L3` |
| 09 | [Meme GIF Generator](skills/meme-gif-generator/) / Meme/GIF 创意生成 | Content & Media | 🟡 Experimental / Assisted | 3.0/5 | `L3` |
| 10 | [Voice Generator](skills/voice-generator/) / AI 配音生成 | Content & Media | 🔵 Integration Required | 4.0/5 | `L3` |
| 11 | [Slides to Video](skills/slides-to-video/) / PPT 转讲解视频 | Content & Media | 🟡 Experimental / Assisted | 3.0/5 | `L3` |
| 12 | [Auto BGM](skills/auto-bgm/) / 视频自动配乐 | Content & Media | 🟡 Experimental / Assisted | 2.5/5 | `L3` |
| 13 | [Live Teleprompter](skills/live-teleprompter/) / 实时 AI 提词器 | Content & Media | 🟡 Experimental / Assisted | 2.5/5 | `L4` |
| 14 | [Article to Video](skills/article-to-video/) / 文章转视频 | Content & Media | 🟡 Experimental / Assisted | 3.0/5 | `L3` |
| 15 | [Recording to Content](skills/recording-to-content/) / 录音多平台内容生成 | Content & Media | 🟢 Production Ready | 4.5/5 | `L2-L3` |
| 16 | [Smart File Organizer](skills/smart-file-organizer/) / 智能文件整理 | Office & Productivity | 🟢 Production Ready | 4.5/5 | `L2` |
| 17 | [Personalized Mail Merge](skills/personalized-mail-merge/) / 个性化批量邮件 | Office & Productivity | 🔵 Integration Required | 4.0/5 | `L3-L4` |
| 18 | [Document Translator](skills/document-translator/) / 文档翻译与排版保留 | Office & Productivity | 🟡 Experimental / Assisted | 3.0/5 | `L2-L3` |
| 19 | [Meeting Minutes](skills/meeting-minutes/) / 会议纪要与待办 | Office & Productivity | 🟢 Production Ready | 4.5/5 | `L2-L3` |
| 20 | [Chat to Todo](skills/chat-to-todo/) / 聊天消息转待办 | Office & Productivity | 🔵 Integration Required | 4.0/5 | `L4` |
| 21 | [Inbox Triage](skills/inbox-triage/) / AI 邮件分流 | Office & Productivity | 🔵 Integration Required | 4.5/5 | `L4` |
| 22 | [Survey Builder](skills/survey-builder/) / 问卷生成与分析 | Office & Productivity | 🔵 Integration Required | 4.0/5 | `L3-L4` |
| 23 | [Calendar Coordinator](skills/calendar-coordinator/) / 会议时间协调 | Office & Productivity | 🔵 Integration Required | 4.0/5 | `L4` |
| 24 | [Weekly Report](skills/weekly-report/) / 自动业务周报 | Office & Productivity | 🔵 Integration Required | 4.5/5 | `L4` |
| 25 | [Expense Parser](skills/expense-parser/) / 报销票据识别 | Office & Productivity | 🔵 Integration Required | 4.5/5 | `L3-L4` |
| 26 | [SOP Generator](skills/sop-generator/) / 操作流程转 SOP | Office & Productivity | 🟡 Experimental / Assisted | 3.5/5 | `L2-L3` |
| 27 | [Employee Onboarding](skills/employee-onboarding/) / 新人入职资料生成 | Office & Productivity | 🔵 Integration Required | 4.0/5 | `L3-L4` |
| 28 | [Contract Signing Workflow](skills/contract-signing-workflow/) / 合同签署流转 | Office & Productivity | 🔵 Integration Required | 3.5/5 | `L4-L5` |
| 29 | [Invoice Data Extractor](skills/invoice-data-extractor/) / 发票数据提取 | Data & Analytics | 🟢 Production Ready | 4.5/5 | `L2-L3` |
| 30 | [Web Data Extractor](skills/web-data-extractor/) / 网页结构化数据采集 | Data & Analytics | 🔵 Integration Required | 4.0/5 | `L2-L4` |
| 31 | [Sales Forecast](skills/sales-forecast/) / 销售预测 | Data & Analytics | 🟡 Experimental / Assisted | 3.5/5 | `L2` |
| 32 | [Spreadsheet Merge](skills/spreadsheet-merge/) / 智能表格合并 | Data & Analytics | 🟢 Production Ready | 4.5/5 | `L2` |
| 33 | [Spreadsheet Dashboard](skills/spreadsheet-dashboard/) / 表格分析与 Dashboard | Data & Analytics | 🟢 Production Ready | 4.0/5 | `L2` |
| 34 | [Trend Research Agent](skills/trend-research/) / 趋势研究 Agent | Data & Analytics | 🟡 Experimental / Assisted | 3.5/5 | `L3-L4` |
| 35 | [Sentiment Analysis](skills/sentiment-analysis/) / 用户情绪与主题分析 | Data & Analytics | 🔵 Integration Required | 3.5/5 | `L2-L3` |
| 36 | [Data Anomaly Monitor](skills/data-anomaly-monitor/) / 数据异常监控 | Data & Analytics | 🔵 Integration Required | 4.0/5 | `L4` |
| 37 | [Document Diff](skills/document-diff/) / 文档语义差异比较 | Data & Analytics | 🟢 Production Ready | 4.0/5 | `L2-L3` |
| 38 | [Data Cleaner](skills/data-cleaner/) / AI 数据清洗 | Data & Analytics | 🟢 Production Ready | 4.5/5 | `L2` |
| 39 | [Log Analyzer](skills/log-analyzer/) / 日志分析与故障复盘 | Development & Engineering | 🟢 Production Ready | 4.0/5 | `L2` |
| 40 | [Figma to Frontend](skills/figma-to-frontend/) / Figma 转前端 | Development & Engineering | 🔵 Integration Required | 4.0/5 | `L3-L4` |
| 41 | [Code Refactor](skills/code-refactor/) / 代码重构 | Development & Engineering | 🟢 Production Ready | 4.5/5 | `L2` |
| 42 | [Framework Migration](skills/framework-migration/) / 技术栈迁移 | Development & Engineering | 🔵 Integration Required | 3.5/5 | `L2-L3` |
| 43 | [Repository Documentation](skills/repository-docs/) / 代码仓库文档生成 | Development & Engineering | 🟢 Production Ready | 4.5/5 | `L2` |
| 44 | [Pull Request Review](skills/pull-request-review/) / PR 代码审查 | Development & Engineering | 🟢 Production Ready | 4.5/5 | `L2-L3` |
| 45 | [API Generator](skills/api-generator/) / 自然语言生成 API | Development & Engineering | 🔵 Integration Required | 4.0/5 | `L2-L3` |
| 46 | [Debug Agent](skills/debug-agent/) / 自动 Debug Agent | Development & Engineering | 🟢 Production Ready | 4.5/5 | `L2` |
| 47 | [Unit Test Generator](skills/unit-test-generator/) / 单元测试生成器 | Development & Engineering | 🟢 Production Ready | 4.5/5 | `L2` |
| 48 | [Cron Builder](skills/cron-builder/) / 定时任务生成器 | Development & Engineering | 🟢 Production Ready | 5.0/5 | `L2` |
| 49 | [Image Upscaler](skills/image-upscale/) / 图片超分与增强 | Design & Creative | 🔵 Integration Required | 4.0/5 | `L3` |
| 50 | [Background Remover](skills/background-remover/) / 自动抠图 | Design & Creative | 🟢 Production Ready | 4.5/5 | `L2-L3` |
| 51 | [Brand Kit Generator](skills/brand-kit-generator/) / 品牌视觉方向生成 | Design & Creative | 🟡 Experimental / Assisted | 3.0/5 | `L3` |
| 52 | [Landing Page Builder](skills/landing-page-builder/) / 落地页生成器 | Design & Creative | 🔵 Integration Required | 4.0/5 | `L2-L4` |
| 53 | [Sketch to UI](skills/sketch-to-ui/) / 草图转高保真 UI | Design & Creative | 🟡 Experimental / Assisted | 3.5/5 | `L3` |
| 54 | [SVG Icon Generator](skills/svg-icon-generator/) / SVG 图标生成 | Design & Creative | 🔵 Integration Required | 3.5/5 | `L2-L3` |
| 55 | [Product Mockup Generator](skills/product-mockup/) / 产品 Mockup 生成 | Design & Creative | 🟡 Experimental / Assisted | 3.0/5 | `L3` |
| 56 | [Palette Extractor](skills/palette-extractor/) / 配色提取 | Design & Creative | 🟢 Production Ready | 5.0/5 | `L2` |
| 57 | [Multi-platform Resize](skills/multi-platform-resize/) / 全平台智能尺寸适配 | Design & Creative | 🟡 Experimental / Assisted | 3.5/5 | `L2-L3` |
| 58 | [Font Pairing](skills/font-pairing/) / 字体搭配建议 | Design & Creative | 🔵 Integration Required | 3.5/5 | `L2-L3` |
| 59 | [Pricing Analysis](skills/pricing-analysis/) / 定价分析 | Business & Growth | 🟡 Experimental / Assisted | 3.5/5 | `L2-L3` |
| 60 | [Competitor Monitor](skills/competitor-monitor/) / 竞争对手自动监控 | Business & Growth | 🔵 Integration Required | 4.0/5 | `L4` |
| 61 | [Earnings Analyzer](skills/earnings-analyzer/) / 财报分析 | Business & Growth | 🟢 Production Ready | 4.5/5 | `L2-L3` |
| 62 | [Lead Follow-up](skills/lead-followup/) / CRM 线索跟进 | Business & Growth | 🔵 Integration Required | 4.0/5 | `L4` |
| 63 | [Invoice Generator](skills/invoice-generator/) / 商业发票生成 | Business & Growth | 🟢 Production Ready | 4.5/5 | `L2-L3` |
| 64 | [Strategy Backtest](skills/strategy-backtest/) / 交易策略回测 | Business & Growth | 🟡 Experimental / Assisted | 3.5/5 | `L2-L3` |
| 65 | [Market Technical Analysis](skills/market-technical-analysis/) / 市场技术指标分析 | Business & Growth | 🟢 Production Ready | 4.0/5 | `L2-L3` |
| 66 | [Budget Analyzer](skills/budget-analyzer/) / 预算与现金流分析 | Business & Growth | 🟢 Production Ready | 4.5/5 | `L2-L4` |
| 67 | [Portfolio Analyzer](skills/portfolio-analyzer/) / 投资组合分析 | Business & Growth | 🟢 Production Ready | 4.5/5 | `L2-L4` |
| 68 | [Knowledge Base Builder](skills/knowledge-base-builder/) / 知识库生成器 | Business & Growth | 🟢 Production Ready | 4.0/5 | `L2-L3` |
| 69 | [Conversation Action Items](skills/conversation-action-items/) / 聊天待办提取 | Communication & Social | 🟢 Production Ready | 4.5/5 | `L2` |
| 70 | [Personalized Greetings](skills/personalized-greetings/) / 个性化祝福 | Communication & Social | 🟢 Production Ready | 4.0/5 | `L1-L2` |
| 71 | [Press Release Generator](skills/press-release-generator/) / 新闻稿生成器 | Communication & Social | 🟢 Production Ready | 4.5/5 | `L1-L2` |
| 72 | [Reply Assistant](skills/reply-assistant/) / 智能回复助手 | Communication & Social | 🟢 Production Ready | 4.5/5 | `L1-L2` |
| 73 | [Pitch Generator](skills/pitch-generator/) / Pitch 生成器 | Communication & Social | 🟢 Production Ready | 4.5/5 | `L1-L2` |
| 74 | [Social FAQ Reply](skills/social-faq-reply/) / 社交媒体 FAQ 回复 | Communication & Social | 🔵 Integration Required | 4.0/5 | `L3-L4` |
| 75 | [Speech Writer](skills/speech-writer/) / 演讲稿与演讲提示 | Communication & Social | 🟢 Production Ready | 4.5/5 | `L1-L2` |
| 76 | [Decision Matrix](skills/decision-matrix/) / 决策矩阵 | Personal Productivity | 🟢 Production Ready | 5.0/5 | `L1-L2` |
| 77 | [Trip Planner](skills/trip-planner/) / 旅行规划 Agent | Personal Productivity | 🔵 Integration Required | 4.0/5 | `L3-L4` |
| 78 | [Gift Recommender](skills/gift-recommender/) / 礼物推荐 | Personal Productivity | 🟡 Experimental / Assisted | 3.5/5 | `L3` |
| 79 | [Resume Builder](skills/resume-builder/) / 简历生成器 | Personal Productivity | 🟢 Production Ready | 4.5/5 | `L1-L2` |
| 80 | [Meal Planner](skills/meal-planner/) / 一周饮食计划 | Personal Productivity | 🔵 Integration Required | 4.0/5 | `L2-L3` |
| 81 | [Conditional Reminder](skills/conditional-reminder/) / 条件式智能提醒 | Personal Productivity | 🔵 Integration Required | 4.0/5 | `L4` |
| 82 | [Habit Planner](skills/habit-planner/) / 习惯计划生成 | Personal Productivity | 🟢 Production Ready | 4.0/5 | `L1-L2` |
| 83 | [Read Later Digest](skills/read-later-digest/) / 稍后阅读摘要 | Personal Productivity | 🔵 Integration Required | 4.0/5 | `L3-L4` |
| 84 | [Git Deploy](skills/git-deploy/) / Git 自动部署 | DevOps & System | 🟢 Production Ready | 4.0/5 | `L3-L5` |
| 85 | [Backup Manager](skills/backup-manager/) / 自动备份管理 | DevOps & System | 🟢 Production Ready | 4.5/5 | `L2-L4` |
| 86 | [SSL Manager](skills/ssl-manager/) / SSL 证书管理 | DevOps & System | 🟢 Production Ready | 4.5/5 | `L3-L4` |
| 87 | [Service Monitor](skills/service-monitor/) / 服务健康监控 | DevOps & System | 🟢 Production Ready | 4.5/5 | `L4` |
| 88 | [Server Security Audit](skills/server-security-audit/) / 服务器安全基线审计 | DevOps & System | 🔵 Integration Required | 4.0/5 | `L3-L5` |
| 89 | [Docker Generator](skills/docker-generator/) / Docker 配置生成器 | DevOps & System | 🟢 Production Ready | 4.5/5 | `L2` |
| 90 | [Secret Scanner](skills/secret-scanner/) / 密钥泄露扫描 | DevOps & System | 🟢 Production Ready | 5.0/5 | `L2-L3` |
| 91 | [Paper Summarizer](skills/paper-summarizer/) / 论文深度解读 | Education & Research | 🟢 Production Ready | 4.5/5 | `L1-L2` |
| 92 | [Flashcard Generator](skills/flashcard-generator/) / 学习卡片生成 | Education & Research | 🟢 Production Ready | 4.5/5 | `L1-L2` |
| 93 | [Study Plan](skills/study-plan/) / AI 学习计划 | Education & Research | 🟢 Production Ready | 4.5/5 | `L1-L2` |
| 94 | [Plain Language Explainer](skills/plain-language-explainer/) / 复杂知识讲人话 | Education & Research | 🟢 Production Ready | 5.0/5 | `L1` |
| 95 | [Mind Map Generator](skills/mind-map-generator/) / 思维导图生成 | Education & Research | 🔵 Integration Required | 4.0/5 | `L2-L3` |
| 96 | [Cheatsheet Generator](skills/cheatsheet-generator/) / 一页速查表 | Education & Research | 🟢 Production Ready | 4.5/5 | `L1-L2` |
| 97 | [Quiz Generator](skills/quiz-generator/) / AI 出题与解析 | Education & Research | 🟢 Production Ready | 4.5/5 | `L1-L2` |
| 98 | [Book Knowledge Map](skills/book-knowledge-map/) / 书籍知识地图 | Education & Research | 🔵 Integration Required | 4.0/5 | `L2-L3` |
| 99 | [Pronunciation Coach](skills/pronunciation-coach/) / AI 发音教练 | Education & Research | 🔵 Integration Required | 4.0/5 | `L3` |
| 100 | [Course Builder](skills/course-builder/) / AI 课程生成器 | Education & Research | 🟡 Experimental / Assisted | 3.5/5 | `L2-L3` |

---

## Repository structure

```text
open-workflow-skills/
├── README.md
├── registry.json
├── install.sh
├── LICENSE
├── SECURITY.md
├── CONTRIBUTING.md
│
├── skills/
│   ├── image-watermark/
│   │   ├── SKILL.md
│   │   ├── references/
│   │   │   └── QUALITY.md
│   │   └── tests/
│   │       └── cases.yaml
│   ├── video-bilingual-subtitles/
│   └── ... 98 more
│
├── schemas/
│   └── registry.schema.json
│
├── scripts/
│   ├── doctor.sh
│   ├── validate_registry.py
│   └── test.sh
│
├── docs/
│   ├── architecture.md
│   ├── safety.md
│   ├── reliability.md
│   └── publishing.md
│
└── .github/
    ├── workflows/
    │   └── validate.yml
    ├── ISSUE_TEMPLATE/
    └── pull_request_template.md
```

---

## A Skill is not an App / Skill 不等于外部连接

A `SKILL.md` can teach an agent a repeatable workflow and may include code/scripts. It does **not** automatically provide an authenticated Gmail session, CRM token, Figma access, bank connection, production SSH key, or other external capability.

For example:

```text
inbox-triage
= Skill workflow
+ email connector / App
+ user authorization
+ account permissions
```

```text
competitor-monitor
= Skill workflow
+ browser/search
+ scheduler
+ destination notification channel
```

This distinction is deliberate.

---

## Evaluation philosophy / Eval 原则

**Do not use an LLM to judge what code can verify mechanically.**

Examples:

```text
image-watermark
✓ output count == input count
✓ images decode successfully
✓ source hash unchanged
✓ dimensions preserved when requested
```

```text
spreadsheet-merge
✓ no silent row loss
✓ duplicate count reported
✓ mapping recorded
✓ output schema valid
```

```text
video-bilingual-subtitles
✓ timestamps are monotonic
✓ subtitles end before video end
✓ output media decodes
✓ source is not overwritten
```

Each skill includes `tests/cases.yaml` as a starting evaluation contract. Mature implementations should add deterministic scripts and fixtures.

---

## Validate against the Agent Skills format

The Agent Skills specification defines `SKILL.md` frontmatter, naming constraints, optional directories, and related conventions.

This repository includes its own validator:

```bash
python3 scripts/validate_registry.py
```

You can also use the Agent Skills reference validator separately:

```bash
python3 -m venv .venv
source .venv/bin/activate

pip install "skills-ref @ git+https://github.com/agentskills/agentskills.git#subdirectory=skills-ref"

for d in skills/*/; do
  skills-ref validate "$d"
done
```

The `skills-ref` project describes itself as a reference/demonstration implementation, so this repository does not treat it as a runtime dependency.

---

## Contributing

A new skill should be:

1. **Specific** — one clear repeatable capability.
2. **Truthful** — no “one-click magic” claims that depend on undeclared services.
3. **Bilingual** — clear Chinese and English explanation.
4. **Permission-aware** — declare filesystem, network, account, shell, or privileged needs.
5. **Evaluable** — define what success and failure mean.
6. **Safe by default** — preserve sources and approval-gate consequential writes.
7. **Installable** — valid Agent Skills folder and `SKILL.md`.

Read [CONTRIBUTING.md](CONTRIBUTING.md).

---

## Roadmap

### v0.1 — Registry
- [x] 100 audited skill definitions
- [x] bilingual descriptions
- [x] reliability labels
- [x] permissions
- [x] install guidance
- [x] baseline eval cases
- [x] repository validation

### v0.2 — Reference implementations
- [ ] deterministic scripts for top 20 Production skills
- [ ] reproducible fixtures
- [ ] OS-specific dependency checks
- [ ] screenshot/demo assets

### v0.3 — Integrations
- [ ] connector recipes
- [ ] OAuth/App setup documentation
- [ ] sandbox test environments
- [ ] webhook/scheduler examples

### v1.0 — Verified catalog
- [ ] automated eval scores
- [ ] signed releases/checksums
- [ ] compatibility matrix
- [ ] community review process
- [ ] searchable website

---

## License

MIT. See [LICENSE](LICENSE).

## Disclaimer

This repository contains workflow definitions and examples. Availability, behavior, external service terms, APIs, pricing, and agent compatibility can change. Financial, legal, security, production-infrastructure, and other consequential workflows require appropriate domain review and authorization.
