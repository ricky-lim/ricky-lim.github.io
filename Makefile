.DEFAULT_GOAL := help

LEKTOR_PROJECT_DIR := ./kutubuku
PUBLIC_DIR := $(LEKTOR_PROJECT_DIR)/public
PAGEFIND_SOURCE := $(PUBLIC_DIR)

.PHONY: dev
dev: prepare serve ## Run development server

.PHONY: prepare ## Prepare for development
prepare: clean build index

.PHONY: clean
clean: ## Clean up
	@echo "Cleaning public directory..."
	@rm -rf $(PUBLIC_DIR)

.PHONY: build
build: ## Build static files
	@echo "Building static files..."
	@cd $(LEKTOR_PROJECT_DIR) && lektor build --output-path ./public

.PHONY: index
index: ## Index pages with pagefind
	@echo "Indexing pages with pagefind..."
	@cd $(LEKTOR_PROJECT_DIR) && npx pagefind --site ./public

.PHONY: serve
serve: ## Serve development server
	@echo "Serving development server..."
	@python -m http.server --directory $(PUBLIC_DIR)

.PHONY: watch
watch: ## Watch for changes and rebuild
	@echo "Watching for changes and rebuilding..."
	@cd $(LEKTOR_PROJECT_DIR) && lektor server

.PHONY: help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-16s\033[0m %s\n", $$1, $$2}'
