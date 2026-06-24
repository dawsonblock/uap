.PHONY: lint check-refs check-stale check build pdf html clean

# Canonical markdown files (exclude archive/)
MD_FILES := $(shell find manuscript appendices references style -name '*.md' 2>/dev/null)
ROOT_MD := README.md CHANGELOG.md
ALL_CANONICAL_MD := $(MD_FILES) $(ROOT_MD)

PYTHON ?= python3

##@ Checks

check: lint check-refs check-stale
	@echo "All checks passed."

lint: ## Run markdownlint on all canonical .md files
	@markdownlint '**/*.md' --config .markdownlint.json --ignore archive
	@echo "markdownlint: OK"

check-refs: ## Verify footnote definitions match references
	@$(PYTHON) scripts/check_footnotes.py
	@echo "check-refs: OK"

check-stale: ## Scan canonical files for forbidden/stale strings
	@$(PYTHON) scripts/check_stale_claims.py
	@echo "check-stale: OK"

##@ Build

build: pdf html ## Build PDF and HTML outputs

pdf: ## Build PDF from the main manuscript (requires pandoc + LaTeX)
	@command -v pandoc >/dev/null 2>&1 || { echo "pandoc not found"; exit 1; }
	pandoc manuscript/uap-comprehensive.md \
		-o build/uap-comprehensive.pdf \
		--pdf-engine=xelatex \
		--toc \
		--metadata title="UAP: Evidence, Physics, and the Limits of Speculation"
	@echo "PDF: build/uap-comprehensive.pdf"

html: ## Build HTML from the main manuscript (requires pandoc)
	@command -v pandoc >/dev/null 2>&1 || { echo "pandoc not found"; exit 1; }
	@mkdir -p build
	pandoc manuscript/uap-comprehensive.md \
		-o build/uap-comprehensive.html \
		--toc \
		--standalone \
		--metadata title="UAP: Evidence, Physics, and the Limits of Speculation"
	@echo "HTML: build/uap-comprehensive.html"

clean:
	rm -rf build
