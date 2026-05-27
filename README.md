# MengyuLi15.github.io

This repository hosts the personal academic website for Mengyu Li and the Daily Paper Push archive.

Website:

- https://mengyuli15.github.io/
- https://mengyuli15.github.io/activities/paper-push/

Wiki:

- https://github.com/MengyuLi15/MengyuLi15.github.io/wiki/Paper-Push-Homepage

## Daily Paper Push

The Paper Push feature publishes a daily literature archive for BGC-Argo, ocean-colour remote sensing, marine heatwaves, phytoplankton vertical structure, and carbon-pump processes.

Main files:

- `_pages/paper-push.md` - Paper Push homepage and date list.
- `_pages/paper-push-YYYY-MM-DD.md` - generated detail page for each daily issue.
- `_data/paper_pushes.yml` - structured issue and paper data.
- `_includes/paper-push-assets.html` - shared styles and script include.
- `assets/js/paper-push.js` - browser-side language switching, saved papers, search, removal, and CSV export.
- `scripts/generate_paper_push.py` - daily paper retrieval, filtering, ranking, Word summary generation, history update, and page creation.
- `scripts/create_paper_push_page.py` - generated page shell for a given date.
- `.github/workflows/paper-push.yml` - scheduled and manually triggered daily generation workflow.
- `.github/workflows/temporary-v2-push.yml` - manual temporary test-push workflow.

The main workflow runs at `06:00 UTC` and `07:00 UTC` to cover `08:00 Europe/Berlin` across daylight-saving changes. DOI/history de-duplication prevents duplicate daily entries when both scheduled runs see the same candidates.

## Local Development

Install the Jekyll dependencies and run the site locally:

```bash
bundle install
bundle exec jekyll serve -l -H localhost
```

The local site is served at:

```text
http://localhost:4000
```

To run only the paper-push generator in dry-run mode:

```bash
python scripts/generate_paper_push.py --dry-run
```

To generate a specific daily push locally:

```bash
python scripts/generate_paper_push.py --date YYYY-MM-DD
```

## 中文说明

本仓库用于维护 Mengyu Li 的个人学术网站，以及“每日论文推送”功能。

每日论文推送页面：

- https://mengyuli15.github.io/activities/paper-push/

该功能会围绕 BGC-Argo、海色遥感、海洋热浪、浮游植物垂向结构和碳泵过程，自动生成每日论文归档。页面支持中英文显示、论文收藏、本地搜索和 CSV 导出。

主要维护入口：

- `_data/paper_pushes.yml` - 每日推送数据。
- `_pages/paper-push.md` - 推送主页。
- `scripts/generate_paper_push.py` - 自动生成脚本。
- `.github/workflows/paper-push.yml` - 每日自动运行 workflow。
- Wiki 页面 - Paper Push 主页功能说明和维护文档。
