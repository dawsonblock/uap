.PHONY: lint check-refs check-stale check build pdf html clean install-deps help

# Canonical markdown files (exclude archive/)
MD_FILES := $(shell find manuscript appendices references style -name '*.md' 2>/dev/null)
ROOT_MD := README.md CHANGELOG.md
ALL_CANONICAL_MD := $(MD_FILES) $(ROOT_MD)

PYTHON ?= python3
MARKDOWNLINT ?= npx --yes markdownlint-cli

##@ Setup

install-deps: ## Install lint and build dependencies (npm + Homebrew)
	@npm install -D markdownlint-cli
	@echo "markdownlint-cli installed via npm"
	@echo "For PDF builds, also install: brew install pandoc && brew install --cask mactex-no-gui"
	@echo "(or: apt install pandoc texlive-xetex on Debian/Ubuntu)"

##@ Checks

check: lint check-refs check-stale
	@echo "All checks passed."

lint: ## Run markdownlint on all canonical .md files
	@$(MARKDOWNLINT) '**/*.md' --config .markdownlint.json --ignore archive
	@echo "markdownlint: OK"

check-refs: ## Verify footnote definitions match references
	@$(PYTHON) scripts/check_footnotes.py
	@echo "check-refs: OK"

check-stale: ## Scan canonical files for forbidden/stale strings
	@$(PYTHON) scripts/check_stale_claims.py
	@echo "check-stale: OK"

##@ Build

build: pdf html ## Build PDF and HTML outputs

pdf: ## Build PDF from the main manuscript (requires pandoc + xelatex)
	@command -v pandoc >/dev/null 2>&1 || { echo "pandoc not found. Run: brew install pandoc"; exit 1; }
	@mkdir -p build
	pandoc manuscript/uap-comprehensive.md \
		-o build/uap-comprehensive.pdf \
		--pdf-engine=xelatex \
		--toc
	@echo "PDF: build/uap-comprehensive.pdf"

html: ## Build HTML from the main manuscript (requires pandoc)
	@command -v pandoc >/dev/null 2>&1 || { echo "pandoc not found. Run: brew install pandoc"; exit 1; }
	@mkdir -p build
	pandoc manuscript/uap-comprehensive.md \
		-o build/uap-comprehensive.html \
		--toc \
		--standalone
	@echo "HTML: build/uap-comprehensive.html"

clean:
	rm -rf build

##@ Help

help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  %-15s %s\n", $$1, $$2}'
